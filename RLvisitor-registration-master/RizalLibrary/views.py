from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import *
from django.http import HttpResponse

# import qrcode (for generating qrcode)
import qrcode

# for email sending
from django.core.mail import EmailMessage
from django.conf import settings
import os

# for video capture
import cv2
import numpy as np
# qr code reader
from pyzbar.pyzbar import decode

# for datetime
from datetime import datetime

# to change queryset to json
from django.core.serializers import serialize

# Create your views here.
def visitor_start_page(request):
    return render(request, 'RizalLibrary/base.html')

def empty_visitors_input(request):
    return render(request, 'RizalLibrary/empty_visitors_input.html')

def visitor_upload_success(request):
    return render(request, 'RizalLibrary/visitor_upload_success.html')

def upload_visitor_info(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            visitor = form.save()
            request.session['VisitorID'] = visitor.visitorID
            request.session.modified = True
            if visitor.visitorType == Visitor.PARTNER_LIBRARY:
                return redirect('partner_library_page')
            elif visitor.visitorType == Visitor.NON_ATENEO_AFFILIATED:
                return redirect('non_ateneo_affiliated_page')  # Updated to match URL pattern name
            elif visitor.visitorType == Visitor.ATENEO_AFFILIATED:
                return redirect('ateneo_affiliated_page')  # Updated to match URL pattern name
    else:

        form = VisitorForm()
    return render(request, 'RizalLibrary/upload_visitor_info.html', {'form': form})

def partner_library_page(request):
    plVisitorID = request.session.get('VisitorID')
    form = PartnerLibraryForm({"plVisitorID": plVisitorID})
    if request.method == 'POST':
        updated_request = request.POST.copy()
        updated_request.update({'plVisitorID': plVisitorID})
        form = PartnerLibraryForm(updated_request)
        if form.is_valid():
            PartnerLibrary = form.save()
            return redirect('visitor_activities')
    else:
        form = PartnerLibraryForm(initial={"plVisitorID":plVisitorID})
    return render(request, 'RizalLibrary/partner_library_page.html', {'form': form})


# it's not saving properly (like based on the visitorID)
def non_ateneo_affiliated_page(request):
    naaVisitorID = request.session.get('VisitorID')
    if request.method == 'POST':
        form = NonAteneoAffiliatedForm(request.POST, request.FILES, {"naaVisitorID": naaVisitorID})
        updated_request = request.POST.copy()
        updated_request.update(request.FILES.copy())
        updated_request.update({'naaVisitorID': naaVisitorID})
        form = NonAteneoAffiliatedForm(updated_request, request.FILES)
        # print(form.data)
        # print(form.is_valid())
    
        
        if form.is_valid():
            form.save()
            return redirect('visitor_activities')
    else:
        form = NonAteneoAffiliatedForm(initial={"naaVisitorID":naaVisitorID})
    return render(request, 'RizalLibrary/non_ateneo_affiliated_page.html', {'form': form})


def ateneo_affiliated_page(request):
    aaVisitorID = request.session.get('VisitorID')
    if request.method == 'POST':
        form = AteneoAffiliatedForm(request.POST, request.FILES, {"aaVisitorID": aaVisitorID})
        updated_request = request.POST.copy()
        updated_request.update(request.FILES.copy())
        updated_request.update({'aaVisitorID': aaVisitorID})
        form = AteneoAffiliatedForm(updated_request, request.FILES)
        # print(form.data)
        # print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('visitor_activities')
    else:
        form = AteneoAffiliatedForm(initial={"aaVisitorID":aaVisitorID})
    return render(request, 'RizalLibrary/ateneo_affiliated_page.html', {'form': form})

def visitor_activities(request):
    if request.method == 'POST':
        visitorID = request.session.get('VisitorID')
        visitDate = request.POST.get("date")
        locationID = request.POST.get("visitLocation")
        if not visitDate:
            # messages.error(request, 'Please enter a valid date')
            return redirect('visitor_activities')
        else:
            visitDate = visitDate.split(',')
            startDate = '3000-01-01'
            endDate = '2000-01-01'
            # print(visitDate)
            for x in visitDate:
                x = datetime.strptime(x, "%m-%d-%Y")
                x = x.strftime('%Y-%m-%d')
                if x < startDate:
                    startDate = x
                if x > endDate:
                    endDate = x

                current_datetime = datetime.now()
                time_only = current_datetime.strftime("%H:%M:%S")
            
            VisitRequest.objects.create(startDate=startDate, endDate=endDate, visitorID=visitorID, locationID=locationID)
            visitRequestID = VisitRequest.objects.last().pk
            for x in visitDate:
                x = datetime.strptime(x, "%m-%d-%Y")
                x = x.strftime('%Y-%m-%d')
                VisitRequestDay.objects.create(dateOfVisit = x, visitRequestID=visitRequestID)
            for i in range(0,3):
                purpose = request.POST.get("purpose"+str(i))
                bookTitle = request.POST.get("bookTitle"+str(i))
                startPage = request.POST.get("startPage"+str(i))
                endPage = request.POST.get("endPage"+str(i))
                if not purpose:
                    break
                else:
                    Activity.objects.create(requestPurpose=purpose, bookTitle=bookTitle, startPage=startPage, endPage=endPage ,  visitorRequestID= visitRequestID)

            otherLocation = request.POST.get("visitOtherLocation")
            if otherLocation == "Yes":
                if locationID == "0": 
                    VisitRequest.objects.create(startDate=startDate, endDate=endDate, visitorID=visitorID, locationID=1)
                else:
                    VisitRequest.objects.create(startDate=startDate, endDate=endDate, visitorID=visitorID, locationID=0)
            visitRequestID = VisitRequest.objects.last().pk
            for x in visitDate:
                x = datetime.strptime(x, "%m-%d-%Y")
                x = x.strftime('%Y-%m-%d')
                VisitRequestDay.objects.create(dateOfVisit = x, visitRequestID=visitRequestID)
            for i in range(0,3):
                purpose = request.POST.get("purpose"+str(i))
                bookTitle = request.POST.get("bookTitle"+str(i))
                startPage = request.POST.get("startPage"+str(i))
                endPage = request.POST.get("endPage"+str(i))
                if not purpose:
                    break
                else:
                    Activity.objects.create(requestPurpose=purpose, bookTitle=bookTitle, startPage=startPage, endPage=endPage ,  visitorRequestID= visitRequestID)

            


        del request.session['VisitorID']
        request.session.modified = True
    
        return redirect('visitor_upload_success')
    return render(request, 'RizalLibrary/visitor_activities.html')

# TESTING EVENT UPLOAD - KEVIN

def event_upload(request):
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        location = request.POST.get("location")
        event_date = request.POST.get('event_date')
        participants_list = request.FILES.get('participants_list')
        
        # Determine locationID based on the selected radio button
        if location == "New_Rizal_Library":
            locationID = 0
        elif location == "SP":
            locationID = 1
        else:
            # Handle the case when no location is selected
            locationID = None
        
        # Creating a new instance of RegisterEvent
        new_event = RegisterEvent(
            eventName=event_name,
            locationID=locationID,
            eventDate=event_date,
            participantsList=participants_list
        )
        new_event.save()
        
        return redirect('visitor_upload_success')
    
    return render(request, 'RizalLibrary/event_upload.html')



# -------------------- for librarians --------------------

def empty_librarian(request):
    userInfo = AccountMoreInfo.objects.get(baseAccount = request.user)
    userAccountType = userInfo.accountType
    userLocation = userInfo.locationID
    return render(request, 'RizalLibrary/empty_librarian.html', {'userAccountType': userAccountType, 'userLocation': userLocation})
def librarian_check_request(request):
    userInfo = AccountMoreInfo.objects.get(baseAccount = request.user)
    userLocation = userInfo.locationID
    if userLocation == 0:
        userLocation = 'New Rizal Library'
    else:
        userLocation = 'Special Collections'
    # for x in user.accountmoreinfo.all:
    #     print(x)
    visitRequests = VisitRequest.objects.all()
    visitors = Visitor.objects.all()
    PartnerLibraries = PartnerLibrary.objects.all()
    AteneoAffiliateds = AteneoAffiliated.objects.all()
    NonAteneoAffiliateds = NonAteneoAffiliated.objects.all()
    VisitRequestDays = VisitRequestDay.objects.all()
    visitRequestPk = []
    visitRequestDay =[]
    visitRequestStatus = []
    visitRequestFKID = []
    
    for x in VisitRequestDays:
        visitRequestPk.append(x.pk)
        date_string = x.dateOfVisit.strftime('%Y-%m-%d')
        visitRequestDay.append(date_string)
        visitRequestStatus.append(x.visitStatus)
        visitRequestFKID.append(x.visitRequestID)

    Activitys = Activity.objects.all()
    Activitys = serialize('json', Activitys)

    visitorJSON = serialize('json', visitors)
    PartnerLibrariesJSON = serialize('json', PartnerLibraries)
    AteneoAffiliatedsJSON = serialize('json', AteneoAffiliateds)
    NonAteneoAffiliatedsJSON = serialize('json', NonAteneoAffiliateds)
    
    return render(request, 'RizalLibrary/librarian_check_request.html', {'visitors':visitors, 'PartnerLibraries':PartnerLibraries,'AteneoAffiliateds':AteneoAffiliateds, 'NonAteneoAffiliateds':NonAteneoAffiliateds,'visitRequests':visitRequests, 'VisitRequestDays':VisitRequestDays
                                                                         ,'visitRequestPk':visitRequestPk, 'visitRequestDay':visitRequestDay, 'visitRequestStatus':visitRequestStatus, 'visitRequestFKID':visitRequestFKID, 'Activitys':Activitys
                                                                         ,'visitorJSON':visitorJSON, 'PartnerLibrariesJSON':PartnerLibrariesJSON, 'AteneoAffiliatedsJSON':AteneoAffiliatedsJSON, 'NonAteneoAffiliatedsJSON':NonAteneoAffiliatedsJSON,
                                                                         'userInfo': userInfo, 'userLocation': userLocation})

def librarian_dashboard(request):
    userInfo = AccountMoreInfo.objects.get(baseAccount = request.user)
    userLocation = userInfo.locationID
    if userLocation == 0:
        userLocation = 'New Rizal Library'
    else:
        userLocation = 'Special Collections'
    todayVisitRequest = VisitRequestDay.objects.all()
    visitRequests = VisitRequest.objects.all()
    visitors = Visitor.objects.all()
    PartnerLibraries = PartnerLibrary.objects.all()
    AteneoAffiliateds = AteneoAffiliated.objects.all()
    NonAteneoAffiliateds = NonAteneoAffiliated.objects.all()

    visitorJSON = serialize('json', visitors)
    PartnerLibrariesJSON = serialize('json', PartnerLibraries)
    AteneoAffiliatedsJSON = serialize('json', AteneoAffiliateds)
    NonAteneoAffiliatedsJSON = serialize('json', NonAteneoAffiliateds)


    todayTime = datetime.now().date()
    return render(request, 'RizalLibrary/librarian_dashboard.html', {'visitors':visitors, 'PartnerLibraries':PartnerLibraries,'AteneoAffiliateds':AteneoAffiliateds, 'NonAteneoAffiliateds':NonAteneoAffiliateds, 'todayVisitRequest': todayVisitRequest, 'visitRequests': visitRequests, 'todayTime': todayTime,
                                                                         'visitorJSON':visitorJSON, 'PartnerLibrariesJSON':PartnerLibrariesJSON, 'AteneoAffiliatedsJSON':AteneoAffiliatedsJSON, 'NonAteneoAffiliatedsJSON':NonAteneoAffiliatedsJSON,
                                                                         'userInfo': userInfo, 'userLocation': userLocation})

def librarian_visitor_record(request):
    userInfo = AccountMoreInfo.objects.get(baseAccount = request.user)
    userLocation = userInfo.locationID
    if userLocation == 0:
        userLocation = 'New Rizal Library'
    else:
        userLocation = 'Special Collections'
    visitors = Visitor.objects.all()
    PartnerLibraries = PartnerLibrary.objects.all()
    AteneoAffiliateds = AteneoAffiliated.objects.all()
    NonAteneoAffiliateds = NonAteneoAffiliated.objects.all()
    visitorJSON = serialize('json', visitors)
    PartnerLibrariesJSON = serialize('json', PartnerLibraries)
    AteneoAffiliatedsJSON = serialize('json', AteneoAffiliateds)
    NonAteneoAffiliatedsJSON = serialize('json', NonAteneoAffiliateds)
    return render(request, 'RizalLibrary/librarian_visitor_record.html', {'visitors':visitors, 'PartnerLibraries':PartnerLibraries,'AteneoAffiliateds':AteneoAffiliateds, 'NonAteneoAffiliateds':NonAteneoAffiliateds,
                                                                          'visitorJSON':visitorJSON, 'PartnerLibrariesJSON':PartnerLibrariesJSON, 'AteneoAffiliatedsJSON':AteneoAffiliatedsJSON, 'NonAteneoAffiliatedsJSON':NonAteneoAffiliatedsJSON,
                                                                          'userInfo': userInfo, 'userLocation': userLocation})

def librarian_event_record(request):
    userInfo = AccountMoreInfo.objects.get(baseAccount = request.user)
    userLocation = userInfo.locationID
    if userLocation == 0:
        userLocation = 'New Rizal Library'
    else:
        userLocation = 'Special Collections'

        newEvent = RegisterEvent.objects.all()
    return render(request, 'RizalLibrary/librarian_event_record.html', {'newEvent':newEvent})

def approve_visitor(request,pk):
    if(request.method == "POST"):
        #  only Librarian and the same with the location can approve the visitor request
        userInfo = AccountMoreInfo.objects.get(baseAccount = request.user)
        userAccountType = userInfo.accountType
        if userAccountType == 'Admin':
            # print('Admin')
            return redirect('librarian_check_request')
        userLocation = userInfo.locationID
        currentRequestCheck = VisitRequest.objects.get(visitorRequestID = pk)
        if userLocation != currentRequestCheck.locationID:
            # print('Different Location')
            return redirect('librarian_check_request')

        #  change the status of the visitor request
        currentRequest = VisitRequest.objects.filter(visitorRequestID = pk).update(visitRequestStatus = 1)
        # change the status of the visitor request day
        currentRequestDays = VisitRequestDay.objects.all()
        for x in currentRequestDays:
            if x.visitRequestID == pk:
                VisitRequestDay.objects.filter(visitRequestID = pk).update(visitStatus = 1)

        # get the email of the visitor
        findingEmail = VisitRequest.objects.get(visitorRequestID=pk).visitorID
        findingEmail = Visitor.objects.get(visitorID=findingEmail).visitorEmail
        print(findingEmail)
        
        # send email with qr code
        send_email_with_qr(pk, findingEmail)

    return redirect('librarian_check_request')

def reject_visitor(request,pk):
    if(request.method == "POST"):
        #  change the status of the visitor request
        currentRequest = VisitRequest.objects.filter(visitorRequestID = pk).update(visitRequestStatus = 2)

        # change the status of the visitor request day
        currentRequestDays = VisitRequestDay.objects.all()
        for x in currentRequestDays:
            if x.visitRequestID == pk:
                VisitRequestDay.objects.filter(visitRequestID = pk).update(visitStatus = 4)

    return redirect('librarian_check_request')

def send_email_with_qr(requestID, visitorEmail):
    #   for creating qrcode
    data = requestID
    img = qrcode.make(data)
    imgName = 'RequestID' + str(requestID)
    img.save( imgName + '.png')

    # for sending email
    subject = 'Rizal Library Registration Confirmation'
    message = f'Hello,\n\nThank you for registering at the Rizal Library. Please present the QR code below to the librarian upon your visit.\n\nBest regards,\nRizal Library'
    recipient = [visitorEmail]
    # print(recipient)
    image_path = os.path.join(os.path.dirname(__file__), f'../{imgName}.png')

    if os.path.exists(image_path):
        # print('imageExist')
        # Open the file in binary mode
        # with open(image_path, 'rb') as file:
        #     image_data = file.read()
        #     image_name = f'{imgName}.png'
        email = EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            recipient
        )
        # Attach the image to the email
        email.attach_file(image_path)
        email.send()
        os.remove(image_path)

    else:
        print('imageNotExist')


