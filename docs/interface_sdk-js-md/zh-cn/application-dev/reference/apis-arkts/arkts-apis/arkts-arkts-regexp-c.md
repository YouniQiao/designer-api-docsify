# RegExp

Regular expression

**继承/实现关系：** RegExp extends [Object](arkts-arkts-object-c.md)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

<!--Device-unnamed-export class RegExp extends Object--><!--Device-unnamed-export class RegExp extends Object-End-->

**系统能力：** SystemCapability.Utils.Lang

## $_invoke

```TypeScript
public static $_invoke(pattern: string, flags?: string): RegExp
```

RegExp constructor call signature, used to create new RegExp instances.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public static $_invoke(pattern: string, flags?: string): RegExp--><!--Device-RegExp-public static $_invoke(pattern: string, flags?: string): RegExp-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pattern | string | 是 | regular expression pattern. |
| flags | string | 否 | regular expression flags. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| RegExp | newly created RegExp instance. |

## $_invoke

```TypeScript
public static $_invoke(pattern: RegExp | string, flags?: string): RegExp
```

RegExp constructor call signature, used to create new RegExp instances.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public static $_invoke(pattern: RegExp | string, flags?: string): RegExp--><!--Device-RegExp-public static $_invoke(pattern: RegExp | string, flags?: string): RegExp-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pattern | RegExp \| string | 是 | regular expression pattern or another RegExp instance. |
| flags | string | 否 | regular expression flags. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| RegExp | newly created RegExp instance. |

## $_invoke

```TypeScript
public static $_invoke(pattern: RegExp | string): RegExp
```

RegExp constructor call signature, used to create new RegExp instances.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public static $_invoke(pattern: RegExp | string): RegExp--><!--Device-RegExp-public static $_invoke(pattern: RegExp | string): RegExp-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pattern | RegExp \| string | 是 | regular expression pattern or another RegExp instance. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| RegExp | newly created RegExp instance. |

## advanceStringIndex

```TypeScript
public static advanceStringIndex(s: string, index: int, unicode: boolean): int
```

Advances the string index according to the Unicode flag.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public static advanceStringIndex(s: string, index: int, unicode: boolean): int--><!--Device-RegExp-public static advanceStringIndex(s: string, index: int, unicode: boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| s | string | 是 | original string. |
| index | int | 是 | current index. &lt;br&gt;The value should be an integer. |
| unicode | boolean | 是 | whether to enable Unicode mode. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | next index. |

## constructor

```TypeScript
constructor(pattern: string, flags?: string)
```

Constructs a new RegExp using pattern and flags

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-constructor(pattern: string, flags?: string)--><!--Device-RegExp-constructor(pattern: string, flags?: string)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pattern | string | 是 | description of a pattern |
| flags | string | 否 | description of flags to be used |

## constructor

```TypeScript
constructor(regexp: RegExp, flags?: string)
```

Constructs a new RegExp by other RegExp. It uses other RegExp's flags if flags aren't provided

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-constructor(regexp: RegExp, flags?: string)--><!--Device-RegExp-constructor(regexp: RegExp, flags?: string)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| regexp | RegExp | 是 | other regexp |
| flags | string | 否 | description of flags to be used |

## constructor

```TypeScript
constructor(regexp: RegExp | string, flags?: string)
```

Constructs a new RegExp by RegExp or string

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-constructor(regexp: RegExp | string, flags?: string)--><!--Device-RegExp-constructor(regexp: RegExp | string, flags?: string)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| regexp | RegExp \| string | 是 | The pattern of the regular expression or another RegExp instance. |
| flags | string | 否 | description of flags to be used. |

## exec

```TypeScript
public exec(str: string, index: int): RegExpExecArray | null
```

Executes a match search on the string starting from the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public exec(str: string, index: int): RegExpExecArray | null--><!--Device-RegExp-public exec(str: string, index: int): RegExpExecArray | null-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| str | string | 是 | the string to match. |
| index | int | 是 | the index to start matching from. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RegExpExecArray](arkts-arkts-regexp-regexpexecarray-c.md) | if match succeeds, returns an array containing match results, otherwise returns null. |

## exec

```TypeScript
public exec(str: string): RegExpExecArray | null
```

Executes a search for a match in a specified string and returns a result array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public exec(str: string): RegExpExecArray | null--><!--Device-RegExp-public exec(str: string): RegExpExecArray | null-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| str | string | 是 | the string to match. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RegExpExecArray](arkts-arkts-regexp-regexpexecarray-c.md) | if match succeeds, returns an array containing match results, otherwise returns null. |

## match

```TypeScript
public match(str: string): RegExpMatchArray | null
```

