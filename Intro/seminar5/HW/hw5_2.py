# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE
#
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_decode_words.txt'
#
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
#
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
#
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

def RLECompressString(src_txt: str):
    # сжатие текста по алгоритму RLE
    res_txt = ''
    cur_ch = ''
    cur_cnt = 0
    for ch in src_txt:
        if cur_ch != ch:
            if cur_cnt > 0:
                res_txt += str(cur_cnt) + cur_ch
            cur_cnt = 1
            cur_ch = ch
        else:
            cur_cnt += 1
    # добавляем количество последнего символа
    res_txt += str(cur_cnt) + cur_ch
    return res_txt


def RLEDecompressString(src_txt: str):
    # восстановление текста по алгоритму RLE
    res_txt = ''
    cur_numb_text = ''
    for ch in src_txt:
        if ch.isdigit():
            cur_numb_text += ch
        if ch.isalpha():
            res_txt += int(cur_numb_text) * ch
            cur_numb_text = ''
    return res_txt


from os.path import exists
from datetime import datetime

txt_file_1 = 'text_words.txt'
txt_file_2 = 'text_code_words.txt'
txt_file_3 = 'text_decode_words.txt'

# проверка наличия файлов
if not exists(txt_file_1):
    print(f'Файл "{txt_file_1}" не найден!')
elif not exists(txt_file_2):
    print(f'Файл "{txt_file_2}" не найден!')
elif not exists(txt_file_3):
    print(f'Файл "{txt_file_3}" не найден!')
else:
    f2 = open(txt_file_2, 'w', encoding='utf8')
    f3 = open(txt_file_3, 'w', encoding='utf8')

    # открываем исходный файл
    with open(txt_file_1, 'r', encoding='utf8') as f1:
        for cur_line in f1:
            #удаляем символ перевода в конце строк
            cur_line = cur_line.strip()
            print(cur_line)

            code_txt = RLECompressString(cur_line)
            f2.write(code_txt + '\n')

            decode_txt = RLEDecompressString(code_txt)
            f3.write(decode_txt + '\n')


    # дату время выполнения программы записываем, чтоб быть уверенными,
    # что данные в файле обновляются
    f2.write('Выполнено: ' + str(datetime.now()))
    f3.write('Выполнено: ' + str(datetime.now()))
    f2.close()
    f3.close()

    print('Программа выполнена успешно. Проверьте также запись в файлы')
