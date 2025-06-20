# print("hola mundo")
# #implementar una calculadora que pida dos numeros y una operacion, vamos a usar la figura se switch...casey luego con if...elif...else.
#calculadora basica:


# num_1 =float(input("primer numero a consulta: "))
# num_2 =float(input("segundo numero a consultar: "))
# operador =input("que operacion vas hacer?(+,-,/,*): ")

# #como asi que switch y case?
# #switch y case es una forma diferente de escribir condicionales,donde se evaluan un parametro,booleano0, y se va a direccionar inmediatamente segun los casos definidos

# match operador:
#     case "+":
#         print("resultado", num_1 + num_2)
#     case "-":
#         print("resultado", num_1 - num_2)
#     case "*":
#         print("resiltado", num_1 * num_2)
#     case "/":
#         if num_2 != 0:
#             print("resultado", num_1 / num_2)
#         else:
#             print("resultado no valido") 
#     case _:
#         print("resultado no valido")

if operador == "+":
    print("resultado", num_1 + num_2)
elif operador == "-":
    print("resultado", num_1 - num_2)
elif operador == "*":
    print("resultado", num_1 * num_2)
elif operador == "/":
    if num_2 != 0:
        print("resultado", num_1 / num_2)
    else: 
        print("erros dividiendo por cero.")
else:
    print("operacion no valida.")
    
