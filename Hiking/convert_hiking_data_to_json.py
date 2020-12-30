import json

def main():
    distance_data = {}

    input_file = open("hiking_data.csv", "r")
    for line in input_file:

        # Skip first line with column headers in CSV file:
        if line.startswith("year;"):
            continue
        
        columns = line.strip("\n").split(";")

        # Distance data (later stacked per month, so we use a dictionary
        # where the key is something like "2020-12" and the value
        # is a list of all tour distances from this month
        key = columns[0] + "-" + columns[1]   # e.g. key = "2020-12"
        if key in distance_data.keys():
            distance_data[key].append(columns[3])
        else:
            distance_data[key]= [columns[3]]  

    # Now bring the distance dictionary into a format that is understandable
    # by Chart.js:
    # * Because we want to have a stacked bar chart, we have to put everything
    #   into datasets. The first tour of each month is put into dataset #1, the
    #   second tour of each month comes into dataset #2, and so on. If a month
    #   hasn't any more tours left for the current dataset, then we just add a
    #   tour with 0 km.
    # * Each dataset gets its own color, which gets gradually more yellow.
    # * The input data uses "," as decimal separator, javascript expects ".",
    #   so this is converted here as well.
    # * At the end, datasets contains all datasets that are later stacked
    #   together by Chart.js.
    datasets = []
    dataset_counter = 0
    color = 0
    while len(distance_data) > 0:
        dataset = {}
        dataset_counter += 1
        dataset["label"] = "Tour " + str(dataset_counter)
        dataset["stack"] = "Stack 0"
        color += 20
        dataset["backgroundColor"] = "rgba(255, " + str(color) + ", 0, 0.6)"
        dataset["borderColor"] = "rgba(255, " + str(color) + ", 0, 1)"
        dataset["borderWidth"] = 1

        data = []
        for year in range(2018, 2021):
            for month in range(1, 13):
                key = str(year) + "-" + str(month)
                if key in distance_data.keys():
                    data.append(distance_data[key].pop().replace(",", "."))
                    if len(distance_data[key]) == 0:
                        distance_data.pop(key)
                else:
                    data.append("0")
                    
        dataset["data"] = data
        datasets.append(dataset)

    # All the distance datasets from above are now combined with the labels
    # (which represent the single months) into the bar chart data for the
    # tour distances. The data is then stored as a JSON file.
    bar_chart_distance_data = {}
    bar_chart_distance_data["datasets"] = datasets
    bar_chart_distance_data["labels"] = []
    for year in range(2018, 2021):
            for month in range(1, 13):
                bar_chart_distance_data["labels"].append(str(year) + "-" + str(month))

    json_data = json.dumps(bar_chart_distance_data)

    output_file = open("hiking_data_distance.json", "w")
    output_file.write(json_data)
    output_file.close()
        
        

if __name__ == "__main__":
    main()
