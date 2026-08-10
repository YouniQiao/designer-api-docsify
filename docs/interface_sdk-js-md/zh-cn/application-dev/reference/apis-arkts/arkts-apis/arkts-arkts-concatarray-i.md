# ConcatArray

this is a concatArray interface

**继承/实现关系：** ConcatArray extends [ArrayLike<T>](ArrayLike<T>)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export interface ConcatArray<out T> extends ArrayLike<T>--><!--Device-unnamed-export interface ConcatArray<out T> extends ArrayLike<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

## at

```TypeScript
at(index: int): T | undefined
```

Returns the element at the specified index in the array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConcatArray-at(index: int): T | undefined--><!--Device-ConcatArray-at(index: int): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index of the element to return. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | The element at the specified index, or undefined if the index is out of bounds. |

## join

```TypeScript
join(separator?: string): string
```

Joins all elements of an array into a string.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConcatArray-join(separator?: string): string--><!--Device-ConcatArray-join(separator?: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| separator | string | 否 | A string used to separate one element of the array from the next in the resulting string. If omitted, the array elements are separated with a comma. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | A string containing all the elements of the array joined. |

## slice

```TypeScript
slice(start?: int, end?: int): Array<T>
```

Returns a shallow copy of a portion of an array into a new array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConcatArray-slice(start?: int, end?: int): Array<T>--><!--Device-ConcatArray-slice(start?: int, end?: int): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | int | 否 | The start index for slice. If negative, it is treated as length + start. &lt;br&gt;The value should be an integer. |
| end | int | 否 | The end index for slice (exclusive). If negative, it is treated as length + end. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | A new array containing the extracted elements. |

