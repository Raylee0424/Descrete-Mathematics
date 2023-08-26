from matplotlib_venn import venn3
import matplotlib.pyplot as plt

# Sizes of sets and intersections
sizeNewsweek = 65
sizeTime = 45
sizeFortune = 42
sizeNewsweekTime = 20
sizeNewsweekFortune = 25
sizeTimeFortune = 15
sizeAll = 8

venn = venn3(subsets=(sizeNewsweek - sizeNewsweekTime - sizeNewsweekFortune + sizeAll,
                      sizeTime - sizeNewsweekTime - sizeTimeFortune + sizeAll,
                      sizeNewsweekTime - sizeAll,
                      sizeFortune - sizeNewsweekFortune - sizeTimeFortune + sizeAll,
                      sizeTimeFortune - sizeAll,
                      sizeNewsweekFortune - sizeAll,
                      sizeAll),
             set_labels=('Newsweek', 'Time', 'Fortune'))

plt.title("Venn Diagram of Magazine Readers")
plt.show()

readNewsweekOnly = sizeNewsweek - sizeNewsweekTime - sizeNewsweekFortune + sizeAll
readTimeOnly = sizeTime - sizeNewsweekTime - sizeTimeFortune + sizeAll
readFortuneOnly = sizeFortune - sizeNewsweekFortune - sizeTimeFortune + sizeAll
readAllThree = sizeAll
totalPeople = 120

print(f"Number of people who read only Newsweek: {readNewsweekOnly}")
print(f"Number of people who read only Time: {readTimeOnly}")
print(f"Number of people who read only Fortune: {readFortuneOnly}")
print(f"Number of people who read all three magazines: {readAllThree}")