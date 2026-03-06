def dictionary():
    dictionary = {}
    while True:
        print("1. Add word")
        print("2. Delete word")
        print("3. Find word")
        print("4. SHow all words")
        x = input("Enter a value: ")
        match x: 
            case "1":
                print("add word")
                word = input("Enter a word: ")
                meaning = input("Enter the meaning: ")
                dictionary[word] = meaning
                print(f"Word {word} added successfully")
                print("=====================================")
            case "2":
                print("delete word")
                word = input("Enter a word: ")
                if word in dictionary:
                    del dictionary[word]
                    print(f"Word {word} deleted successfully")
                else:
                    print(f"Word {word} not found")
                print("=====================================")

            case "3":
                print("find word")
                word = input("Enter a word: ")
                if word in dictionary:
                    print(f"The meaning of {word} is: {dictionary[word]}")
                else:
                    print(f"Word {word} not found")
                print("=====================================")

            case "4":
                print("show all words")
                for word, meaning in dictionary.items():
                    print(f"{word}: {meaning}")
                print("=====================================")
            case _:
                print("quit")
                return
# dictionary()   

# =========================================================================


def calculate_character_in_string(s : str) -> dict:
    character_count = {}
    for char in s:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count
s = "hello world"
result = calculate_character_in_string(s)
print(result)


# ========================================================================

def fibonanci_n (n: int) -> list:
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence

print(fibonanci_n(10))

# ========================================================================

txt = "hello world"

def tao_file_va_ghi_noi_dung(ten_file, noi_dung):
    try:
        with open(ten_file, 'w', encoding='utf-8') as f:
            f.write(noi_dung)
        print(f"Nội dung đã được ghi vào file {ten_file} thành công.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def thong_ke_file(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            noi_dung = f.read()
            
            # 1. Đếm số dòng: Tách chuỗi dựa trên ký tự xuống dòng
            # Lưu ý: splitlines() xử lý tốt hơn split('\n') vì nó loại bỏ ký tự xuống dòng ở cuối
            f.seek(0) 
            dong = f.readlines()
            print(type(dong))
            so_dong = len(dong)
            
            # 2. Đếm số từ: Tách chuỗi dựa trên khoảng trắng
            # split() mặc định sẽ tách mọi khoảng trắng (space, tab, newline)
            so_tu = len(noi_dung.split())
            
            so_ky_tu = len(noi_dung)
            
            print(f"--- Kết quả thống kê cho file: {ten_file} ---")
            print(f"Số dòng: {so_dong}")
            print(f"Số từ: {so_tu}")
            print(f"Số ký tự: {so_ky_tu}")
            
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file. Bạn hãy kiểm tra lại đường dẫn nhé!")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Gọi hàm với tên file của bạn
# thong_ke_file('du_lieu.txt')