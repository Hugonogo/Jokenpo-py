import emoji
import random
import time
#emojis{raised_first, raised_hand, victory_hand}
jogo = True
fim = False
while(jogo):
    time.sleep(2)
    print('#' * 20)
    print("Quer jogar jokenpo?\n (S): Sim\n (N): Não")
    resposta = input('>>').upper().strip()
    print('#' * 20)
    if resposta == 'S':
        print(emoji.emojize('Pedra = :raised_fist: (1)'))
        print(emoji.emojize('Papel = :raised_hand: (2)'))
        print(emoji.emojize('Tesoura = :victory_hand: (3)'))

        escolha = int(input("sua escolha: "))
        p2 = random.randint(1,3)

        if escolha == p2:
            if escolha == 1 and p2 == 1:
                print(emoji.emojize(':raised_fist:  :raised_fist:'))
            elif escolha == 2 and p2 == 2:
                print(emoji.emojize(':raised_hand:  :raised_hand:'))
            elif escolha == 3 and p2 == 3:
                print(emoji.emojize(':victory_hand:  :victory_hand:'))
            
            print('empate')

        if escolha == 1 and p2 == 3:
            print(emoji.emojize(':raised_fist:  :victory_hand: '))
            print('ganhou')
        elif escolha == 2 and p2 == 1:
            print(emoji.emojize(':raised_hand:  :raised_fist:'))
            print('ganhou')
        elif escolha == 3 and p2 == 2:
            print(emoji.emojize(':victory_hand:  :raised_hand:'))
            print('ganhou')
        elif escolha == 1 and p2 == 2:
            print(emoji.emojize(':raised_fist:  :raised_hand: '))
            print('Perdeu')
        elif escolha == 2 and p2 == 3:
            print(emoji.emojize(':raised_hand:  :victory_hand:'))
            print('perdeu')
        elif escolha == 3 and p2 == 1:
            print(emoji.emojize(':victory_hand:  :raised_fist:'))
            print('perdeu')
        
    else:
         jogo = fim

