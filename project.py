import time
from datetime import datetime, timedelta
def display_date():
  current_date = datetime.now()
  formatted_date = current_date.strftime("%Y-%m-%d")
  print(formatted_date)


def display_time():
  # Define the UTC offset for Indian Standard Time (IST)
  ist_offset = timedelta(hours=5, minutes=30)

  current_utc_time = datetime.utcnow()
  ist_time = current_utc_time + ist_offset

  # Format the time as HH:MM:SS AM/PM
  ist_formatted = ist_time.strftime("%I:%M:%S %p")

  print("Indian Standard Time (IST):", ist_formatted)

#Timer code 
def timer():
  my_time=int(input("Enter the time in seconds: "))

  for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours=int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

  print("TIME'S UP Broo!!")

# Home Page
print("\n1. Display current date")
print("2. Display current time")
print("3. Set a timer")
print("4. Exit")
choice= int(input("Enter your choice(1/2/3):"))

if choice==1:
  display_date()
elif choice==2:
  display_time()
elif choice==3:
  timer()
elif choice==4: 
  print("Exiting...")
else:
  print("Invalid choice.Please try again")