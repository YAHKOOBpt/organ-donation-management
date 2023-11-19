from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

###################home ########################    

def index(request):
    
    return render(request, "donor/index.html")

def home(request):
    
    return render(request, "home/index.html")


######################################donor panel ######################################

def donor_home(request):

    return render(request,"donor/index1.html")

##################donor registeration ################

def donor_register(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        passw = request.POST.get("password")
        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'donor/register1.html')
        else:
            user = User.objects.create_user(
                username=uname,
                password=passw,
                is_donor=True,
            )
            # Add a success message
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('donor_login')
    else:
        return render(request, "donor/register1.html")
    


#############login #########################
def donor_login(request):  
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')

        user = User.objects.filter(username=uname).first()
        
        if user is not None and user.check_password(passw) and user.is_donor:
            login(request, user)
            return redirect('donor_home')
        else:
            messages.error(request, 'Invalid login credentials.')
    return render(request, "donor/login1.html")

#####################donor logout ########################
def donor_logout(request):
    logout(request)
    return redirect('home')

############add donor details ######################
def add_donor_details(request):
    if request.method == "POST":
        # Retrieve form data from request.POST
        name = request.POST.get("name")
        age = request.POST.get("age")
        address = request.POST.get("Address")
        mobile = request.POST.get("Contact")
        email = request.POST.get("mail")
        country = request.POST.get("country")
        district = request.POST.get("district")
        gender = request.POST.get("genter")
        blood_group = request.POST.get("blood_group")
        organs_to_donate = request.POST.get("organs_to_donate")
        status = request.POST.get("status")
        cause_of_death = request.POST.get("cause_of_death")
        # Create a new user or retrieve the current user (assuming the donor is logged in)
        if request.user.is_authenticated:
            current_user = request.user
        else:
            current_user = User.objects.create_user(username="a_random_username", password="a_random_password", is_donor=True)
         # Update the user's details with the form data
        current_user.name = name
        current_user.age = age
        current_user.address = address
        current_user.mobile = mobile
        current_user.email = email
        current_user.country = country
        current_user.district = district
        current_user.gender = gender
        current_user.blood_grou = blood_group
        current_user.organs_to_donat = organs_to_donate
        
        current_user.cause_of_death = cause_of_death
        if status is not None:
            current_user.status = True  # Checkbox was selected
        else:
            current_user.status = False  # Checkbox was not selected

        # Save the user object with the updated details
        current_user.save()
        return redirect('donor_home')  # Redirect to the donor's dashboard or a success page
    return render(request, 'donor/create_donor.html')

###################view donor details #########################
def view_donor_details(request, donor_id):
    donor = get_object_or_404(User, id=donor_id, is_donor=True)

    return render(request, 'donor/view_donor.html', {'donor': donor})
######################update donor details ######################
def Update_donor_details(request, donor_id):
    donor = get_object_or_404(User, id=donor_id, is_donor=True)
    if request.method == 'POST':
        donor.name=request.POST.get('name')
        donor.age=request.POST.get('age')
        donor.address=request.POST.get('address')
        donor.mobile=request.POST.get('Contact')
        donor.email=request.POST.get('mail')
        donor.country=request.POST.get('country')
        donor.district=request.POST.get('district')
        donor.gender=request.POST.get('genter')
        donor.blood_grou=request.POST.get('blood_group')
        donor.organs_to_donat=request.POST.get('organs_to_donate')
        donor.cause_of_death=request.POST.get('cause_of_death')
        status = request.POST.get("status")
        if status is not None:
            donor.status = True  
        else:
                donor.status = False 
        donor.save()
        messages.success(request,"Update successfully")
        return redirect('view_donor_details',donor_id=donor.id)

    context = {
        'donor': donor
        }
    return render(request, 'donor/update_donor.html',context)

#############delete donor details ##################
def delete_donor_details(request, donor_id):
    donor = get_object_or_404(User, id=donor_id, is_donor=True)

    if request.method == 'POST':
        # Assuming you have a confirmation step before deleting
        # Delete the specific details without deleting the entire account
        donor.name = None
        donor.age = None
        donor.address = None
        donor.mobile = None
        donor.email = None
        donor.country = None
        donor.district = None
        donor.gender = None
        donor.blood_grou = None
        donor.organs_to_donat = None
        donor.status = False  # Assuming you want to deactivate the donor status
        donor.cause_of_death = None
        donor.save()

        messages.success(request, "Donor details deleted successfully")
        return redirect('view_donor_details', donor_id=donor.id)

    context = {
        'donor': donor
    }
    return render(request, 'donor/delete_donor.html', context)

############ donor home ###############
def home_donor(request, donor_id):
    donor = get_object_or_404(User, id=donor_id, is_donor=True)
    context = {
        'donor': donor
    }
    return render(request, 'donor/base.html', context)

################# view organ request #########################3
def view_organ_request(request):
    donorid= request.user.pk
    requests = OrganRequest.objects.filter(donor_id=donorid)

    return render(request, 'donor/view_organ_reques.html', {'requests': requests})


################### update organ request ##############################
def Update_organ_request(request, pk):
    organ = get_object_or_404(OrganRequest, pk=pk)
    if request.method == 'POST':
        organ.patient_name=request.POST.get('name')
        organ.patient_age=request.POST.get('age')
        organ.patient_email=request.POST.get('mail')
        organ.needed_organ=request.POST.get('organs_to_donate')
        
        
        status = request.POST.get("status")
        if status is not None:
            organ.status = True  
        else:
            organ.status = False 
        organ.save()
        messages.success(request,"Update successfully")
        return redirect('view_organ_request')
    context = {
        'organ': organ
        }
    return render(request, 'donor/update_request.html',context)

