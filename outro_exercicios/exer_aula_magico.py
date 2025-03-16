

# __ne__(self, other)
# Define o comportamento do operador da desigualdade, .!=
# __lt__(self, other)
# Define o comportamento do operador less-than, .<
# __gt__(self, other)
# Define o comportamento do operador maior que, .>
# __le__(self, other)
# Define o comportamento do operador menor que ou igual a, .<=
# __ge__(self, other)
# Define o comportamento do operador maior ou igual a, .>=


# ============================================
def test_eq(nome,idade ):
    if idade.__eq__(18) :
        print(nome)
        print(idade)
        return
    print('difirente')


#===================================================================
def test_invert(nome,idade ):
    idade = idade.__invert__()
    print(nome)
    print(idade)
    return nome,idade

    p =test_invert('ana',-32)
    print(p)

#==================================================================
def test_neg(nome,idade ):
    idade = idade.__neg__()
    print(nome)
    print(idade)
    return nome,idade

    o = test_neg('ana',32)
    print(o)

#==================================================================
def test_round(nome,idade ):
    idade = idade.__round__(3)
    print(nome)
    print(idade)
    return nome,idade

o = test_round('ana',32.898878)
print(o)




