import random

import xlwt  # 导入模块


def header(sheet):
    """
    生成表头
    :param sheet: 工作表
    :return: sheet
    """
    # 是否为敏感籍贯（1不是/2是）,
    # 是否敏感行政区（1不是/2是）,
    # 经营业态（1高/2中/3低）,
    # 是否有降级降档（1不是/2是）,
    # 近半年内是否有违法记录（1不是/2是）,
    # 历史违法总次数（全1）,
    # 近两年内违法次数（全1）,
    # 中华周进货增长率（0.6~1.4）,
    # 利群周进货增长率（0.6~1.4）,
    # 与同区同期同定量类别零售户平均存销比比值（0.3~1.5）,
    # 周卷烟终端销售量增长率（0.5~1.8）,
    # 敏感时间（1不/2一般/3特别）全1,
    # 结果（1不违法/2违法）全1
    sheet.write(0, 0, '是否为敏感籍贯（1不是/2是）')
    sheet.write(0, 1, '是否敏感行政区（1不是/2是）')
    sheet.write(0, 2, '经营业态（1高/2中/3低）')
    sheet.write(0, 3, '是否有降级降档（1不是/2是）')
    sheet.write(0, 4, '近半年内是否有违法记录（1不是/2是）')
    sheet.write(0, 5, '历史违法总次数')
    sheet.write(0, 6, '近两年内违法次数')
    sheet.write(0, 7, '中华周进货增长率（0.6~1.4）')
    sheet.write(0, 8, '利群周进货增长率（0.6~1.4）')
    sheet.write(0, 9, '与同区同期同定量类别零售户平均存销比比值（0.3~1.5）')
    sheet.write(0, 10, '周卷烟终端销售量增长率（0.5~1.8）')
    sheet.write(0, 11, '敏感时间（1不/2一般/3特别）')
    sheet.write(0, 12, '结果（1不是/2是）')
    return sheet


def generate_normal(sheet, i):
    """
    在第i行生成不违法数据
    :param sheet:工作表
    :param i:第i行
    :return:sheet
    """
    random.choice([1, 2, 3])

    # 随机的1， 2 按70%，30%开的概率
    r1 = random.randint(1, 100)  # 生成1， 100随机数
    if r1 <= 70:
        yes_no = 1
    else:
        yes_no = 2

    # 随机的1，2 ，3 按60%，20%， 20%的概率
    r2 = random.randint(1, 100)
    if r2 <= 60:
        level = 1
    elif 60 < r2 <= 80:
        level = 2
    else:
        level = 3

    # 历史违法数据
    history = 0
    two_year = 0

    # 半年内有没有违法 20%概率
    r3 = random.randint(1, 100)  # 生成1， 100随机数
    if r3 <= 80:
        half_year = 1
    else:
        half_year = 2

    # 如果生成的半年内违法了, 两年内和历史肯定也违法了至少1次
    if half_year == 2:
        two_year += 1
        history += 1
    print(half_year, two_year, history)

    # 历史违法次数加0-2
    r4 = random.randint(0, 1)
    history += r4

    rate1 = random.randrange(start=6, stop=14, step=1) * 0.05  # 生成6-14随机数，再乘0.05
    rate2 = random.randrange(3, 15) * 0.05
    rate3 = random.randrange(5, 18) * 0.05

    sheet.write(i, 0, yes_no)  # '是否为敏感籍贯（1不是/2是）')
    sheet.write(i, 1, yes_no)  # '是否敏感行政区（1不是/2是）')
    sheet.write(i, 2, level)  # '经营业态（1高/2中/3低）')
    sheet.write(i, 3, yes_no)  # '是否有降级降档（1不是/2是）')
    sheet.write(i, 4, yes_no)  # '近半年内是否有违法记录（1不是/2是）')
    sheet.write(i, 5, history)  # '历史违法总次数')
    sheet.write(i, 6, two_year)  # '近两年内违法次数')
    sheet.write(i, 7, rate1)  # '中华周进货增长率（0.6~1.4）')
    sheet.write(i, 8, rate1)  # '利群周进货增长率（0.6~1.4）')
    sheet.write(i, 9, rate2)  # '与同区同期同定量类别零售户平均存销比比值（0.3~1.5）')
    sheet.write(i, 10, rate3)  # '周卷烟终端销售量增长率（0.5~1.8）')
    sheet.write(i, 11, level)  # '敏感时间（1不/2一般/3特别）')
    # sheet.write(i, 12, yes_no)  # '结果（1不是/2是）')
    return sheet


