from manager import Manager

def menu():
    choice = None
    manager = Manager()
    while choice != 'q':
        print('CRYTPTO CONVERTER')
        print('a: convert to USD: ')
        print('b: convert to EUR: ')
        print('q: Quit ')
        choice = input("Action: ")
        coin_list = manager.coin_list()

        def sub_menu(to):
            print('Available coins:')
            print(', '.join(coin_list))
            amount = int(input("Amount: "))
            symbol = input('coin: ')
            symbol = symbol.upper()
            if symbol in coin_list:
                result = manager.calculate(amount, symbol, to)
                print('-'* 50)
                print(f'{amount} {symbol} is {result} {to}')
                print('-'* 50)
            else:
                print(symbol, 'is not available')
        if choice == "a":
            sub_menu('USD')
        
        elif choice == "b":
            sub_menu("EUR")

        else:
            pass


if __name__=='__main__':
    menu()