################################## patient panel #################################################

def intex_1(request):
    
    return render(request, 'patient/index_1.html')

################# patient registration ########################

def Patient_register(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        passw = request.POST.get("password")
        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'patient/register.html')
        else:
            user = User.objects.create_user(
                username=uname,
                password=passw,
                is_patient=True,
            )
            # Add a success message
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('Patient_login')
    else:
        return render(request, "patient/register.html")
    
#############login #########################
def Patient_login(request):  
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')

        user = User.objects.filter(username=uname).first()
        
        if user is not None and user.check_password(passw) and user.is_patient:
            login(request, user)
            return redirect('intex_1')
        else:
            messages.error(request, 'Invalid login credentials.')
    return render(request, "patient/login.html")

#####################donor logout ########################
def patient_logout(request):
    logout(request)
    return redirect('home')

############add Patient details ######################
def add_patient_details(request):
    if request.method == "POST":
        # Retrieve form data from request.POST
        name = request.POST.get("name")
        age = request.POST.get("age")
        address = request.POST.get("Address")
        mobile = request.POST.get("Contact")
        email = request.POST.get("mail")
        country = request.POST.get("country")
        district = request.POST.get("district")
        gender = request.POST.get("genter")
        blood_group = request.POST.get("blood_group")
        needed_organ = request.POST.get("needed_organ")
        
        # Create a new user or retrieve the current user (assuming the donor is logged in)
        if request.user.is_authenticated:
            current_user = request.user
        else:
            current_user = User.objects.create_user(username="a_random_username", password="a_random_password", is_patient=True)
         # Update the user's details with the form data
        current_user.name = name
        current_user.age = age
        current_user.address = address
        current_user.mobile = mobile
        current_user.email = email
        current_user.country = country
        current_user.district = district
        current_user.gender = gender
        current_user.blood_grou = blood_group
        current_user.needed_organ= needed_organ

        # Save the user object with the updated details
        current_user.save()
        return redirect('intex_1')  # Redirect to the donor's dashboard or a success page
    return render(request, 'patient/create_patient.html')

###################view donor details #########################
def view_patient_details(request, patient_id):
    patient = get_object_or_404(User, id=patient_id, is_patient=True)

    return render(request, 'patient/view_patient.html', {'patient': patient})

######################update donor details ######################
def Update_patient_details(request, patient_id):
    patient = get_object_or_404(User, id=patient_id, is_patient=True)
    if request.method == 'POST':
        patient.name=request.POST.get('name')
        patient.age=request.POST.get('age')
        patient.address=request.POST.get('address')
        patient.mobile=request.POST.get('Contact')
        patient.email=request.POST.get('mail')
        patient.country=request.POST.get('country')
        patient.district=request.POST.get('district')
        patient.gender=request.POST.get('genter')
        patient.blood_grou=request.POST.get('blood_group')
        patient.needed_organ=request.POST.get('needed_organ')
        
        
        patient.save()
        messages.success(request,"Update successfully")
        return redirect('view_patient_details',patient_id = patient.id)

    context = {
        'patient': patient
        }
    return render(request, 'patient/update_patient.html',context)

#############delete donor details ##################
def delete_patient_details(request, patient_id):
    patient = get_object_or_404(User, id=patient_id, is_patient=True)

    if request.method == 'POST':
        # Assuming you have a confirmation step before deleting
        # Delete the specific details without deleting the entire account
        patient.name = None
        patient.age = None
        patient.address = None
        patient.mobile = None
        patient.email = None
        patient.country = None
        patient.district = None
        patient.gender = None
        patient.blood_grou = None
        patient.needed_organ = None    
        patient.save()

        messages.success(request, "Donor details deleted successfully")
        return redirect('view_patient_details', patient_id=patient.id)

    context = {
        'patient': patient
    }
    return render(request, 'patient/delete_patient.html', context)

####################### view all organ details #########################

def view_organ_details(request):
    organ = User.objects.filter(is_donor=True)

    context ={
        'organ':organ
    }

    return render(request, 'patient/view_all_organ.html', context)


##################### send request #########################################


def give_request(request, pk):
    get_request = get_object_or_404(User, pk=pk)
    patientid = request.user.pk
    patient_name = request.user.name
    patient_age = request.user.age
    patient_email = request.user.email
    if request.method == "POST":
        donor_id = request.POST.get("donor_id")
        
        
        donor_name = request.POST.get("name")
        donor_age = request.POST.get("age")
        donor_email = request.POST.get("mail")
        
        needed_organ = request.POST.get("organs_to_donate")
        
        # status = 'Pending'
        reque = OrganRequest.objects.create(
                
                
                donor_name=donor_name,
                donor_age=donor_age ,
                donor_email=donor_email,
                needed_organ=needed_organ,
                donor_id=donor_id,
                patient_id=patientid,

                patient_name = patient_name,
                patient_age = patient_age,
                patient_email= patient_email 
                # status=status,
                
            )
            
            # Add a success message
        messages.success(request, 'Registration successful. You can now log in.')
        return redirect('view_organ_details')
        
    context = {'give_request':get_request}

    return render(request, 'patient/give_request.html', context)

###################view send request #########################
# @login_required(login_url='login')


def view_send_request(request):
    patientid= request.user.pk
    requests = OrganRequest.objects.filter(patient_id=patientid)

    return render(request, 'patient/view_request_hist.html', {'requests': requests})