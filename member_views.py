from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Enrollment, Feedback, Query_Doubts

def check_session(request):
    """Utility function to check if user is logged in."""
    if "session_key" not in request.session:
        messages.error(request, "You need to log in to access this page.")
        return False
    return True

def registration(request):
    if request.method == "GET":
        return render(request, 'class_app/member/registration.html')
    
    if request.method == "POST":
        # Gather the form data
        stu_name = request.POST.get("name")
        stu_email = request.POST.get("email")
        stu_phone = request.POST.get("phone")
        stu_city = request.POST.get("city")
        stu_address = request.POST.get("address")
        stu_choosecourse = request.POST.getlist("coursename")
        stu_pic = request.FILES.get("studentPic")

        # Validation (You can enhance this further)
        if not stu_name or not stu_email or not stu_phone or not stu_city or not stu_address or not stu_choosecourse or not stu_pic:
            messages.error(request, "All fields are required!")
            return render(request, 'class_app/member/registration.html')

        # Create and save the student object
        student_obj = Enrollment(
            name=stu_name,
            email=stu_email,
            phone_no=stu_phone,
            city=stu_city,
            address=stu_address,
            choose_course=','.join(stu_choosecourse),
            fee_status=False,
            stu_pic=stu_pic
        )
        student_obj.save()
        
        messages.success(request, "❤️❤️ Registration Completed Successfully ❤️❤️  ||  For ID and Password, please pay 500 Rupees via UPI (6389593152) and then check your mail for ID and password.")
        return redirect("registration")  # Redirect to the same page or a success page

    # Fallback for unexpected request methods
    return render(request, 'class_app/member/registration.html')
def student_dashboard(request): 
    if not check_session(request):
        return redirect("student_login")
    
    stu_id = request.session["session_key"]
    stu_object = get_object_or_404(Enrollment, student_id=stu_id)
    context = {"student_key": stu_object}
    return render(request, 'class_app/member/student_dashboard.html', context)

def logout(request):
    request.session.flush()  # Clear the entire session
    messages.success(request, "You have been logged out successfully.")
    return redirect("student_login")

def student_login(request):
    if request.method == "GET":
        return render(request, 'class_app/member/student_login.html')
    
    if request.method == "POST":
        stud_id = request.POST.get("ID")
        stud_password = request.POST.get("password")
        student_list = Enrollment.objects.filter(student_id=stud_id, password=stud_password, fee_status=True)

        if student_list.exists():
            student_obj = student_list.first()
            request.session["session_key"] = stud_id
            request.session["role"] = "student"

            context = {"student_key": student_obj}
            return render(request, 'class_app/member/student_dashboard.html', context)
        else:
            messages.error(request, "Invalid User ID or your fee has not been submitted.")
            return redirect("student_login")

def feedback(request):
    if not check_session(request):
        return redirect("student_login")

    if request.method == "GET":
        return render(request, "class_app/member/feedback.html")

    if request.method == "POST":
        user_name = request.POST.get("name")
        user_email = request.POST.get("email")
        user_remark = request.POST.get("rating")
        user_review = request.POST.get("review")
        
        feedback_obj = Feedback(name=user_name, email=user_email, rating=user_remark, review=user_review)
        feedback_obj.save()
        
        messages.success(request, "Thank you for your valuable feedback! 👍👍")
        return redirect("feedback")

def querydoubt(request):
    if not check_session(request):
        return redirect("student_login")

    if request.method == "GET":
        return render(request, 'class_app/member/query_doubt.html')
    
    if request.method == "POST":
        user_name = request.POST.get("name")
        user_email = request.POST.get("email")
        user_subject = request.POST.get("subject")
        user_question = request.POST.get("question")

        query_doubt_obj = Query_Doubts(name=user_name, email=user_email, subject=user_subject, question=user_question)
        query_doubt_obj.save()
        
        messages.success(request, "Your query has been submitted successfully! 👍")
        return redirect("querydoubt")

def view_answer(request):
    if not check_session(request):
        return redirect("student_login")
    
    id = request.session["session_key"]
    answer_list = Query_Doubts.objects.filter(member_id=id)
    context = {"answer_key": answer_list}

    return render(request, 'class_app/member/view_answer.html', context)

def viewprofile(request):
    if not check_session(request):
        return redirect("student_login")
    
    id = request.session["session_key"]
    stu_object = get_object_or_404(Enrollment, student_id=id)
    
    context = {
        "student_key": stu_object,
        "resource": stu_object.resource_file  # Assuming resource_file is a single file field
    }
    
    return render(request, 'class_app/member/view_profile.html', context)

def rating(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'class_app/member/ratings.html', {'feedbacks': feedbacks})

def connectedmediaclass(request):
    if not check_session(request):
        return redirect("student_login")
    
    # Render a relevant page or provide proper context here
    return render(request, 'class_app/member/some_other_page.html')  # Replace with a relevant page

