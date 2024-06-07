# 1. შექმენი ფუნქცია, რომელიც მომხმარებლისგან მიღებულ ინფორმაციას გაასამმაგებს
# და დაბეჭდავს შემდეგნაირად:

input: “word”
Output: „Tripled: wordwordword“

def triple_info(info):

  tripled_info = info * 3
  # print("word")
  print(f"Tripled: {tripled_info}")

triple_info("word")

# 2. შექმენი ფუნქცია, რომელიც მიიღებს მომხმარებლის წონას და დააბრუნებს მის წონას
# მთვარეზე. (მთვარის გრავიტაცია 6_ჯერ ნაკლებია დედამიწისაზე)

def weight_on_moon(earth_weight):

  moon_gravity = (1/6)

  return earth_weight * moon_gravity

weight = 60
moon_weight = weight_on_moon(weight)

print(f"An object weighing {weight} kilograms on Earth would weigh approximately {moon_weight} kilograms on the moon.")

# 3. შექმენი კალკულატორის ფუნქცია, რომელიც მიიღებს გამოსახულებას
# მომხმარებლისგან input() ფუნქციის დახმარებით (სამ მონაცემს _ პირველ რიცხვს,
# მოქმედებას (+ - * / ^), მეორე რიცხვს)
# მაგ. „2 * 6“ დათვლის და დააბრუნებს შედეგს. გაითვალისწინე რომ რიცხვის შეყვანის
# მაგიერ სიმბოლოების შეყვანის შემთხვევაში უნდა დააბრუნოს ფუნქციამ შესაბამისი
# მესიჯი. ასევე ნულზე გაყოფა არ შეიძ ება, ამ შემთხვევაშიც უნდა დააბრუნოს
# შესაბამისი მესიჯი. (დააბრუნოს და არა დაპრინტოს)

def calculator(expression):

  try:
    parts = expression.split()
    if len(parts) != 3:
      raise ValueError("Invalid expression format")

    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    if operator == "+":
      result = num1 + num2
    elif operator == "-":
      result = num1 - num2
    elif operator == "*":
      result = num1 * num2
    elif operator == "/":
      if num2 == 0:
        raise ZeroDivisionError("Division by zero")
      result = num1 / num2
    elif operator == "^":
      result = num1 ** num2
    else:
      raise ValueError("Invalid operator")

    return result

  except (ValueError, ZeroDivisionError) as e:
    return str(e)

expression = input("Enter your expression (e.g., 2 * 3): ")
result = calculator(expression)
print(result)

# 4. გავლილი მასალის გამოყენებით შექმენი ფუნქცია, რომელიც მიიღებს ლათინური
# სიმბოლოებით დაწერილ სიტყვას, დაშიფრავს მორზეს ანბანით და დააბრუნებს შედეგს.

MORSE_CODE = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': "...", 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '.---', 'Z': '--..',
    ' ': '/'
}

def text_to_morse(text):

  text = text.upper()
  morse_code = []
  for char in text:
    if char in MORSE_CODE:
      morse_code.append(MORSE_CODE[char])
    else:
      pass
  return ' '.join(morse_code)

text = "tiko"
morse_code = text_to_morse(text)
print(morse_code)