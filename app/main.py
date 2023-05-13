from flask import Flask, redirect, url_for, render_template, request, session, flash,  send_from_directory
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.graphics import renderPDF
from datetime import datetime
import csv
from random import randint
import pickle 
PDF_ROOT = './pdfs/'
csvfile = 'Data.csv'
binfile = 'informations.pickle'

data = {}
app = Flask(__name__)
app.config['SECRET_KEY'] = 'randomsecretkey'
app.config['UPLOAD_FOLDER'] = PDF_ROOT
app.config['CSV_FOLDER'] = csvfile

def rollnogen(state):
    words = state.split()
    prefix = ''
    if 'kerala' in state.lower():
        prefix += 'KL'
    else:
        if len(words) > 1:
            for i in words:
                prefix += i[0]
        else:
            prefix = state[:2]
    prefix = prefix.upper()
    prefix += str(randint(10000000, 99999999))
    return prefix



def pdfgen(data):
    for key, value in data.items():
        if type(value) == str:
            data[key] = value.upper()
    ROLLNO =  data['rollno']
    FILENAME = f"{data['name']}-{ROLLNO}.pdf"
    cname = 'ST DOMINIC PUBLIC SCHOOL'
    caddr1 = 'OLLUKKARA P.O KALATHODE, THRISSUR,'
    caddr2 = '680263, KERALA'
    c = canvas.Canvas(os.path.join('./pdfs', FILENAME), pagesize=A4)
    c.setAuthor("2023-2024 St Jude XII CS")
    c.setTitle("Registration")
    c.setSubject("SEE Hall ticket.")
    # border outlines
    c.line(20, 530, 20, 820)  # left line 1
    c.line(20, 520, 20, 80)  # left line 2
    c.line(20, 820, 575, 820)  # top line
    c.line(575, 820, 575, 80)  # right line
    c.line(575, 80, 20, 80)  # bottom line


    # outlines
    c.line(20, 590, 400, 590)
    c.line(20, 710, 575, 710)
    c.line(20, 530, 400, 530)
    c.line(400, 710, 400, 530)
    c.line(20, 520, 575, 520)
    c.line(400, 680, 575, 680) 
    c.line(435, 670, 435, 540)
    c.line(435, 670, 540, 670)
    c.line(435, 540, 540, 540)
    c.line(540, 670, 540, 540)
    c.line(20, 485, 575, 485)
    c.line(20,460 , 575, 460)
    c.line(20,435 , 575, 435)
    c.line(20,410 , 575, 410)
    c.line(100,410 , 100, 520 )
    c.line(250,410 , 250, 520 )
    c.line(320,410 , 320, 520 )
    c.line(450,410 , 450, 520 )
    c.line(20,360 , 575, 360)
    c.line(20,330 , 575, 330)
    c.line(40,210 , 555, 210)
    c.line(40,175 , 555, 175)
    c.line(40,150 , 555, 150)
    c.line(40,125 , 555, 125)
    c.line(40,100 , 555, 100)
    c.line(40, 210, 40, 100)
    c.line(110, 210, 110, 100)
    c.line(260, 210, 260, 100)
    c.line(320, 210, 320, 100)
    c.line(440, 210, 440, 100)
    c.line(555, 210, 555, 100)
    c.drawInlineImage('logo.png', 30, 713, height=105, width=105)

    # static writings
    c.setFont("Helvetica-Bold", 19)
    c.drawString(200, 790, "ST JUDE PUBLIC SCHOOL")
    c.setFont("Helvetica", 9)
    c.drawString(145, 775, 'Resgistered Under Section XXI of Societies Registration Act 1860; Registration Number:X-XXXX')
    c.setFont("Helvetica-Bold", 10)
    c.drawString(130, 765,'Examination Office: #15, Block-II, Bypass Road, Kuttenellur PO, Thrissur-680014')
    c.setFont("Helvetica", 13)
    c.drawString(180, 750,'Standard Entrance Examination 2022-2023')
    c.drawString(230, 735,'(SEE- SEEP/SEEC/SEEM)')
    c.setFont("Helvetica-Bold", 15)
    c.drawString(270, 720,'Hall Ticket')  
    c.setFont("Helvetica", 13)
    c.drawString(30, 690,'Student\'s Name: ')
    c.drawString(30, 670,'F/M                   : ')
    c.drawString(30, 650,'Date Of Birth    : ')
    c.drawString(30, 630,'Name Of Your School: ')
    c.drawString(30, 600,'Place Of Study: ')  
    c.setFont("Helvetica-Bold", 11)
    c.drawString(30, 575,'Name & Address of Test Center: ')
    c.drawString(30, 562, cname)
    c.setFont("Helvetica", 11)
    c.drawString(30, 550,caddr1)
    c.drawString(30, 540, caddr2)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(420, 690,f"Roll No: {ROLLNO}")
    c.setFont("Helvetica", 9)
    c.drawString(450, 620,"Paste Your Recent")
    c.drawString(460, 607,"Passport Size ")
    c.drawString(463, 594,"Picture Here")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, 500, 'Subject')
    c.setFont("Helvetica-Bold", 11)
    c.drawString(110, 500, 'Examination Date & Time')
    c.drawString(260, 500, 'Language')
    c.drawString(335, 500, 'Student\'s Signature')
    c.drawString(455, 500, 'Invigilator\'s Signature')
    c.setFont("Helvetica-Bold", 10)
    c.drawString(40, 470, 'Physics')
    c.drawString(40, 445, 'Chemistry')
    c.drawString(40, 420, 'Maths')
    c.setFont("Helvetica", 10)
    c.drawString(270, 470, 'English')
    c.drawString(270, 445, 'English')
    c.drawString(270, 420, 'English')
    c.setFont("Helvetica", 9)
    c.drawString(105, 470, '27-Jan-2023, 8.30 am to 10.30 am')
    c.drawString(105, 445, '27-Jan-2023, 11.30 am to 1.30 pm')
    c.drawString(105, 420, '27-Jan-2023, 2.30 pm to 4.30 pm')
    c.setFont("Helvetica-Bold", 8)
    c.drawString(30, 400, 'OFFICE COPY')
    c.setFont("Courier-BoldOblique", 9)
    c.drawString(85, 390, 'NOTE: INVIGILATOR IS REQUESTED TO TEAR AND HANDOVER HE STUDENT COPY TO CANDITATE.')
    c.drawString(40, 370, f'{"-"* 31} (Invigilator- Please Tear Here) {"-"* 31}')
    c.setFont("Helvetica-Bold", 11)
    c.drawString(40, 340, 'ST JUDE SSE 2022-2023 (SEE- SEEP/SEEC/SEEM)           Hall Ticket')
    c.setFont("Helvetica", 13)
    c.drawString(30, 310,'Student\'s Name : ')
    c.drawString(30, 290,'F\M                    :')
    c.drawString(30, 270,'Roll Number      : ')
    c.drawString(30, 250,'Examination Center: ')
    c.drawString(30, 230,'Address             : ')
    c.setFont("Helvetica-Bold", 12)
    c.drawString(55, 190, 'Subject')
    c.setFont("Helvetica-Bold", 10)
    c.drawString(115, 190, 'Examination Date & Time')
    c.drawString(265, 190, 'Language')
    c.drawString(335, 190, 'Student\'s Signature')
    c.drawString(445, 190, 'Invigilator\'s Signature')
    c.setFont("Helvetica", 10)
    c.drawString(272, 160, 'English')
    c.drawString(272, 135, 'English')
    c.drawString(272, 110, 'English')
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, 160, 'Physics')
    c.drawString(50, 135, 'Chemistry')
    c.drawString(50, 110, 'Maths')
    c.setFont("Helvetica", 9)
    c.drawString(117, 160, '27-Jan-2023, 8.30 am to 10.30 am')
    c.drawString(117, 135, '27-Jan-2023, 11.30 am to 1.30 pm')
    c.drawString(117, 110, '27-Jan-2023, 2.30 pm to 4.30 pm')

    # Dynamic content
    c.setFont("Helvetica", 13)
    c.drawString(130, 690,data['name'])
    c.drawString(130, 670,data['fname'])
    c.drawString(130, 650,data['dob'])
    c.drawString(165, 630,data['sname'])
    c.drawString(130, 600,f"{data['sdist']} {data['sstate']} - {data['spin']}")
    c.drawString(140, 310,data['name'])
    c.drawString(140, 290,data['fname'])
    c.drawString(140, 270, ROLLNO)
    c.drawString(160, 250, cname)
    c.drawString(140, 230,caddr1+caddr2)
    c.setFont("Times-BoldItalic", 10)
    c.drawString(40, 65, 'Warning: THIS IS A FAKE HALL TICKET FOR EDUCATIONAL PURPOSE ONLY, IT DOES')
    c.drawString(40, 50, 'NOT CORRESPOND TO ANY REAL EXAMINATION CONDUCTED BY THE ST JUDE ON THE DATE')
    c.drawString(40, 35, 'MENTIONED ABOVE AND THE HALL TICKET DESIGN IS INSPIRED FROM THE NSE HALL-TICKET')
    c.setFont("Courier-BoldOblique", 10)
    c.drawString(40, 20, f'Issued On: {str(datetime.now())}')

    c.showPage()
    c.save()
    return FILENAME
