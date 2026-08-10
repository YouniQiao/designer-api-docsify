# ConcatArray

this is a concatArray interface

**Inheritance/Implementation:** ConcatArray extends [ArrayLike<T>](ArrayLike<T>)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export interface ConcatArray<out T> extends ArrayLike<T>--><!--Device-unnamed-export interface ConcatArray<out T> extends ArrayLike<T>-End-->

**System capability:** SystemCapability.Utils.Lang

## at

```TypeScript
at(index: int): T | undefined
```

Returns the element at the specified index in the array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConcatArray-at(index: int): T | undefined--><!--Device-ConcatArray-at(index: int): T | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index of the element to return. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| T | The element at the specified index, or undefined if the index is out of bounds. |

## join

```TypeScript
join(separator?: string): string
```

Joins all elements of an array into a string.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConcatArray-join(separator?: string): string--><!--Device-ConcatArray-join(separator?: string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| separator | string | No | A string used to separate one element of the array from the next in the resulting string. If omitted, the array elements are separated with a comma. |

**Return value:**

| Type | Description |
| --- | --- |
| string | A string containing all the elements of the array joined. |

## slice

```TypeScript
slice(start?: int, end?: int): Array<T>
```

Returns a shallow copy of a portion of an array into a new array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConcatArray-slice(start?: int, end?: int): Array<T>--><!--Device-ConcatArray-slice(start?: int, end?: int): Array<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | No | The start index for slice. If negative, it is treated as length + start. &lt;br&gt;The value should be an integer. |
| end | int | No | The end index for slice (exclusive). If negative, it is treated as length + end. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;T&gt; | A new array containing the extracted elements. |

