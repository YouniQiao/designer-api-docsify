# RegExpResultArray

Regular expression result descriptor

**Inheritance/Implementation:** RegExpResultArray extends [Array<string | undefined>](regexp-regexpresultarray-c.md#result)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-unnamed-export class RegExpResultArray extends Array<string | undefined>--><!--Device-unnamed-export class RegExpResultArray extends Array<string | undefined>-End-->

**System capability:** SystemCapability.Utils.Lang

## $_get

```TypeScript
$_get(index: string): string
```

Returns the first match if "0" is given and the first match exists

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExpResultArray-$_get(index: string): string--><!--Device-RegExpResultArray-$_get(index: string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | string | Yes | string index. |

**Return value:**

| Type | Description |
| --- | --- |
| string | the first match as string or null |

## $_get

```TypeScript
$_get(index: int): string | undefined
```

Returns result string by index.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExpResultArray-$_get(index: int): string | undefined--><!--Device-RegExpResultArray-$_get(index: int): string | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Integer index.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| string | resulting string. |

## $_set

```TypeScript
public $_set(index: int, val: string | undefined): void
```

Set the matching result at the specified index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExpResultArray-public $_set(index: int, val: string | undefined): void--><!--Device-RegExpResultArray-public $_set(index: int, val: string | undefined): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | the index to be set.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |
| val | string \| undefined | Yes | the value to be set. |

## constructor

```TypeScript
constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)
```

Creates a RegExpResultArray instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExpResultArray-constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)--><!--Device-RegExpResultArray-constructor(index: int, input: string, result: Array<string | undefined>, indices: Array<Array<int>>)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | the starting index of the match result.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |
| input | string | Yes | the original string used for matching. |
| result | Array&lt;string \| undefined&gt; | Yes | the string array that matches. |
| indices | Array&lt;Array&lt;int&gt;&gt; | Yes | the start and end index arrays of each matching substring. |

## indices

```TypeScript
public get indices(): Array<Array<int>>
```

Get an array containing the start and end indices of each matching substring.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExpResultArray-public get indices(): Array<Array<int>>--><!--Device-RegExpResultArray-public get indices(): Array<Array<int>>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;Array&lt;int&gt;&gt; | index array. |

## postExecProcessing

```TypeScript
public postExecProcessing(res: RegExpResultArray, input: string, index: int, hasIndices: boolean): void
```

Post execution processing.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExpResultArray-public postExecProcessing(res: RegExpResultArray, input: string, index: int, hasIndices: boolean): void--><!--Device-RegExpResultArray-public postExecProcessing(res: RegExpResultArray, input: string, index: int, hasIndices: boolean): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| res | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the result array. |
| input | string | Yes | the input string. |
| index | int | Yes | the index.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |
| hasIndices | boolean | Yes | whether has indices. |

## result

```TypeScript
public get result(): Array<string | undefined>
```

Get the matching result array itself.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExpResultArray-public get result(): Array<string | undefined>--><!--Device-RegExpResultArray-public get result(): Array<string | undefined>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string \| undefined&gt; | Match result array. |

## toString

```TypeScript
public toString(): string
```

Returns a string representation of the matching result.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RegExpResultArray-public toString(): string--><!--Device-RegExpResultArray-public toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | a string representing the match result. |

