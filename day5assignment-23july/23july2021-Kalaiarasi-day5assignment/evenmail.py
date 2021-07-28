import smtplib
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("kalai.iprimed@gmail.com","Kalai@2404")
n=int(input("enter num:"))
even=""
for i in range(0,n):
    x=int(input())
    if(x%2==0):
       even=even+""+str(x)
message=even
connection.sendmail("kalai.iprimed@gmail.com","pkalai2404@gmail.com",message)
print("email send sucessfully")
connection.quit()