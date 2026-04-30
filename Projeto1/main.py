from web3 import Web3
import random
import os

# Conexão com nó RPC via HTTPProvider


bsc_url = "https://bsc-dataseed.binance.org/"

bsc_url2 = "https://bsc.publicnode.com/"

auto_walletAddress = ['0x8894E0a0c962CB723c1976a4421c95949bE2D4E3','0xF977814e90dA44bFA03b6295A0616a897441aceC','0x28C6c06298d514Db089934071355E5743bf21d60','0x3f5CE5FBFe3E9af3971dD833D26bA9b5C936f0bE']
auto_tokenAddress = ['0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82','0x55d398326f99059fF775485246999027B3197955','0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56', '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c']

''' Variáveis '''

wallet_Address = ''
w_Address = ''
token_Address = ''
t_Address = ''

token_Contract = ''

saldo_Wallet = ''
decimais_Token = ''
saldo_TokenBruto = ''
convert_SaldoWallet = ''
convert_SaldoToken = ''

w3 = Web3(Web3.HTTPProvider(bsc_url))

bloco = '' 


# ABI para consulta de dados

abi =    [
    {
        "constant": True,
        "inputs":[{"name":"Endereco", "type":"address"}],
        "name": "balanceOf",
        "outputs":[{"name":"Resultado", "type":"uint256"}],
        "type": "function"

    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "type": "function"
    }

]


''' Funções  '''


# Função para limpar o terminal
def Clean():

    os.system('clear' if os.name == 'posix' else 'clear')


def Menu(): 
    
    while True:

        Clean()

        print("Escolha uma das opções a seguir:  \n 1 - Consultar Carteira e Token \n 2 - Consultar somente a Carteira  \n 3 - Consultar Carteira e Token aleatorio (Automatico) \n 4 - Sair")
    
        opcao = int(input(""))


        if opcao <= 4:

            match opcao:
                case 1:
                    
                    Clean()

                    print("- Consultar Carteira e Token -")

                    wallet_Address = input("Informe o código da carteira :")
                    
                    w_Address = w3.to_checksum_address(wallet_Address)

                    if w3.is_address(w_Address):

                        print("Endereço de carteira válido")

                        saldo_Wallet = w3.eth.get_balance(w_Address)

                        convert_SaldoWallet = w3.from_wei(saldo_Wallet, 'ether')

                        token_Address = input("Informe o código do token :")

                        t_Address = w3.to_checksum_address(token_Address)


                        if w3.is_address(t_Address):

                            token_Contract = w3.eth.contract(address = t_Address, abi= abi)

                            try:    
                                decimais_Token = token_Contract.functions.decimals().call()

                                saldo_TokenBruto = token_Contract.functions.balanceOf(w_Address).call()

                                convert_SaldoToken = saldo_TokenBruto / (10 ** decimais_Token)

                                print("Endereço de token válido")

                                print(f"Bloco atual da BSC: {bloco} \nSaldo de BNB: {convert_SaldoWallet:.2f} \nSaldo de Tokens: {convert_SaldoToken:.2f}")

                                fim = input("Aperte qualquer tecla para continuar:")

                            except:
                                print("Token inválido, tente novamente")
                                fim = input("Aperte qualquer tecla para continuar:")



                        else:

                            print("Endereço de token inválido, tente novamente.")
                            fim = input("Aperte qualquer tecla para continuar:")
      
                    
                    else:

                        print("Erro, endereço de carteira inválido.")
                        fim = input("Aperte qualquer tecla para continuar:")


                case 2:
                    
                    Clean()

                    print("- Consultar somente a Carteira -")

                    wallet_Address = input("Informe o código da carteira :")
                    
                    w_Address = w3.to_checksum_address(wallet_Address)

                    if w3.is_address(w_Address):

                        print("Endereço de carteira válido")

                        saldo_Wallet = w3.eth.get_balance(w_Address)

                        convert_SaldoWallet = w3.from_wei(saldo_Wallet, 'ether')

                        print(f"Bloco atual da BSC: {bloco} \nSaldo de BNB: {convert_SaldoWallet:.2f}")

                        fim = input("Aperte qualquer tecla para continuar:")

                    else:

                        print("Endereço de carteira inválido, tente novamente.")
                        fim = input("Aperte qualquer tecla para continuar:")



                case 3:

                    Clean()

                    print("- Consultar Carteira e Token aleatorio (Automatico) -")

                    # Seleção automatica de um Wallet e um Token aleatório
                    select_Wallet = random.choice(auto_walletAddress)
                    select_Token = random.choice(auto_tokenAddress)

                    saldo_Wallet = w3.eth.get_balance(select_Wallet)

                    convert_SaldoWallet = w3.from_wei(saldo_Wallet, 'ether')

                    token_Contract = w3.eth.contract(address = select_Token, abi= abi)

                    decimais_Token = token_Contract.functions.decimals().call()

                    saldo_TokenBruto = token_Contract.functions.balanceOf(select_Wallet).call()

                    convert_SaldoToken = saldo_TokenBruto / (10 ** decimais_Token)

                    print(f"Bloco atual da BSC: {bloco} \nSaldo de BNB: {convert_SaldoWallet:.2f} \nSaldo de Tokens: {convert_SaldoToken:.2f}")

                    fim = input("Aperte qualquer tecla para continuar:")



                case 5: 

                    print("Saindo...")
                    break
    
        else:

            print("Opção inválida, tente novamente!")
            fim = input("Aperte qualquer tecla para continuar:")
            return    


    return



''' Código principal do projeto '''



if w3.is_connected():

    print("Conectado a BSC")

    bloco = w3.eth.block_number

    Menu()


else:

    w3 = Web3(Web3.HTTPProvider(bsc_url2))

    if w3.is_connected():

        print("Conectado a BSC via link Backup")

        bloco = w3.eth.block_number

        Menu()

    else:

        print("Falha na conexão, verifique sua rede")



