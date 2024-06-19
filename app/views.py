from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse
import json
from django.http import JsonResponse, HttpResponseForbidden
from django.views.generic import TemplateView
from .models import StudentResponse, ExpertResponse

MAX = 10

class HomePageView(TemplateView):
    template_name = "home.html"

class InstructionsPageView(TemplateView):
    template_name = "instructions.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve the current user
        current_user = self.request.user
        # Retrieve the current_response associated with the current user and split it into an array of sentences
        current_response = current_user.current_response.id
        context['current_response_id'] = current_response # Send array of sentences to html page
        return context


class TaggingPageView(TemplateView):
    template_name = "tagging.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve the current user
        current_user = self.request.user
        # Retrieve the current_response associated with the current user and split it into an array of sentences
        current_response = current_user.current_response.response.split(".")
        context['current_response'] = current_response # Send array of sentences to html page
        context['id'] = current_user.current_response.id - 1 # This represent the number of responses the user has completed 
        return context
    
    
def save_data(request):
    try:
        # Get the current user + username
        current_user = request.user

        # Get the current_response associated with the current user
        current_response = current_user.current_response

        # Get the data from the POST request
        data = json.loads(request.body)

        # Iterate through object, retrieve data, create ExpertResponse object, and save it to database
        for entry in data:
            sentence = entry.get('sentence')
            knowledge = entry.get('knowledge')
            confidence = entry.get('confidence')
            strength = entry.get('strength')
            comment = entry.get('comments')

            # Create ExpertResponse and associate it with the current_response
            expert_response = ExpertResponse.objects.create(
                    user=current_user,
                    sentence=sentence,
                    knowledge=knowledge,
                    confidence=confidence,
                    strength=strength,
                    comments=comment,
                )

            # Associate the ExpertResponse with the current_response
            current_response.expert_responses.add(expert_response)  

        # Get the next student response object in the database
        next_response = StudentResponse.objects.filter(id__gt=current_response.id).first()

        # Update the current_response of the current user to the next response
        current_user.current_response = next_response
        current_user.save()

        return JsonResponse({'message': 'Data saved successfully'})
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data provided'}, status=400)
      
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

class ThanksPageView(TemplateView):
    template_name = "thanks.html"

class ExpertReviewView(TemplateView):
    template_name = "review.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve the current user
        current_user = self.request.user
        context['id'] = current_user.current_response.id - 1 # This represent the number of responses the user has completed 
        context['range'] = range(1, MAX + 1)
        return context

def handle_selection(request):
    if request.method == "POST":
        
        selected_value = request.POST.get('selected_value')

        student_response = get_object_or_404(StudentResponse, pk=selected_value)  # Assuming 'selected_value' is a primary key
        
        current_user = request.user
        experts = student_response.expert_responses.filter(user=current_user)

        student_response_list = student_response.response.split(".")

        # Store data in session
        request.session['student_response'] = student_response_list
        request.session['experts'] = [
            {'sentence': expert.sentence, 'user': expert.user.username, 'knowledge': expert.knowledge, 'confidence': expert.confidence, 'strength': expert.strength, 'comments': expert.comments} for expert in experts
        ]

        return redirect('review_pt2')  # Adjust the redirect URL as needed

def review_pt2(request):
    student_response = request.session.get('student_response', [])
    experts = request.session.get('experts', [])

    colored_student_response = []
    expert_sentences = {review['sentence'].strip() for review in experts}

    for sentence in student_response:
        full_sentence = sentence.strip() + "."  # Add period and strip any extra spaces
        if full_sentence in expert_sentences:
            modify_sentence = f"<span style='color: blue'>{sentence}.</span>"
        else:
            modify_sentence = f"<span style='color: black'>{sentence}.</span>"
        colored_student_response.append(modify_sentence)
        
    context = {
        'student_response': colored_student_response,
        'experts': experts,
    }

    return render(request, 'review_pt2.html', context)

def superuser_only_view(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to access this page.")
    # Your view logic here
    return render(request, 'superuser_only_page.html')

    


    
