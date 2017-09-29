
PRECEDENCE = {"*": 3,
              "/": 3,
              "+": 2,
              "-": 2,
              "(": 1}

def infix_to_postfix(infixexpr):

    opStack = []
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:

        if token.isalnum():
            #if a letter or number add to the postfixlist
            postfixList.append(token)
        elif token == '(':
            #parenthesis start add to op
            opStack.append(token)
        elif token == ')':
            #close paren, pop until we find the beginning
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while len(opStack) and (PRECEDENCE[opStack[-1]] >= PRECEDENCE[token]):
                  postfixList.append(opStack.pop())
            opStack.append(token)

    while len(opStack):
        postfixList.append(opStack.pop())

    return " ".join(postfixList)



opf = {'*': lambda x,y: x*y,
       '+': lambda x,y: x+y,
       '/': lambda x,y: x/y,
       '-': lambda x,y: x-y}


def eval_postfix(postfixExpr):
    pass


assert eval_postfix(infix_to_postfix("9 + ( 7 * 6 )")) == 51

