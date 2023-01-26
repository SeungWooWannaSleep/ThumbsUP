list_one=['bbq','경북대 센트럴파크',3,30]
list_two=['피자 알볼로','경진로10길 21',4,50]
list_three=['맛나감자탕','경북대 쪽문',2,40]
list_four=['와플대학','경북대 북문',3,30]
new_list=[]
new_list_two=[]
new_list_three=[]
new_list_four=[]
count=0

username_one=input("이름을 입력하세요:  ").split()
print("")

while count==0:
    print("1. 새로운 거래 등록   2. 거래 목록 ")
    menu=int(input("원하시는 메뉴를 선택하세요:  "))
    if menu==1:
        storename=input("가게 이름을 입력하세요:  ")
        if storename in list_one:
            print("이미 목록에 있는 가게입니다.")
            print(list_one)
            print("")
            continue
        if storename in list_two:
            print("이미 목록에 있는 가게입니다.")
            print(list_two)
            print("")
            continue
        if storename in list_three:
            print("이미 목록에 있는 가게입니다.")
            print(list_three)
            print("")
            continue
        if storename in list_four:
            print("이미 목록에 있는 가게입니다.")
            print(list_four)
            print("")
            continue
        else:
            location=input("거래 장소를 입력하세요:  ")
            num=int(input("모집인원을 입력하세요:  "))
            time=int(input("유효시간을 입력하세요:   "))
            print("")
            new_list.append(storename)
            new_list.append(location)
            new_list.append(num)
            new_list.append(time)
            print("새로운 거래가 등록되었습니다")
            count=count+1
            print("")
        
        
    else :
        print("")
        print("거래 목록-----------")
        print("")
        print(*list_one)
        print(*list_two)
        print(*list_three)
        print(*list_four)
        print(*new_list)
        print(*new_list_two)
        print(*new_list_three)
        print(*new_list_four)
        print("")
        elsemenu=int(input("원하시는 가게의 순서를 선택하세요: "))
        if elsemenu==1:
            print("")
            print("거래를 진행합니다")
            print("가게 이름:",list_one[0])
            print("거래 장소:",list_one[1])
            print("")
            print("모집 인원수가 ",list_one[2]-1,"로 변경됩니다")
            print("")
            list_one=['bbq','경북대 센트럴파크',list_one[2]-1,30]
        if elsemenu==2:
            print("")
            print("거래를 진행합니다")
            print("가게 이름:",list_two[0])
            print("거래 장소:",list_two[1])
            print("")
            print("모집 인원수가 ",list_two[2]-1,"로 변경됩니다")
            print("")
            list_two=['피자 알볼로','경진로10길 21',list_two[2]-1,50]
        if elsemenu==3:
            print("")
            print("거래를 진행합니다")
            print("가게 이름:",list_three[0])
            print("거래 장소:",list_three[1])
            print("")
            print("모집 인원이 다 모였으므로 결제를 진행합니다")
            print("")
            list_three=[]
        if elsemenu==4:
            print("")
            print("거래를 진행합니다")
            print("가게 이름:",list_four[0])
            print("거래 장소:",list_four[1])
            print("")
            print("모집 인원수가 ",list_four[2]-1,"로 변경됩니다")
            print("")
            list_four=['와플대학','경북대 북문',list_four[2]-1,30]
            
        
    
