eng=int(input())
tel=int(input())
hindi=int(input())
maths=int(input())
sci=int(input())
soc=int(input())
if eng>=35:
 if eng>=75:
        print("english:",eng,"100\t", "p\t","A+")
 elif eng>=65:
        print("english:",eng,"100\t",  "p\t","A")
 elif eng>=55:
        print("english:",eng,"100\t",  "p\t","B")
 elif eng>=35:
        print("english:",eng,"100\t",   "p\t","C")
else:
    print("english:",eng ,"100\t",   "f\t","f")
if tel>=35:
 if tel>=75:
        print("telugu:",tel ,"100", "p\t","/A+")
 elif tel>=65:
        print("telugu:",tel ,"100\t",  "p\t","/A")
 elif tel>=55:
        print("telugu:",tel ,"100\t",  "p\t","/B")
 elif tel>=45:
        print("telugu:",tel ,"100\t",   "p\t","C")
else:
     print("telugu:",tel  ,"100\t",   "f\t","f")
if hindi>=35:
 if hindi>=75:
        print("hindi:",hindi ,"100\t", "p\t","A+")
 elif hindi>=65:
        print("hindi:",hindi ,"100\t",  "p\t","A")
 elif hindi>=55:
        print("hindi:",hindi ,"100\t",  "p\t","B")
 elif hindi>=35:
        print("hindi:",hindi ,"100\t",   "p\t","C")
else:
     print("hindi:",hindi ,"100\t",   "f\t","f")
if maths>=35:
 if maths>=75:
        print("maths:",maths ,"100\t", "p\t","A+")
 elif maths>=65:
        print("maths:",maths ,"100\t",  "p\t","A")
 elif maths>=55:
        print("maths:",maths  ,"100\t",  "p\t","B")
 elif maths>=35:
        print("maths:",maths  ,"100\t",   "p\t","C")
else:
    print("maths:",maths  ,"100\t",   "f\t","f")
if sci>=35:
 if sci>=75:
        print("science:",sci ,"100\t", "p\t","A+")
 elif sci>=65:
        print("science:",sci ,"100\t",  "p\t","A")
 elif sci>=55:
        print("science:",sci ,"100\t",  "p\t","B")
 elif sci>=35:
        print("science:",sci ,"100\t",   "p\t","C")
else:
      print("science:",sci ,"100\t",   "f\t","f")
if soc>=35:
 if soc>=75:
        print("social:",soc ,"100\t", "p\t","A+")
 elif soc>=65:
        print("social:",soc ,"100\t",  "p\t","A")
 elif soc>=55:
        print("social:",soc ,"100\t",  "p\t","B")
 elif soc>=35:
        print("social:",soc ,"100\t",   "p\t","C")
else:
     print("social:",soc ,"100",   "f","f")
score=eng+tel+hindi+maths+sci+soc
per=(score/600)*100
print("marks:",score)
print("percent:",per)
if (eng<=35 and tel<=35 and hindi<=35 and maths<=35 and sci<=35 and soc<=35):
    per = 0
    if((eng and tel and hindi and maths and sci and soc)>=35):
        if per>=75:
            print("Overal percentage:",per,"/100","p","Grade: A+")
        elif per>=65:
            print("Overal percentage:",per,"/100","p","Grade: A")
        elif per>=55:
            print("Overal percentage:",per,"/100","p","Grade: B")
        elif per>=35:
            print("Overal percentage:",per,"/100","p","Grade: C")
else:
    print("Overal percentage:",per,"\n","100","f","Grade: Fail")

