from django.shortcuts import render

def home(request):
	return render(request,'home.html', {})

def add(request):
	from random import randint
	num_1 = randint(0,10)
	num_2 = randint(0,10)

	if request.method == "POST":		
		answer = request.POST.get('answer')
		old_num_1 = request.POST.get('old_num_1')
		old_num_2 = request.POST.get('old_num_2')


		if not answer:
			my_answer = "N'oublies pas de donner une réponse !!!"
			color = 'dark'
			return render(request,'add.html', {
				'answer':answer,
				'my_answer':my_answer,
				'num_1':num_1,
				'num_2':num_2,
				'color':color,											
			})



		correct_answer = int(old_num_1) + int(old_num_2)		

		if int(answer) == correct_answer:			
			my_answer = "Juste ! " + old_num_1 + "+" + old_num_2 + " est bien égal à " + answer + "."
			color = "success"
		else:
			my_answer = "Faux...  " + old_num_1 + "+" + old_num_2 + " est égal à " + str(correct_answer) + " pas à " + answer + "."
			color = "danger"			

		return render(request,'add.html', {
				'answer':answer,
				'my_answer':my_answer,
				'correct_answer':correct_answer,
				'num_1':num_1,
				'num_2':num_2,
				'color':color,								
			})
		
	return render(request,'add.html', {
		'num_1':num_1,
		'num_2':num_2,
		})

def add0100(request):
	from random import randint
	num_1 = randint(0,100)
	num_2 = randint(0,100)

	if request.method == "POST":		
		answer = request.POST.get('answer')
		old_num_1 = request.POST.get('old_num_1')
		old_num_2 = request.POST.get('old_num_2')
		

		if not answer:
			my_answer = "N'oublies pas de donner une réponse !!!"
			color = 'dark'
			return render(request,'add0100.html', {
				'answer':answer,
				'my_answer':my_answer,
				'num_1':num_1,
				'num_2':num_2,
				'color':color,											
			})



		correct_answer = int(old_num_1) + int(old_num_2)		

		if int(answer) == correct_answer:			
			my_answer = "Juste ! " + old_num_1 + "+" + old_num_2 + " est bien égal à " + answer + "."
			color = "success"
		else:
			my_answer = "Faux...  " + old_num_1 + "+" + old_num_2 + " est égal à " + str(correct_answer) + " pas à " + answer + "."
			color = "danger"			

		return render(request,'add0100.html', {
				'answer':answer,
				'my_answer':my_answer,
				'correct_answer':correct_answer,
				'num_1':num_1,
				'num_2':num_2,
				'color':color,								
			})
		
	return render(request,'add0100.html', {
		'num_1':num_1,
		'num_2':num_2,
		})

def add01000(request):
	from random import randint
	num_1 = randint(0,1000)
	num_2 = randint(0,1000)

	if request.method == "POST":		
		answer = request.POST.get('answer')
		old_num_1 = request.POST.get('old_num_1')
		old_num_2 = request.POST.get('old_num_2')
		

		if not answer:
			my_answer = "N'oublies pas de donner une réponse !!!"
			color = 'dark'
			return render(request,'add01000.html', {
				'answer':answer,
				'my_answer':my_answer,
				'num_1':num_1,
				'num_2':num_2,
				'color':color,											
			})



		correct_answer = int(old_num_1) + int(old_num_2)		

		if int(answer) == correct_answer:			
			my_answer = "Juste ! " + old_num_1 + "+" + old_num_2 + " est bien égal à " + answer + "."
			color = "success"
		else:
			my_answer = "Faux...  " + old_num_1 + "+" + old_num_2 + " est égal à " + str(correct_answer) + " pas à " + answer + "."
			color = "danger"			

		return render(request,'add01000.html', {
				'answer':answer,
				'my_answer':my_answer,
				'correct_answer':correct_answer,
				'num_1':num_1,
				'num_2':num_2,
				'color':color,								
			})
		
	return render(request,'add01000.html', {
		'num_1':num_1,
		'num_2':num_2,
		})

def subtract(request):
	from random import randint
	num_1 = randint(0,10)
	num_2 = randint(0,num_1)

	if request.method == "POST":		
		answer = request.POST.get('answer')
		old_num_1 = request.POST.get('old_num_1')
		old_num_2 = request.POST.get('old_num_2')


		if not answer:
			my_answer = "N'oublies pas de donner une réponse !!!"
			color = 'dark'
			return render(request,'subtract.html', {
				'answer':answer,
				'my_answer':my_answer,
				'num_1':num_1,
				'num_2':num_2,
				'color':color,						
			})	

		
		correct_answer = int(old_num_1) - int(old_num_2)
		if int(answer) == correct_answer:				
			my_answer = "Juste ! " + old_num_1 + "-" + old_num_2 + " est bien égal à " + answer + "."
			color = "success"
		else:
			my_answer = "Faux...  " + old_num_1 + "-" + old_num_2 + " est égal à " + str(correct_answer) + " pas à " + answer + "."
			color = "danger"
		
		return render(request,'subtract.html', {
				'answer':answer,
				'my_answer':my_answer,
				'correct_answer':correct_answer,
				'num_1':num_1,
				'num_2':num_2,
				'color':color,											
			})
		
	return render(request,'subtract.html', {
		'num_1':num_1,
		'num_2':num_2,
		})

