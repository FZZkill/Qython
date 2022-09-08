# Note

这是我写 Qython 时候的学习笔记，希望可以帮到大家 <br>
感谢：
感谢知乎大佬 <a hraf = "https://www.zhihu.com/people/llwanghong">Hong</a> 的文章搬运

感谢 Github 大佬项目<a hraf = "https://github.com/PowerAngelXD/YoLang">YoLang</a>

写这个的时候也得罪了不少人（指我啥都不会）需要Stars回血
# 语言叙述

    int x = 10
    println("Hello, World!")
    if (x == 10)
        {
        println("this is if")
    }
    //这一点也不像Python :-(

# 开始

## Parser

### 要点

-   多拆分些函数，保证函数足够小。
-   每个函数保证只做好一件事即可。
-   不要试图使用正则去做解析。但是你可以使用正则进项小部分解析。
-   当不确定如何解析某部分时，就当成错误抛出来。

代码以及实现应该分成三部分写 :

1. 字符流(Byte Stream)
2. Token 流(Lexer)
3. 语法解析器

字符流我们可以用循环写

-   line
-   column
-   pos

Token 一般长这样(这只是例子)

    { type: "punc", value: "(" }           // punctuation: parens, comma, semicolon etc.
    { type: "num", value: 5 }              // numbers
    { type: "string", value: "Hello World!" } // strings
    { type: "string", value: "a" }            // identifiers
    { type: "op", value: "!=" }

我们用var a = 10来举例子

    Token : < VAR | - >
    Token : < IDENTIFIER | a >
    Token : < E | - >
    Token : < NUMBER | 10 >

"|" 可以被任何分隔符号代替，Qython用的是",", 使用的是列表 + 元组的形式

在`./source/check.py`中的 `def Token(value)`函数中

我不打算考虑除了英文以外的字符，因为这是个练手项目
