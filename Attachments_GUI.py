import email
from email.mime.image import MIMEImage
from tkinter import * 
from tkinter import filedialog
import smtplib #mail transfer protocol 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
import os.path
from email.mime.application import MIMEApplication

#Global Variables
attachments = []

def attachFile():
    filename = filedialog.askopenfilename(initialdir='C:/', title='Select a file')
    attachments.append(filename)
    attachmentLabel = Label(root, text=f'Attached {str(len(attachments))} files ', width=25, fg='green', font=('bold',10))
    attachmentLabel.place(x=300, y=550)

def reset():
    emailE.delete(0, 'end')
    paswordE.delete(0, 'end')
    senderE.delete(0, 'end')
    ccInp.delete(0, 'end')
    studyTitleInp.delete(0, 'end')
    refNoInp.delete(0, 'end')
    amendmentNoInp.delete(0, 'end')
    amendmentDateInp.delete(0, 'end')
    #email sent successfully/error
    label_6 = Label(root, text='', width=25, font=('bold',10))
    label_6.place(x=20, y=550)
    #remove attachments
    attachments.clear()
    attachmentLabel = Label(root, text='', width=25, font=('bold',10))
    attachmentLabel.place(x=300, y=550)
  
#GUI
root = Tk()
root.geometry('500x640')
root.title('LTHT Amendment Sender')
#title screen
Label_0 = Label(root, text='Enter Your Email Account', width=20, fg='#3CB371', font=('bold',20))
Label_0.place(x=50, y=33)

#email lablel- text field
Label_1 = Label(root, text='Your Email Account:', width=20,  font=('bold',10))
Label_1.place(x=20, y=110)
#######
#for getting entry input
inpMail = StringVar()
inpPass = StringVar()
inpSender = StringVar()
inpCC = StringVar()
inpSubject = StringVar()
inpStudyTitle = StringVar()
inpRefNo = StringVar()
inpAmendmentNo = StringVar()
inpAmendmentDate = StringVar()

#######
#email input field
emailE = Entry(root, width=40, textvariable=inpMail)
emailE.place(x=175, y=110)

#Password label
Label_2 = Label(root, text='Your Password:', width=20,  font=('bold',10))
Label_2.place(x=20, y=160)
#Password input field
paswordE = Entry(root, width=40, show="*", textvariable=inpPass)
paswordE.place(x=175, y=160)


#Amendment Section
amendementLabel = Label(root, text='Amendment Details', fg='#CD5C5C', width=20,  font=('bold',20))
amendementLabel.place(x=20, y=210)

#Sendtoemail label
Label_3 = Label(root, text='Send to Email:', width=20,  font=('bold',10))
Label_3.place(x=20, y=260)
#Sendtoemail input field
senderE = Entry(root, width=40, textvariable=inpSender)
senderE.place(x=175, y=260)


#CC Label
cc = Label(root, text='CC Email:', width=20,  font=('bold',10))
cc.place(x=20, y=310)
#CC input
ccInp = Entry(root, width=40, textvariable=inpCC)
ccInp.place(x=175, y=310)

#StudyTitle Label
studyTitle = Label(root, text='Study Title:', width=20,  font=('bold',10))
studyTitle.place(x=20, y=360)
#Study title input
studyTitleInp = Entry(root, width=40, textvariable=inpStudyTitle)
studyTitleInp.place(x=175, y=360)

#R&I No Label
refNo = Label(root, text='R&I No:', width=20,  font=('bold',10))
refNo.place(x=20, y=410)
#R&I No input
refNoInp = Entry(root, width=40, textvariable=inpRefNo)
refNoInp.place(x=175, y=410)

#AmendmentNo Label
amendmentNo = Label(root, text='Amendment No:', width=20,  font=('bold',10))
amendmentNo.place(x=20, y=460)
#AmendmentNo input
amendmentNoInp = Entry(root, width=40, textvariable=inpAmendmentNo)
amendmentNoInp.place(x=175, y=460)

#Amendment Date Label
amendmentDate = Label(root, text='Amendment Date:', width=20,  font=('bold',10))
amendmentDate.place(x=20, y=510)
#Amendment Date input
amendmentDateInp = Entry(root, width=40, textvariable=inpAmendmentDate)
amendmentDateInp.place(x=175, y=510)


