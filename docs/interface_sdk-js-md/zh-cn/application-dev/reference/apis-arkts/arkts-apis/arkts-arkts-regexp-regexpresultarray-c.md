# RegExpResultArray

Regular expression result descriptor

**继承/实现关系：** RegExpResultArray extends [Array<string | undefined>](Array<string | undefined>)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

<!--Device-unnamed-export class RegExpResultArray extends Array<string | undefined>--><!--Device-unnamed-export class RegExpResultArray extends Array<string | undefined>-End-->

**系统能力：** SystemCapability.Utils.Lang

## $_get

```TypeScript
$_get(index: string): string
```

Returns the first match if "0" is given and the first match exists

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpResultArray-$_get(index: string): string--><!--Device-RegExpResultArray-$_get(index: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | string | 是 | string index. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the first match as string or null |

## $_get

```TypeScript
$_get(index: int): string | undefined
```

Returns result string by index.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpResultArray-$_get(index: int): string | undefined--><!--Device-RegExpResultArray-$_get(index: int): string | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | Integer index. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | resulting string. |

## $_set

```TypeScript
public $_set(index: int, val: string | undefined): void
```

Set the matching result at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpResultArray-public $_set(index: int, val: string | undefined): void--><!--Device-RegExpResultArray-public $_set(index: int, val: string | undefined): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | the index to be set. &lt;br&gt;The value should be an integer. |
| val | string \| undefined | 是 | the value to be set. |

## constructor

```TypeScript
constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)
```

Creates a RegExpResultArray instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpResultArray-constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)--><!--Device-RegExpResultArray-constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | the starting index of the match result. &lt;br&gt;The value should be an integer. |
| input | string | 是 | the original string used for matching. |
| result | Array&lt;string \| undefined&gt; | 是 | the string array that matches. |
| indices | Array&lt;Array&lt;int&gt;&gt; | 是 | the start and end index arrays of each matching substring. |

## postExecProcessing

```TypeScript
public postExecProcessing(res: RegExpResultArray, input: string, index: int, hasIndices: boolean): void
```

Post execution processing.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpResultArray-public postExecProcessing(res: RegExpResultArray, input: string, index: int, hasIndices: boolean): void--><!--Device-RegExpResultArray-public postExecProcessing(res: RegExpResultArray, input: string, index: int, hasIndices: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| res | [RegExpResultArray](arkts-arkts-regexp-regexpresultarray-c.md) | 是 | the result array. |
| input | string | 是 | the input string. |
| index | int | 是 | the index. &lt;br&gt;The value should be an integer. |
| hasIndices | boolean | 是 | whether has indices. |

## toString

```TypeScript
public toString(): string
```

Returns a string representation of the matching result.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpResultArray-public toString(): string--><!--Device-RegExpResultArray-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | a string representing the match result. |

## indices

```TypeScript
public get indices(): Array<Array<int>>
```

Get an array containing the start and end indices of each matching substring.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpResultArray-public get indices(): Array<Array<int>>--><!--Device-RegExpResultArray-public get indices(): Array<Array<int>>-End-->

**系统能力：** SystemCapability.Utils.Lang

## result

```TypeScript
public get result(): Array<string | undefined>
```

Get the matching result array itself.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpResultArray-public get result(): Array<string | undefined>--><!--Device-RegExpResultArray-public get result(): Array<string | undefined>-End-->

**系统能力：** SystemCapability.Utils.Lang

