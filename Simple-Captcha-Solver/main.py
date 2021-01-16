from PIL import Image
import numpy as np

np.set_printoptions(threshold=np.inf)

nums = list()

def prepareNums():  # 准备好10个数字
    for num in range(10):
        num_img = Image.open("nums/" + str(num) + ".png").convert("1")
        nums.append(num_img)
        # num_img.show()

def compareImgtoNum(img): # img 是验证码抠出来的图，num 是数字的图(都只有1位)
    arrImg = np.asarray(img).flatten()
    # print(arrImg)
    SIZE = arrImg.size
    result = -1
    for num in range(10): # 枚举所有数字
        arrNum = np.asarray(nums[num]).flatten()
        # print(arrImg)
        if(SIZE != arrNum.size):
            ValueError("Num and Captcha size don't equal.")
        flag = 0 # 0 代表没问题
        for i in range(SIZE): # 这个验证码很蠢，只会白变黑，不会黑变白
            if(arrImg[i] > arrNum[i]):
                # print("error:",i,"num:",arrImg[i],arrNum[i])
                flag = 1
                break
        if(flag == 0):
            if(result != -1):
                ValueError("Multi-answers. This shouldn't happen.")
            else:
                result = num
    return result # 没有匹配返回 -1

def getCaptchaNumber(imgFileName): # 返回验证码的字符串
    captchaImg = Image.open(imgFileName).convert("1")
    ans = ""
    for startPos in range(2,15): # 枚举左侧开始位置
        ans = ""
        flag = 0 # flag = 0 代表没问题
        for digit in range(4): # 切开四个数位
            L = startPos + 11 * digit #left
            R = L+11 #right
            U = 1 #up
            D = 19 #down
            digitImg = captchaImg.crop((L,U,R,D))
            # digitImg.show()
            dignum = compareImgtoNum(digitImg)
            if(dignum == -1):
                flag = 1
                break
            else:
                ans = ans + str(dignum)
        if(flag == 0):
            return ans
    return -1


if __name__ == "__main__":
    prepareNums()
    output = open("result.txt","w") # 输出答案
    output.truncate()
    for i in range(1000):
        print("Picture:",i)
        print(getCaptchaNumber("img/" + str(i) + ".jpg"),file = output)
    pass