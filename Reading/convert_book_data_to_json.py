import json

def main():
    non_fiction_books_data = {}
    fiction_books_data = {}

    input_file = open("book_data.csv", "r")
    for line in input_file:

        # Skip first line with column headers in CSV file:
        if line.startswith("year;"):
            continue
        
        columns = line.strip("\n").split(";")

        # The two book types (non-fiction and fiction) are later stacked
        # per month, so we use two dictionaries where the key is something like
        # "2020-12" and the value is the number of books read in this month: 
        key = columns[0] + "-" + columns[1]   # e.g. key = "2020-12"

        non_fiction_books_data[key] = columns[2]
        fiction_books_data[key] = columns[3]
         

    # Now bring the distance dictionary into a format that is understandable
    # by Chart.js:
    # * Because we want to have a stacked bar chart, we have to put everything
    #   into datasets. The first dataset contains the non-fictional books, the
    #   second dataset contains the fictional books
    # * At the end, datasets contains all datasets that are later stacked
    #   together by Chart.js.
    datasets = []
    
    dataset = {}
    dataset["label"] = "Non-Fiction"
    dataset["stack"] = "Stack 0"
    dataset["backgroundColor"] = "rgba(255, 0, 0, 0.6)"
    dataset["borderColor"] = "rgba(255, 0, 0, 1)"
    dataset["borderWidth"] = 1

    data = []
    for year in range(2018, 2021):
        for month in range(1, 13):
            key = str(year) + "-" + str(month)
            data.append(non_fiction_books_data[key])
                        
    dataset["data"] = data
    datasets.append(dataset)

    dataset = {}
    dataset["label"] = "Fiction"
    dataset["stack"] = "Stack 0"
    dataset["backgroundColor"] = "rgba(0, 0, 255, 0.6)"
    dataset["borderColor"] = "rgba(0, 0, 255, 1)"
    dataset["borderWidth"] = 1

    data = []
    for year in range(2018, 2021):
        for month in range(1, 13):
            key = str(year) + "-" + str(month)
            data.append(fiction_books_data[key])
                        
    dataset["data"] = data
    datasets.append(dataset)

    # All the distance datasets from above are now combined with the labels
    # (which represent the single months) into the bar chart data for the
    # tour distances. The data is then stored as a JSON file.
    bar_chart_book_data = {}
    bar_chart_book_data["datasets"] = datasets
    bar_chart_book_data["labels"] = []
    for year in range(2018, 2021):
        for month in range(1, 13):
            bar_chart_book_data["labels"].append(str(year) + "-" + str(month))

    json_data = json.dumps(bar_chart_book_data)

    output_file = open("book_data.json", "w")
    output_file.write(json_data)
    output_file.close()
        
        

if __name__ == "__main__":
    main()
