# RegExpMatchArray

Represents the matching result returned by string.prototype.matchAll(),or the non iterative result of RegExp.prototype.exec() in global mode.

**继承/实现关系：** RegExpMatchArray extends [RegExpResultArray](arkts-arkts-regexp-regexpresultarray-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class RegExpMatchArray extends RegExpResultArray--><!--Device-unnamed-export class RegExpMatchArray extends RegExpResultArray-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)
```

Creates a RegExpMatchArray instance that contains matching results.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpMatchArray-constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)--><!--Device-RegExpMatchArray-constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | the starting index of the matching result. &lt;br&gt;The value should be an integer. |
| input | string | 是 | the original string used for matching. |
| result | Array&lt;string \| undefined&gt; | 是 | the string array that matches. |
| indices | Array&lt;Array&lt;int&gt;&gt; | 是 | the start and end index arrays of each matching substring. |

## constructor

```TypeScript
constructor(index: int, input: string, result: Array<string | undefined>)
```

Creates a RegExpMatchArray instance containing matching results.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpMatchArray-constructor(index: int, input: string, result: Array<string | undefined>)--><!--Device-RegExpMatchArray-constructor(index: int, input: string, result: Array<string | undefined>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | the starting index of the matching result. &lt;br&gt;The value should be an integer. |
| input | string | 是 | the original string used for matching. |
| result | Array&lt;string \| undefined&gt; | 是 | the string array that matches. |

## index

```TypeScript
public set index(val: int | undefined)
```

Sets the starting index of the match result.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpMatchArray-public set index(val: int | undefined)--><!--Device-RegExpMatchArray-public set index(val: int | undefined)-End-->

**系统能力：** SystemCapability.Utils.Lang

## input

```TypeScript
public set input(val: string | undefined)
```

Sets the original string used for matching.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpMatchArray-public set input(val: string | undefined)--><!--Device-RegExpMatchArray-public set input(val: string | undefined)-End-->

**系统能力：** SystemCapability.Utils.Lang