# for qr code detection after pressing the button on base.html
def qrtest(request):
    qrData = qrDetect()
    
    #  only Librarian and the same with the location can approve the visitor request
    userInfo = AccountMoreInfo.objects.get(baseAccount = request.user)
    userAccountType = userInfo.accountType
    if userAccountType == 'Admin':
        # print('Admin')
        return redirect('librarian_dashboard')
    

    # update the visit status of the visit request day
    try:
        currentRequestDay = VisitRequestDay.objects.get(visitRequestID = qrData, dateOfVisit = datetime.now().strftime('%Y-%m-%d'))
        userLocation = userInfo.locationID
        currVisitRequest = VisitRequest.objects.get(visitorRequestID = qrData)
        if userLocation == currVisitRequest.locationID:
            if currentRequestDay:
                currentRequestDayFilter = VisitRequestDay.objects.filter(visitRequestID = qrData, dateOfVisit = datetime.now().strftime('%Y-%m-%d'))
                if currentRequestDay.visitStatus == 1:
                    currentRequestDayFilter.update(visitStatus = 2)
                    currentRequestDayFilter.update(arrivalTime = datetime.now().strftime('%H:%M:%S'))
                elif currentRequestDay.visitStatus == 2:
                    currentRequestDayFilter.update(visitStatus = 3)
                    currentRequestDayFilter.update(exitTime = datetime.now().strftime('%H:%M:%S'))
                elif currentRequestDay.visitStatus == 3:
                    currentRequestDayFilter.update(visitStatus = 2)
                    currentRequestDayFilter.update(arrivalTime = datetime.now().strftime('%H:%M:%S'))
                    currentRequestDayFilter.update(exitTime = None)
            # Store the alert message in the messages framework
        # User location is not the same with the location of the visitor request
        else:
            return redirect('librarian_dashboard')

            
    except VisitRequestDay.DoesNotExist:
        # messages.success(request, 'Your alert message goes here')
        pass
        
    return redirect('librarian_dashboard')

