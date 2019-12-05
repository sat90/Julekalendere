def findWishList(lista):
    l = list(lista)
    for i in range(int(len(l)/2)):
        if i % 3 == 0:
            for j in range(3):
                c = l[i+j]
                l[i+j] = l[len(l)-3-i+j]
                l[len(l)-3-i+j] = c

    for i in range(len(l)-1):
        if i % 2 == 0:
            c = l[i]
            l[i] = l[i+1]
            l[i+1] = c

    for i in range(int(len(l)/2)):
        c = l[i]
        l[i] = l[i+int(len(l)/2)]
        l[i+int(len(l)/2)] = c

    return "".join(l)


print(findWishList("tMlsioaplnKlflgiruKanliaebeLlkslikkpnerikTasatamkDpsdakeraBeIdaegptnuaKtmteorpuTaTtbtsesOHXxonibmksekaaoaKtrssegnveinRedlkkkroeekVtkekymmlooLnanoKtlstoepHrpeutdynfSneloietbol"))

assert "PonnistallHoppeslottTrommesett" == findWishList(
    "oepHlpslainttnotePmseormoTtlst")
