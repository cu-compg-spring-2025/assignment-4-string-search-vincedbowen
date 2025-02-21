def get_shift_match_table(P):
    m = len(P)
    shift_match_table = {}

    for shift in range(m - 1, 0, -1):
        p_1 = m - 1
        p_2 = m - shift - 1

        while p_2 >= 0:
            if P[p_2] == P[p_1]:
                p_1 -= 1
                p_2 -= 1
                if p_2 < 0:
                    shift_match_table[shift] = m - shift
                    break
            else:
                shift_match_table[shift] = m - shift - p_2 - 1
                break
    shift_match_table[m] = 0
    return shift_match_table

def get_good_suffix_table(P):
    m = len(P)

    good_suffix_table = {}
    good_suffix_table[0] = 1

    shift_match_table = get_shift_match_table(P)

    for i in range(1, m + 1):
        good_suffix_table[i] = i + m

    for i in range(m, 0, -1):
        if shift_match_table[i] > 0:
            good_suffix_table[shift_match_table[i]] = i + shift_match_table[i]

    for i in range(m, 0, -1):
        if shift_match_table[i] + i == m:
            for j in range(shift_match_table[i] + 1, m+1):
                good_suffix_table[j] = min(good_suffix_table[j], j + i)
    # print(good_suffix_table)
    return good_suffix_table

def get_bad_char_table(P):
    bad_char_table = {}
    #####################################################################
    ## ADD CODE HERE
    #####################################################################
    for i in range(len(P)):
        bad_char_table[P[i]] = len(P) - i - 1
    bad_char_table['*'] = len(P)
    return bad_char_table

def boyer_moore_search(T, P):
    occurrences = []
    #####################################################################
    ## ADD CODE HERE
    #####################################################################
    gbt = get_bad_char_table(P)
    gst = get_good_suffix_table(P)

    text_index = len(P) - 1
    while text_index < len(T):
        pattern_index = len(P) - 1
        while pattern_index >= 0:
            if T[text_index] == P[pattern_index]:
                if pattern_index == 0:
                    occurrences.append(text_index)
                    text_index += len(P)
                    break
                pattern_index -= 1
                text_index -= 1
            else:
                if T[text_index] in gbt:
                    gbt_shift = gbt.get(T[text_index])
                else:
                    gbt_shift = gbt.get('*')
                gst_shift = gst.get(len(P) - pattern_index - 1)
                shift = max(gbt_shift, gst_shift)
                text_index += shift
                break
    
    return occurrences

def boyer_moore_search_shifts(T, P):
    num_shifts = 0 
    #####################################################################
    ## ADD CODE HERE
    #####################################################################
    gbt = get_bad_char_table(P)
    gst = get_good_suffix_table(P)

    text_index = len(P) - 1
    while text_index < len(T):
        pattern_index = len(P) - 1
        while pattern_index >= 0:
            if T[text_index] == P[pattern_index]:
                if pattern_index == 0:
                    text_index += len(P)
                    break
                pattern_index -= 1
                text_index -= 1
            else:
                if T[text_index] in gbt:
                    gbt_shift = gbt.get(T[text_index])
                else:
                    gbt_shift = gbt.get('*')
                gst_shift = gst.get(len(P) - pattern_index - 1)
                shift = max(gbt_shift, gst_shift)
                num_shifts += 1
                text_index += shift
                break
    
    return num_shifts
