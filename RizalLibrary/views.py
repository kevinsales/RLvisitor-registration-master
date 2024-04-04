from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import *

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

            # for testing purpose
            # print(form['plVisitorID'].value())
            # print(form['librarianName'].value())
            # print(form['requestorName'].value())
            # print(form['requestorEmail'].value())
            # print(form['representativeName'].value())
            # print(form['representativeEmail'].value())
            # print(form['representativeID'].value())
            # for x in form:
            #     print(x)
            # for creating qrcode
            # data = form['plVisitorID'].value()
            # img = qrcode.make(data)
            # img.save('MyQRCode11.png')
            return redirect('visitor_activities')
    else:
        form = PartnerLibraryForm(initial={"plVisitorID":plVisitorID})
    return render(request, 'RizalLibrary/partner_library_page.html', {'form': form})


def non_ateneo_affiliated_page(request):
    naaVisitorID = request.session.get('VisitorID')
    form = NonAteneoAffiliatedForm({"naaVisitorID": naaVisitorID})
    if request.method == 'POST':
        updated_request = request.POST.copy()
        updated_request.update({'naaVisitorID': naaVisitorID})
        form = NonAteneoAffiliatedForm(updated_request)
        if form.is_valid():
            NonAteneoAffiliated = form.save()
            return redirect('visitor_activities')
    else:
        form = NonAteneoAffiliatedForm(initial={"naaVisitorID":naaVisitorID})
    return render(request, 'RizalLibrary/non_ateneo_affiliated_page.html', {'form': form})


def ateneo_affiliated_page(request):
    aaVisitorID = request.session.get('VisitorID')
    form = AteneoAffiliatedForm({"aaVisitorID": aaVisitorID})
    if request.method == 'POST':
        updated_request = request.POST.copy()
        updated_request.update({'aaVisitorID': aaVisitorID})
        form = AteneoAffiliatedForm(updated_request)
        if form.is_valid():
            NonAteneoAffiliated = form.save()
            return redirect('visitor_activities')
    else:
        form = AteneoAffiliatedForm(initial={"aaVisitorID":aaVisitorID})
    return render(request, 'RizalLibrary/ateneo_affiliated_page.html', {'form': form})

def visitor_activities(request):
    if request.method == 'POST':
        return redirect('visitor_upload_success')
    return render(request, 'RizalLibrary/visitor_activities.html')

def event_upload(request):
    return render(request, 'RizalLibrary/event_upload.html')

def visitors(request):
    visitors = Visitor.objects.all()
    PartnerLibraries = PartnerLibrary.objects.all()
    if request.method == 'POST':
        visitorID = request.POST.get('visitorID')
        send_email_with_qr(visitorID)
        return render(request, 'RizalLibrary/visitors.html', {'visitors':visitors, 'PartnerLibraries':PartnerLibraries})

    return render(request, 'RizalLibrary/visitors.html', {'visitors':visitors, 'PartnerLibraries':PartnerLibraries})


def send_email_with_qr(visitorID):
    #   for creating qrcode
    data = visitorID
    img = qrcode.make(data)
    imgName = 'VisitorID' + str(visitorID)
    img.save( imgName + '.png')

    # for sending email
    subject = 'Rizal Library Registration Confirmation'
    visitor = Visitor.objects.get(pk=visitorID)
    message = 'testing'
    recipient = [visitor.visitorEmail]
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
    # it returns the visitorID
    print(qrData)
    return redirect('visitors')

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
    return (myData)