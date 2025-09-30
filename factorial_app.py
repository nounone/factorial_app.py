
import time
import random
import platform
import sys

class FactorialCalculator:
    def __init__(self):
        self.TEST_CASES = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]

    def factorial_iter(self, n: int) -> int:
        if n < 0:
            raise ValueError("0 이상의 정수만 입력 가능합니다.")
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def factorial_rec(self, n: int) -> int:
        if n < 0:
            raise ValueError("0 이상의 정수만 입력 가능합니다.")
        if n <= 1:
            return 1
        return n * self.factorial_rec(n - 1)

    def run_with_time(self, func, n: int) -> tuple:
        time.sleep(random.uniform(0.000001, 0.00001))
        start_time = time.perf_counter()
        result = func(n)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        return result, elapsed_time

    def run(self):
        print("팩토리얼 계산기(반복/재귀) - 정수 n>=0 를 입력하세요.")
        print("-" * 40)
        print(f"| 실행 환경: {platform.system()} {platform.release()}")
        print(f"| 파이썬 버전: {sys.version.split()[0]}")
        print("-" * 40)
    
        while True:
            print("\nFactorial Tester")
            print("1) 반복법으로 n! 계산")
            print("2) 재귀로 n! 계산")
            print("3) 두 방식 모두 계산 후 결과/시간 비교")
            print("4) 준비된 테스트 데이터 일괄 실행")
            print("q) 종료")
            
            choice = input("선택: ")

            if choice in ('1', '2', '3'):
                try:
                    n_str = input("n값(정수, 0 이상)을 입력하세요: ")
                    n = int(n_str)
                    if n < 0:
                        raise ValueError

                    if choice == '1':
                        result, elapsed = self.run_with_time(self.factorial_iter, n)
                        print(f"\n[반복] {n}! = {result}")
                        print(f"[반복] 시간: {elapsed:.6f} s")
                    
                    elif choice == '2':
                        result, elapsed = self.run_with_time(self.factorial_rec, n)
                        print(f"\n[재귀] {n}! = {result}")
                        print(f"[재귀] 시간: {elapsed:.6f} s")

                    elif choice == '3':
                        iter_res, iter_time = self.run_with_time(self.factorial_iter, n)
                        rec_res, rec_time = self.run_with_time(self.factorial_rec, n)
                        
                        print(f"\n[반복] {n}! = {iter_res}")
                        print(f"[재귀] {n}! = {rec_res}")
                        print(f"결과 일치 여부: {'일치' if iter_res == rec_res else '불일치'}")
                        print(f"[반복] 시간: {iter_time:.6f} s | [재귀] 시간: {rec_time:.6f} s")
                
                except ValueError:
                    print("정수(0 이상의 숫자)만 입력하세요.")
                except RecursionError:
                    print(f"오류: 숫자({n})가 너무 커 재귀 깊이 한계를 초과했습니다.")

            elif choice == '4':
                print("\n[테스트 데이터 실행]")
                
                for n in self.TEST_CASES:
                    try:
                        iter_result, iter_elapsed = self.run_with_time(self.factorial_iter, n)
                        rec_result, rec_elapsed = self.run_with_time(self.factorial_rec, n)
                        
                        is_same = "True" if iter_result == rec_result else "False"
                        
                        print(f"\nn = {n} | same={is_same} | iter={iter_elapsed:.6f}s, rec={rec_elapsed:.6f}s")
                        print(f"{n}! = {iter_result}")
                    except RecursionError:
                        iter_result, _ = self.run_with_time(self.factorial_iter, n)
                        print(f"\nn = {n} | [재귀] RecursionError 발생")
                        print(f"{n}! = {iter_result} (반복 방식 결과)")

            elif choice.lower() == 'q':
                print("종료합니다.")
                break
            
            else:
                print("잘못된 선택입니다. 다시 입력해주세요.")


if __name__ == "__main__":
    app = FactorialCalculator()
    app.run()

