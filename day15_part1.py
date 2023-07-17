import time as tm
import matplotlib.pyplot as plt

times = []
mistakes = 0
print("This Program will help you type faster. You will have to type the word 'programming' as fast as you can for five times. ")
input("Press enter to continue.")

while len(times) < 5:
    start = tm.time()
    word = input("Type the word: ")
    end = tm.time()
    time_elapsed = end - start

    times.append(time_elapsed)

    if (word.lower() != 'programming'):
        mistakes += 1

print("You made " + str(mistakes) + " mistake(s).")
print("Now let's see your evolution.")
print(time_elapsed)
tm.sleep(5)

x = [1, 2, 3, 4, 5]
y = times
plt.plot(x, y)

legend = ["1", "2", "3", "4", "5"]
plt.xticks(x, legend)
plt.ylabel("Time in Seconds")
plt.xlabel("Attempts")
plt.title("Your Typing Evolution")
plt.show()
