import json
import requests
from django.shortcuts import render
from problems.models import Problem
from .models import Submission
from account.models import Account
from django.contrib.auth.models import User
from problems.models import SolvedProblem

def submit_code(request, id):
    try:
        # Fetch the problem by id
        problem = Problem.objects.filter(id=id).first()
        if not problem:
            return render(request, 'submissions/error.html', {'error': 'Problem not found'})

        # Combine sample and hidden test cases
        test_cases = problem.sample_test_cases + problem.hidden_test_cases
    except Problem.DoesNotExist:
        return render(request, 'submissions/error.html', {'error': 'Problem not found'})

    if request.method == "POST":
        # Fetch user-submitted code
        version = ""
        user_code = request.POST.get("code", "")

        if len(user_code) == 0:
            return render(request, 'submissions/error.html', {'error': 'Please Enter Code'})

        selected_language = request.POST.get('language')
        
        # Handle file naming based on selected language
        if selected_language == "python":
            filename = "main.py"
            version = "3.10.0"
        elif selected_language == "javascript":
            filename = "main.js"
            version="18.15.0"
        elif selected_language == "java":
            filename = "Main.java"
            version="15.0.2"
        elif selected_language == "c++":
            filename = "main.cpp"
            version="10.2.0"
        elif selected_language == "c":
            filename = "main.c"
            version="10.2.0"
        else:
            filename = "main.txt"

        # API endpoint for Piston execution
        url = "https://emkc.org/api/v2/piston/execute"
        headers = {"Content-Type": "application/json"}

        # Execute code for each test case
        all_results = []
        passed = 0
        failed = 0
        for test_case in test_cases:
            stdin_input = test_case['input']
            payload = {
                "language": selected_language,
                "version": version,
                "files": [
                    {
                        "name": filename,
                        "content": user_code,
                    }
                ],
                "stdin": stdin_input  # Use dynamic stdin input from test cases
            }

            try:
                # Send POST request to execute code
                response = requests.post(url, headers=headers, data=json.dumps(payload))

                # Debugging output
                print(f"Response Status Code: {response.status_code}")
                print(f"Response Content: {response.text}")

                if response.status_code == 200:
                    result = response.json()
                    output = result["run"]["output"].strip()  # Get the output and strip leading/trailing spaces
                    print(f"Test Case Input: {stdin_input} Output: {output}")

                    # Compare output with expected output
                    expected_output = test_case['output']
                    if output == expected_output:
                        passed += 1
                        test_case_result = {'input': stdin_input, 'expected': expected_output, 'actual': output, 'status': 'passed'}
                    else:
                        failed += 1
                        test_case_result = {'input': stdin_input, 'expected': expected_output, 'actual': output, 'status': 'failed'}

                    all_results.append(test_case_result)

                    # Increment problem count if all test cases passed
                else:
                    # Error handling if API fails
                    all_results.append({
                        "input": stdin_input,
                        "error": "Failed to execute code",
                        "details": response.text
                    })
            except requests.exceptions.RequestException as e:
                # Handle request errors (e.g., network issues)
                all_results.append({
                    "input": stdin_input,
                    "error": "Failed to connect to the execution API",
                    "details": str(e)
                })
            
        status = "Accepted" if passed == len(test_cases) else "Wrong Answer"
        if passed == len(test_cases):
            try:
                if request.user.is_authenticated:
                    user_id = request.user.id
                    print(user_id)
                    user = Account.objects.get(user_id=user_id) 
                    print(user)
                    if not SolvedProblem.objects.filter(problem_id=id,user_id=user_id).exists():
                        user_instance = User.objects.get(id=user_id)
                        problem_instance = Problem.objects.get(id=id)
                        solved_problem = SolvedProblem(
                                        user=user_instance,
                                        problem=problem_instance,
                                        status="solved"
                                    )
                        solved_problem.save()

                        print(user.easy)
                        print(problem.difficulty)
                        if problem.difficulty == 'Easy':
                            user.easy += 1
                        elif problem.difficulty == 'Medium':
                            user.medium += 1
                        elif problem.difficulty == 'Hard':
                            user.hard += 1
                        user.total_solved=user.easy+user.medium+user.hard
                        print(user.total_solved)
                        print(problem)
                        user.save()  # Update the user's total solved count
            except Account.DoesNotExist:
                print("User not found!")
        submission = Submission.objects.create(
                                user=request.user,
                                problem=problem,
                                status=status,
                                language=selected_language,
                            )

        # Return results in HTML format using Tailwind CSS
        return render(request, 'submissions/submit_results.html', {
            'id': id,
            "problem_name": problem.title,
            'results': all_results,
            'passed': passed,
            'failed': failed,
            'total': len(test_cases)
        })

    return render(request, 'submissions/error.html', {'error': 'Invalid request method'})
