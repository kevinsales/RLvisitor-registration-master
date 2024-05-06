# HOW TO START SERVER:
# Navigate to BADProject Directory
# BADScripts\Scripts\activate
# python3 manage.py makemigrations
# python3 manage.py migrate 
# python3 manage.py runserver

# python manage.py makemigrations
# python manage.py migrate 
# python manage.py runserver


from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    # locationID = models.AutoField(primary_key = True, validators=)
    # 0 = New Rizal Library
    # 1 = Old Rizal Library / Special Collections
    locationID = models.AutoField(primary_key = True)
    building = models.CharField(max_length=30)
    objects = models.Manager()
    def getLocationID(self):
        return self.locationID
    
    def getBuilding(self):
        return self.building


        

class AccountMoreInfo(models.Model):
    baseAccount = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accountmoreinfo', null=True)
    locationID = models.SmallIntegerField()
    
    # Librarian
    # Admin

    USER_TYPE_CHOICES = [
    ('Librarian','Librarian'),
    ('Admin', 'Admin'),
    ]

    accountType = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
    )
    objects = models.Manager()

    def getBaseAccount(self):
        return self.baseAccount
    def __str__(self) :
        return self.baseAccount.username

#  not using this because i'm using User model from django because it provides authentication
class Account(models.Model):

    librarianEmail = models.EmailField(max_length=100)

    # min length of password is 8
    password = models.CharField(max_length=50)
    locationID = models.SmallIntegerField(max_length=2)
    

    # Librarian
    # Admin
    accountType = models.CharField(max_length=20)
    objects = models.Manager()

    def getLibrarianEmail(self):
        return self.librarianEmail
    
    def getPassword(self):
        return self.password
    
    def getLocationID(self):
        return self.locationID.locationID # if this doesnt work imma remove this idk how to do a func for a foreign key

    def getAccountType(self):
        return self.accountType
    
class Visitor(models.Model):
    visitorID = models.AutoField(primary_key = True, max_length=5)
    lastName = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50, blank=True)
    visitorEmail = models.EmailField(max_length=100)
    idNumber = models.CharField(max_length=50)
    affiliation = models.CharField(max_length=100)

    objects = models.Manager()

    PARTNER_LIBRARY = 'PartnerLibrary'
    NON_ATENEO_AFFILIATED = 'NonAteneoAffiliated'
    ATENEO_AFFILIATED = 'AteneoAffiliated'

    VISITOR_TYPE_CHOICES = [
        (PARTNER_LIBRARY, 'Partner Library'),
        (NON_ATENEO_AFFILIATED, 'Non Ateneo Affiliated'),
        (ATENEO_AFFILIATED, 'Ateneo Affiliated'),
    ]

    visitorType = models.CharField(
        max_length=22,
        choices=VISITOR_TYPE_CHOICES,
        default=ATENEO_AFFILIATED,
    )

    def getVisitorID(self):
        return self.visitorID
    
    def getLastName(self):
        return self.lastName
    
    def getFirstName(self):
        return self.firstName
    
    def getMiddleName(self):
        return self.middleName
    
    def getVisitorEmail(self):
        return self.visitorEmail
    
    def getIDNumber(self):
        return self.idNumber 
    
    def getAffiliation(self):
        return self.affiliation
    
    def getVisitorType(self):
        return self.visitorType
    
    def __str__(self):
        return f"{self.visitorID},{self.lastName},{self.firstName},{self.middleName},{self.visitorEmail},{self.idNumber},{self.visitorType},{self.affiliation}" 

class PartnerLibrary(models.Model):
    plVisitorID = models.SmallIntegerField(primary_key = True, max_length=5) 
    librarianName = models.CharField(max_length = 100) 
    requestorName = models.CharField(max_length = 100)
    requestorEmail = models.EmailField(max_length = 100)
    representativeName = models.CharField(max_length = 100, blank=True)
    representativeEmail = models.EmailField(max_length = 100, blank=True)
    representativeID = models.CharField(max_length=100, blank=True)

    objects = models.Manager()

    def getPLVisitorID(self):
        return self.plVisitorID
    
    def getLibrarianName(self):
        return self.librarianName
    
    def getRequestorName(self):
        return self.requestorName
    
    def getRequestorEmail(self):
        return self.requestorEmail
    
    def getRepresentativeName(self):
        return self.representativeName
    
    def getRepresentativeEmail(self):
        return self.representativeEmail
    
    def getRepresentativeID(self):
        return self.representativeID
    
    def __str__(self):
        return f"{self.plVisitorID},{self.librarianName},{self.requestorName},{self.requestorEmail},{self.representativeName},{self.representativeEmail},{self.representativeID}"

