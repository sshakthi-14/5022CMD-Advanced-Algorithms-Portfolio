import time

class Transaction:
    def __init__(self, transaction_id, customer_name, product_name, amount, transaction_date, payment_status):
        self.transaction_id = transaction_id
        self.customer_name = customer_name
        self.product_name = product_name
        self.amount = amount
        self.transaction_date = transaction_date
        self.payment_status = payment_status

    def __str__(self):
        return (
            f"ID: {self.transaction_id} | "
            f"Customer: {self.customer_name} | "
            f"Product: {self.product_name} | "
            f"Amount: RM{self.amount:.2f} | "
            f"Date: {self.transaction_date} | "
            f"Status: {self.payment_status}"
        )


class TransactionManager:
    def __init__(self):
        self.transactions = []
        self.recursive_calls = 0
        self.is_sorted = False

    def load_sample_data(self):

        self.transactions = [
            Transaction(1042, "Aisyah", "Wireless Mouse", 45.90, "03/06/2026", "Paid"),
            Transaction(1015, "Daniel", "Laptop Stand", 89.00, "01/06/2026", "Paid"),
            Transaction(1098, "Mei Lin", "Bluetooth Speaker", 129.90, "08/06/2026", "Pending"),
            Transaction(1007, "Ravi", "Keyboard Cover", 18.50, "02/06/2026", "Paid"),
            Transaction(1066, "Sofia", "USB-C Hub", 75.00, "05/06/2026", "Paid"),
            Transaction(1031, "Jason", "Phone Charger", 32.90, "04/06/2026", "Cancelled"),
            Transaction(1083, "Nurul", "Smart Watch Strap", 24.00, "07/06/2026", "Paid"),
            Transaction(1024, "Hannah", "Webcam", 110.00, "03/06/2026", "Pending"),
            Transaction(1075, "Arun", "Gaming Mousepad", 39.90, "06/06/2026", "Paid"),
            Transaction(1058, "Priya", "Earbuds Case", 16.90, "05/06/2026", "Paid"),
            Transaction(1112, "Kevin", "Portable SSD", 299.00, "10/06/2026", "Paid"),
            Transaction(1101, "Farah", "Tablet Sleeve", 49.90, "09/06/2026", "Pending"),
            Transaction(1125, "Marcus", "Ring Light", 68.00, "11/06/2026", "Paid"),
            Transaction(1137, "Leela", "Power Bank", 95.50, "12/06/2026", "Paid"),
            Transaction(1144, "Ethan", "HDMI Cable", 22.00, "13/06/2026", "Cancelled"),
        ]
        self.is_sorted = False

    def display_transactions(self):
        print("\n" + "=" * 110)
        print("SHOPEASE ONLINE SHOPPING TRANSACTION RECORDS")
        print("=" * 110)

        if not self.transactions:
            print("No transaction records available.")
        else:
            for index, transaction in enumerate(self.transactions, start=1):
                print(f"{index:02d}. {transaction}")

        print("=" * 110)

    def merge_sort(self, transaction_list):

        self.recursive_calls += 1

        if len(transaction_list) <= 1:
            return transaction_list

        middle = len(transaction_list) // 2
        left_half = transaction_list[:middle]
        right_half = transaction_list[middle:]


        sorted_left = self.merge_sort(left_half)
        sorted_right = self.merge_sort(right_half)


        return self.merge(sorted_left, sorted_right)

    def merge(self, left, right):

        sorted_list = []
        left_index = 0
        right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index].transaction_id <= right[right_index].transaction_id:
                sorted_list.append(left[left_index])
                left_index += 1
            else:
                sorted_list.append(right[right_index])
                right_index += 1

        while left_index < len(left):
            sorted_list.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            sorted_list.append(right[right_index])
            right_index += 1

        return sorted_list

    def sort_transactions(self):
        print("\nSorting transactions using Merge Sort...")

        self.recursive_calls = 0

        start_time = time.perf_counter_ns()
        self.transactions = self.merge_sort(self.transactions)
        end_time = time.perf_counter_ns()

        self.is_sorted = True

        print("Transactions sorted successfully by Transaction ID.")
        print(f"Recursive Calls Made: {self.recursive_calls}")
        print(f"Merge Sort Time Taken: {end_time - start_time} ns")

    def binary_search(self, target_id):
        if not self.is_sorted:
            print("\nTransactions must be sorted before using Binary Search.")
            return None, 0

        low = 0
        high = len(self.transactions) - 1
        comparisons = 0

        while low <= high:
            comparisons += 1
            middle = (low + high) // 2
            current_id = self.transactions[middle].transaction_id

            if current_id == target_id:
                return self.transactions[middle], comparisons
            elif target_id < current_id:
                high = middle - 1
            else:
                low = middle + 1

        return None, comparisons

    def linear_search(self, target_id):
        comparisons = 0

        for transaction in self.transactions:
            comparisons += 1
            if transaction.transaction_id == target_id:
                return transaction, comparisons

        return None, comparisons

    def search_transaction_binary(self):
        try:
            target_id = int(input("\nEnter Transaction ID to search using Binary Search: "))
            transaction, comparisons = self.binary_search(target_id)

            print("\n========== BINARY SEARCH RESULT ==========")
            if transaction:
                print("Transaction found.")
                print(f"Comparisons Made: {comparisons}")
                print(transaction)
            else:
                print("Transaction not found.")
                print(f"Comparisons Made: {comparisons}")
            print("==========================================")

        except ValueError:
            print("Invalid input. Transaction ID must be a number.")

    def search_transaction_linear(self):
        try:
            target_id = int(input("\nEnter Transaction ID to search using Linear Search: "))
            transaction, comparisons = self.linear_search(target_id)

            print("\n========== LINEAR SEARCH RESULT ==========")
            if transaction:
                print("Transaction found.")
                print(f"Comparisons Made: {comparisons}")
                print(transaction)
            else:
                print("Transaction not found.")
                print(f"Comparisons Made: {comparisons}")
            print("==========================================")

        except ValueError:
            print("Invalid input. Transaction ID must be a number.")

    def insert_transaction(self):
        try:
            print("\n========== ADD NEW TRANSACTION ==========")
            transaction_id = int(input("Enter Transaction ID: "))
            customer_name = input("Enter Customer Name: ")
            product_name = input("Enter Product Name: ")
            amount = float(input("Enter Amount (RM): "))
            transaction_date = input("Enter Transaction Date (DD/MM/YYYY): ")
            payment_status = input("Enter Payment Status: ")

            new_transaction = Transaction(
                transaction_id,
                customer_name,
                product_name,
                amount,
                transaction_date,
                payment_status
            )

            self.transactions.append(new_transaction)
            self.is_sorted = False

            print("\nNew transaction added successfully.")
            print("Note: The transaction list is now unsorted. Please sort again before using Binary Search.")

        except ValueError:
            print("Invalid input. Please enter the correct data type.")

    def compare_search_performance(self):
        if not self.is_sorted:
            print("\nTransactions must be sorted before performance comparison.")
            print("Please choose option 2 to sort transactions first.")
            return

        test_ids = [1007, 1042, 1083, 1112, 1144, 9999, 8888, 7777]

        total_binary_time = 0
        total_linear_time = 0
        total_binary_comparisons = 0
        total_linear_comparisons = 0

        print("\n" + "=" * 95)
        print("BINARY SEARCH VS LINEAR SEARCH PERFORMANCE COMPARISON")
        print("=" * 95)
        print(f"{'Test ID':<12}{'Binary Time(ns)':<20}{'Linear Time(ns)':<20}{'Binary Comp.':<15}{'Linear Comp.':<15}")
        print("-" * 95)

        for test_id in test_ids:
            start_binary = time.perf_counter_ns()
            _, binary_comparisons = self.binary_search(test_id)
            end_binary = time.perf_counter_ns()
            binary_time = end_binary - start_binary

            start_linear = time.perf_counter_ns()
            _, linear_comparisons = self.linear_search(test_id)
            end_linear = time.perf_counter_ns()
            linear_time = end_linear - start_linear

            total_binary_time += binary_time
            total_linear_time += linear_time
            total_binary_comparisons += binary_comparisons
            total_linear_comparisons += linear_comparisons

            print(
                f"{test_id:<12}"
                f"{binary_time:<20}"
                f"{linear_time:<20}"
                f"{binary_comparisons:<15}"
                f"{linear_comparisons:<15}"
            )

        total_tests = len(test_ids)

        print("-" * 95)
        print(f"Average Binary Search Time : {total_binary_time / total_tests:.2f} ns")
        print(f"Average Linear Search Time : {total_linear_time / total_tests:.2f} ns")
        print(f"Average Binary Comparisons : {total_binary_comparisons / total_tests:.2f}")
        print(f"Average Linear Comparisons : {total_linear_comparisons / total_tests:.2f}")
        print("=" * 95)

    def compare_merge_sort_and_binary_search(self):
        test_id = 1042
        copied_transactions = self.transactions.copy()

        print("\n" + "=" * 90)
        print("MERGE SORT VS BINARY SEARCH EXECUTION TIME")
        print("=" * 90)

        self.recursive_calls = 0

        start_sort = time.perf_counter_ns()
        sorted_transactions = self.merge_sort(copied_transactions)
        end_sort = time.perf_counter_ns()
        merge_sort_time = end_sort - start_sort

        start_binary = time.perf_counter_ns()

        low = 0
        high = len(sorted_transactions) - 1
        comparisons = 0
        found_transaction = None

        while low <= high:
            comparisons += 1
            middle = (low + high) // 2
            current_id = sorted_transactions[middle].transaction_id

            if current_id == test_id:
                found_transaction = sorted_transactions[middle]
                break
            elif test_id < current_id:
                high = middle - 1
            else:
                low = middle + 1

        end_binary = time.perf_counter_ns()
        binary_search_time = end_binary - start_binary

        print(f"Test Transaction ID       : {test_id}")
        print(f"Merge Sort Time Taken     : {merge_sort_time} ns")
        print(f"Binary Search Time Taken  : {binary_search_time} ns")
        print(f"Recursive Calls Made      : {self.recursive_calls}")
        print(f"Binary Search Comparisons : {comparisons}")

        if found_transaction:
            print("Search Result             : Transaction found.")
        else:
            print("Search Result             : Transaction not found.")

        print("=" * 90)