def sendAmendment():
    # print(str(inpMail
    #.get()))
    # print(str(Rpswrd.get()))
    # print(str(Rsender.get()))
    # print(str(Rsubject.get()))
    # #message body
    # print(msgbodyE.get(1.0, 'end'))


    htmlStudyTitle = inpStudyTitle.get()
    htmlRefNo = inpRefNo.get()
    htmlAmendmentNo = inpAmendmentNo.get()
    htmlAmendmentDate = inpAmendmentDate.get()
    subject = f'R&I No: {htmlRefNo} | {htmlAmendmentNo} | Amendment Acknowledgement'
    html_body =f"""
<html>
<body style="font-family:Calibri;">
Dear All,

<h4 style='color:rgb(73,135,210); font-size:16px; weight:bold;'><strong>Re. {htmlStudyTitle}<br>
R&I No: {htmlRefNo}</strong></h4>

<p>Thank you for fowarding the amendment below:</p>
<ul>
<li><strong>Amendment Number: {htmlAmendmentNo}</strong></li>
<li><strong>Amendment Date: {htmlAmendmentDate}</strong></li>
</ul>

<p>The R&I team follow the Health Research Authority <a href="#">UK wide process on the handling of amendments</a> and we acknowledge receipt of this amendment. 
The HRA process presumes implementation of the amendment <strong>unless an objection is raised by the NHS organisation</strong> within 35 days of receipt of the amendment. </p>

<p style='color:rgb(210,79,73); text-decoration:underline'><strong>There will be no further email issued by the R&I team regarding the implementation of  this amendment.</strong></p>

<p><strong>Research Team POC/Principal Investigator:</strong> You must consider whether any Key Service Support (KSS) departments are affected by this change. 
If so, it is your responsibility contact the relevant team to request their continued support for the amendment outlining the proposed changes. It is also your responsibility to notify the sponsor of this.
If there is an expected impact on local delivered as a result of the amendment, 
<strong>then you must confirm with the sponsor that you are unable to implement the amendment within the 35 day expected timeline.</strong>
If you are able to implement sooner you can contact the sponsor and advise them of this.</p>

<p><i>Please note <strong>you must not</strong> implement this amendment until all relevant regulatory approvals are in place. 
This will be communicated to you by the sponsor.</i></p>

<p><i>If there is an amendment to the contract due to this amendment, then the sponsor should inform you of the next steps.</i></p>

</body>
</html>
    """

    try:
        message=MIMEMultipart()
        message['From'] = str(inpMail.get())
        message['To'] = str(inpSender.get())
        message['Cc'] = str(inpCC.get())
        message['Subject'] = subject
        message.attach(MIMEText(html_body, 'html'))

        for f in attachments:
            with open(f, 'rb') as a_file:
                basename = os.path.basename(f)
                part = MIMEApplication(a_file.read(), Name=basename)

            part['Content-Disposition'] = 'attachment; filename="%s"' % basename
            message.attach(part)

        server=smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(str(inpMail.get()), str(inpPass.get()))
        text = message.as_string()
        server.sendmail(str(inpMail.get()), str(inpSender.get()), text)
        #Success Label
        label_6 = Label(root, text='Email sent successfully', width=25, fg='green', font=('bold',10))
        label_6.place(x=20, y=550)

        server.quit()
    except:
        #Error Label
        label_6 = Label(root, text='Ooops, something went wrong!!', width=25, fg='red', font=('bold',10))
        label_6.place(x=20, y=550)

#Send Button
Button(root, text='Send', width=10, bg='#1E90FF', fg='white', command=sendAmendment, font=('bold',10)).place(x=60, y=590)
#Attach Button
Button(root, text='Attachments', width=10, bg='#1E90FF', fg='white', command=attachFile, font=('bold',10)).place(x=360, y=590)
#Reset Button
Button(root, text='Reset', width=10, bg='#1E90FF', fg='white', command=reset, font=('bold',10)).place(x=210, y=590)

root.mainloop()