# from django.shortcuts import render
# from django.http import JsonResponse
# from openai import OpenAI
# # Create your views here.
# client = OpenAI(api_key=open_ai_apikey)
# def ask_openai(message):
#     response = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {
#                 "role": "user",
#                 "content": "Write a haiku about recursion in programming."
#             }
#         ]
#     )
#     print(response)
#     # ans = response.choices[0].text.strip()
#     # return ans


# # def chatbot(request):
# #     if request.method == 'POST':
# #         message = request.POST.get('message')
# #         response = ask_openai(message)
# #         return JsonResponse({'message': message,'response':response})

# #     return render(request,'chatbot.html')
