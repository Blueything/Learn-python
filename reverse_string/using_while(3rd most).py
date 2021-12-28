def reverse(text):
    length = len(text)-1
    rev=""
    
    while length >= 0:
        rev = rev + text[length]
        length=length-1
        
    return rev

print(reverse("kidrah"))
