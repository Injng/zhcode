# stdlib.py
# translations for the Python Standard Library

# keywords not to exceed one charcater
keywords = {
        "用" : "import",
        "定" : "def",
        "为" : "for",
        "在" : "in",
        "是" : "if",
        "还" : "elif",
        "否" : "else",
        "回" : "return",
        "通" : "pass",
        "断" : "break",
        "或" : "or",
        "与" : "and",
        "当" : "while",
        "真" : "True",
        "假" : "False",
        "提" : "raise",
        "试" : "try",
        "以" : "with",
        "配" : "match",
        "说" : "assert",
        "续" : "continue",
        "全" : "global",
        "类" : "class",
        "自" : "self"



        }

# names and functions/methods not to exceed four characters
names = {
        "数学" : "math",
        "系统" : "sys"

        }

dunder = {
        "——名——" : "__name__",
        "——主——" : "__main__",
        "——初——" : "__init__"

        }

core = {
        "范围" : "range",
        "整" : "int",
        "印" : "print",
        "附加" : "append",
        "总和" : "sum",
        "格式" : "format"

        }

math = {
        "上整" : "ceil",
        "组合" : "comb",
        "抄性" : "copysign",
        "绝对值" : "fabs",
        "阶乘" : "factorial",
        "下整" : "floor",
        "取模" : "fmod",
        "尾指数" : "frexp",
        "浮点和" : "fsum",
        "大公约数" : "gcd",
        "是近" : "isclose",
        "是有限" : "isfinite",
        "是无穷" : "isinf",
        "是不是数" : "isnan",
        "整平方根" : "isqrt",
        "小公约数" : "lcm",
        "反尾指数" : "ldexp",
        "分整部" : "modf",
        "下浮点值" : "nextafter",
        "排列" : "perm",
        "积" : "prod",
        "余" : "remainder",
        "少分数" : "trunc",
        "最后位" : "ulp",
        "三次根" : "cbrt",
        "次方自然" : "exp",
        "次方二" : "exp2",
        "次方减一" : "expm1",
        "对数" : "log",
        "对数加一" : "log1p",
        "对数二" : "log2",
        "对数十" : "log10",
        "次方" : "pow",
        "平方根" : "sqrt",
        "反余弦" : "acos",
        "反正弦" : "asin",
        "反正切" : "atan",
        "反正切二" : "atan2",
        "余弦" : "cos",
        "距离" : "dist",
        "弦" : "hypot",
        "正弦" : "sin",
        "正切" : "tan",
        "度数" : "degrees",
        "弧度" : "radians",
        "反曲余弦" : "acosh",
        "反曲正弦" : "asinh",
        "反曲正切" : "atanh",
        "曲余弦" : "cosh",
        "曲正弦" : "sinh",
        "曲正切" : "tanh",
        "误差函数" : "erf",
        "一减误差" : "erfc",
        "伽玛" : "gamma",
        "对绝伽玛" : "lgamma",
        "圆周率" : "pi",
        "自然数" : "e",
        "二圆周率" : "tau",
        "无穷大" : "inf",
        "不是数" : "nan"
        }

func = core | math