class AteneoAffiliated(models.Model):
    aaVisitorID = models.SmallIntegerField(primary_key = True, max_length=5)
    #  change it to not null / blank = required
    aaYear = models.IntegerField(max_length=4) 
    aaCourse = models.CharField(max_length=50, blank=True)
    aaLastSem = models.CharField(max_length=50, blank=True)
    aaIDPhoto= models.ImageField(upload_to='images/AF/id')
    aaPaymentConfirmation = models.ImageField(upload_to='images/AF/payment')

    objects = models.Manager()

    ALUMNI = 'ALUMNI (Admu)'
    BEU = 'Basic Education Unit (BEU)'
    LOA = 'Leave of Absence (LOA)'
    
    VISITOR_TYPE_CHOICES = [
        (ALUMNI, 'ALUMNI (Admu)'),
        (BEU, 'Basic Education Unit (BEU)'),
        (LOA, 'Leave of Absence (LOA)'),
    ]

    aaType = models.CharField(
        max_length=32,
        choices=VISITOR_TYPE_CHOICES,
        default=ALUMNI,
    )

    def getAAVisitorID(self):
        return self.aaVisitorID
    
    def getAAType(self):
        return self.aaType
    
    def getAAYear(self):
        return self.aaYear
    
    def getAACourse(self):
        return self.aaCourse
    
    def getAAInvitation(self):
        return self.aaInvitation 
    def getAAPaymentConfirmation(self):
        return self.aaPaymentConfirmation 
    
    def __str__(self):
        return f"{self.aaVisitorID},{self.aaType},{self.aaYear},{self.aaIDPhoto},{self.aaCourse},{self.aaLastSem},{self.aaPaymentConfirmation}"

class NonAteneoAffiliated(models.Model):
    naaVisitorID = models.SmallIntegerField(primary_key = True, max_length=5)
    naaCompanions = models.CharField(max_length=100)
    naaInvitation = models.ImageField(upload_to='images/NAF/invitation')
    naaPaymentConfirmation = models.ImageField(upload_to='images/NAF/payment') 
    objects = models.Manager()

    PUBLIC_RESEARCHER = 'Public Researcher'
    LIBRARY_GUEST = 'Library Guest '
    VENDOR_SUPPLIER = 'Vendor/Supplier'

    #  It's hard to see from phone
    # VISITOR_TYPE_CHOICES = [
    #     (PUBLIC_RESEARCHER, 'Public Researcher (incl. from Private Institutions, Graduate, Undergraduate, etc.)'),
    #     (LIBRARY_GUEST, 'Library Guest (Rizal Library Exhibit guests, and guests with special arrangements)'),
    #     (VENDOR_SUPPLIER, 'Vendor/Supplier (e.g. book vendors, maintenance, etc.)'),
    # ]

    VISITOR_TYPE_CHOICES = [
        (PUBLIC_RESEARCHER, 'Public Researcher'),
        (LIBRARY_GUEST, 'Library Guest'),
        (VENDOR_SUPPLIER, 'Vendor/Supplier'),
    ]

    naaType = models.CharField(
        max_length=29,
        choices=VISITOR_TYPE_CHOICES,
        default=LIBRARY_GUEST,
    )


    def getNAAVisitorID(self):
        return self.naaVisitorID 
    
    def getNAAType(self):
        return self.naaType
    
    def getNAACompanions(self):
        return self.naaCompanions 
    
    def getNAAInvitation(self):
        return self.naaInvitation
    
    def getNAAPaymentConfirmation(self):
        return self.naaPaymentConfirmation 
    
    def __str__(self):
        return f"{self.naaVisitorID},{self.naaType},{self.naaCompanions}, {self.naaInvitation}, {self.naaPaymentConfirmation}"

# OLD EVENT CLASS
class Event(models.Model):
    eventPassID = models.AutoField(primary_key = True)
    eventName = models.CharField(max_length=100)
    participantsNum = models.SmallIntegerField()
    pointPerson = models.CharField(max_length = 100)
    eventDate = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    librarianEmail = models.ForeignKey(Account, on_delete=models.CASCADE)
    locationID = models.ForeignKey(Location, on_delete=models.CASCADE)
    objects = models.Manager()

