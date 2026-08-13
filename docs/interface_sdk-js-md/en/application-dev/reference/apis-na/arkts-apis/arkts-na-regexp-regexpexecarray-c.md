# RegExpExecArray

Represents the return result of exec(), containing detailed information of a single match.

**Inheritance/Implementation:** RegExpExecArray extends [RegExpResultArray](arkts-na-regexp-regexpresultarray-c.md#RegExpResultArray)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export class RegExpExecArray--><!--Device-unnamed-export class RegExpExecArray-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)
```

Creates a RegExpExecArray instance containing match results.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExpExecArray-constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)--><!--Device-RegExpExecArray-constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | the starting index of the match result. &lt;br&gt;The value should be an integer. |
| input | string | Yes | the original string used for matching. |
| result | Array&lt;string \| undefined&gt; | Yes | the array of matched strings. |
| indices | Array&lt;Array&lt;int&gt;&gt; | Yes | the start and end index arrays of each matching substring. |

## constructor

```TypeScript
constructor(index: int, input: string, result: Array<string | undefined>)
```

Creates a RegExpExecArray instance containing match results (without indices).

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExpExecArray-constructor(index: int, input: string, result: Array<string | undefined>)--><!--Device-RegExpExecArray-constructor(index: int, input: string, result: Array<string | undefined>)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | the starting index of the match result. &lt;br&gt;The value should be an integer. |
| input | string | Yes | the original string used for matching. |
| result | Array&lt;string \| undefined&gt; | Yes | the array of matched strings. |

