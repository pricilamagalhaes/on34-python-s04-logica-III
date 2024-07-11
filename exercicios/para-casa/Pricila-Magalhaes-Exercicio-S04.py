print("Vamos Contar quantas palavras 'LEI' existem nos texto?\n")

texto1 = "Uma infecção curada de dengue confere ao paciente imunidade contra o tipo de vírus responsável. Por existirem quatro tipos diferentes de vírus, para estar totalmente imunizado, é necessário ter tido contato com todos eles. Caso contrário, a cada contágio com um novo tipo de vírus, os sintomas são mais intensos e o risco de desenvolver a dengue grave é mais alto."
texto2 = "Já num sentido amplo, lei é somente a regra jurídica escrita, excluindo-se dessa aceção, portanto, o costume jurídico. Por fim, numa aceção técnica e específica, a palavra lei designa uma modalidade de regra escrita, que apresenta determinadas características; no direito brasileiro, são técnicas apenas a lei complementar e a lei ordinária."
texto3 = "Na linha do tempo do futebol feminino brasileiro, ele passou tanto tempo proibido quanto regulamentado: 38 anos. De 1941 a 1979, a lei nacional não permitia a prática do esporte por mulheres devido às “condições da sua natureza”. Já o regulamento da modalidade, que permanece válido até 2021, só foi feito em 1983. "
texto4 = "A lei dos cossenos é uma expressão matemática que relaciona os três lados de um triângulo qualquer. Por não estar restrita ao triângulo retângulo, a lei dos cossenos pode ser entendida como uma generalização do teorema de Pitágoras."

print(f"Texto 1: {texto1}\n")
print(f"Texto 2: {texto2}\n")
print(f"Texto 3: {texto3}\n")
print(f"Texto 4: {texto4}\n")


       
textos = [texto1, texto2, texto3, texto4]
texto_escolhido= ""
qtpalavralei= 0
    
for texto in textos:
    palavra= texto.split()
    qt_no_texto= palavra.count("lei")
    
    print(f"A quantidade da palavra no texto é: {qt_no_texto}")

    if qt_no_texto > qtpalavralei:
        texto_escolhido = texto
        qtpalavralei = qt_no_texto


print("\n")
print(f"O texto onde mais referencia a palavra 'lei' é o texto: {texto_escolhido}")