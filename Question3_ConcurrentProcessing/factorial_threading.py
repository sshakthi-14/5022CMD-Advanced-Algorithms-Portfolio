import threading
import time


class FactorialPerformanceAnalyzer:
    def __init__(self):
        self.numbers = [50, 100, 200]
        self.rounds = 10

    def factorial(self, number):
        # This function calculates the factorial of a given number.
        # Example: 5! = 5 x 4 x 3 x 2 x 1
        result = 1

        for value in range(2, number + 1):
            result *= value

        return result

    def calculate_factorial_task(self, number, results):
        # This function is used as the target task for each thread.
        # Each thread calculates one factorial value and stores the result.
        results[number] = self.factorial(number)

    def run_multithreaded_once(self):
        # This method calculates 50!, 100!, and 200! using three separate threads.
        results = {}
        threads = []

        start_time = time.perf_counter_ns()

        for number in self.numbers:
            thread = threading.Thread(
                target=self.calculate_factorial_task,
                args=(number, results)
            )
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        end_time = time.perf_counter_ns()
        elapsed_time = end_time - start_time

        return elapsed_time, results

    def run_sequential_once(self):
        # This method calculates 50!, 100!, and 200! without using multithreading.
        results = {}

        start_time = time.perf_counter_ns()

        for number in self.numbers:
            results[number] = self.factorial(number)

        end_time = time.perf_counter_ns()
        elapsed_time = end_time - start_time

        return elapsed_time, results

    def display_factorial_samples(self, results):
        print("\n" + "=" * 90)
        print("FACTORIAL CALCULATION RESULTS")
        print("=" * 90)

        for number in self.numbers:
            factorial_value = results[number]
            factorial_text = str(factorial_value)

            print(f"{number}! = {factorial_text}")
            print(f"Number of digits in {number}! = {len(factorial_text)}")
            print("-" * 90)

    def test_multithreading(self):
        print("\n" + "=" * 90)
        print("MULTITHREADING FACTORIAL TEST")
        print("=" * 90)
        print("Calculating 50!, 100!, and 200! using 3 separate threads")
        print("-" * 90)
        print(f"{'Round':<10}{'Time Taken (ns)':<25}")
        print("-" * 90)

        total_time = 0
        final_results = {}

        for round_number in range(1, self.rounds + 1):
            elapsed_time, results = self.run_multithreaded_once()
            total_time += elapsed_time
            final_results = results

            print(f"{round_number:<10}{elapsed_time:<25}")

        average_time = total_time / self.rounds

        print("-" * 90)
        print(f"Average Multithreading Time: {average_time:.2f} ns")
        print("=" * 90)

        self.display_factorial_samples(final_results)

        return average_time

    def test_sequential(self):
        print("\n" + "=" * 90)
        print("SEQUENTIAL FACTORIAL TEST")
        print("=" * 90)
        print("Calculating 50!, 100!, and 200! without multithreading")
        print("-" * 90)
        print(f"{'Round':<10}{'Time Taken (ns)':<25}")
        print("-" * 90)

        total_time = 0
        final_results = {}

        for round_number in range(1, self.rounds + 1):
            elapsed_time, results = self.run_sequential_once()
            total_time += elapsed_time
            final_results = results

            print(f"{round_number:<10}{elapsed_time:<25}")

        average_time = total_time / self.rounds

        print("-" * 90)
        print(f"Average Sequential Time: {average_time:.2f} ns")
        print("=" * 90)

        self.display_factorial_samples(final_results)

        return average_time

    def compare_performance(self):
        print("\n" + "=" * 90)
        print("FULL PERFORMANCE COMPARISON")
        print("=" * 90)

        multithread_average = self.test_multithreading()
        sequential_average = self.test_sequential()

        print("\n" + "=" * 90)
        print("PERFORMANCE SUMMARY")
        print("=" * 90)
        print(f"Average Multithreading Time : {multithread_average:.2f} ns")
        print(f"Average Sequential Time     : {sequential_average:.2f} ns")

        if multithread_average < sequential_average:
            difference = sequential_average - multithread_average
            print(f"Result: Multithreading was faster by {difference:.2f} ns.")
        elif sequential_average < multithread_average:
            difference = multithread_average - sequential_average
            print(f"Result: Sequential execution was faster by {difference:.2f} ns.")
        else:
            print("Result: Both methods recorded the same average time.")

        print("\nNote:")
        print("For CPU-bound calculations in Python, multithreading may not always improve")
        print("performance because of the Global Interpreter Lock (GIL).")
        print("=" * 90)

    def display_big_o_explanation(self):
        print("\n" + "=" * 90)
        print("FACTORIAL FUNCTION TIME COMPLEXITY")
        print("=" * 90)
        print("The factorial function uses a loop from 2 to n.")
        print("For each loop iteration, one multiplication operation is performed.")
        print("If n is the input number, the loop runs approximately n - 1 times.")
        print("Therefore, the time complexity of the factorial function is O(n).")
        print("=" * 90)


def print_system_header():
    print("\n" + "=" * 90)
    print("FACTORIAL PERFORMANCE ANALYZER")
    print("=" * 90)
    print("Concurrent Processing Experiment using Python Multithreading")
    print("Factorials calculated: 50!, 100!, and 200!")
    print("Time measurement unit: Nanoseconds")
    print("System Version: 1.0")
    print("=" * 90)


def print_main_menu():
    print("\n" + "=" * 90)
    print("MAIN MENU")
    print("=" * 90)
    print("1. Display Big-O Explanation")
    print("2. Run Multithreading Test")
    print("3. Run Sequential Test")
    print("4. Run Full Performance Comparison")
    print("5. Exit System")
    print("=" * 90)


def main():
    analyzer = FactorialPerformanceAnalyzer()

    print_system_header()

    while True:
        print_main_menu()
        choice = input("Please select an option (1-5): ")

        if choice == "1":
            analyzer.display_big_o_explanation()

        elif choice == "2":
            analyzer.test_multithreading()

        elif choice == "3":
            analyzer.test_sequential()

        elif choice == "4":
            analyzer.compare_performance()

        elif choice == "5":
            print("Exiting Factorial Performance Analyzer. Thank you.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
