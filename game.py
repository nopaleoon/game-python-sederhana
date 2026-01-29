def guess_number():
    while True:
        print()
        print("===================================")
        print("Selamat Datang di game tebak angka")
        print("===================================")

        import random
        angka_random = random.randint(1, 10)
        kesempatan = 3
        tebakan = 0
        
        while tebakan < kesempatan:
            tebakan +=1
            user_input = int(input("Tebak angka 1-10: "))
            if user_input < angka_random:
                print("terlalu kecil")
            elif user_input > angka_random:
                print("terlalu besar")
            else:
                print("TEBAKAN ANDA BENAR...")
                break
        else:
            print(f"angka rahasianya adalah {angka_random}")
            
        play_again = input("apakah anda ingin main lagi? (y/n): ")
        if play_again == 'n':
            print('Terimakasi sudah main game ini...')
            break
        
        
def guess_word():
    pass
    
def suit():
    while True:
        print()
        print("============================")
        print("GAME BATU GUNTING KERTAS")
        print("============================")
        import random
        suit = ['batu', 'gunting', 'kertas']
        komputer = random.choice(suit)
        
        user_input = input("Pilih batu, gunting, atau kertas: ").lower()
        
        if user_input == komputer:
            print(f'user : {user_input} vs komputer : {komputer}')
            print(f'Seri!')
            
        elif (user_input == 'batu' and komputer == 'gunting') or \
            (user_input == 'gunting' and komputer == 'kertas') or \
            (user_input == 'kertas' and komputer == 'batu'):
            print(f'user : {user_input} vs komputer : {komputer}')
            print('CONGRATS, YOU WIN!')
            
        else:
            print(f'user : {user_input} vs komputer : {komputer}')
            print('YOU LOSE!')

        main_lagi = input("apakah anda ingin keluar dari game? (y/n): ")
        if main_lagi != 'n':
            print("terimakasih telah bermain!")
            break
        
def menu():
    while True:
        print("Welcome to game hub!")
        print("1. Guess Number Game")
        print("2. Rock, Paper, Scissors Game")
        print("3. Exit")
        
        try:
            pilih = int(input("Choose game what you want: "))
            if pilih == 1:
                guess_number()
            elif pilih == 2:
                suit()
            elif pilih == 3:
                print("Thanks!")
                break
            else:
                print("Pilihan tidak valid, silakan coba lagi.")
        except ValueError:
            print('pilih angka pada menu')
menu()