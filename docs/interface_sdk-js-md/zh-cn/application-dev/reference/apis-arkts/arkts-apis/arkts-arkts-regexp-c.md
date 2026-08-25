# RegExp

正则表达式。

**继承/实现关系：** RegExp extends [Object](arkts-arkts-object-c.md)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

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

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pattern](../../apis-sensor-service-kit/arkts-apis/arkts-sensorservice-vibrator-vibratefrompattern-i.md) | string | 是 |
| [flags](#flags) | string | 否 |

**返回值：**

| 类型 |
| --- |
| RegExp |

## $_invoke

```TypeScript
public static $_invoke(pattern: RegExp | string, flags?: string): RegExp
```

RegExp构造函数的调用签名，用于创建新的RegExp实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pattern](../../apis-sensor-service-kit/arkts-apis/arkts-sensorservice-vibrator-vibratefrompattern-i.md) | RegExp \| string | 是 |
| [flags](#flags) | string | 否 |

**返回值：**

| 类型 |
| --- |
| RegExp |

## $_invoke

```TypeScript
public static $_invoke(pattern: RegExp | string): RegExp
```

RegExp构造函数的调用签名，用于创建新的RegExp实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pattern](../../apis-sensor-service-kit/arkts-apis/arkts-sensorservice-vibrator-vibratefrompattern-i.md) | RegExp \| string | 是 |

**返回值：**

| 类型 |
| --- |
| RegExp |

## advanceStringIndex

```TypeScript
public static advanceStringIndex(s: string, index: int, unicode: boolean): int
```

根据Unicode标志位推进字符串索引。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| s | string | 是 |
| index | int | 是 |
| [unicode](#unicode) | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## constructor

```TypeScript
constructor(pattern: string, flags?: string)
```

使用模式和标志位构造新的RegExp。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pattern](../../apis-sensor-service-kit/arkts-apis/arkts-sensorservice-vibrator-vibratefrompattern-i.md) | string | 是 |
| [flags](#flags) | string | 否 |

## constructor

```TypeScript
constructor(regexp: RegExp, flags?: string)
```

根据另一个RegExp构造新的RegExp。未传入标志位时，沿用该RegExp的标志位。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| regexp | RegExp | 是 |
| [flags](#flags) | string | 否 |

## constructor

```TypeScript
constructor(regexp: RegExp | string, flags?: string)
```

根据RegExp或字符串构造新的RegExp。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| regexp | RegExp \| string | 是 |
| [flags](#flags) | string | 否 |

## exec

```TypeScript
public exec(str: string, index: int): RegExpExecArray | null
```

从指定索引开始对字符串执行匹配查找。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| str | string | 是 |
| index | int | 是 |

**返回值：**

| 类型 |
| --- |
| [RegExpExecArray](arkts-arkts-regexp-regexpexecarray-c.md) \| null |

## exec

```TypeScript
public exec(str: string): RegExpExecArray | null
```

在指定字符串中执行匹配查找，并返回结果数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| str | string | 是 |

**返回值：**

| 类型 |
| --- |
| [RegExpExecArray](arkts-arkts-regexp-regexpexecarray-c.md) \| null |

## match

```TypeScript
public match(str: string): RegExpMatchArray | null
```

在字符串中查找匹配，并以数组形式返回所有匹配结果。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| str | string | 是 |

**返回值：**

| 类型 |
| --- |
| [RegExpMatchArray](arkts-arkts-regexp-regexpmatcharray-c.md) \| null |

## matchAll

```TypeScript
public matchAll(str: string): IterableIterator<RegExpMatchArray>
```

返回遍历字符串中所有匹配结果的迭代器。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| str | string | 是 |

**返回值：**

| 类型 |
| --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[RegExpMatchArray](arkts-arkts-regexp-regexpmatcharray-c.md)&gt; |

## replace

```TypeScript
public replace(str: string, replaceValue: string): string
```

使用替换字符串替换字符串中匹配到的子串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| str | string | 是 |
| replaceValue | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## replace

```TypeScript
public replace(str: string, replacer: (substr: string, args: Object[]) => string): string
```

使用函数替换字符串中匹配到的子串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| str | string | 是 |
| replacer | (substr: string, args: Object[]) = & gt; string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## search

```TypeScript
public search(str: string): int
```

在字符串中查找匹配，并返回匹配的起始索引。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| str | string | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## split

```TypeScript
public split(str: string, limit: Int | undefined): string[]
```

使用正则表达式将字符串分割为子串数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| str | string | 是 |
| limit | Int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| string[] |

## test

```TypeScript
public test(str: string): boolean
```

在正则表达式与指定字符串之间执行匹配查找。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| str | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## toString

```TypeScript
public toString(): string
```

返回表示该正则表达式的字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## dotAll

```TypeScript
get dotAll(): boolean
```

获取dotAll标志位，表示'.'是否匹配换行符。

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## flags

```TypeScript
get flags(): string
```

获取正则表达式的标志位。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## global

```TypeScript
get global(): boolean
```

获取global标志位，表示是否执行全局匹配。

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## hasIndices

```TypeScript
get hasIndices(): boolean
```

获取hasIndices标志位，表示是否包含匹配子串的索引信息。

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## ignoreCase

```TypeScript
get ignoreCase(): boolean
```

获取ignoreCase标志位，表示是否忽略大小写。

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## multiline

```TypeScript
get multiline(): boolean
```

获取multiline标志位，表示是否执行多行匹配。

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## source

```TypeScript
get source(): string
```

返回包含该正则表达式源文本的字符串。

**类型：** string

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## sticky

```TypeScript
get sticky(): boolean
```

获取sticky标志位，表示是否执行粘性匹配。

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## unicode

```TypeScript
get unicode(): boolean
```

获取unicode标志位，表示是否启用Unicode模式。

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## unicodeSets

```TypeScript
get unicodeSets(): boolean
```

获取unicodeSets标志位，表示是否启用Unicode集合模式。

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang
