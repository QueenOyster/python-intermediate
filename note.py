## 1. if__mane__ == "__main__":
from flask import Flask
app = Flask(__name__)
@app.route("/hello") # 아래 함수 실행
def hello():
    return "<h1>Hello Flask!</h1>"

# 모듈이 아니라면 웹서버를 띄워라
if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")


## 2. 중첩함수
def outer_func(num):
    def inner_func():
        print(num)
        return 'complex'
    
    return inner_func
    
fn = outer_func(10) # First-class function
print(fn())         # Closure 호출
# =>inner_func()


## 3. First-class function example
sample_list = ['apple', 'banana', 'citrus']

def index_creator(input_list):
    def text_wrapper():
        print ('<ol>')
        for item in input_list:
            print ('<li>' + item + '</li>')
        print ('</ol>')
    return text_wrapper

func1 = index_creator(sample_list)
# print (func1)
func1()


## 4. Closure Function example
digit_list = [1, 2, 3, 4, 5]

def calc_power(exp):
    def power(digit_list):
        for digit in digit_list:
            print(digit ** exp)
    return power

for expo in range(1, 6):
    func1 = calc_power(expo)
    func1(digit_list)
    print()