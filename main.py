import random
from hangman_art import stages, logo
from hangman_words import word_list

#Kelime listesinden rastgele bir kelime seçer.
def choose_word():
    return random.choice(word_list)

def create_placeholder(word):
    return ["_"] * len(word) #kelimenin uzunluğu kadar alt tireden (_) oluşan bir liste

#bir liste halindeki karakterleri yan yana getirip, aralarına boşluk koyarak ekrana okunabilir bir şekilde yazdırmayı sağlar
def display_current_state(display):
    print("Word to guess: " + " ".join(display))

#Kullanıcı doğru giriş yapana kadar sorar.
def get_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1: #alfabetik (harf) olup olmadığı
            print("Please enter a single valid letter.")
        elif guess in guessed_letters: #Daha önce girilmiş mi?
            print("You already guessed that letter.")
        else:
            return guess

#Kelimeyi index ile dolaşır.
def update_display(word, display, guess):
    for i, letter in enumerate(word): #her adımda bir çift (tuple): (index, eleman)
        if letter == guess:
            display[i] = guess
    return display

def play_game():
    print(logo)

    chosen_word = choose_word()
    display = create_placeholder(chosen_word)

    lives = 6
    guessed_letters = []

    while True:
        print(f"\n{'*' * 20} {lives}/6 LIVES LEFT {'*' * 20}")
        display_current_state(display)

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        #Yanlış tahmin kontrolü
        if guess not in chosen_word:
            lives -= 1
            print(f"{guess} is not in the word.")

        #Kelimeyi güncelle
        display = update_display(chosen_word, display, guess)

        #Kazanma kontrolü
        if "_" not in display:
            display_current_state(display)
            print("YOU WIN!")
            break

        #Kaybetme kontrolü
        if lives == 0:
            print(stages[lives])
            print(f"YOU LOSE! The word was: {chosen_word}")
            break

        #kalan cana göre görsel değişir
        print(stages[lives])

#Python her dosyaya otomatik bir değişken verir: __name__
#1-Dosyayı direkt çalıştırırsan: if __name__ == "__main__": true olur, oyun başlar
#2-Dosyayı başka dosyada kullanırsan: import hangman: __name__ == "hangman": false olur statik çağrılırsa çalışır.
if __name__ == "__main__":
    play_game()