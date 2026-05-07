import time

while True:
    try:
        seconds = int(input("How many seconds the timer should be: "))
        
        if seconds <= 0:
            print("Please enter a positive number!")
            continue
        
        print(f"Starting {seconds} second timer...\n")
        
        for i in range(seconds, 0, -1):
            print(f"Time remaining: {i} seconds", end="\r")
            time.sleep(1)
        
        print("\n✅ Time's up!")
        
        # Ask if user wants to run timer again
        again = input("\nDo you want to set another timer? (yes/no): ").lower()
        if again not in ['yes', 'y']:
            print("Thanks for using the timer! Goodbye! 👋")
            break
            
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")