while count==1:
    print("1. 새로운 거래 등록   2. 거래 목록 ")
    menu=int(input("원하시는 메뉴를 선택하세요:  "))
    if menu==1:
        storename=input("가게 이름을 입력하세요:  ")
        if storename in list_one:
            print("이미 목록에 있는 가게입니다.")
            print(list_one)
            print("")
            continue
        if storename in list_two:
            print("이미 목록에 있는 가게입니다.")
            print(list_two)
            print("")
            continue
        if storename in list_three:
            print("이미 목록에 있는 가게입니다.")
            print(list_three)
            print("")
            continue
        if storename in list_four:
            print("이미 목록에 있는 가게입니다.")
            print(list_four)
            print("")
            continue
        if storename in new_list:
            print("이미 목록에 있는 가게입니다.")
            print(new_list)
            print("")
            continue
            
        else:
            location=input("거래 장소를 입력하세요:  ")
            num=int(input("모집인원을 입력하세요:  "))
            time=int(input("유효시간을 입력하세요:   "))
            print("")
            new_list_two.append(storename)
            new_list_two.append(location)
            new_list_two.append(num)
            new_list_two.append(time)
            print("새로운 거래가 등록되었습니다")
            count=count+1
            print("")
            

        
    else :
        print("")
        print("거래 목록-----------")
        print("")
        print(*list_one)
        print(*list_two)
        print(*list_three)
        print(*list_four)
        print(*new_list)
        print(*new_list_two)
        print(*new_list_three)
        print(*new_list_four)
        elsemenu=int(input("원하시는 가게의 순서를 선택하세요: "))
        if elsemenu==1:
            print("")
            print("거래를 진행합니다")
            print("가게 이름:",list_one[0])
            print("거래 장소:",list_one[1])
            print("")
            print("모집 인원수가 ",list_one[2]-1,"로 변경됩니다")
            print("")
            list_one=['bbq','경북대 센트럴파크',list_one[2]-1,30]
        if elsemenu==2:
            print("")
            print("거래를 진행합니다")
            print("가게 이름:",list_two[0])
            print("거래 장소:",list_two[1])
            print("")
            print("모집 인원수가 ",list_two[2]-1,"로 변경됩니다")
            print("")
            list_two=['피자 알볼로','경진로10길 21',list_two[2]-1,50]
        if elsemenu==3:
            print("")
            print("거래를 진행합니다")
            print("가게 이름:",list_three[0])
            print("거래 장소:",list_three[1])
            print("")
            print("모집 인원이 다 모였으므로 결제를 진행합니다")
            print("")
            list_three=[]
        if elsemenu==4:
            print("")
            print("거래를 진행합니다")
            print("가게 이름:",list_four[0])
            print("거래 장소:",list_four[1])
            print("")
            print("모집 인원수가 ",list_four[2]-1,"로 변경됩니다")
            print("")
            list_four=['와플대학','경북대 북문',list_four[2]-1,30]
        if elsemenu==5:
            print("")
            print("거래를 진행합니다")
            print("가게 이름:",new_list[0])
            print("거래 장소:",new_list[1])
            print("")
            print("모집 인원수가 ",new_list[2]-1,"로 변경됩니다")
            print("")
            new_list[2]=new_list[2]-1
        

while count==2:
    print("1. 새로운 거래 등록   2. 거래 목록 ")
    menu=int(input("원하시는 메뉴를 선택하세요:  "))
    if menu==1:
        storename=input("가게 이름을 입력하세요:  ")
        if storename in list_one:
            print("이미 목록에 있는 가게입니다.")
            print(list_one)
            print("")
            continue
        if storename in list_two:
            print("이미 목록에 있는 가게입니다.")
            print(list_two)
            print("")
            continue
        if storename in list_three:
            print("이미 목록에 있는 가게입니다.")
            print(list_three)
            print("")
            continue
        if storename in list_four:
            print("이미 목록에 있는 가게입니다.")
            print(list_four)
            print("")
            continue
        if storename in new_list:
            print("이미 목록에 있는 가게입니다.")
            print(new_list)
            print("")
            continue
        if storename in new_list_two:
            print("이미 목록에 있는 가게입니다.")
            print(new_list_two)
            print("")
            continue
        else:
            location=input("거래 장소를 입력하세요:  ")
            num=int(input("모집인원을 입력하세요:  "))
            time=int(input("유효시간을 입력하세요:   "))
            print("")
            new_list_three.append(storename)
            new_list_three.append(location)
            new_list_three.append(num)
            new_list_three.append(time)
            print("새로운 거래가 등록되었습니다")
            count=count+1
            print("")

        
    else :
        print("")
        print("거래 목록-----------")
        print("")
        print(*list_one)
        print(*list_two)
        print(*list_three)
        print(*list_four)
        print(*new_list)
        print(*new_list_two)
        print(*new_list_three)
        print(*new_list_four)
        elsemenu=int(input("원하시는 가게의 순서를 선택하세요: "))
        if elsemenu==1:
            print("")
            print("거래를 진행합니다")
            print("가게 이름:",list_one[0])
            print("거래 장소:",list_one[1])
            print("")
            print("모집 인원수가 ",list_one[2]-1,"로 변경됩니다")
            print("")
            list_one=['bbq','경북대 센트럴파크',list_one[2]-1,30]
        if elsemenu==2:
            print("")
            print("거래를 진행합니다")
            print("가게 이름:",list_two[0])
            print("거래 장소:",list_two[1])
            print("")
            print("모집 인원수가 ",list_two[2]-1,"로 변경됩니다")
            print("")
            list_two=['피자 알볼로','경진로10길 21',list_two[2]-1,50]
        if elsemenu==3:
            print("")
            print("거래를 진행합니다")
            print("가게 이름:",list_three[0])
            print("거래 장소:",list_three[1])
            print("")
            print("모집 인원이 다 모였으므로 결제를 진행합니다")
            print("")
            list_three=[]
        if elsemenu==4:
            print("")
            print("거래를 진행합니다")
            print("가게 이름:",list_four[0])
            print("거래 장소:",list_four[1])
            print("")
            print("모집 인원수가 ",list_four[2]-1,"로 변경됩니다")
            print("")
            list_four=['와플대학','경북대 북문',list_four[2]-1,30]
        if elsemenu==5:
            print("")
            print("거래를 진행합니다")
            print("가게 이름:",new_list[0])
            print("거래 장소:",new_list[1])
            print("")
            print("모집 인원수가 ",new_list[2]-1,"로 변경됩니다")
            print("")
            new_list[2]=new_list[2]-1
        if elsemenu==6:
            print("")
            print("거래를 진행합니다")
            print("가게 이름:",new_list_two[0])
            print("거래 장소:",new_list_two[1])
            print("")
            print("모집 인원수가 ",new_list_two[2]-1,"로 변경됩니다")
            print("")
            new_list_two[2]=new_list_two[2]-1

