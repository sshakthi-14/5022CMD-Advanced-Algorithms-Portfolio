import time
import random

class Medicine:
    def __init__(self, medicine_id, name, category, supplier, expiry_date, quantity, price):
        self.medicine_id = medicine_id
        self.name = name
        self.category = category
        self.supplier = supplier
        self.expiry_date = expiry_date
        self.quantity = quantity
        self.price = price

    def stock_status(self):
        return "LOW STOCK" if self.quantity < 20 else "AVAILABLE"

    def __str__(self):
        return (
            f"ID: {self.medicine_id} | "
            f"Name: {self.name} | "
            f"Category: {self.category} | "
            f"Supplier: {self.supplier} | "
            f"Expiry: {self.expiry_date} | "
            f"Qty: {self.quantity} | "
            f"Price: RM{self.price:.2f} | "
            f"Status: {self.stock_status()}"
        )

class HashTable:
    def __init__(self, size=20):
        self.size = size
        self.table = [None] * size
        self.count = 0
        self.collision_count = 0

    def hash_function(self, key):
        return key % self.size

    def insert(self, medicine, show_process=False):
        index = self.hash_function(medicine.medicine_id)
        original_index = index
        probes = 0

        if show_process:
            print(f"\nHash Calculation: {medicine.medicine_id} % {self.size} = {index}")

        while self.table[index] is not None:
            if self.table[index].medicine_id == medicine.medicine_id:
                self.table[index] = medicine
                if show_process:
                    print(f"Medicine updated at bucket {index}.")
                return index

            self.collision_count += 1
            probes += 1

            if show_process:
                print(f"Collision detected at bucket {index}. Moving to next bucket...")

            index = (index + 1) % self.size

            if index == original_index:
                print("Hash table is full. Cannot insert medicine.")
                return None

        self.table[index] = medicine
        self.count += 1

        if show_process:
            print(f"Medicine inserted into bucket {index}.")
            print(f"Total probes used: {probes}")

        return index

    def search_by_id(self, medicine_id):
        index = self.hash_function(medicine_id)
        original_index = index
        comparisons = 0

        while self.table[index] is not None:
            comparisons += 1

            if self.table[index].medicine_id == medicine_id:
                return self.table[index], index, comparisons

            index = (index + 1) % self.size

            if index == original_index:
                break

        return None, None, comparisons

    def search_by_name(self, name):
        results = []

        for index, medicine in enumerate(self.table):
            if medicine is not None and name.lower() in medicine.name.lower():
                results.append((medicine, index))

        return results

    def display_inventory(self):
        print("\n" + "=" * 110)
        print("TRUECARE PHARMACY INVENTORY")
        print("=" * 110)

        for index, medicine in enumerate(self.table):
            if medicine is None:
                print(f"Bucket {index:02d}: EMPTY")
            else:
                print(f"Bucket {index:02d}: {medicine}")

        print("=" * 110)

    def inventory_summary(self):
        medicines = [medicine for medicine in self.table if medicine is not None]

        if not medicines:
            print("No medicines available.")
            return

        total_quantity = sum(medicine.quantity for medicine in medicines)
        average_price = sum(medicine.price for medicine in medicines) / len(medicines)
        low_stock_items = [medicine for medicine in medicines if medicine.quantity < 20]
        most_expensive = max(medicines, key=lambda medicine: medicine.price)
        lowest_stock = min(medicines, key=lambda medicine: medicine.quantity)
        load_factor = self.count / self.size

        print("\n" + "=" * 65)
        print("TRUECARE PHARMACY INVENTORY SUMMARY")
        print("=" * 65)
        print(f"Total Medicines Stored : {self.count}")
        print(f"Hash Table Size        : {self.size}")
        print(f"Load Factor            : {load_factor:.2f}")
        print(f"Total Quantity         : {total_quantity} units")
        print(f"Average Price          : RM{average_price:.2f}")
        print(f"Low Stock Items        : {len(low_stock_items)}")
        print(f"Most Expensive Item    : {most_expensive.name} - RM{most_expensive.price:.2f}")
        print(f"Lowest Stock Item      : {lowest_stock.name} - {lowest_stock.quantity} units")
        print(f"Total Collisions       : {self.collision_count}")

        if low_stock_items:
            print("\nLow Stock Medicine List:")
            for medicine in low_stock_items:
                print(f"- {medicine.name} ({medicine.quantity} units)")

        print("=" * 65)


