import os
import platform

def testar_conexao(host):
    # Ajusta o comando dependendo do sistema (Windows usa '-n', Linux '-c')
    parametro = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    comando = f"ping {parametro} {host}"
    
    # Executa o comando e guarda o resultado
    resposta = os.system(comando)
    
    if resposta == 0:
        return "CONECTADO"
    else:
        return "FALHOU"

print("--- DIAGNÓSTICO DE SUPORTE DA BARBARA ---")

# 1. Testando o Google (Internet Geral)
print(f"Testando Internet (Google): {testar_conexao('8.8.8.8')}")

# 2. Testando DNS (Resolução de nomes)
print(f"Testando DNS (google.com): {testar_conexao('google.com')}")

# 3. Testando sua rede local (Roteador - geralmente final .1)
print(f"Testando Rede Local: {testar_conexao('192.168.15.1')}")

print("-----------------------------------------")