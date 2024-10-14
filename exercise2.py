import re
import json


def count_unique_words(input_string):
    # Chuyển chuỗi về chữ thường để không phân biệt chữ hoa chữ thường
    input_string = input_string.lower()

    # Loại bỏ địa chỉ email
    input_string = re.sub(r"[\w\.,]+@[\w\.,]+\.\w+", "", input_string)

    # Loại bỏ các số
    input_string = re.sub(r"\b\d+\b", "", input_string)

    # Loại bỏ các dấu câu (dấu chấm, phẩy, chấm than, chấm hỏi, v.v.)
    input_string = re.sub(r"[^\w\s]", "", input_string)

    # Tách các từ từ chuỗi, sử dụng split() với dấu cách
    words = input_string.split()

    # Sử dụng set để loại bỏ các từ trùng lặp
    unique_words = set(words)

    # Loại bỏ các phần tử rỗng (nếu có)
    unique_words.discard("")
    # Trả về số lượng từ duy nhất
    return len(unique_words)


def count_word_by_keyword(input_string, list_of_keyword):
    # Chuyển chuỗi và danh sách từ khóa về chữ thường để không phân biệt chữ hoa chữ thường
    input_string = input_string.lower()
    list_of_keyword = [keyword.lower() for keyword in list_of_keyword]

    # Tách các từ từ chuỗi
    words = input_string.split()

    # Tạo từ điển để lưu số lần xuất hiện của mỗi từ khóa
    keyword_count = {keyword: 0 for keyword in list_of_keyword}

    # Đếm số lần mỗi từ khóa xuất hiện
    for word in words:
        if word in keyword_count:
            keyword_count[word] += 1

    return keyword_count


def extract_numeric(input_string):
    num = []
    for word in input_string.split():
        try:
            num.append(float(word))
        except ValueError:
            pass
    return num


def extract_email(input_string):
    lst_email = []
    match = re.findall(r"[\w\.,]+@[\w\.,]+\.\w+", input_string)
    for i in match:
        lst_email.append(i)
    return lst_email


def process_text(input_string, **kwargs):
    result = {}
    if config["count_words"]:
        result["count_words"] = count_unique_words(input_string)
    if config["find_keywords"]:
        result["keywords"] = count_word_by_keyword(
            input_string, config["find_keywords"]
        )
    if config["uppercase"]:
        result["uppercase_text"] = input_string.upper()
    if config["extract_integers"]:
        result["integers"] = extract_numeric(input_string)
    if config["extract_email"]:
        result["emails"] = extract_email(input_string)
    return result


if __name__ == "__main__":
    with open("config.json", "r") as file:
        config = json.load(file)
    file = open("sample.txt", "r")
    input_string = file.read()
    result = process_text(input_string, config)

    with open("result.json", "w") as f:
        json.dump(result, f)
