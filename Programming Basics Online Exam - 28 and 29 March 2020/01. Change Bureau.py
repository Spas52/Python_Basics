bitcoins = int(input())
china_una = float(input())
comission = float(input())
comission1 = comission * 0.01
bitcoins_price_in_leva = bitcoins * 1168
china_una_in_dollars = china_una * 0.15
china_una_in_leva = china_una_in_dollars * 1.76
summary_in_euro = (bitcoins_price_in_leva + china_una_in_leva) / 1.95
summary_in_euro1 = summary_in_euro - (summary_in_euro * comission1)
print(f"{summary_in_euro1:.2f}")