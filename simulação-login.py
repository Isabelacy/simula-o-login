usuario_correto = "Isabela"
senha_correta = "isabela2024"

usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login realizado com sucesso! Bem-vinda.")
else:
    print("Usuário ou senha incorretos. Tente novamente.")
