# import csv
# import sqlite3
#
# db = sqlite3.connect("Baza.db")
#
# cursor = db.cursor()
#
# cursor.execute(f"SELECT * FROM admins ")
#
# res = cursor.fetchall()
#
# file = open("admins.csv", "w", newline="")
# # test = [["ndjmkmd", "bxnnxjz","sbhjdnzljx"],
# #         ["ssjskksj","jzjxhxhz", "zjsjhxhhs"]]\
# test = []
# for i in res:
#     ar = [str(i[0])+" ", i[1] + " ", i[2] + " "]
#     test.append(ar)
# print(test)
# with file:
#     write = csv.writer(file, delimiter=";")
#     write.writerows(test)



