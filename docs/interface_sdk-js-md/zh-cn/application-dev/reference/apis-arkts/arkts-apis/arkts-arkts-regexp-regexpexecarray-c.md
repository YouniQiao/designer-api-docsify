# RegExpExecArray

Represents the return result of exec(), containing detailed information of a single match.

**继承/实现关系：** RegExpExecArray extends [RegExpResultArray](arkts-arkts-regexp-regexpresultarray-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class RegExpExecArray extends RegExpResultArray--><!--Device-unnamed-export class RegExpExecArray extends RegExpResultArray-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)
```

Creates a RegExpExecArray instance containing match results.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpExecArray-constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)--><!--Device-RegExpExecArray-constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | the starting index of the match result. &lt;br&gt;The value should be an integer. |
| input | string | 是 | the original string used for matching. |
| result | Array&lt;string \| undefined&gt; | 是 | the array of matched strings. |
| indices | Array&lt;Array&lt;int&gt;&gt; | 是 | the start and end index arrays of each matching substring. |

## constructor

```TypeScript
constructor(index: int, input: string, result: Array<string | undefined>)
```

Creates a RegExpExecArray instance containing match results (without indices).

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpExecArray-constructor(index: int, input: string, result: Array<string | undefined>)--><!--Device-RegExpExecArray-constructor(index: int, input: string, result: Array<string | undefined>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | the starting index of the match result. &lt;br&gt;The value should be an integer. |
| input | string | 是 | the original string used for matching. |
| result | Array&lt;string \| undefined&gt; | 是 | the array of matched strings. |

## index

```TypeScript
public set index(val: int)
```

Sets the starting index of the match result.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpExecArray-public set index(val: int)--><!--Device-RegExpExecArray-public set index(val: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

## input

```TypeScript
public set input(val: string)
```

Sets the original string used for matching.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RegExpExecArray-public set input(val: string)--><!--Device-RegExpExecArray-public set input(val: string)-End-->

**系统能力：** SystemCapability.Utils.Lang