# for qr code detection
def qrDetect():
    cap = cv2.VideoCapture(0)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(3, 640)
    cap.set(4, 480)

    foundQR = False
    while not foundQR:
        success, img = cap.read()
            
        for qr in decode(img):
            # getting the data from the qr code
            myData = (qr.data.decode('utf-8'))
            #  for putting the rectangle around the qr code
            pts = np.array([qr.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], True, (0, 255, 0), 5)
            # for putting text above the video / maybe delete this for the final version
            pts2 = qr.rect
            cv2.putText(img, myData, (pts2[0],pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            foundQR = True
        cv2.imshow('QR Code', img)
        cv2.waitKey(1)
    cap.release()
    cv2.destroyAllWindows()
    # it returns the visitorID
    return (myData)

# not used anymore
def visitors(request):
    visitors = Visitor.objects.all()
    PartnerLibraries = PartnerLibrary.objects.all()
    if request.method == 'POST':
        visitorID = request.POST.get('visitorID')
        send_email_with_qr(visitorID)
        return render(request, 'RizalLibrary/visitors.html', {'visitors':visitors, 'PartnerLibraries':PartnerLibraries})

    return render(request, 'RizalLibrary/visitors.html', {'visitors':visitors, 'PartnerLibraries':PartnerLibraries})

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         Accounts = Account.objects.all()
#         for account in Accounts:
#             if account.librarianEmail == username and account.password == password:
#                 if account.accountType == 'librarian':
#                     return redirect('librarian_dashboard')
#                 elif account.accountType == 'admin':
#                     return redirect('adminDashboard')

#     return render(request, 'RizalLibrary/signin.html')

def adminDashboard(request):
    Users = User.objects.all()
    userInfo = AccountMoreInfo.objects.all()
    return render(request, 'RizalLibrary/admindashboard.html', {'Users':Users, 'userInfo':userInfo})

def edit_visitor(request, pk):
    # visitor = Visitor.objects.get(pk=pk)
    if request.method == 'POST':
        lastName = request.POST.get('lastName')
        firstName = request.POST.get('firstName')
        middleName = request.POST.get('middleName')
        visitorEmail = request.POST.get('visitorEmail')
        idNumber = request.POST.get('idNumber')
        Visitor.objects.filter(pk=pk).update(lastName=lastName, firstName=firstName, middleName=middleName, visitorEmail=visitorEmail, idNumber=idNumber)
        if Visitor.objects.get(pk=pk).visitorType == 'PartnerLibrary':
            librarianName = request.POST.get('librarianName')
            requestorName = request.POST.get('requestorName')
            requestorEmail = request.POST.get('requestorEmail')
            representativeName = request.POST.get('representativeName')
            representativeEmail = request.POST.get('representativeEmail')
            representativeID = request.POST.get('representativeID')
            PartnerLibrary.objects.filter(pk=pk).update(librarianName=librarianName, requestorName=requestorName, requestorEmail=requestorEmail, representativeName=representativeName, representativeEmail=representativeEmail, representativeID=representativeID)
        elif Visitor.objects.get(pk=pk).visitorType == 'NonAteneoAffiliated':
            naaType = request.POST.get('naaType')
            naaCompanions = request.POST.get('naaCompanions')
            NonAteneoAffiliated.objects.filter(pk=pk).update(naaType=naaType, naaCompanions=naaCompanions)
        elif Visitor.objects.get(pk=pk).visitorType == 'AteneoAffiliated':
            aaType = request.POST.get('aaType')
            aaYear = request.POST.get('aaYear')
            aaCourse = request.POST.get('aaCourse')
            aaLastSem = request.POST.get('aaLastSem')
            AteneoAffiliated.objects.filter(pk=pk).update(aaType=aaType, aaYear=aaYear, aaCourse=aaCourse, aaLastSem=aaLastSem)

    return redirect('librarian_visitor_record')


def create_user(request):
    accountTypeSelect = request.POST.get('accountTypeSelect')
    locationSelect = request.POST.get('locationSelect')

    emailInput = request.POST.get('emailInput')
    passwordInput = request.POST.get('passwordInput')
    confirmPasswordInput = request.POST.get('confirmPasswordInput')
    print(accountTypeSelect, locationSelect, emailInput, passwordInput, confirmPasswordInput)
    if not accountTypeSelect or not locationSelect or not emailInput or not passwordInput or not confirmPasswordInput:
        # messages.error(request, 'Please fill all fields')
        return redirect('adminDashboard')
    else:
        print('asd')
        if passwordInput == confirmPasswordInput:
            print('sad')
            User.objects.create_user(password=passwordInput, username=emailInput)
            if locationSelect == 'NewRizalLibrary':
                AccountMoreInfo.objects.create(baseAccount=User.objects.last(), locationID=0, accountType=accountTypeSelect)
            else:
                AccountMoreInfo.objects.create(baseAccount=User.objects.last(), locationID=1, accountType=accountTypeSelect)
            
            print('success')
        else:
            # messages.error(request, 'Passwords do not match')
            return redirect('adminDashboard')
    
    return redirect('adminDashboard')


