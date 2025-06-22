import json
import os
from datetime import datetime


if os.path.exists("denuncias.json"):
    with open("denuncias.json", "r") as arquivo:
        try:
            denuncias = json.load(arquivo)
        except json.JSONDecodeError:
            denuncias = []
else:
    denuncias = []

def salvar_dados():
    with open("denuncias.json", "w") as arquivo:
        json.dump(denuncias, arquivo, indent=4)

def fazer_denúncia():
    print("\n📝 Faça sua denúncia:")
    descricao = input("➡️ Informe a descrição da sua denúncia: ")
    local = input("📍 Informe o local da denúncia: ")
    status = "em análise"
    tipo = input("🚱 Tipo do problema (água, esgoto, lixo, etc): ")
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    denuncia = {
        "descricao": descricao,
        "local": local,
        "status": status,
        "tipo": tipo,
        "data_hora": data_hora,
    }
    denuncias.append(denuncia)
    salvar_dados()
    print("✅ Denúncia feita com sucesso! Obrigado por ajudar! 🙌")

def listar_denuncias():
    print("\n📋 Lista de denúncias:")
    if not denuncias:
        print("⚠️ Nenhuma denúncia registrada.")
        return
    for i, denuncia in enumerate(denuncias, start=1):
        print(f"\n[{i}] 🆔 Descrição: {denuncia['descricao']}")
        print(f"📍 Local: {denuncia['local']}")
        print(f"🕒 Data/Hora: {denuncia['data_hora']}")
        print(f"🚩 Tipo: {denuncia['tipo']}")
        print(f"🔖 Status: {denuncia['status']}")

def excluir_denúncia():
    if not denuncias:
        print("⚠️ Não há denúncias para remover.")
        return

    print("\n🗑️ Lista de denúncias:")
    for i, denuncia in enumerate(denuncias, start=1):
        print(f"{i} - {denuncia['descricao']}")

    try:
        escolha = int(input("❌ Digite o número da denúncia que você quer remover: "))
        if 1 <= escolha <= len(denuncias):
            removida = denuncias.remove(escolha - 1)
            salvar_dados()
            print(f"🗑️ Denúncia '{removida['descricao']}' removida com sucesso!")
        else:
            print("⚠️ Número inválido. Tente novamente.")
    except ValueError:
        print("⚠️ Por favor, digite um número válido.")

def alterar_status():
    if not denuncias:
        print("⚠️ Não há denúncias para alterar.")
        return

    print("\n🔄 Lista de denúncias:")
    for i, denuncia in enumerate(denuncias, start=1):
        print(f"{i} - {denuncia['descricao']} - Status atual: {denuncia['status']}")

    try:
        escolha = int(input("\n✏️ Digite o número da denúncia que você quer mudar o status: "))
        if 1 <= escolha <= len(denuncias):
            novo_status = input("🆕 Informe o novo status (Exemplo: Em análise, Resolvido): ")
            denuncias[escolha - 1]["status"] = novo_status
            salvar_dados()
            print("✅ Status alterado com sucesso!")
        else:
            print("⚠️ Número inválido. Tente novamente.")
    except ValueError:
        print("⚠️ Por favor, digite um número válido.")

while True:
    print("""
███████╗ █████╗ ███╗   ██╗███████╗ █████╗      
██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗    
███████╗███████║██╔██╗ ██║█████╗  ███████║    
╚════██║██╔══██║██║╚██╗██║██╔══╝  ██╔══██║    +
███████║██║  ██║██║ ╚████║███████╗██║  ██║  
╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝    
                                                       
""")
    print("🚰🌱 Bem-vindo ao sistema de denúncias de Saneamento - SANEA+ 🌱🚰\n")

    print("📌 Menu principal:")
    print("1️⃣  Fazer uma nova denúncia")
    print("2️⃣  Ver todas as denúncias")
    print("3️⃣  Alterar status de denúncia")
    print("4️⃣  Remover denúncia")
    print("5️⃣  Sair\n")

    try:
        opcao = int(input("👉 Escolha uma opção: "))
    except ValueError:
        print("⚠️ Por favor, digite um número válido.\n")
        continue

    if opcao == 1:
        fazer_denúncia()
    elif opcao == 2:
        listar_denuncias()
    elif opcao == 3:
        alterar_status()
    elif opcao == 4:
        excluir_denúncia()
    elif opcao == 5:
        print("👋 Saindo do sistema...")
        break
    else:
        print("❌ Opção inválida, tente novamente.\n")
