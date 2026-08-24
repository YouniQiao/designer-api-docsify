# RegExp

正则表达式。

**继承/实现关系：** RegExp extends [Object](arkts-arkts-object-c.md)

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

<!--Device-unnamed-export class RegExp--><!--Device-unnamed-export class RegExp-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## $_invoke

```TypeScript
public static $_invoke(pattern: string, flags?: string): RegExp
```

RegExp构造函数的调用签名，用于创建新的RegExp实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public static $_invoke(pattern: string, flags?: string): RegExp--><!--Device-RegExp-public static $_invoke(pattern: string, flags?: string): RegExp-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pattern | string | 是 | 正则表达式模式。 |
| flags | string | 否 | 正则表达式的标志位。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| RegExp | 新创建的RegExp实例。 |

## $_invoke

```TypeScript
public static $_invoke(pattern: RegExp | string, flags?: string): RegExp
```

RegExp构造函数的调用签名，用于创建新的RegExp实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public static $_invoke(pattern: RegExp | string, flags?: string): RegExp--><!--Device-RegExp-public static $_invoke(pattern: RegExp | string, flags?: string): RegExp-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pattern | RegExp \| string | 是 | 正则表达式模式，或另一个RegExp实例。 |
| flags | string | 否 | 正则表达式的标志位。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| RegExp | 新创建的RegExp实例。 |

## $_invoke

```TypeScript
public static $_invoke(pattern: RegExp | string): RegExp
```

RegExp构造函数的调用签名，用于创建新的RegExp实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public static $_invoke(pattern: RegExp | string): RegExp--><!--Device-RegExp-public static $_invoke(pattern: RegExp | string): RegExp-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pattern | RegExp \| string | 是 | 正则表达式模式，或另一个RegExp实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| RegExp | 新创建的RegExp实例。 |

## advanceStringIndex

```TypeScript
public static advanceStringIndex(s: string, index: int, unicode: boolean): int
```

根据Unicode标志位推进字符串索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public static advanceStringIndex(s: string, index: int, unicode: boolean): int--><!--Device-RegExp-public static advanceStringIndex(s: string, index: int, unicode: boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| s | string | 是 | 原始字符串。 |
| index | int | 是 | 当前索引。 <br>取值约束：应为整数。 |
| unicode | boolean | 是 | 是否启用Unicode模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 下一个索引。 |

## constructor

```TypeScript
constructor(pattern: string, flags?: string)
```

使用模式和标志位构造新的RegExp。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-constructor(pattern: string, flags?: string)--><!--Device-RegExp-constructor(pattern: string, flags?: string)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pattern | string | 是 | 模式的描述。 |
| flags | string | 否 | 所使用标志位的描述。 |

## constructor

```TypeScript
constructor(regexp: RegExp, flags?: string)
```

根据另一个RegExp构造新的RegExp。未传入标志位时，沿用该RegExp的标志位。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-constructor(regexp: RegExp, flags?: string)--><!--Device-RegExp-constructor(regexp: RegExp, flags?: string)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| regexp | RegExp | 是 | 另一个正则表达式。 |
| flags | string | 否 | 所使用标志位的描述。 |

## constructor

```TypeScript
constructor(regexp: RegExp | string, flags?: string)
```

根据RegExp或字符串构造新的RegExp。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-constructor(regexp: RegExp | string, flags?: string)--><!--Device-RegExp-constructor(regexp: RegExp | string, flags?: string)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| regexp | RegExp \| string | 是 | 正则表达式的模式，或另一个RegExp实例。 |
| flags | string | 否 | 所使用标志位的描述。 |

## exec

```TypeScript
public exec(str: string, index: int): RegExpExecArray | null
```

从指定索引开始对字符串执行匹配查找。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public exec(str: string, index: int): RegExpExecArray | null--><!--Device-RegExp-public exec(str: string, index: int): RegExpExecArray | null-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| str | string | 是 | 待匹配的字符串。 |
| index | int | 是 | 开始匹配的索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RegExpExecArray](arkts-arkts-regexp-regexpexecarray-c.md) \| null | 匹配成功时返回包含匹配结果的数组， 否则返回null。 |

## exec

```TypeScript
public exec(str: string): RegExpExecArray | null
```

在指定字符串中执行匹配查找，并返回结果数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public exec(str: string): RegExpExecArray | null--><!--Device-RegExp-public exec(str: string): RegExpExecArray | null-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| str | string | 是 | 待匹配的字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RegExpExecArray](arkts-arkts-regexp-regexpexecarray-c.md) \| null | 匹配成功时返回包含匹配结果的数组， 否则返回null。 |

## match

```TypeScript
public match(str: string): RegExpMatchArray | null
```

在字符串中查找匹配，并以数组形式返回所有匹配结果。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public match(str: string): RegExpMatchArray | null--><!--Device-RegExp-public match(str: string): RegExpMatchArray | null-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| str | string | 是 | 待匹配的字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RegExpMatchArray](arkts-arkts-regexp-regexpmatcharray-c.md) \| null | 找到匹配时返回包含所有匹配结果的数组， 否则返回null。 |

## matchAll

```TypeScript
public matchAll(str: string): IterableIterator<RegExpMatchArray>
```

返回遍历字符串中所有匹配结果的迭代器。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public matchAll(str: string): IterableIterator<RegExpMatchArray>--><!--Device-RegExp-public matchAll(str: string): IterableIterator<RegExpMatchArray>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| str | string | 是 | 待匹配的字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[RegExpMatchArray](arkts-arkts-regexp-regexpmatcharray-c.md)&gt; | 遍历所有匹配结果的迭代器。 |

## replace

```TypeScript
public replace(str: string, replaceValue: string): string
```

使用替换字符串替换字符串中匹配到的子串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public replace(str: string, replaceValue: string): string--><!--Device-RegExp-public replace(str: string, replaceValue: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| str | string | 是 | 原始字符串。 |
| replaceValue | string | 是 | 用于替换的字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 替换后的新字符串。 |

## replace

```TypeScript
public replace(str: string, replacer: (substr: string, args: Object[]) => string): string
```

使用函数替换字符串中匹配到的子串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public replace(str: string, replacer: (substr: string, args: Object[]) => string): string--><!--Device-RegExp-public replace(str: string, replacer: (substr: string, args: Object[]) => string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| str | string | 是 | 原始字符串。 |
| replacer | (substr: string, args: Object[]) =&gt; string | 是 | 用于生成新子串的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 替换后的新字符串。 |

## search

```TypeScript
public search(str: string): int
```

在字符串中查找匹配，并返回匹配的起始索引。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public search(str: string): int--><!--Device-RegExp-public search(str: string): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| str | string | 是 | 待搜索的字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 找到匹配时返回其起始索引，否则返回-1。 |

## split

```TypeScript
public split(str: string, limit: Int | undefined): string[]
```

使用正则表达式将字符串分割为子串数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public split(str: string, limit: Int | undefined): string[]--><!--Device-RegExp-public split(str: string, limit: Int | undefined): string[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| str | string | 是 | 待分割的字符串。 |
| limit | Int \| undefined | 是 | 限制返回数组的最大长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 分割后得到的子串数组。 |

## test

```TypeScript
public test(str: string): boolean
```

在正则表达式与指定字符串之间执行匹配查找。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public test(str: string): boolean--><!--Device-RegExp-public test(str: string): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| str | string | 是 | 与正则表达式进行匹配的字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该字符串存在匹配则返回true，否则返回false。 |

## toString

```TypeScript
public toString(): string
```

返回表示该正则表达式的字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public toString(): string--><!--Device-RegExp-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该正则表达式的字符串表示。 |

