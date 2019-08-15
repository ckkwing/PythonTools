import xlrd
import datetime
import time


def t2s(t):
    h, m, s = t.strip().split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)


def str2second(param_str_time):
    x = time.strptime(param_str_time.split('.')[0], '%H:%M:%S')
    total_seconds = datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()
    str_millisecond = param_str_time.split('.')[1]
    if str_millisecond:
        str_millisecond = "0.{}".format(str_millisecond)
        total_seconds += float(str_millisecond)
    return total_seconds


def filterOneDriveApiRequest(param_table, param_host, param_url_start):
    # support_method_list = ["POST", "PUT"]
    cost_total_milliseconds = 0
    columes_in_header = param_table.row_values(0)
    index_colume_host = -1
    index_colume_url = -1
    index_colume_timetaken = -1
    index_colume_method = -1;
    for i in range(len(columes_in_header)):
        key = columes_in_header[i]
        # print(key)
        if key.lower() == "host":
            index_colume_host = i
        elif key.lower() == "url":
            index_colume_url = i
        elif key.lower() == "time taken":
            index_colume_timetaken = i
        elif key.lower() == "method":
            index_colume_method = i

    nrows = param_table.nrows

    for rownum in range(1, nrows):
        row = param_table.row_values(rownum)
        if row:
            host = row[index_colume_host]
            if host != param_host:
                continue
            url = row[index_colume_url]
            if param_url_start:
                if not url.startswith(param_url_start):
                    continue
            # if url.startswith("/v1.0/drive/root/view.delta?"):
            #     continue
            method = row[index_colume_method]
            # if method not in support_method_list:
            #     continue
            time_taken = row[index_colume_timetaken]
            # print("host: {0}, url: {1}, time taken: {2}".format(host, url, str2second(time_taken)))
            if time_taken:
                cost_total_milliseconds += float(time_taken)

    return cost_total_milliseconds


input_str = input("Excel path is: ")
path = input_str.strip()
excel_file = xlrd.open_workbook(path)


table_web = excel_file.sheet_by_name("Web")
cost_milliseconds_1 = filterOneDriveApiRequest(table_web, "api.onedrive.com", "")
print("Total milliseconds cost when upload in Web client is: {}".format(cost_milliseconds_1))

table_drivespan = excel_file.sheet_by_name("DriveSpan-PC")
cost_milliseconds_2 = filterOneDriveApiRequest(table_drivespan, "graph.microsoft.com", "/v1.0/me/drive")
print("Total milliseconds cost when upload in DriveSpan client is: {}".format(cost_milliseconds_2))
