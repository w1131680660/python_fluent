
import pandas as pd
import  pymysql
def connect_mysql_operate(sql_text, dbs='operation', type='dict'):
    # conn = pymysql.Connect(host='106.52.43.196', port=3306, user='beyoungsql', passwd='Hp19921026.', db=dbs)
    # conn = pymysql.Connect(host='172.16.0.6', port=3306, user='beyoungsql', passwd='By1590123!@', db=dbs)
    conn = pymysql.Connect(host='gz-cdb-lwqgjirt.sql.tencentcdb.com', port=59656, user='beyoungsql', passwd='Bymy2021_', db=dbs)
    if type == 'tuple':
        cursor = conn.cursor()
    else:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql_text)
    response = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return response
# 供应链的
def connect_mysql_financial(sql_text, dbs='financial', type='dict'):
    # conn = pymysql.Connect(host='172.16.0.6', port=3306, user='beyoungsql', passwd='By1590123!@', db=dbs)
    conn = pymysql.Connect(host='gz-cdb-lwqgjirt.sql.tencentcdb.com', port=59656, user='beyoungsql', passwd='Bymy2021_', db=dbs)
    #                        passwd='By1590123!@', db=dbs)
    if type == 'tuple':
        cursor = conn.cursor()
    else:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql_text)
    response = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return response

def test():
    import os

    path =  os.path.join(os.getcwd(),'place_order/','T1000-订单数据.xlsx')

    data_pd = pd.read_excel(path, skiprows=3,keep_default_na=False )

    re_list = []
    error_list = []
    for index, data in data_pd.iterrows():
        data_dict = {}

        # print(data['sku'],data['货名'],data['规格说明'], data['下单数量'])
        # sql = " SELECT product_code,commodity_name FROM commodity_information  where sku ='%s'" % (data['sku'])
        if data['sku'] and data['数量']:
            sql = "select ci.product_code, product_name,product_package_size from commodity_information ci join " \
                  "     product_message pm on ci.product_code=pm.product_code where sku='%s' " % (data['sku'])
            print(sql)
            re_data = connect_mysql_operate(sql, type='dict')
            # print(re_list)
            print(123123, re_data)
            re_name = re_data[0].get('product_code') if re_data else ''
            commodity_name = re_data[0].get('product_name') if re_data else ''

            if data['sku'] == '总计':
                print('这里是11111111111111111', print(data['数量']))
                pass
            else:
                print(data['数量'], commodity_name, re_name)

                if not commodity_name:
                    data_dict['sku'] = data['sku']
                    data_dict['num'] = data['数量']
                    error_list.append(data_dict)
                else:
                    data_dict['sku'] = data['sku']
                    data_dict['commodity_name'] = commodity_name
                    data_dict['num'] = data['数量']
                    data_dict['product_code'] = re_name
                    re_list.append(data_dict)

def return_order():
    import os

    path = os.path.join(os.getcwd(),  'return_file/胤佑日本.txt.')

    data_pd = pd.read_table(path, keep_default_na=False,encoding='GBk')
    # data_pd.to_csv('胤佑日本.csv', encoding="utf_8_sig")
    site = '胤佑'
    country = '日本'
    for index, i in data_pd.iterrows():
        date = i[0]
        date = date.replace('T',' ').split('+')[0]
        order_id = i[1]
        sku = i[2]
        asin = i[3]
        fnsku = i[4]
        quantity = i[6]
        return_reason = i[-3]
        customer_comments = i[-1]
        print(date, order_id ,sku ,quantity,asin ,fnsku ,return_reason ,customer_comments)
        judge_sql = " SELECT * FROM sales_return_report WHERE order_id = '{0}'".format(order_id)
        prduct_name_sql = "SELECT pr.product_name FROM commodity_information AS co ,product_message as" \
                     "  pr WHERE co.product_code = pr.product_code AND co.sku='{0}' ".format(sku)
        prduct_name = connect_mysql_operate(prduct_name_sql, type='dict')
        if prduct_name:
            prduct_name = prduct_name[0].get('product_name')
        else:prduct_name =''
        re_judge_data = connect_mysql_financial(judge_sql, type='dict')
        if not re_judge_data:
            insert_sql = " INSERT INTO sales_return_report ( station,country,order_id,sku, " \
                         " asin ,fnsku , product_name,quantity,return_dates ) VALUES \
                          ('{0}' , '{1}' ,'{2}' ,'{3}' ,'{4}' ,'{5}' ,'{6}', '{7}','{8}')"\
                      .format(site, country, order_id, sku, asin ,fnsku, prduct_name, quantity,date)
            print(insert_sql)
            connect_mysql_financial(insert_sql)
        else:
            update_sql = " UPDATE sales_return_report SET station = '{0}',country ='{1}'," \
                         " order_id ='{2}',sku ='{3}',asin ='{4}' , fnsku ='{5}' ," \
                         "   product_name ='{6}' ,quantity ='{7}' , return_dates ='{8}' WHERE " \
                         " order_id ='{2}'  ".format(site, country, order_id, sku, asin ,fnsku, prduct_name, quantity,date)
            connect_mysql_financial(update_sql)
return_order()