while count==3:
    print("1. 새로운 거래 등록   2. 거래 목록 ")
    menu=int(input("원하시는 메뉴를 선택하세요:  "))
    if menu==1:
        storename=input("가게 이름을 입력하세요:  ")
        if storename in list_one:
            print("이미 목록에 있는 가게입니다.")
            print(list_one)
            print("")
            continue
        if storename in list_two:
            print("이미 목록에 있는 가게입니다.")
            print(list_two)
            print("")
            continue
        if storename in list_three:
            print("이미 목록에 있는 가게입니다.")
            print(list_three)
            print("")
            continue
        if storename in list_four:
            print("이미 목록에 있는 가게입니다.")
            print(list_four)
            print("")
            continue
        if storename in new_list:
            print("이미 목록에 있는 가게입니다.")
            print(new_list)
            print("")
            continue
        if storename in new_list_two:
            print("이미 목록에 있는 가게입니다.")
            print(new_list_two)
            print("")
            continue
        if storename in new_list_three:
            print("이미 목록에 있는 가게입니다.")
            print(new_list_three)
            print("")
            continue
        else:
            location=input("거래 장소를 입력하세요:  ")
            num=int(input("모집인원을 입력하세요:  "))
            time=int(input("유효시간을 입력하세요:   "))
            print("")
            new_list_four.append(storename)
            new_list_four.append(location)
            new_list_four.append(num)
            new_list_four.append(time)
            print("새로운 거래가 등록되었습니다")
            count=count+1
            print("")
  
        
    else :
        print("")
        print("거래 목록-----------")
        print("")
        print(*list_one)
        print(*list_two)
        print(*list_three)
        print(*list_four)
        print(*new_list)
        print(*new_list_two)
        print(*new_list_three)
        print(*new_list_four)
        elsemenu=int(input("원하시는 가게의 순서를 선택하세요: "))
        if elsemenu==1:
            print("")
            print("거래를 진행합니다")
            print("가게 이름:",list_one[0])
            print("거래 장소:",list_one[1])
            print("")
            print("모집 인원수가 ",list_one[2]-1,"로 변경됩니다")
            print("")
            list_one=['bbq','경북대 센트럴파크',list_one[2]-1,30]
        if elsemenu==2:
            print("")
            print("거래를 진행합니다")
            print("가게 이름:",list_two[0])
            print("거래 장소:",list_two[1])
            print("")
            print("모집 인원수가 ",list_two[2]-1,"로 변경됩니다")
            print("")
            list_two=['피자 알볼로','경진로10길 21',list_two[2]-1,50]
        if elsemenu==3:
            print("")
            print("거래를 진행합니다")
            print("가게 이름:",list_three[0])
            print("거래 장소:",list_three[1])
            print("")
            print("모집 인원이 다 모였으므로 결제를 진행합니다")
            print("")
            list_three=[]
        if elsemenu==4:
            print("")
            print("거래를 진행합니다")
            print("가게 이름:",list_four[0])
            print("거래 장소:",list_four[1])
            print("")
            print("모집 인원수가 ",list_four[2]-1,"로 변경됩니다")
            print("")
            list_four=['와플대학','경북대 북문',list_four[2]-1,30]
        if elsemenu==5:
            print("")
            print("거래를 진행합니다")
            print("가게 이름:",new_list[0])
            print("거래 장소:",new_list[1])
            print("")
            print("모집 인원수가 ",new_list[2]-1,"로 변경됩니다")
            print("")
            new_list[2]=new_list[2]-1
        if elsemenu==6:
            print("")
            print("거래를 진행합니다")
            print("가게 이름:",new_list_two[0])
            print("거래 장소:",new_list_two[1])
            print("")
            print("모집 인원수가 ",new_list_two[2]-1,"로 변경됩니다")
            print("")
            new_list_two[2]=new_list_two[2]-1
        if elsemenu==7:
            print("")
            print("거래를 진행합니다")
            print("가게 이름:",new_list_three[0])
            print("거래 장소:",new_list_three[1])
            print("")
            print("모집 인원수가 ",new_list_three[2]-1,"로 변경됩니다")
            print("")
            new_list_three[2]=new_list_three[2]-1


    


