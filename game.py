def guess_number():
    while True:
        print()
        print("===================================")
        print("SELAMAT DATANG DI GAME TEBAK ANGKA")
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
    while True:
        print("================")
        print("SELAMAT DATANG DI GAME TEBAK KATA")
        print("================")
        print()
        
        import random
        words = ['kendal', 'solo', 'ums', 'informatika', 'astrea']
        random.shuffle(words)
        random_word = random.choice(words)
        kesempatan = 3
        tebakan = 0
        
        print("tebak apa yang dipikirkan komputer dari kata berikut:")
        print(words)
        while tebakan < kesempatan:
            tebakan +=1
            pilihan = input("Tebak pikiran komputer: ").lower()
            if pilihan == random_word:
                print("TEBAKAN ANDA BENAR...")
                break
            else:
                print("Salah coba lagi")
                
        play_again = input("apakah anda ingin main lagi? (y/n): ")
        if play_again == 'n':
            print('Terimakasi sudah main game ini...')
            break
    
def suit():
    while True:
        print()
        print("============================")
        print("SELAMAT DATANG DI GAME BATU GUNTING KERTAS")
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
        
def mad_libs():
    while True:
        print("=============================")
        print("SELAMAT DATANG DI GAME MAD LIBS")
        print("=============================")
        print("Masukkan kata/kalimat yang tepat untuk melengkapi peribahasa berikut:")
        print()
        
        skor = 0
        
        peribahasa = {
            "Seperti pinang dibelah" : "dua",
            "Air beriak tanda" : "tidak dalam",
            "Besar .... daripada tiang" : "pasak",
            "Ada gula ada" : "semut",
            "Ada udang di balik" : "batu"
        }

        for soal, jawaban in peribahasa.items():
            print(f"{soal} = ")
            user_input = input("Masukan jawaban: ").lower()
            if user_input == jawaban:
                print("Jawaban Anda benar!")
                skor += 10
            else:
                print(f'Kurang tepat, jawaban yang benar adalah => {jawaban}')
        
        print(f"Skor Anda: {skor}")
        play_again = input("apakah anda ingin main lagi? (y/n): ")
        if play_again == 'n':
            print('Terimakasi sudah main game ini...')
            break
        
def menu():
    while True:
        print()
        print("Welcome to game hub!")
        print("1. Guess Number Game")
        print("2. Rock, Paper, Scissors Game")
        print("3. Guess Word")
        print("4. Mad Libs")
        print("5. Exit")
        
        try:
            pilih = int(input("Choose game what you want: "))
            if pilih == 1:
                guess_number()
            elif pilih == 2:
                suit()
            elif pilih == 3:
                guess_word()
            elif pilih == 4:
                mad_libs()    
            elif pilih == 5:
                print("Thanks!")
                break
            else:
                print("Pilihan tidak valid, silakan coba lagi.")
        except ValueError:
            print('pilih angka pada menu')
menu()