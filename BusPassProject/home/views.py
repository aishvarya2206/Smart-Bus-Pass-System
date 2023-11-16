from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from home import models
from .pdf import html_to_pdf
from datetime import date
from dateutil.relativedelta import relativedelta

# Create your views here.
# Website page starts
def home(request):
    return render(request, 'home.html')

def login_student(request):
    return render(request, 'login.html')

def login_college(request):
    return render(request, 'login_college.html')

def login_manager(request):
    return render(request, 'login_manager.html')

def handleLogin(request):
    
    if request.method == 'POST' :
        username = request.POST['username'],
        password = request.POST['password']
        user = authenticate(username=username[0],password=password[0])
        usertype =  models.AuthUser.objects.get(user = user)

        if usertype.type == 1:
            if user is not None:
                login(request,user)
                # response = redirect('/student_dashboard/%i/' %student.student_id)
                messages.success(request,"Successfull Login")
                response = redirect('/student_dashboard')
                return response
            else:
                messages.success(request,"Invalid Credentials")
                response = redirect('/login_student')
                return response
        elif usertype.type == 2:
            if user is not None:
                login(request,user)
                messages.success(request,"Successfull Login")
                response = redirect('/college_dashboard')
                return response
            else:
                messages.success(request,"Invalid Credentials")
                response = redirect('/login_college')
                return response    
        elif usertype.type == 3:
            if user is not None:
                login(request,user)
                messages.success(request,"Successfull Login")
                response = redirect('/manager_dashboard')
                return response
            else:
                messages.success(request,"Invalid Credentials")
                response = redirect('/login_manager')
                return response    
    return HttpResponse('<h1>Page was found</h1>')
    
def handleLogout(request):
    logout(request)
    response = redirect('/')
    return response

def register(request):
    college = models.College.objects.all().values()
    context = {'college_data': college }
    return render(request,'register.html',context)

def register_college(request):
    college = models.College.objects.all().values()
    context = {'college_data': college }
    return render(request,'register_college.html',context)

def register_manager(request):
    return render(request,'register_manager.html')

