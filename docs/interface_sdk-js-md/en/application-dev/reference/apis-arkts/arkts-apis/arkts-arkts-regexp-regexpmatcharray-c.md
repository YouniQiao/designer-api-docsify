# RegExpMatchArray

Represents the matching result returned by string.prototype.matchAll(),or the non iterative result of RegExp.prototype.exec() in global mode.

**Inheritance/Implementation:** RegExpMatchArray extends [RegExpResultArray](arkts-arkts-regexp-regexpresultarray-c.md#RegExpResultArray)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export class RegExpMatchArray extends RegExpResultArray--><!--Device-unnamed-export class RegExpMatchArray extends RegExpResultArray-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)
```

Creates a RegExpMatchArray instance that contains matching results.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExpMatchArray-constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)--><!--Device-RegExpMatchArray-constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | the starting index of the matching result. &lt;br&gt;The value should be an integer. |
| input | string | Yes | the original string used for matching. |
| result | Array&lt;string \| undefined&gt; | Yes | the string array that matches. |
| indices | Array&lt;Array&lt;int&gt;&gt; | Yes | the start and end index arrays of each matching substring. |

## constructor

```TypeScript
constructor(index: int, input: string, result: Array<string | undefined>)
```

Creates a RegExpMatchArray instance containing matching results.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExpMatchArray-constructor(index: int, input: string, result: Array<string | undefined>)--><!--Device-RegExpMatchArray-constructor(index: int, input: string, result: Array<string | undefined>)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | the starting index of the matching result. &lt;br&gt;The value should be an integer. |
| input | string | Yes | the original string used for matching. |
| result | Array&lt;string \| undefined&gt; | Yes | the string array that matches. |

## index

```TypeScript
public set index(val: int | undefined)
```

Sets the starting index of the match result.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExpMatchArray-public set index(val: int | undefined)--><!--Device-RegExpMatchArray-public set index(val: int | undefined)-End-->

**System capability:** SystemCapability.Utils.Lang

## input

```TypeScript
public set input(val: string | undefined)
```

Sets the original string used for matching.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExpMatchArray-public set input(val: string | undefined)--><!--Device-RegExpMatchArray-public set input(val: string | undefined)-End-->

**System capability:** SystemCapability.Utils.Lang