def print_system_header():
    print("\n" + "=" * 75)
    print("TRUECARE PHARMACY")
    print("Inventory Management System")
    print("=" * 75)
    print("Address: 3G-G-2, Jalan Seri Tanjung Pinang,")
    print("         Seri Tanjung Pinang, 10470 Tanjung Tokong,")
    print("         Pulau Pinang")
    print("System Version: 1.0")
    print("=" * 75)


def linear_array_search(medicine_array, medicine_id):
    comparisons = 0

    for medicine in medicine_array:
        comparisons += 1
        if medicine.medicine_id == medicine_id:
            return medicine, comparisons

    return None, comparisons


def load_sample_data(hash_table, medicine_array):
    sample_medicines = [
        Medicine(2051, "Paracetamol 500mg", "Tablet", "Duopharma", "12/2027", 80, 5.50),
        Medicine(3178, "Vitamin C 1000mg", "Supplement", "Appeton", "08/2028", 60, 18.90),
        Medicine(1086, "Ibuprofen 200mg", "Tablet", "Hovid", "06/2027", 15, 7.90),
        Medicine(2245, "Amoxicillin 250mg", "Capsule", "MediLab", "09/2027", 45, 22.50),
        Medicine(5092, "Cough Syrup", "Syrup", "Prospan", "04/2028", 35, 14.90),
        Medicine(7811, "Eye Drops", "Liquid", "Alcon", "01/2028", 18, 11.80),
        Medicine(4157, "Calcium Plus", "Supplement", "Kordel's", "10/2028", 55, 25.50),
        Medicine(9934, "Loratadine 10mg", "Tablet", "PharmaLife", "07/2027", 27, 9.90),
        Medicine(6203, "Omega 3 Fish Oil", "Supplement", "Blackmores", "05/2029", 40, 28.90),
        Medicine(1475, "Antacid Chewable", "Tablet", "HealCare", "11/2027", 12, 6.20),
    ]

    print("\nLoading TrueCare Pharmacy sample medicine records...")

    for medicine in sample_medicines:
        hash_table.insert(medicine, show_process=True)
        medicine_array.append(medicine)


def add_medicine(hash_table, medicine_array):
    try:
        print("\n========== ADD NEW MEDICINE ==========")
        medicine_id = int(input("Enter Medicine ID: "))
        name = input("Enter Medicine Name: ")
        category = input("Enter Category: ")
        supplier = input("Enter Supplier: ")
        expiry_date = input("Enter Expiry Date (MM/YYYY): ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price (RM): "))

        medicine = Medicine(medicine_id, name, category, supplier, expiry_date, quantity, price)
        bucket = hash_table.insert(medicine, show_process=True)

        if bucket is not None:
            medicine_array.append(medicine)
            print("\nMedicine successfully added to TrueCare Pharmacy inventory.")
            print(f"Stored in bucket: {bucket}")

    except ValueError:
        print("Invalid input. Please enter correct data types.")


def search_medicine_by_id(hash_table):
    try:
        medicine_id = int(input("\nEnter Medicine ID to search: "))
        medicine, bucket, comparisons = hash_table.search_by_id(medicine_id)

        print("\n========== SEARCH RESULT ==========")
        if medicine:
            print("Medicine found in TrueCare Pharmacy inventory.")
            print(f"Bucket Location : {bucket}")
            print(f"Comparisons     : {comparisons}")
            print(medicine)
        else:
            print("Medicine not found.")
            print(f"Comparisons made: {comparisons}")
        print("===================================")

    except ValueError:
        print("Invalid input. Medicine ID must be a number.")


def search_medicine_by_name(hash_table):
    name = input("\nEnter Medicine Name to search: ")
    results = hash_table.search_by_name(name)

    print("\n========== NAME SEARCH RESULT ==========")
    if results:
        for medicine, bucket in results:
            print(f"Bucket {bucket}: {medicine}")
    else:
        print("No medicine found with that name.")
    print("========================================")


