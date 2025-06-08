def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
   
    shopping_list = [] # Initialize an empty list named shopping_list

    while True:
        display_menu() # Display the menu to the user
        choice = input("Enter your choice: ") # Get the user's choice

        if choice == '1':
            # Add Item functionality
            item_to_add = input("Enter the item to add: ").strip() # Prompt for item name, remove leading/trailing whitespace
            if item_to_add: # Ensure the item name is not empty
                shopping_list.append(item_to_add) # Add the item to the list
                print(f"'{item_to_add}' has been added to your shopping list.")
            else:
                print("Item name cannot be empty. Please try again.")
        elif choice == '2':
            # Remove Item functionality
            if not shopping_list: # Check if the list is empty before trying to remove
                print("Your shopping list is empty. Nothing to remove.")
            else:
                item_to_remove = input("Enter the item to remove: ").strip() # Prompt for item name
                if item_to_remove in shopping_list: # Check if the item exists in the list
                    shopping_list.remove(item_to_remove) # Remove the item from the list
                    print(f"'{item_to_remove}' has been removed from your shopping list.")
                else:
                    print(f"'{item_to_remove}' not found in your shopping list.") # Display message if item not found
        elif choice == '3':
            # View List functionality
            if not shopping_list: # Check if the list is empty
                print("Your shopping list is currently empty.")
            else:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list, 1): # Iterate and print each item with a number
                    print(f"{i}. {item}")
                print("--------------------------")
        elif choice == '4':
            # Exit functionality
            print("Goodbye!")
            break # Exit the loop, ending the program
        else:
            # Handle invalid menu choices gracefully
            print("Invalid choice. Please try again.")

# This ensures that main() is called only when the script is executed directly
if __name__ == "__main__":
    main()