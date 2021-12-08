# Generate sql file according to the value in Book1.xlsx
# Output example:
# INSERT INTO app.user (USER_ID, CLIENT_SRF, WL_ID, WL_NAME, WL_EFFECTIVE_DATE, CREATED_BY) VALUES
# ('4519000100020003', '123456789', 2, 'flyaway', '2021-12-07 05:00:00', 'flayaway'),
# ('4519000100020004', '123456780', 2, 'flyaway', '2021-12-07 05:00:00', 'flayaway');

# hint: use panadas to read_excel file
import pandas
import datetime
input = pandas.read_excel('/Users/Xuan/Desktop/Book1.xlsx',sheet_name=0)
input.Client_No
input.Srf_Number
# with open('/Users/Xuan/Desktop/myfile.sql', 'w') as f:
#     f.write("%s\n" % ("INSERT INTO app.user (USER_ID, CLIENT_SRF, WL_ID, WL_NAME, WL_EFFECTIVE_DATE, CREATED_BY) VALUES"))
#     for i in range(len(input.Client_No)):
#         if i < len(input.Client_No) - 1:
#             f.write("%s\n" % ("(\'" + str(input.Client_No[i])+ "\', \'" + str(input.Srf_Number[i])+ "\', 2, \'flyaway\', \'"+ str(datetime.datetime.now()) +"\', \'flayaway\'),"))
#         else:
#             f.write("%s\n" % ("(\'" + str(input.Client_No[i])+ "\', \'" + str(input.Srf_Number[i])+ "\', 2, \'flyaway\', \'"+ str(datetime.datetime.now()) +"\', \'flayaway\');"))


with open('/Users/Xuan/Desktop/myfile.sql', 'w') as f:
    f.write("%s\n" % ("INSERT INTO app.user (USER_ID, CLIENT_SRF, WL_ID, WL_NAME, WL_EFFECTIVE_DATE, CREATED_BY) VALUES"))
    for i in range(len(input)):
        line = "(\'" + str(input["Client_No"][i])+ "\', \'" + str(input["Srf_Number"][i])+ "\', 2, \'flyaway\', \'"+ str(datetime.datetime.now()) +"\', \'flayaway\')"
        f.write(line)
        if i < len(input) - 1:
            f.write(',\n')
        else:
            f.write(';\n')