def subtract0100(request):
	from random import randint
	num_1 = randint(0,100)
	num_2 = randint(0,num_1)

	if request.method == "POST":		
		answer = request.POST.get('answer')
		old_num_1 = request.POST.get('old_num_1')
		old_num_2 = request.POST.get('old_num_2')


		if not answer:
			my_answer = "N'oublies pas de donner une réponse !!!"
			color = 'dark'
			return render(request,'subtract0100.html', {
				'answer':answer,
				'my_answer':my_answer,
				'num_1':num_1,
				'num_2':num_2,
				'color':color,						
			})	

		
		correct_answer = int(old_num_1) - int(old_num_2)
		if int(answer) == correct_answer:				
			my_answer = "Juste ! " + old_num_1 + "-" + old_num_2 + " est bien égal à " + answer + "."
			color = "success"
		else:
			my_answer = "Faux...  " + old_num_1 + "-" + old_num_2 + " est égal à " + str(correct_answer) + " pas à " + answer + "."
			color = "danger"
		
		return render(request,'subtract0100.html', {
				'answer':answer,
				'my_answer':my_answer,
				'correct_answer':correct_answer,
				'num_1':num_1,
				'num_2':num_2,
				'color':color,											
			})
		
	return render(request,'subtract0100.html', {
		'num_1':num_1,
		'num_2':num_2,
		})


def subtract01000(request):
	from random import randint
	num_1 = randint(0,1000)
	num_2 = randint(0,num_1)

	if request.method == "POST":		
		answer = request.POST.get('answer')
		old_num_1 = request.POST.get('old_num_1')
		old_num_2 = request.POST.get('old_num_2')


		if not answer:
			my_answer = "N'oublies pas de donner une réponse !!!"
			color = 'dark'
			return render(request,'subtract01000.html', {
				'answer':answer,
				'my_answer':my_answer,
				'num_1':num_1,
				'num_2':num_2,
				'color':color,						
			})	

		
		correct_answer = int(old_num_1) - int(old_num_2)
		if int(answer) == correct_answer:				
			my_answer = "Juste ! " + old_num_1 + "-" + old_num_2 + " est bien égal à " + answer + "."
			color = "success"
		else:
			my_answer = "Faux...  " + old_num_1 + "-" + old_num_2 + " est égal à " + str(correct_answer) + " pas à " + answer + "."
			color = "danger"
		
		return render(request,'subtract0100.html', {
				'answer':answer,
				'my_answer':my_answer,
				'correct_answer':correct_answer,
				'num_1':num_1,
				'num_2':num_2,
				'color':color,											
			})
		
	return render(request,'subtract01000.html', {
		'num_1':num_1,
		'num_2':num_2,
		})

def multiply(request):
	from random import randint
	num_1 = randint(0,10)
	num_2 = randint(0,10)

	if request.method == "POST":		
		answer = request.POST.get('answer')
		old_num_1 = request.POST.get('old_num_1')
		old_num_2 = request.POST.get('old_num_2')

		if not answer:
			my_answer = "N'oublies pas de donner une réponse !!!"
			color = 'dark'
			return render(request,'multiply.html', {
				'answer':answer,
				'my_answer':my_answer,
				'num_1':num_1,
				'num_2':num_2,
				'color':color,											
			})

		correct_answer = int(old_num_1) * int(old_num_2)		

		if int(answer) == correct_answer:			
			my_answer = "Juste ! " + old_num_1 + "X" + old_num_2 + " est bien égal à " + answer + "."
			color = "success"
		else:
			my_answer = "Faux...  " + old_num_1 + "X" + old_num_2 + " est égal à " + str(correct_answer) + " pas à " + answer + "."
			color = "danger"			

		return render(request,'multiply.html', {
				'answer':answer,
				'my_answer':my_answer,
				'correct_answer':correct_answer,
				'num_1':num_1,
				'num_2':num_2,
				'color':color,								
			})
		
		return render(request,'multiply.html', {
			'num_1':num_1,
			'num_2':num_2,
			})

def multiply0510(request):
	import random
	liste =[0, 1, 2, 3, 4, 5, 10]
	num_1 = random.choice(liste)
	num_2 = random.choice(liste)

	if request.method == "POST":		
		answer = request.POST.get('answer')
		old_num_1 = request.POST.get('old_num_1')
		old_num_2 = request.POST.get('old_num_2')

		if not answer:
			my_answer = "N'oublies pas de donner une réponse !!!"
			color = 'dark'
			return render(request,'multiply0510.html', {
				'answer':answer,
				'my_answer':my_answer,
				'num_1':num_1,
				'num_2':num_2,
				'color':color,											
			})

		correct_answer = int(old_num_1) * int(old_num_2)		

		if int(answer) == correct_answer:			
			my_answer = "Juste ! " + old_num_1 + "X" + old_num_2 + " est bien égal à " + answer + "."
			color = "success"
		else:
			my_answer = "Faux...  " + old_num_1 + "X" + old_num_2 + " est égal à " + str(correct_answer) + " pas à " + answer + "."
			color = "danger"			

		return render(request,'multiply0510.html', {
				'answer':answer,
				'my_answer':my_answer,
				'correct_answer':correct_answer,
				'num_1':num_1,
				'num_2':num_2,
				'color':color,								
			})
		
	return render(request,'multiply0510.html', {
		'num_1':num_1,
		'num_2':num_2,
		})

def divide(request):
	return render(request,'divide.html', {})

def about(request):
	return render(request,'about.html', {})


