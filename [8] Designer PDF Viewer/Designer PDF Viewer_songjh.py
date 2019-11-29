import os

def designerPdfViewer(h, word):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # a부터 z까지 저장된 리스트
    word_list = list(word) # 문자열을 리스트로 변환
    num_list = [] # word의 각 알파벳을 위의 alpha 리스트에서의 인덱스 번호로 저장하는 리스트
    word_h = [] # h 중에 문지열 word의 대한 길이만을 모은 list

    for i in alphabet:
        for j in word_list:
            if i == j:
                number = alphabet.index(j)
                num_list.append(number)            
    # 이 과정을 거치면 num_list에는 word의 단어들이 alpha의 인덱스로 저장되어 있다.
    
    for x in num_list: # alpha 리스트와 h 리스트의 인덱스가 서로 같으므로
        word_h.append(h[x]) 

    res = len(word_list) * max(word_h) # 가로 * 세로

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split())) # a~z 알파벳에 주어진 길이 리스트

    word = input() # 문자열

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
