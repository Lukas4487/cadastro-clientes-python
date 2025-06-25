# Sistema simples de cadastro de clientes
clientes = []

def menu():
    print("\n=== Sistema de Cadastro de Clientes ===")
    print("1 - Adicionar cliente")
    print("2 - Listar clientes")
    print("3 - Buscar cliente por nome")
    print("4 - Excluir cliente")
    print("5 - Sair")

def adicionar_cliente():
    nome = input("Nome: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")
    cliente = {"nome": nome, "email": email, "telefone": telefone}
    clientes.append(cliente)
    print("✅ Cliente adicionado com sucesso!")

def listar_clientes():
    if not clientes:
        print("⚠️ Nenhum cliente cadastrado.")
    else:
        print("\n📋 Lista de Clientes:")
        for i, c in enumerate(clientes, 1):
            print(f"{i}. {c['nome']} | {c['email']} | {c['telefone']}")

def buscar_cliente():
    nome = input("Digite o nome para busca: ").lower()
    encontrados = [c for c in clientes if nome in c["nome"].lower()]
    if encontrados:
        for c in encontrados:
            print(f"🔎 {c['nome']} | {c['email']} | {c['telefone']}")
    else:
        print("❌ Nenhum cliente encontrado com esse nome.")

def excluir_cliente():
    nome = input("Nome do cliente para excluir: ").lower()
    for c in clientes:
        if nome == c["nome"].lower():
            clientes.remove(c)
            print("🗑️ Cliente excluído com sucesso.")
            return
    print("❌ Cliente não encontrado.")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_cliente()
    elif opcao == "2":
        listar_clientes()
    elif opcao == "3":
        buscar_cliente()
    elif opcao == "4":
        excluir_cliente()
    elif opcao == "5":
        print("Encerrando o programa. 👋")
        break
    else:
        print("Opção inválida. Tente novamente.")