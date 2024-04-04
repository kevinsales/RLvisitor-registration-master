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

class Location(models.Model):
    locationID = models.AutoField(primary_key = True)
    building = models.CharField(max_length=50)

    def getLocationID(self):
        return self.locationID
    
    def getBuilding(self):
        return self.building

class Account(models.Model):
    librarianEmail = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    locationID = models.ForeignKey(Location, on_delete=models.CASCADE)
    accountType = models.CharField(max_length=50)

    def getLibrarianEmail(self):
        return self.librarianEmail
    
    def getPassword(self):
        return self.password
    
    def getLocationID(self):
        return self.locationID.locationID # if this doesnt work imma remove this idk how to do a func for a foreign key

    def getAccountType(self):
        return self.accountType
    
class Visitor(models.Model):
    visitorID = models.AutoField(primary_key = True)
    lastName = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50, blank=True)
    visitorEmail = models.EmailField(max_length=100)
    idNumber = models.CharField(max_length=50)
    affiliation = models.CharField(max_length=100)

    PARTNER_LIBRARY = 'PartnerLibrary'
    NON_ATENEO_AFFILIATED = 'NonAteneoAffiliated'
    ATENEO_AFFILIATED = 'AteneoAffiliated'

    VISITOR_TYPE_CHOICES = [
        (PARTNER_LIBRARY, 'Partner Library'),
        (NON_ATENEO_AFFILIATED, 'Non Ateneo Affiliated'),
        (ATENEO_AFFILIATED, 'Ateneo Affiliated'),
    ]

    visitorType = models.CharField(
        max_length=50,
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
        return f"Visitor ID: {self.visitorID}, Name: {self.lastName}, {self.firstName} {self.middleName}, Email: {self.visitorEmail}, ID Number: {self.idNumber}, Type: {self.visitorType}" 

class PartnerLibrary(models.Model):
    plVisitorID = models.IntegerField(primary_key = True) 
    librarianName = models.CharField(max_length = 100) 
    requestorName = models.CharField(max_length = 100)
    requestorEmail = models.EmailField(max_length = 100)
    representativeName = models.CharField(max_length = 100, blank=True)
    representativeEmail = models.EmailField(max_length = 100, blank=True)
    representativeID = models.CharField(max_length=100, blank=True)

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
        return f"PL Visitor Info: {self.plVisitorID}, {self.librarianName}, {self.requestorName}, {self.requestorEmail}, {self.representativeName}, {self.representativeEmail}, Type: {self.representativeID}"

class AteneoAffiliated(models.Model):
    aaVisitorID = models.AutoField(primary_key = True)
    aaYear = models.IntegerField(4) # idk if this is correct
    aaCourse = models.CharField(max_length=50)
    aaLastSem = models.CharField(max_length=50, null=True) # idk if this is correct 
    
    aaIDPhoto= models.FileField(blank=True)
    aaPaymentConfirmation = models.FileField(blank=True)

    ALUMNI = 'ALUMNI (Admu)'
    BEU = 'Basic Education Unit (BEU)'
    LOA = 'Leave of Absence (LOA)'
    
    VISITOR_TYPE_CHOICES = [
        (ALUMNI, 'ALUMNI (Admu)'),
        (BEU, 'Basic Education Unit (BEU)'),
        (LOA, 'Leave of Absence (LOA)'),
    ]

    aaType = models.CharField(
        max_length=50,
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
        return f"AA Visitor Info: {self.aaVisitorID}, {self.aaType}, {self.aaYear}, {self.aaIDPhoto}, {self.aaCourse}, {self.aaLastSem}"

class NonAteneoAffiliated(models.Model):
    naaVisitorID = models.AutoField(primary_key = True)
    naaCompanions = models.CharField(max_length=100)

    #  change this later (remove blank=True) 
    #  change this later (remove blank=True)
    #  change this later (remove blank=True)
    naaInvitation = models.FileField(blank=True)
    naaPaymentConfirmation = models.FileField(blank=True)

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
        max_length=50,
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
        return f"NAA Info: {self.naaVisitorID}, {self.naaType}, {self.naaCompanions}, {self.naaInvitation}, {self.naaPaymentConfirmation}"

class Event(models.Model):
    eventPassID = models.AutoField(primary_key = True)
    eventName = models.CharField(max_length=100)
    participantsNum = models.IntegerField()
    pointPerson = models.CharField(max_length = 100)
    eventDate = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    librarianEmail = models.ForeignKey(Account, on_delete=models.CASCADE)
    locationID = models.ForeignKey(Location, on_delete=models.CASCADE)

    def getEventPassID(self):
        return self.eventPassID 
    
    def getEventName(self):
        return self.eventName
    
    def getParticipantsNum(self):
        return self.participantsNum 
    
    def getPointPerson(self):
        return self.pointPerson
    
    def getEventDate(self):
        return self.eventDate
    
    def getStartTime(self):
        return self.startTime
    
    def getEndTime(self):
        return self.endTime
    
    def getLibrarianEmail(self):
        return self.librarianEmail
    

class VisitRequest(models.Model):
    visitorRequestID = models.AutoField(primary_key = True)
    startDate = models.DateField()
    endDate = models.DateField()
    visitorID = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    eventPassID = models.ForeignKey(Event, on_delete=models.CASCADE)

    def getVisitorRequestID(self):
        return self.visitorRequestID
    
    def getStartDate(self):
        return self.startDate
    
    def getEndDate(self):
        return self.endDate
    
    def __str__(self):
        return f"{self.visitorRequestID}, {self.startDate}, {self.endDate}, {self.visitorID}, {self.eventPassID}"

class VisitRequestDay(models.Model):
    visitRequestDayID = models.AutoField(primary_key = True)
    dateOfVisit = models.DateField()
    visitTime = models.TimeField()
    visitStatus = models.CharField(max_length = 50)
    visitRequestID = models.ForeignKey(VisitRequest, on_delete=models.CASCADE)

    def getVisitRequestDayID(self):
        return self.visitRequestDayID
    
    def getDateOfVisit(self):
        return self.dateOfVisit
    
    def getVisitTime(self):
        return self.visitTime
    
    def getVisitStatus(self):
        return self.visitStatus
    
    def __str__(self):
        return f"{self.visitRequestDayID}, {self.dateOfVisit}, {self.visitTime}, {self.visitStatus}, {self.visitRequestID}"


class Activity(models.Model):
    activityID = models.AutoField(primary_key = True)
    requestPurpose = models.CharField(max_length=225)
    bookTitle = models.CharField(max_length = 225)
    startPage = models.IntegerField(5)
    endPage = models.IntegerField(5)
    visitorRequestID = models.ForeignKey(VisitRequest, on_delete=models.CASCADE)

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

class AccountVisitRequest(models.Model):
    librarianEmail = models.ForeignKey(Account, on_delete=models.CASCADE)
    visitRequestID = models.ForeignKey(VisitRequest, on_delete=models.CASCADE)

class LocationVisitRequest(models.Model):
    locationID = models.ForeignKey(Location, on_delete=models.CASCADE)
    visitorRequestID = models.ForeignKey(VisitRequest, on_delete=models.CASCADE)
    locationSection = models.CharField(max_length = 50)

    def getLocationSection(self):
        return self.locationSection


