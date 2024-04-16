# 한글 숫자와 해당하는 아라비아 숫자를 매핑하는 딕셔너리
korean_numbers = {'영': 0, '공': 0, '빵': 0, '일': 1, '하나': 1, '이': 2, '둘': 2, '삼': 3, '셋' : 3, '사': 4, '넷': 4, '오': 5, 
                    '다섯': 5, '육': 6, '여섯': 6, '칠': 7, '일곱': 7, '팔': 8, '여덟': 8, '구': 9, '아홉': 9, '십': 10, '열': 10,
                    '스물': 20, '서른': 30, '마흔': 40, '쉰': 50, '예순': 60, '일흔': 70, '여든': 80, '아흔': 90, 
                    '백': 100, '천': 1000, '만': 10000, '억': 100000000, 
                    '조': 1000000000000}


# 한글 숫자를 실제 숫자로 바꾸는 메서드
def korean_to_number(korean):
    
    result = 0
    last_word = None
    no_word = False
    continue_flag = True
    basic_num = 1
    partial_num = 0
    temp_num = 0
    last_num = 0
    multi_result = []
    is_basic = False

    for i, word in enumerate(korean):
        if word == '일' and len(korean) > i+1 and str(word + korean[i+1]) in korean_numbers:
            last_word = word
            no_word = True
            continue_flag = False
        
        elif word not in korean_numbers:
            if no_word:
                word = last_word + word
                no_word = False
                continue_flag = True
            else:
                last_word = word
                no_word = True
                continue_flag = False

        if continue_flag:
            if word in korean_numbers:
                num = korean_numbers[word]
            else:
                return korean
        
            if num < 10:
                if is_basic:
                    if result:
                        if last_num < 10:
                            result += last_num
                        multi_result.append(result)
                        result = 0
                    else:
                        if last_num < 10:
                            temp_num += last_num
                        multi_result.append(temp_num)
                        temp_num = 0
                    
                basic_num = num
                is_basic = True


            else: # 단위 처리
                is_basic = False
                unit_num = num
                # 만, 억, 조 단위 나오면 temp_num 처리
                if unit_num >= 10000:
                    if last_num < 10:
                        temp_num += last_num
                    if temp_num == 0:
                        temp_num = 1
                    
                    if len(str(result)) > len(str(unit_num)) or result == 0:
                        result += temp_num * unit_num
                        
                    else:
                        if last_num < 10:
                            result += last_num
                        multi_result.append(result)
                        result = temp_num * unit_num

                    basic_num = 1
                    temp_num = 0

                else:
                    partial_num = basic_num * unit_num
                    if len(str(temp_num)) > len(str(partial_num)) or temp_num == 0:
                        temp_num += partial_num
                    else:
                        if last_num < 10:
                            temp_num += last_num
                        multi_result.append(temp_num)
                        partial_num = unit_num
                        temp_num = partial_num
                        basic_num = 1
                        last_num = 0
                        continue
                    
                    basic_num = 1
                    
            last_num = num

    result += temp_num
    if last_num < 10:
        result += last_num

    if multi_result:
        multi_result.append(result)
        multi_result_str = ''
        for i in multi_result:
            res = (format (i, ',d'))
            multi_result_str += res + ' '
        return multi_result_str[:-1]

    res = (format (result, ',d')) 
    return str(res)

if __name__ == "__main__":
    korean_number = "백십백십일백십이백십삼"
    number = korean_to_number(korean_number)
    print(number)
