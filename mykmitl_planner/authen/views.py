from django.contrib import messages
from django.shortcuts import render,redirect
from django.views import View
from allauth.account.forms import SignupForm, LoginForm
from django.contrib.auth import login, logout  # Import Django's login function
from planner.models import Student
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .forms import ProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
class SignInPage(View):
    
    def get(self, request):
        form = LoginForm()  # ใช้ฟอร์มล็อกอินจาก allauth
        return render(request, "account/signin.html", {
            'form': form  # ส่งฟอร์มไปยัง template
        })

    def post(self, request):
        form = LoginForm(request.POST, request=request)  # Pass the request to the form
        if form.is_valid():
            user = form.user  
            
            # ตรวจสอบว่าผู้ใช้ยืนยันอีเมลแล้วหรือไม่
            if not user.emailaddress_set.filter(verified=True).exists():
                # หากผู้ใช้ยังไม่ได้ยืนยันอีเมล
                messages.error(request, "Please verify your email before logging in.")
                return render(request, "account/signin.html", {
                    'form': form
                })

            messages.success(request, "You have signed in successfully.")
            login(request, user)  # ใช้ฟังก์ชัน login ของ Django เพื่อทำการล็อกอิน
            return redirect('planner_dashboard')  # Redirect หลังจากล็อกอินสำเร็จ
        else:
            # ฟอร์มไม่ถูกต้อง ส่งกลับพร้อมข้อผิดพลาด
            messages.error(request, "Invalid email or password. Please try again.")
            return render(request, "account/signin.html", {
                'form': form
            })


class SignUpPage(View):
    def get(self, request):
        form = SignupForm()
        return render(request, "account/signup.html", {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            # ตรวจสอบว่าอีเมลลงท้ายด้วย '@kmitl.ac.th'
            email = form.cleaned_data.get('email')
            if not email.endswith('@kmitl.ac.th'):
                messages.error(request, "You must use a KMITL email address (kmitl.ac.th)")
                return render(request, "account/signup.html", {'form': form})

            try:
                # บันทึกผู้ใช้
                user = form.save(self.request)
                userid = User.objects.get(username=user.username)
                
                # สร้างข้อมูล Student
                Student.objects.create(
                    student_user=userid,
                    email=user.email
                )
                
                email_address = user.emailaddress_set.get(email=user.email) 
                if not email_address.verified:
                    email_address.send_confirmation(self.request)  # ส่งอีเมลยืนยันอีกครั้งหากยังไม่ได้ยืนยัน
                
                messages.success(request, "You have signed up successfully.")
                return redirect('account_email_confirmation')
            except ValueError as e:
                return render(request, "account/signup.html", {'form': form})
        else:
            return render(request, "account/signup.html", {'form': form})

class EmailConfirmationSentView(View):
    
    def get(self, request):
        return render(request, "account/email_confirmemail.html", {})    

class LogOutPage(View):
    
    def get(self, request):
        logout(request)
        messages.success(request, "You have been logged out successfully.")
        return redirect('account_login')
    
class EditProfile(View):
    
    def get(self, request):
        # ดึงข้อมูลโปรไฟล์ของผู้ใช้ปัจจุบัน
        student = Student.objects.get(student_user=request.user)
        form = ProfileForm(instance=student)
        formpass = PasswordChangeForm(user=request.user)
        
        return render(request, "editaccount.html", {
            'form': form,
            'formpass' : formpass,
            'student': student,  
        })

    def post(self, request):

        student = Student.objects.get(student_user=request.user)
        form = ProfileForm(request.POST, request.FILES, instance=student)

        if form.is_valid():
            form.save()  # บันทึกข้อมูลที่แก้ไข
            messages.success(request, "update profile successfully")
            return redirect('profile')  # เปลี่ยนเส้นทางไปยังหน้าดูโปรไฟล์
        
        return render(request, "editaccount.html", {
            'form': form,
            'student': student,
        })

class PasswordChangeView(View):

    def post(self, request):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password has been changed successfully.")
            return redirect('profile')  # Redirect ไปหน้าโปรไฟล์หรือหน้าอื่นที่ต้องการ
        else:
            messages.error(request, "There was an error with your form. Please try again.")
            return render(request, 'account/password_change.html', {
                'form': form
            })