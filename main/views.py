from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from .models import State, District, SocietyType, Application,Society,Bank,Liquidation,User
import difflib
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import hashlib
import random
import os
import base64


def stateWiseList(request):
    states = State.objects.all()
    stateList = []
    count = 1
    for state in states:
        entries = Society.objects.filter(state=state).count()
        stateList.append([count,state.stateName,entries])
        count = count + 1
    return HttpResponse(json.dumps(stateList), content_type="application/json")

def calenderWiseList(request):
    years = {}
    societies = Society.objects.all()
    for society in societies:
        if society.Date != None:
            years[society.Date.year] = years.get(society.Date.year,0) + 1
    dataArr = []
    for key in years:
        dataArr.append([key,years[key]])
    dataArr.sort(key=lambda x: x[0])
    count = 1
    for i in range(len(dataArr)):
        dataArr[i] = [count,dataArr[i][0],dataArr[i][1]]
        count = count + 1
    return HttpResponse(json.dumps(dataArr), content_type="application/json")

def financialYearWiseList(request):
    years = {}
    societies = Society.objects.all()
    for society in societies:
        if society.Date is not None:
            year = society.Date.year
            if society.Date.month >= 4:
                year += 1
            years[year] = years.get(year, 0) + 1
    
    dataArr = []
    for key in years:
        dataArr.append([key, years[key]])
    dataArr.sort(key=lambda x: x[0])
    
    count = 1
    for i in range(len(dataArr)):
        dataArr[i] = [count,str(dataArr[i][0]-1)+"-"+str(dataArr[i][0]), dataArr[i][1]]
        count += 1
    return HttpResponse(json.dumps(dataArr), content_type="application/json")

def ReceivedApplication(request):
    applications = Application.objects.all()
    dataArr = []
    count = 1
    for application in applications:
        receivedDate = application.receivedDate
        disposalDate = application.disposalDate
        if receivedDate is not None:
            receivedDate = receivedDate.strftime("%d-%m-%Y")
        else:
            receivedDate = ""
        if disposalDate is not None:
            disposalDate = disposalDate.strftime("%d-%m-%Y")
        else:
            disposalDate = ""
        dataArr.append([count,application.societyName,application.state.stateName,application.district.districtName,application.societyType.societyType,receivedDate,disposalDate])
        count = count + 1
    return HttpResponse(json.dumps(dataArr), content_type="application/json")

def searchRecord(request):
    societies = Society.objects.all()
    dataArr = []
    count = 1
    for society in societies:
        if  society.societyType != None:
            societyType = society.societyType.societyType
        else:
            societyType = ""
        if society.Date != None:
            date = society.Date.strftime("%d-%m-%Y")
        else:
            date = ""
        if society.Address != None:
            address = society.Address
        else:
            address = ""
        if society.state != None:
            state = society.state.stateName
        else:
            state = ""
        if society.district != None:
            district = society.district.districtName
        else:
            district = ""
        dataArr.append([count,society.societyName,address,state,district,date,societyType])
        count = count + 1
    return HttpResponse(json.dumps(dataArr), content_type="application/json")

def liquidationList(request):
    liquidations = Liquidation.objects.all()
    dataArr = []
    count = 1
    for liquidation in liquidations:
        if liquidation.societyName != None:
            society = liquidation.societyName
        else:
            society = ""
        if liquidation.state != None:
            state = liquidation.state.stateName
        else:
            state = ""
        if liquidation.nameOfLiquidator != None:
            nameOfLiquidator = liquidation.nameOfLiquidator
        else:
            nameOfLiquidator = ""
        if liquidation.appoinmentDate != None:
            appoinmentDate = liquidation.appoinmentDate.strftime("%d-%m-%Y")
        else:
            appoinmentDate = ""
        if liquidation.validityDate != None:
            validityDate = liquidation.validityDate.strftime("%d-%m-%Y")
        else:
            validityDate = ""
        if liquidation.status != None:
            status = liquidation.status
        else:
            status = ""
        dataArr.append([count,society,state,nameOfLiquidator,appoinmentDate,validityDate,status])
        count = count + 1
    return HttpResponse(json.dumps(dataArr), content_type="application/json")