Searches the string for matches and returns all matches as an array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public match(str: string): RegExpMatchArray | null--><!--Device-RegExp-public match(str: string): RegExpMatchArray | null-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| str | string | 是 | the string to match. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RegExpMatchArray](arkts-arkts-regexp-regexpmatcharray-c.md) | if matches are found, returns an array containing all matches, otherwise returns null. |

## matchAll

```TypeScript
public matchAll(str: string): IterableIterator<RegExpMatchArray>
```

Returns an iterator that iterates over all matches in the string.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public matchAll(str: string): IterableIterator<RegExpMatchArray>--><!--Device-RegExp-public matchAll(str: string): IterableIterator<RegExpMatchArray>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| str | string | 是 | the string to match. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;RegExpMatchArray&gt; | an iterator that iterates over all match results. |

## replace

```TypeScript
public replace(str: string, replaceValue: string): string
```

Replaces matched substrings in the string using a replacement string.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public replace(str: string, replaceValue: string): string--><!--Device-RegExp-public replace(str: string, replaceValue: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| str | string | 是 | the original string. |
| replaceValue | string | 是 | the string used for replacement. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the new string after replacement. |

## replace

```TypeScript
public replace(str: string, replacer: (substr: string, args: Object[]) => string): string
```

Replaces matched substrings in the string using a function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public replace(str: string, replacer: (substr: string, args: Object[]) => string): string--><!--Device-RegExp-public replace(str: string, replacer: (substr: string, args: Object[]) => string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| str | string | 是 | the original string. |
| replacer | (substr: string, args: Object[]) =&gt; string | 是 | a function used to generate new substrings. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the new string after replacement. |

## search

```TypeScript
public search(str: string): int
```

Searches for matches in the string and returns the starting index of the match.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public search(str: string): int--><!--Device-RegExp-public search(str: string): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| str | string | 是 | the string to search. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | if a match is found, returns its starting index; otherwise returns -1. |

## split

```TypeScript
public split(str: string, limit: Int | undefined): string[]
```

Splits the string into an array of substrings using the regular expression.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public split(str: string, limit: Int | undefined): string[]--><!--Device-RegExp-public split(str: string, limit: Int | undefined): string[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| str | string | 是 | the string to split. |
| limit | [Int](arkts-arkts-int-c.md) \| undefined | 是 | limits the maximum length of the returned array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | the array of substrings after splitting. |

## test

```TypeScript
public test(str: string): boolean
```

Executes a search for a match between a regular expression and specified string.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public test(str: string): boolean--><!--Device-RegExp-public test(str: string): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| str | string | 是 | the string against which to match the regular expression. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | if the string has matches, returns true; otherwise returns false. |

## toString

```TypeScript
public toString(): string
```

Returns a string representing the regular expression.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-public toString(): string--><!--Device-RegExp-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the string representation of the regular expression. |

## dotAll

```TypeScript
get dotAll(): boolean
```

Gets the dotAll flag, indicating whether '.' matches newline characters.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-get dotAll(): boolean--><!--Device-RegExp-get dotAll(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

## flags

```TypeScript
get flags(): string
```

Gets the flags of the regular expression.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-get flags(): string--><!--Device-RegExp-get flags(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

## global

```TypeScript
get global(): boolean
```

Gets the global flag, indicating whether to perform global matching.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-get global(): boolean--><!--Device-RegExp-get global(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

## hasIndices

```TypeScript
get hasIndices(): boolean
```

Gets the hasIndices flag, indicating whether to include indices of matching substrings.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-get hasIndices(): boolean--><!--Device-RegExp-get hasIndices(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

## ignoreCase

```TypeScript
get ignoreCase(): boolean
```

Gets the ignoreCase flag, indicating whether to ignore case.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-get ignoreCase(): boolean--><!--Device-RegExp-get ignoreCase(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

## multiline

```TypeScript
get multiline(): boolean
```

Gets the multiline flag, indicating whether to perform multiline matching.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-get multiline(): boolean--><!--Device-RegExp-get multiline(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

## source

```TypeScript
get source(): string
```

Returns a string containing the source text of this regular expression

**类型：** string

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-get source(): string--><!--Device-RegExp-get source(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

## sticky

```TypeScript
get sticky(): boolean
```

Gets the sticky flag, indicating whether to perform sticky matching.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-get sticky(): boolean--><!--Device-RegExp-get sticky(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

## unicode

```TypeScript
get unicode(): boolean
```

Gets the unicode flag, indicating whether to enable Unicode mode.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-get unicode(): boolean--><!--Device-RegExp-get unicode(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

## unicodeSets

```TypeScript
get unicodeSets(): boolean
```

Gets the unicodeSets flag, indicating whether Unicode set mode is enabled.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExp-get unicodeSets(): boolean--><!--Device-RegExp-get unicodeSets(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