def print_system_header():
    print("\n" + "=" * 90)
    print("SHOPEASE TRANSACTION SORTING AND SEARCH SYSTEM")
    print("=" * 90)
    print("Online Shopping Transaction Management System")
    print("Developed using Divide and Conquer Algorithms")
    print("Algorithms: Merge Sort | Binary Search | Linear Search")
    print("System Version: 1.0")
    print("=" * 90)


def print_main_menu():
    print("\n" + "=" * 90)
    print("MAIN MENU")
    print("=" * 90)
    print("1. Display All Transactions")
    print("2. Sort Transactions by ID using Merge Sort")
    print("3. Search Transaction by ID using Binary Search")
    print("4. Search Transaction by ID using Linear Search")
    print("5. Add New Transaction")
    print("6. Compare Binary Search and Linear Search Performance")
    print("7. Compare Merge Sort and Binary Search Time")
    print("8. Exit System")
    print("=" * 90)


def main():
    manager = TransactionManager()
    manager.load_sample_data()

    print_system_header()

    while True:
        print_main_menu()
        choice = input("Please select an option (1-8): ")

        if choice == "1":
            manager.display_transactions()

        elif choice == "2":
            print("\nBefore Sorting:")
            manager.display_transactions()

            manager.sort_transactions()

            print("\nAfter Sorting:")
            manager.display_transactions()

        elif choice == "3":
            manager.search_transaction_binary()

        elif choice == "4":
            manager.search_transaction_linear()

        elif choice == "5":
            manager.insert_transaction()

        elif choice == "6":
            manager.compare_search_performance()

        elif choice == "7":
            manager.compare_merge_sort_and_binary_search()

        elif choice == "8":
            print("Exiting ShopEase Transaction System. Thank you.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