def bankList(request):
    banks = Bank.objects.all()
    dataArr = []
    count = 1
    for bank in banks:
        if bank.bankName != None:
            bankName = bank.bankName
        else:
            bankName = ""
        if bank.Address != None:
            Address = bank.Address
        else:
            Address = ""
        if bank.state != None:
            state = bank.state.stateName
        else:
            state = ""
        if bank.district != None:
            district = bank.district.districtName
        else:
            district = ""
        dataArr.append([count,bankName,Address,state,district])
        count = count + 1
    return HttpResponse(json.dumps(dataArr), content_type="application/json")

def registeredUsers(request):
    users = User.objects.all()
    dataArr = []
    count = 1
    for user in users:
        if user.date != None:
            date = user.date.strftime("%d-%m-%Y")
        else:
            date = ""
        if user.state != None:
            state = user.state.stateName
        else:
            state = ""
        if user.district != None:
            district = user.district.districtName
        else:
            district = ""
        if user.societyType != None:
            societyType = user.societyType.societyType
        else:
            societyType = ""
        dataArr.append([count,user.name,state,district,societyType,date])
        count = count + 1
    return HttpResponse(json.dumps(dataArr), content_type="application/json")

def stateFetcher(request):
	states = State.objects.all()
	dataArr = []
	for state in states:
		dataArr.append(state.stateName)
	return HttpResponse(json.dumps(dataArr), content_type="application/json")

def districtFetcher(request):
	state = request.GET.get('state')
	state = State.objects.get(stateName=state)
	districts = District.objects.filter(state=state)
	dataArr = []
	for district in districts:
		dataArr.append(district.districtName)
	return HttpResponse(json.dumps(dataArr), content_type="application/json")

def societyTypeFetcher(request):
	typeCode = request.GET.get('typeCode','society')
	societyTypes = SocietyType.objects.filter(typeCode=typeCode).all()
	dataArr = []
	for societyType in societyTypes:
		dataArr.append(societyType.societyType)
	dataArr.sort()
	return HttpResponse(json.dumps(dataArr), content_type="application/json")

def societyNameFetcher(request):
	societyType = request.GET.get('societyType')
	district = request.GET.get('district','')
	state = request.GET.get('state','')
	societyType = SocietyType.objects.get(societyType=societyType)
	societies = Society.objects.filter(societyType=societyType)
	if state != '':
		state = State.objects.get(stateName=state)
		societies = societies.filter(state=state)
		if district != '':
			district = District.objects.get(districtName=district)
			societies = societies.filter(district=district).all()
		else:
			societies = societies.all()
	else:
		societies = societies.all()
	dataArr = []
	for society in societies:
		dataArr.append(society.societyName)
	dataArr.sort()
	return HttpResponse(json.dumps(dataArr), content_type="application/json")

