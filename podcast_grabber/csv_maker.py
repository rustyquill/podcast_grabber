import csv
import random
import os




def dict_2D(a_dict,heading_key, filename='~/Documents/report.csv'):
    filename = os.path.expanduser(filename)
    with open(filename, 'w', newline='') as csvfile:
       headings = [' '] 
       [headings.append(_) for _ in a_dict[heading_key] ]
       writer = csv.writer(csvfile)
       writer.writerow(headings)
       headings.pop(0)
       for each_item in a_dict:
          row = [each_item]
          print(headings)
          for key in headings:
             print(key)
             print(a_dict)
             row.append(a_dict[each_item].get(key))
          writer.writerow(row)


if __name__ == "__main__":
   dict_2D({"tma": {"pod":"url", "other":"other_url"},"rqg": {"pod":"url", "other":"other_url"}},"tma")