def writecsv(path):
    with open(path, 'rb') as f1:
        with open('./csv/informations.csv', 'w+', newline='') as f:
            header = True
            try:
                while True:
                    data = pickle.load(f1)              
                    writer = csv.writer(f)
                    if header == True:
                        writer.writerow(data.keys())
                        header = False
                    if len(data) != 0:
                        writer.writerow(data.values())
            except EOFError:
                print('finished')


def writepickle(data):
    with open(binfile, 'ab') as f:
        pickle.dump(data, f)


def getentry(rollno, email):
    with open(binfile, 'rb') as f:
        try:
            while True:
                data = pickle.load(f)
                if data['rollno'] == rollno and data['email'].upper()== email.upper():
                    return data
        except EOFError:
            return 0



@app.route('/signin/', methods=['POST'])
def signin():
    if request.method == 'POST':
        name = request.form['name']
        mail = request.form['email']
        if len(mail) != 0 and len(name) != 0:
            data['name'] = name
            data['mail'] = mail
            return redirect(url_for('register',email= mail, usrname=name))
        else:
            return redirect(url_for('home'))


@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=('GET', 'POST'))
def home():
    return render_template('signin.html')


@app.route('/gethallticket/<rollno>')
def gethallticket(rollno):
    return render_template('gethallticket.html', rollnum=rollno)



