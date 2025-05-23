from django.shortcuts import render,redirect

from .models import Problem, SolvedProblem
from random import choice
from django.core.paginator import Paginator

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect

def problem_list(request):
    try:
        user = request.user  

        if not user.is_authenticated:
            return redirect('login')

        # Get IDs of problems solved by the user
        solved_problem_ids = SolvedProblem.objects.filter(user=user).values_list('problem_id', flat=True)

        # Base queryset excluding solved problems, with explicit ordering
        problems = Problem.objects.exclude(id__in=solved_problem_ids).order_by('id')

        # Filter by difficulty
        difficulty = request.GET.get('difficulty')
        if difficulty:
            problems = problems.filter(difficulty__iexact=difficulty)

        # Filter by status (todo, solved, attempted)
        status = request.GET.get('status')
        if status:
            if status == "todo":
                # Problems that are not solved (already handled by base queryset)
                pass
            elif status == "solved":
                # Override the queryset to show only solved problems
                problems = Problem.objects.filter(id__in=solved_problem_ids).order_by('id')

        # Filter by topic (tags)
        topic = request.GET.get('topic')
        if topic:
            problems = problems.filter(tags__icontains=topic)

        # Search by title
        title = request.GET.get('problem-title')
        if title:
            problems = problems.filter(title__icontains=title)

        # Add pagination
        paginator = Paginator(problems, 10)  # Show 10 problems per page
        page_number = request.GET.get('page')
        try:
            page_obj = paginator.get_page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        print("page",page_obj)
        return render(request, 'problems/problem.html', {'problems':page_obj})

    except Exception as e:
        # Log the exception
        print(f"Error occurred: {e}")
        return render(request, 'problems/problem.html', {'problems': []})



def pick_random(request):
    user = request.user
    solved_problem_ids = SolvedProblem.objects.filter(user=user).values_list('problem_id', flat=True)
    problems = Problem.objects.exclude(id__in=solved_problem_ids)
    if problems.exists():
      selected_problem = choice(problems)  # Select a random problem
      print(selected_problem.id)
      return redirect('solve', id=selected_problem.id)
    return render(request, 'problems/problem.html', {'problems':problems})
    




# def problem(request):
#   problems = Problem.objects.all()
#   return render(request, 'problems/problem.html',{'problems':problems})

def solve(request, id):
  problem = Problem.objects.get(id=id)
  constraints_html=""
  for constraint in problem.constraints.split(';'):
    constraint = constraint.strip()
    constraints_html += f"<li>{constraint}</li>"
  constraints_html = constraints_html.replace("\n", "") 

  
  test_cases_html = ""

# Iterate over the test cases
  for idx, case in enumerate(problem.sample_test_cases, start=1):
    test_cases_html += f"""
    <div class="test-case">
        <p class="font-semibold text-gray-700">Test Case {idx}:</p>
        <p class="text-gray-600">Input: nums = {case['input']}</p>
        <p class="text-gray-600">Output: {case['output']}</p>
    </div>
    """
  context={
    'problem':problem,
    'constraints_html':constraints_html,
    'test_cases_html':test_cases_html
    }
  
  
  return render(request, 'problems/solve.html',context)