@csrf_exempt
def userRegistration(request):
    if request.method == "POST":
        state = request.POST.get('state')
        district = request.POST.get('district')
        SocietyTypeStr = request.POST.get('SocietyType')
        socName = request.POST.get('socName')
        address = request.POST.get('address')
        panNo = request.POST.get('panNo')
        tanNo = request.POST.get('tanNo')
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        mobileNo = request.POST.get('mobileNo')
        email = request.POST.get('email')
        serviceTaxNo = request.POST.get('serviceTaxNo')
        password = request.POST.get('password')
        cnfpassword = request.POST.get('cnfpassword')

        if password != cnfpassword:
            return HttpResponse(json.dumps({"error":"passwords do not match"}), content_type="application/json")
        elif len(password) < 8:
            return HttpResponse(json.dumps({"error":"password should be atleast 8 characters long"}), content_type="application/json")
        elif User.objects.filter(email=email).exists():
            return HttpResponse(json.dumps({"error":"email already exists"}), content_type="application/json")
        elif User.objects.filter(mobileNo=mobileNo).exists():
            return HttpResponse(json.dumps({"error":"mobile number already exists"}), content_type="application/json")
        elif User.objects.filter(panNo=panNo).exists():
            return HttpResponse(json.dumps({"error":"pan number already exists"}), content_type="application/json")
        elif User.objects.filter(tanNo=tanNo).exists():
            return HttpResponse(json.dumps({"error":"tan number already exists"}), content_type="application/json")
        elif User.objects.filter(taxNo=serviceTaxNo).exists():
            return HttpResponse(json.dumps({"error":"service tax number already exists"}), content_type="application/json")
        else:
            password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            user = User()
            user.name = name
            user.state = State.objects.filter(stateName=state).first()
            user.district = District.objects.filter(districtName=district).first()
            user.societyType = SocietyType.objects.filter(societyType = SocietyTypeStr ).first()
            user.society = Society.objects.filter(societyName =socName ).first()
            user.date = datetime.today().date()
            user.panNo = panNo
            user.tanNo = tanNo
            user.address = address
            user.designation = designation 
            user.mobileNo = mobileNo
            user.email = email
            user.taxNo = serviceTaxNo
            user.password = password
            user.save()
            return HttpResponse(json.dumps({"msg":"success"}), content_type="application/json")

    return HttpResponse(json.dumps("you were not supposed be here"), content_type="application/json")

def captchaFecther(request):
    if request.method == "GET":
        captcha = random.choice(os.listdir("media/captcha"))
        with open("media/captcha/"+captcha, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        encoded_string = encoded_string.decode('utf-8')
        captcha = captcha.split(".")[0]
        captcha = hashlib.sha256(captcha.encode('utf-8')).hexdigest()
        return HttpResponse(json.dumps({"captcha":captcha,"img":encoded_string}), content_type="application/json")

@csrf_exempt
def deleteSociety(request):
	if request.method == "POST":
		name = request.POST.get('name')
		socType = request.POST.get('socType')
		state = request.POST.get('state')
		district = request.POST.get('district','')
		print(name,socType,state,district)
		societyType = SocietyType.objects.filter(societyType=socType).first()
		societies = Society.objects.filter(societyName=name,societyType=societyType)
		if state != '':
			stateObj = State.objects.get(stateName=state)
			societies = societies.filter(state=stateObj)
			if district != '':
				districtObj = District.objects.get(districtName=district)
				society = societies.filter(district=districtObj).first()
			else:
				society = societies.first()
		else:
			society = societies.first()
		print(society)
		society.delete()
		return HttpResponse("The society has been deleted")
	return HttpResponse(json.dumps("you were not supposed be here"), content_type="application/json")

@csrf_exempt
def loginUser(request):
    if request.method == "POST":
        mobileNo = request.POST.get('mobileNo')
        password = request.POST.get('password')
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        
        user= User.objects.filter(mobileNo=mobileNo).first()
        if user != None:
            if(password == user.password):
                request.session['status'] = "logined"
                
                return HttpResponse(json.dumps(request.session['status'] ), content_type="application/json")
            else:
                return HttpResponse(json.dumps("Invalid ID-pass "), content_type="application/json")
        else:
            return HttpResponse("user does not exists")
        
        
    return HttpResponse(json.dumps("you were not supposed be here"), content_type="application/json")


@csrf_exempt
def societyCountFetcher(request):
    socTypes = SocietyType.objects.filter(typeCode="society").all()
    states = State.objects.all()
    temparr = []
    for socType in socTypes:
        temp = {}
        temp['type'] = socType.societyType
        temp['count'] = Society.objects.filter(societyType=socType).count()
        temp["states"] = []
        if (temp['count'] != 0):
            for state in states:
                temp2 = {}
                temp2['state'] = state.stateName
                temp2['count'] = Society.objects.filter(societyType=socType,state=state).count()
                if (temp2['count'] != 0):
                    temp["states"].append(temp2)
        temparr.append(temp)
    return HttpResponse(json.dumps(temparr), content_type="application/json")



def dataManipulator(request):
    return HttpResponse("done")