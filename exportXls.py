import pymysql
import xlwt


def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='developer', passwd='developer', db='test', charset='utf8')
    return conn


def query_all(cur, sql, args):
    cur.execute(sql, args)
    return cur.fetchall()


def read_mysql_to_xlsx(filename):
    list_table_head = ['pid','ID','XK_WSH','XK_XMMC','XK_SPLB','XK_NR','XK_XDR',
    'XK_XDR_SHXYM','XK_XDR_ZDM','XK_XDR_GSDJ','XK_XDR_SWDJ','XK_XDR_SFZ','XK_FR','XK_JDRQ','XK_JZQ','XK_JZQ','XK_YXQ',
    'XK_XZJG','XK_XZBM','XK_ZT','DFBM','SJC','BZ','DATA_TYPE','FINGER_PRINT']	
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
    for i in range(len(list_table_head)):
        sheet.write(0, i, list_table_head[i])

    conn = get_conn()
    cur = conn.cursor()
    sql = "select * from `csv_data` where `XK_XDR_SHXYM` is not null and `XK_XDR_SHXYM` != '空' and `XK_XDR_SHXYM` != '无'"
    results = query_all(cur, sql, None)
    conn.commit()
    cur.close()
    conn.close()
    row = 1
    for result in results:
        col = 0
        print(type(result))
        print(result)
        for item in result:
            print(item)
            sheet.write(row, col, item)
            col += 1
        row += 1
    workbook.save(filename)


if __name__ == '__main__':
    read_mysql_to_xlsx('/Users/wzm/Desktop/result.xlsx')