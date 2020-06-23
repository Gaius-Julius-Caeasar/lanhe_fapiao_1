{
    "GlobalVar": [
        {
            "inpar_Order": "",
            "inpar_filetype": "",
            "inpar_helpdesc": "",
            "inpar_init": "",
            "inpar_required": "0",
            "inputpar": "1",
            "vardef": "{'AmountInWords':'佰叁拾圆叁角肆分','NoteDrawer':'谢登梅','SellerAddress':'深州市龙华区庆湾街道庆津大道乌庆旺路文汇处民治商务中心1栋115栋、2、3栋、4幢009栋7553323188', 'CommodityPrice':'[]','CommodityNum':'[]','SellerRegisterNum': '91440300689404127F','SellerBank':'农业银行龙华支行41028900040099987','Remarks':'订单号1047426466044621910支付日期2020-06-07','CommodityTaxRate':'[]','TotalTax':'62.05', 'CheckCode':'17960524178417916383','InvoiceCode': '044031900111','InvoiceDate':'2020年06月11日', 'PurchaserRegisterNum':'91440300MA5EGKDJ92','InvoiceTypeOrg': '深圳增值税电子普通发票','Password':'','PurchaserBank':'', 'AmountInFiguers':'937.34','Checker':'郑晓碧','TotalAmount': '875.29','CommodityAmount':\"[{'row':'1','word':'875.29'}]\", 'PurchaserName':'深圳市蓝禾技术有限公司','CommodityType': '[]','InvoiceType':'电子普通发票','PurchaserAddress':'', 'CommodityTax':\"[{'row':'1','word':'62.05'}]\", 'CommodityUnit':'[]','Payee':'刘笑额','SellerName':'深圳康润华商贸有限公司','CommodityName':\"[{'row':'1','word':'(详见销货清单'}]\",'InvoiceNum':'23838102'}",
            "vardesc": "gv_1",
            "varname": "dict_info",
            "varpasstype": "1",
            "varrobot": "",
            "vartype": "1"
        }
    ],
    "MainSeq": {
        "seq": "Main"
    },
    "OpenFlow": "[\n    {\n        \"seq\": \"Main\"\n    },\n    {\n        \"seq\": \"flow1\"\n    }\n]\n",
    "ProInfo": {
        "ProChange": "2020/06/23 17:18:10",
        "ProCreate": "2020/06/23 14:04:25",
        "ProDesc": "",
        "ProImports": "",
        "ProIsAdminRun": "1",
        "ProName": "lanhe_fapiao",
        "ProStudio": "2020.2.0.20",
        "ProTag": "",
        "ProUserID": "78d4e8e144104176813ebd2975273896",
        "ProVersion": "1.0.0.0"
    },
    "SequenceGroup": [
    ],
    "SequenceList": [
        {
            "group": "",
            "num": "1",
            "sdc": "",
            "seq": "Main",
            "sop": "Close",
            "spy": "Main"
        },
        {
            "group": "",
            "num": "1",
            "sdc": "",
            "seq": "flow1",
            "sop": "Close",
            "spv": [
                {
                    "inpar_Order": "",
                    "inpar_filetype": "",
                    "inpar_helpdesc": "",
                    "inpar_init": "",
                    "inpar_required": "0",
                    "inputpar": "",
                    "vardef": "['电子普通发票','深圳增值税电子普通发票','91440300MA5EGKDJ92', '2020年06月11日','044031900111','23838102', '17960524178417916383','875.29','62.05','937.34',\"[{'row': '1', 'word': '(详见销货清单'}]\"]",
                    "vardesc": "",
                    "varname": "t",
                    "varpasstype": "1",
                    "varrobot": "",
                    "vartype": "1"
                },
                {
                    "inpar_Order": "",
                    "inpar_filetype": "",
                    "inpar_helpdesc": "",
                    "inpar_init": "",
                    "inpar_required": "0",
                    "inputpar": "",
                    "vardef": "[dict_info['InvoiceType'],dict_info['InvoiceTypeOrg'],dict_info['PurchaserRegisterNum'],dict_info[ 'InvoiceDate'],dict_info['InvoiceCode'],dict_info['InvoiceNum'],dict_info['CheckCode'],dict_info['TotalAmount'],dict_info['TotalTax'],dict_info['AmountInFiguers'],dict_info['CommodityName']",
                    "vardesc": "",
                    "varname": "lv_6",
                    "varpasstype": "1",
                    "varrobot": "",
                    "vartype": "1"
                }
            ],
            "spy": "Main"
        }
    ]
}