def performance_comparison(hash_table, medicine_array):
    existing_keys = [medicine.medicine_id for medicine in medicine_array]
    non_existing_keys = [9001, 9002, 9003, 9004, 9005, 9101, 9102, 9103, 9104, 9105]

    search_keys = []
    for _ in range(50):
        search_keys.append(random.choice(existing_keys))
        search_keys.append(random.choice(non_existing_keys))

    total_hash_time = 0
    total_array_time = 0
    total_hash_comparisons = 0
    total_array_comparisons = 0

    print("\n" + "=" * 75)
    print("TRUECARE PHARMACY: HASH TABLE VS ARRAY PERFORMANCE TEST")
    print("=" * 75)
    print("Experiment: 100 searches, including existing and non-existing IDs")
    print("-" * 75)
    print(f"{'No.':<5}{'Key':<10}{'Hash Time(ns)':<20}{'Array Time(ns)':<20}")
    print("-" * 75)

    for i, key in enumerate(search_keys, start=1):
        start_hash = time.perf_counter_ns()
        _, _, hash_comparisons = hash_table.search_by_id(key)
        end_hash = time.perf_counter_ns()
        hash_time = end_hash - start_hash

        start_array = time.perf_counter_ns()
        _, array_comparisons = linear_array_search(medicine_array, key)
        end_array = time.perf_counter_ns()
        array_time = end_array - start_array

        total_hash_time += hash_time
        total_array_time += array_time
        total_hash_comparisons += hash_comparisons
        total_array_comparisons += array_comparisons

        if i <= 10:
            print(f"{i:<5}{key:<10}{hash_time:<20}{array_time:<20}")

    avg_hash_time = total_hash_time / len(search_keys)
    avg_array_time = total_array_time / len(search_keys)
    avg_hash_comparisons = total_hash_comparisons / len(search_keys)
    avg_array_comparisons = total_array_comparisons / len(search_keys)

    print("-" * 75)
    print("Only the first 10 searches are displayed.")
    print(f"Average Hash Table Search Time : {avg_hash_time:.2f} ns")
    print(f"Average Array Search Time      : {avg_array_time:.2f} ns")
    print(f"Average Hash Comparisons       : {avg_hash_comparisons:.2f}")
    print(f"Average Array Comparisons      : {avg_array_comparisons:.2f}")

    if avg_hash_time > 0:
        print(f"Array Search / Hash Search Ratio: {avg_array_time / avg_hash_time:.2f} times")

    print("=" * 75)


def explain_hashing():
    print("\n" + "=" * 70)
    print("HASHING AND LINEAR PROBING EXPLANATION")
    print("=" * 70)
    print("Hash Function Used:")
    print("medicine_id % table_size")
    print("\nExample:")
    print("2051 % 20 = 11")
    print("Therefore, medicine ID 2051 starts at bucket 11.")
    print("\nCollision Example:")
    print("7811 % 20 = 11")
    print("Since bucket 11 may already be occupied, linear probing checks")
    print("the next available bucket until an empty bucket is found.")
    print("=" * 70)


def main():
    hash_table = HashTable(size=20)
    medicine_array = []

    print_system_header()
    load_sample_data(hash_table, medicine_array)

    while True:
        print("\n" + "=" * 75)
        print("TRUECARE PHARMACY INVENTORY MANAGEMENT SYSTEM")
        print("=" * 75)
        print("1. Display Pharmacy Inventory")
        print("2. Add New Medicine")
        print("3. Search Medicine by ID")
        print("4. Search Medicine by Name")
        print("5. Inventory Statistics")
        print("6. Hash Table vs Array Performance Test")
        print("7. Hashing and Linear Probing Explanation")
        print("8. Exit System")
        print("=" * 75)

        choice = input("Please select an option (1-8): ")

        if choice == "1":
            hash_table.display_inventory()
        elif choice == "2":
            add_medicine(hash_table, medicine_array)
        elif choice == "3":
            search_medicine_by_id(hash_table)
        elif choice == "4":
            search_medicine_by_name(hash_table)
        elif choice == "5":
            hash_table.inventory_summary()
        elif choice == "6":
            performance_comparison(hash_table, medicine_array)
        elif choice == "7":
            explain_hashing()
        elif choice == "8":
            print("Exiting TrueCare Pharmacy Inventory Management System. Thank you.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