@app.route('/finalregister', methods=['POST'])
def finalregister():
    if request.method == 'POST':
        d = request.form
        data = {
            'name': d['fname']+' ' + d['lname'],
            'fname':d['fathername'],
            'dob': d['dob'],
            'gender': d['gender'],
            'addhr': d['adhr'],
            'email':  d['email'],
            'phno':d['phno'],
            'class':  d['class'],
            'sname': d['schlname'],
            'saddr': d['schladdr'],
            'scity': d['schlcity'],
            'sdist': d['schldist'],
            'sstate':d['schlstate'],
            'spin':  d['schlpin'],
            'board':  d['medium'],
            'hname':  d['hname'],
            'haddr':  d['haddr'],
            'hcity':  d['hcity'],
            'hdist': d['hdist'],
            'hstate': d['hstate'],
            'hpin': d['hpin'],
            'rollno': rollnogen(d['schlstate'])


        }
        filename = writepickle(data)
        return redirect(url_for('afterregistration', rollno = data['rollno'], email=data['email']))
    else:
        return redirect(url_for('home'))

@app.route('/registrationstatus/<rollno>&<email>')
def afterregistration(rollno, email):
    return render_template('afterregistration.html', rollnum = rollno, email=email)

@app.route('/dwld')
def dwld():
    writecsv(binfile)
    return send_from_directory(directory='./csv', path='informations.csv')


@app.route('/getpdf/', methods=['POST'])
def pdfdwld():
    if request.method == 'POST':
        d = request.form
        rollno = d['rollno'].upper()
        email = d['email'].upper()
        data = getentry(rollno, email)
        if data != 0:
            filename = pdfgen(data)
            return send_from_directory(directory='./pdfs', path=filename)
        else:
            return redirect(url_for('gethallticket', rollno=rollno))


@app.route('/register?email=<email>&usrname=<usrname>', methods=['GET', 'POST'])
def register(usrname, email):
    return render_template('register.html', usrname=usrname, email=email)

@app.route('/registerstatus?filename=<filename>')
def success(filename):
    return send_from_directory(directory=PDF_ROOT, path=filename)



@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404



if __name__ == '__main__':
	app.run(debug=True)



