# Character

提供Unicode字符属性相关的接口，例如：判断一个字符是否是数字。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [Unicode](arkts-localization-i18n-unicode-c.md#Unicode)

<!--Device-i18n-export class Character--><!--Device-i18n-export class Character-End-->

**系统能力：** SystemCapability.Global.I18n

## getType

```TypeScript
getType(ch: string): string
```

获取输入的字符的一般类别值。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getType](arkts-localization-i18n-unicode-c.md#getType)

<!--Device-Character-getType(ch: string): string--><!--Device-Character-getType(ch: string): string-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## isDigit

```TypeScript
isDigit(ch: string): boolean
```

判断输入的字符是否是数字。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isDigit](arkts-localization-i18n-unicode-c.md#isDigit)

<!--Device-Character-isDigit(ch: string): boolean--><!--Device-Character-isDigit(ch: string): boolean-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isIdeograph

```TypeScript
isIdeograph(ch: string): boolean
```

判断输入的字符是否是表意文字。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isIdeograph](arkts-localization-i18n-unicode-c.md#isIdeograph)

<!--Device-Character-isIdeograph(ch: string): boolean--><!--Device-Character-isIdeograph(ch: string): boolean-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isLetter

```TypeScript
isLetter(ch: string): boolean
```

判断输入的字符是否是字母。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isLetter](arkts-localization-i18n-unicode-c.md#isLetter)

<!--Device-Character-isLetter(ch: string): boolean--><!--Device-Character-isLetter(ch: string): boolean-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isLowerCase

```TypeScript
isLowerCase(ch: string): boolean
```

判断输入的字符是否是小写字母。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isLowerCase](arkts-localization-i18n-unicode-c.md#isLowerCase)

<!--Device-Character-isLowerCase(ch: string): boolean--><!--Device-Character-isLowerCase(ch: string): boolean-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isRTL

```TypeScript
isRTL(ch: string): boolean
```

判断输入的字符是否是从右到左语言的字符。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isRTL](arkts-localization-i18n-unicode-c.md#isRTL)

<!--Device-Character-isRTL(ch: string): boolean--><!--Device-Character-isRTL(ch: string): boolean-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isSpaceChar

```TypeScript
isSpaceChar(ch: string): boolean
```

判断输入的字符是否是空格符。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isSpaceChar](arkts-localization-i18n-unicode-c.md#isSpaceChar)

<!--Device-Character-isSpaceChar(ch: string): boolean--><!--Device-Character-isSpaceChar(ch: string): boolean-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isUpperCase

```TypeScript
isUpperCase(ch: string): boolean
```

判断输入的字符是否是大写字母。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isUpperCase](arkts-localization-i18n-unicode-c.md#isUpperCase)

<!--Device-Character-isUpperCase(ch: string): boolean--><!--Device-Character-isUpperCase(ch: string): boolean-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isWhitespace

```TypeScript
isWhitespace(ch: string): boolean
```

判断输入的字符是否是空白符。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isWhitespace](arkts-localization-i18n-unicode-c.md#isWhitespace)

<!--Device-Character-isWhitespace(ch: string): boolean--><!--Device-Character-isWhitespace(ch: string): boolean-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
