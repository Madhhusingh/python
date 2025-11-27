# SUPER BEAUTIFUL EXPENSE TRACKER (No Functions, No Imports)

# ==== COLORS ====
RESET="\033[0m"
BOLD="\033[1m"
RED="\033[91m"
GREEN="\033[92m"
YELLOW="\033[93m"
BLUE="\033[94m"
MAGENTA="\033[95m"
CYAN="\033[96m"
WHITE="\033[97m"

# ==== Data ====
expensesList = []

# ==== Fake Animation Heading ====
for line in ["\n", "Loading Expense Tracker...", ".", "..", "..."]:
    print(MAGENTA + BOLD + line + RESET)

print(MAGENTA + BOLD)
print("╔" + "═" * 55 + "╗")
print("║" + "🎯  WELCOME TO ADVANCED EXPENSE TRACKER  🎯".center(55) + "║")
print("╚" + "═" * 55 + "╝")
print(RESET)

while True:

    print(CYAN + BOLD + "\n═════════════════════════════════")
    print("              MENU")
    print("═════════════════════════════════" + RESET)

    print(
        YELLOW +
        "1) ➕ Add Expense\n"
        "2) 📜 View All Expenses\n"
        "3) 📊 Category Wise Total\n"
        "4) 💰 Total Spending\n"
        "5) 🚪 Exit\n"
        + RESET
    )

    choice = input(BLUE + BOLD + "👉 Enter Your Choice: " + RESET)

# ======================================================================
#                          ADD EXPENSE
# ======================================================================
    if choice == "1":

        print(GREEN + BOLD + "\n➕ ADDING NEW EXPENSE…" + RESET)

        date = input("📅 Date (DD-MM-YYYY): ")
        category = input("📂 Category (Food/Travel/Books/Shopping): ")
        description = input("📝 Description: ")

        amount_input = input("💵 Amount: ")

        # Validation
        valid = True
        for ch in amount_input:
            if ch not in "0123456789.":
                valid = False
                break

        if valid:
            amount = float(amount_input)
        else:
            print(RED + "❌ Invalid Amount! Only numbers allowed." + RESET)
            continue

        expensesList.append({
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        })

        print(GREEN + "\n✔ Expense Added Successfully!" + RESET)

# ======================================================================
#                       VIEW ALL EXPENSES
# ======================================================================
    elif choice == "2":

        if len(expensesList) == 0:
            print(RED + "\n⚠ No Expenses Added Yet!" + RESET)
        else:

            print(MAGENTA + BOLD + "\n📜 ALL EXPENSES" + RESET)
            print(YELLOW + "────────────────────────────────────────────────────────────────────────")
            print(" No |     Date     | Category     |   Description        | Amount ")
            print("────────────────────────────────────────────────────────────────────────" + RESET)

            count = 1
            for e in expensesList:
                print(
                    f" {count:<3}| {e['date']:<12} | {e['category']:<12} | {e['description']:<18} | ₹{e['amount']}"
                )
                count += 1

            print(YELLOW + "────────────────────────────────────────────────────────────────────────" + RESET)

# ======================================================================
#                   CATEGORY WISE TOTAL
# ======================================================================
    elif choice == "3":

        if len(expensesList) == 0:
            print(RED + "\n⚠ No Data Available!" + RESET)
        else:

            print(CYAN + BOLD + "\n📊 CATEGORY WISE TOTAL" + RESET)
            print(YELLOW + "──────────────────────────────────────" + RESET)

            categories = {}

            # No functions, no defaultdict — pure manual loop
            for e in expensesList:
                cat = e["category"]
                amt = e["amount"]
                if cat in categories:
                    categories[cat] += amt
                else:
                    categories[cat] = amt

            for cat in categories:
                print(GREEN + f"{cat:<12} : ₹{categories[cat]}" + RESET)

            print(YELLOW + "──────────────────────────────────────" + RESET)

# ======================================================================
#                         TOTAL SPENDING
# ======================================================================
    elif choice == "4":

        total = 0
        for e in expensesList:
            total += e["amount"]

        print(BLUE + BOLD + f"\n💰 TOTAL EXPENSE = ₹{total}" + RESET)

# ======================================================================
#                             EXIT
# ======================================================================
    elif choice == "5":

        print(GREEN + BOLD + "\n🙏 THANK YOU FOR USING EXPENSE TRACKER!" + RESET)

        # Beautiful goodbye box
        print(MAGENTA + BOLD)
        print("╔" + "═" * 40 + "╗")
        print("║" + " Goodbye! Have a great day ❤ ".center(40) + "║")
        print("╚" + "═" * 40 + "╝" + RESET)
        break

    else:
        print(RED + "❌ Invalid Choice!" + RESET)

    input(YELLOW + "\n➡ Press ENTER to continue…" + RESET)