# NEW EVENT CLASS
class RegisterEvent(models.Model):
    eventID = models.AutoField(primary_key = True)
    eventName = models.CharField(max_length=100)
    # 0 = New Rizal Library
    # 1 = Old Rizal Library / Special Collections
    locationID = models.SmallIntegerField()
    eventDate = models.DateField()
    participantsList = models.FileField(upload_to="files/event")
    objects = models.Manager()

class VisitRequest(models.Model):
    visitorRequestID = models.AutoField(primary_key = True)
    startDate = models.DateField()
    endDate = models.DateField()
    
    visitorID = models.IntegerField(null=True)
    # visitorID = models.ForeignKey(Visitor, on_delete=models.CASCADE, null=True)

    eventPassID = models.IntegerField(null=True, blank=True)
    # eventPassID = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    
    # 0 = New Rizal Library
    # 1 = Old Rizal Library / Special Collections
    locationID = models.SmallIntegerField()
    
    
    # 0 = pending
    # 1 = accepted
    # 2 = rejected
    visitRequestStatus = models.SmallIntegerField(default = 0, max_length=1)

    objects = models.Manager()

    def getVisitorRequestID(self):
        return self.visitorRequestID
    
    def getStartDate(self):
        return self.startDate
    
    def getEndDate(self):
        return self.endDate
    
    def __str__(self):
        return f"{self.visitorRequestID}, {self.startDate}, {self.endDate}, {self.visitorID}, {self.eventPassID}, {self.visitRequestStatus}"

class VisitRequestDay(models.Model):
    visitRequestDayID = models.AutoField(primary_key = True, max_length=5)
    dateOfVisit = models.DateField()
    arrivalTime = models.TimeField(null=True)
    exitTime = models.TimeField(null=True)

    # 0 = pending
    # 1 = accepted
    # 2 = entered
    # 3 = left
    # 4 = rejected
    visitStatus = models.SmallIntegerField(default = 0)

    visitRequestID = models.SmallIntegerField()
    # visitRequestID = models.ForeignKey(VisitRequest, on_delete=models.CASCADE)
    objects = models.Manager()

    def getVisitRequestDayID(self):
        return self.visitRequestDayID
    
    def getDateOfVisit(self):
        return self.dateOfVisit

    
    def getVisitStatus(self):
        return self.visitStatus
    
    def __str__(self):
        return f"{self.visitRequestDayID}, {self.dateOfVisit}, {self.visitStatus}, {self.visitRequestID}"


class Activity(models.Model):
    activityID = models.AutoField(primary_key = True)
    requestPurpose = models.CharField(max_length=15)
    bookTitle = models.CharField(max_length = 225)
    startPage = models.SmallIntegerField()
    endPage = models.SmallIntegerField()

    visitorRequestID = models.SmallIntegerField()
    # visitorRequestID = models.ForeignKey(VisitRequest, on_delete=models.CASCADE)

    
    # otherLocationID = models.CharField(max_length = 4)

    objects = models.Manager()

    def getActivityID(self):
        return self.activityID
    
    def getRequestPurpose(self):
        return self.requestPurpose
    
    def getBookTitle(self):
        return self.bookTitle
    
    def getStartPage(self):
        return self.startPage
    
    def getEndPage(self):
        return self.endPage
    
    def __str__(self):
        return f"{self.activityID}, {self.requestPurpose}, {self.bookTitle}, {self.startPage}, {self.endPage}, {self.visitorRequestID}"



#  ---------------------------------------------------
# class AccountVisitRequest(models.Model):
#     librarianEmail = models.ForeignKey(Account, on_delete=models.CASCADE)
#     visitRequestID = models.ForeignKey(VisitRequest, on_delete=models.CASCADE)
#     objects = models.Manager()


# class LocationVisitRequest(models.Model):
#     locationID = models.ForeignKey(Location, on_delete=models.CASCADE)
#     # visitorRequestID = models.ForeignKey(VisitRequest, on_delete=models.CASCADE)
#     locationSection = models.CharField(max_length = 50)
#     objects = models.Manager()

#     def getLocationSection(self):
#         return self.locationSection


