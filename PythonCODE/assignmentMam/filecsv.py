import csv

# with open('act.csv','w',newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["sn","image","resolution"])
#     writer.writerow([1,"tenet","720x1080"])
#     writer.writerow([2,"inception","720x1080"])
#     writer.writerow([3,"RRR","1260x760"])

##

# with open('C:\\Users\\purushottam.kumar\\PycharmProjects\\pythonProject\\PythonCODE\\csvFile\\act.csv',) as csvfile:
#     data = csv.reader(csvfile,delimiter=' ')
#     for row in data:
#         print(' '.join(row))


# Inheritance program

class Employee:

    def eDetails(self):
        with open('acti.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["sn", "Image", "resolution"])
            writer.writerow([1, "tenet", "720x1527"])
            writer.writerow([2, "inception", "1080x720"])
            writer.writerow([3, "RRR", "720x1080"])


class Department(Employee):

     def dDetails(self):

         super()

         with open('C:\\Users\\purushottam.kumar\\PycharmProjects\\pythonProject\\PythonCODE\\csvFile\\action.csv', ) as csvfile:
             data = csv.reader(csvfile, delimiter=' ')
             for row in data:
                 print(' '.join(row))

obj = Department()

obj.dDetails()





