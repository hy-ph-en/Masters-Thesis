/bin/bash

# Initialize counter
counter=1

# Loop to run the Python script with an incrementing counter up to 3
while [ $counter -le 41 ]; do
  # Run the Python script with the current counter as an argument
  python "./Inital Run.py" ${counter}
 
  # Increment the counter
  ((counter++))
 
  # Sleep for 1 second
  sleep 1
done