def generate_illegal(sheet, i):
    """
    在第i行生成违法数据
    :param sheet:工作表
    :param i:第i行
    :return:sheet
    """
    random.choice([1, 2, 3])

    # 随机的1， 2 按50%，50%开的概率
    r1 = random.randint(1, 100)  # 生成1， 100随机数
    if r1 <= 50:
        yes_no = 1
    else:
        yes_no = 2

    # 随机的1，2 ，3 按40%，30%， 30%的概率
    r2 = random.randint(1, 100)
    if r2 <= 40:
        level = 1
    elif 40 < r2 <= 70:
        level = 2
    else:
        level = 3

    # 历史违法数据
    history = 0
    two_year = 0

    # 半年内有没有违法 60%概率
    r3 = random.randint(1, 100)  # 生成1， 100随机数
    if r3 <= 60:
        half_year = 1
    else:
        half_year = 2

    # 如果生成的半年内违法了, 两年内和历史肯定也违法了至少1次
    if half_year == 2:
        two_year += 1
        history += 1
    print(half_year, two_year, history)

    # 历史违法次数加0-2
    r4 = random.randint(0, 2)
    history += r4

    rate1 = random.randrange(start=6, stop=14, step=1) * 0.1  # 生成6-14随机数，再乘0.1
    rate2 = random.randrange(3, 15) * 0.1
    rate3 = random.randrange(5, 18) * 0.1

    sheet.write(i, 0, yes_no)  # '是否为敏感籍贯（1不是/2是）')
    sheet.write(i, 1, yes_no)  # '是否敏感行政区（1不是/2是）')
    sheet.write(i, 2, level)  # '经营业态（1高/2中/3低）')
    sheet.write(i, 3, yes_no)  # '是否有降级降档（1不是/2是）')
    sheet.write(i, 4, yes_no)  # '近半年内是否有违法记录（1不是/2是）')
    sheet.write(i, 5, history)  # '历史违法总次数')
    sheet.write(i, 6, two_year)  # '近两年内违法次数')
    sheet.write(i, 7, rate1)  # '中华周进货增长率（0.6~1.4）')
    sheet.write(i, 8, rate1)  # '利群周进货增长率（0.6~1.4）')
    sheet.write(i, 9, rate2)  # '与同区同期同定量类别零售户平均存销比比值（0.3~1.5）')
    sheet.write(i, 10, rate3)  # '周卷烟终端销售量增长率（0.5~1.8）')
    sheet.write(i, 11, level)  # '敏感时间（1不/2一般/3特别）')
    # sheet.write(i, 12, yes_no)  # '结果（1不是/2是）')
    return sheet


if __name__ == '__main__':
    # 不违法数据
    workbook = xlwt.Workbook(encoding='utf-8')  # 创建workbook 对象,
    worksheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)  # 创建工作表sheet1, 允许覆盖=True

    worksheet1 = header(worksheet1)
    for i in range(1, 7501):
        worksheet1 = generate_normal(worksheet1, i)

    workbook.save('./demo_data_legal.xls')  # 保存表为students.xls

    # 违法数据
    workbook = xlwt.Workbook(encoding='utf-8')  # 创建workbook 对象,
    worksheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)  # 创建工作表sheet1, 允许覆盖=True

    worksheet1 = header(worksheet1)
    for i in range(1, 2501):
        worksheet1 = generate_illegal(worksheet1, i)

    workbook.save('./demo_data_illegal.xls')  # 保存表为students.xls