def handleSignup(request):

    if request.method == 'POST' :

        if request.POST['type'][0] == '1':
            name = request.POST['name'],
            type = request.POST['type'],
            fathername = request.POST['fathername'],
            college = request.POST['collegename'],
            roll = request.POST['roll'],
            course = request.POST['course'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            username = request.POST['username'],
            password = request.POST['password']
            # check for errorneous input
            # save in user table and student
            #if type[0] == '1':
            student_content = models.Student(
            name=name[0],
            fathername= fathername[0],
            college=models.College.objects.get(college_id = college[0]),
            roll=roll[0],
            course=course[0],
            phone=phone[0]
            )
            student_content.save()
            std_id = student_content.student_id
            # user table entry
            myuser = User.objects.create_user(
                username=username[0],
                first_name=name[0], 
                email=email[0],
                password=password[0]
            )
            myuser.save()
            uid = myuser.id
            # AuthUser Model create ---- user model inherited model
            authuser = models.AuthUser(
                user = models.User.objects.get(id = uid),
                type=1,
                student_id=models.Student.objects.get(student_id = std_id)
            )
            authuser.save()
        #if type == '2':
        if request.POST['type'][0] == '2':
            name = request.POST['name'],
            type = request.POST['type'],
            college = request.POST['collegename'],
            email = request.POST['email'],
            username = request.POST['username'],
            password = request.POST['password']
            # user table entry
            myuser = User.objects.create_user(
                username=username[0],
                first_name=name[0], 
                email=email[0],
                password=password[0]
            )
            myuser.save()
            uid = myuser.id
            # AuthUser Model create ---- user model inherited model
            authuser = models.AuthUser(
                user = models.User.objects.get(id = uid),
                type=2,
                college_id=models.College.objects.get(college_id = college[0])
            )
            authuser.save()
        #if type == '3':
        if request.POST['type'][0] == '3':
            name = request.POST['name'],
            type = request.POST['type'],
            email = request.POST['email'],
            username = request.POST['username'],
            password = request.POST['password']
            # manager table entry
            manager = models.Manager(
                name=name[0]
            )
            manager.save()
            mid = manager.manager_id
            # user table entry
            myuser = User.objects.create_user(
                username=username[0],
                first_name=name[0], 
                email=email[0],
                password=password[0]
            )
            myuser.save()
            uid = myuser.id
            # AuthUser Model create ---- user model inherited model
            authuser = models.AuthUser(
                user = models.User.objects.get(id = uid),
                type=3,
                manager_id=models.Manager.objects.get(manager_id = mid)
            )
            authuser.save()
        
        response = redirect('/login_student')
        return response
# Website page ends

# Student dashboard starts

def student_dashboard(request):
    
    current_user = request.user
    login_user = models.AuthUser.objects.get(user=current_user)
    student = models.Student.objects.get(student_id=login_user.student_id.student_id)
    bus_pass = models.Pass.objects.filter(student = student.student_id)
    #bus_pass = models.Pass.objects.all()
    if student.route_to:
        to_route = models.Route.objects.get(route_id =student.route_to.route_id)
        if bus_pass:
            data = {'std_data':student,'to_route':to_route, 'pass' : bus_pass[0]}
        else:
            data = {'std_data':student,'to_route':to_route}
    else :
        data = {'std_data':student}
    return render(request, 'student_dashboard.html',data)

def profile(request):

    if request.method == "POST":
        name = request.POST['name'],
        fathername = request.POST['fathername'],
        college = request.POST['collegename'],
        roll = request.POST['roll'],
        course = request.POST['course'],
        phone = request.POST['phone'],
        aadhar_number = request.POST['aadhar'],
        previous_pass = request.POST['previous_pass'],
        pass_number = request.POST['pass_number']

        content = models.Student(
            name=name[0],
            fathername= fathername[0],
            college=models.College.objects.get(college_id = college[0]),
            roll=roll[0],
            course=course[0],
            phone=phone[0],
            aadhar_number=aadhar_number[0],
            previous_pass=bool(previous_pass[0]),
            pass_number=pass_number[0])
        content.save()

    current_user = request.user
    login_user = models.AuthUser.objects.get(user=current_user)
    college = models.College.objects.all().values()
    student = models.Student.objects.get(student_id=login_user.student_id.student_id)
    clg = models.College.objects.get(college_id =student.college_id)
    context = {'college_data': college ,'student_data': student, 'clg' : clg }
    return render(request, 'profile.html',context)

def set_route(request):

    college = models.Route.objects.all().values()
    context = {'route_data': college }
    return render(request,'set_route.html',context)

def handleRoute(request):

    if request.method == "POST":
        routefrom = request.POST['routefrom']
        routeto = request.POST['routeto']
        current_user = request.user
        login_user = models.AuthUser.objects.get(user=current_user)
        std = models.Student.objects.get(student_id=login_user.student_id.student_id)
        std.route_from=models.Route.objects.get(route_id = routefrom[0])
        std.route_to= models.Route.objects.get(route_id = routeto[0])
        std.save()
        response = redirect('/view_route')
        return response
    
def view_route(request):

    current_user = request.user
    login_user = models.AuthUser.objects.get(user=current_user)
    student = models.Student.objects.get(student_id=login_user.student_id.student_id)
    if student.route_from :
        from_route = models.Route.objects.get(route_id =student.route_from.route_id)
        to_route = models.Route.objects.get(route_id =student.route_to.route_id)

        ##########################
        graph = [[0, 30, 28, 42, 59, 56, 109], 
            [30, 0, 35, 72, 53, 42, 95],
			[28, 32, 0, 39, 33, 35, 90], 
            [42, 72, 39, 0, 59, 74, 129],
            [59, 53, 33, 59, 0, 14, 72],
            [56, 42, 35, 74, 14, 0, 58],
            [109, 95, 90, 129, 72, 58,0]]
        start = (from_route.route_id)-1
        end = (to_route.route_id)-1
        dist = graph[start][end]
        
        ##########################

        context = {'student_data': student, 'from_route':from_route,'to_route':to_route,'dist' : dist }
    else :
        context = {'student_data': student}
    return render(request,'view_route.html',context)

def apply_pass(request):
    if request.method == "POST":
        apply = request.POST['apply']
        current_user = request.user
        login_user = models.AuthUser.objects.get(user=current_user)
        std = models.Student.objects.get(student_id=login_user.student_id.student_id)
        std.apply = bool(apply[0])
        print(bool(apply[0]))
        std.save()
        response = redirect('/verification')
        return response
    
def verification(request):

    current_user = request.user
    login_user = models.AuthUser.objects.get(user=current_user)
    student = models.Student.objects.get(student_id=login_user.student_id.student_id)
    if student.apply == 1:
        if  student.verify_college == 1 :
            if student.verify_manager == 1:
                context = {'student_data': "Your request verification is cleared. You can now generate your pass" }
                return render(request,'verification.html',context)
            context = {'student_data': "We have received your request . Your college verification is cleared done but bus pass manager is not verified your request yet." }
            return render(request,'verification.html',context)
        context = {'student_data': "We have received your request ." }
        return render(request,'verification.html',context)
    else:
        context = {'student_data': "You have not applied for pass yet." }
        return render(request,'verification.html',context)

def generate_pass(request):
   
    current_user = request.user
    login_user = models.AuthUser.objects.get(user=current_user)
    student = models.Student.objects.get(student_id=login_user.student_id.student_id)
    
    if student.verify_manager == 1:
        clg = models.College.objects.get(college_id =student.college_id)
        from_route = models.Route.objects.get(route_id =student.route_from.route_id)
        to_route = models.Route.objects.get(route_id =student.route_to.route_id)
        std_pass = models.Pass.objects.get(student=login_user.student_id.student_id)
        manager=models.Manager.objects.get(manager_id=std_pass.manager.manager_id)
        
        pdf_print = html_to_pdf('pdf.html',{'name': student.name ,'college' : clg.name,'roll': student.roll ,'source' : from_route.name ,'destination' : to_route.name, 'pass_number': std_pass.pass_id, 'valid_from': std_pass.valid_from, 'valid_to': std_pass.valid_to, 'manager_name' : manager.name })
        return HttpResponse(pdf_print, content_type ="application/pdf" ) 
    else:
        context = {'data': "Your pass can not generate yet, please check your verification update  regarding pass." }
        return render(request,'generate_pass.html',context)

def payment(request):
    return render(request,'payment.html')


# Student dashboard ends

# College dashboard starts
def college_dashboard(request):
    
    current_user = request.user
    login_user = models.AuthUser.objects.get(user=current_user)
    college = models.College.objects.get(college_id=login_user.college_id.college_id)
    request_student = models.Student.objects.filter(apply=True,college_id=college.college_id).order_by('-pass_requests_created')[:5]
    count_request = models.Student.objects.filter(verify_college=False,college_id=college.college_id).count()
    count_verified = models.Student.objects.filter(verify_college=True,college_id=college.college_id).count()
    count_passholder = models.Student.objects.filter(verify_manager=True,college_id=college.college_id).count()
    context = {'request_student': request_student,'count_request' : count_request,'count_verified': count_verified,'count_passholder':count_passholder, 'college': college}
    return render(request,'college_dashboard.html',context)

def student_verification(request):

    current_user = request.user
    login_user = models.AuthUser.objects.get(user=current_user)
    college = models.College.objects.get(college_id=login_user.college_id.college_id)
    request_student = models.Student.objects.filter(apply=True,college_id=college.college_id)
    context = {'request_student': request_student}
    return render(request,'student_verification.html',context)

def verified_student(request):

    current_user = request.user
    login_user = models.AuthUser.objects.get(user=current_user)
    college = models.College.objects.get(college_id=login_user.college_id.college_id)
    verified_student = models.Student.objects.filter(verify_college=True,college_id=college.college_id)
    context = {'verified_student': verified_student}
    return render(request,'verified_student.html',context)

def college_verify(request):

    if request.method == "POST":
        id = request.POST['student_id']
        std = models.Student.objects.get(student_id=id)
        std.verify_college_reject = False
        std.verify_college = True
        std.save()
        response = redirect('/college_dashboard')
        return response
    
def college_verify_reject(request):

    if request.method == "POST":
        id = request.POST['student_id']
        std = models.Student.objects.get(student_id=id)
        std.verify_college_reject = True
        std.verify_college = False
        std.save()
        response = redirect('/college_dashboard')
        return response
    
# College dashboard ends

# Manager dashboard starts
def manager_dashboard(request):

    current_user = request.user
    login_user = models.AuthUser.objects.get(user=current_user)
    manager = models.Manager.objects.get(manager_id=login_user.manager_id.manager_id)
    count_request = models.Student.objects.filter(apply=True , verify_college=True,verify_manager=False,verify_manager_reject=False).count()
    count_verified = models.Student.objects.filter(verify_manager=True).count()
    count_passholder = models.Student.objects.filter(verify_manager=True).count()
    context = {'count_request' : count_request,'count_verified': count_verified,'count_passholder':count_passholder,'manager':manager}
    return render(request,'manager_dashboard.html',context)

def approval(request):

    current_user = request.user
    login_user = models.AuthUser.objects.get(user=current_user)
    manager = models.Manager.objects.get(manager_id=login_user.manager_id.manager_id)
    request_student = models.Student.objects.filter(apply=True, verify_college=True)
    context = {'request_student': request_student, 'manager':manager}
    return render(request,'approval.html',context)

def generate(request):
    return render(request,'generate.html')

def report(request):
    return render(request,'report.html')

def manager_verify(request):

    if request.method == "POST":

        id = request.POST['student_id']
        manager_id = request.POST['manager_id']
        std = models.Student.objects.get(student_id=id)
                # update pass model 
        content = models.Pass(
            student=models.Student.objects.get(student_id =id),
            college=models.College.objects.get(college_id =std.college_id),
            valid_from=date.today(),
            valid_to=date.today() + relativedelta(months=3),
            payment = True,
            manager =models.Manager.objects.get(manager_id =manager_id)
            #pass_file =
            )
        content.save()
                # update student model
        std.verify_manager = True
        std.verify_manager_reject = False
        std.save()
        response = redirect('/approval')
        return response
    
def manager_verify_reject(request):

    if request.method == "POST":

        id = request.POST['student_id']
        std = models.Student.objects.get(student_id=id)
                # update pass model 
        pas =models.Pass.objects.get(student =id)
        pas.delete()
                # update student model
        std.verify_manager_reject = True
        std.verify_manager = False
        std.save()
        response = redirect('/approval')
        return response
    

# Manager dashboard ends
