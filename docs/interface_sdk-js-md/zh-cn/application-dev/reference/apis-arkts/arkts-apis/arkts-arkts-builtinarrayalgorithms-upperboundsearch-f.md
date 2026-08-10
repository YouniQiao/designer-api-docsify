# upperBoundSearch

## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<boolean>, key: boolean, startIndex: int, endIndex: int): int
```

Tries to find an upper bound of a key in sorted arr.The array has to be sorted before calling this function.Upper bound is an index of a first element, where (key < element) is true. If no such element is found than upper bound is endIndex

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<boolean>, key: boolean, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<boolean>, key: boolean, startIndex: int, endIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;boolean&gt; | 是 | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | boolean | 是 | The value to find upper bound of |
| startIndex | int | 是 | The index of arr to begin search with &lt;br&gt;The value should be an integer. |
| endIndex | int | 是 | The last index to stop search in arr, i.e. arr[endIndex] is not checked &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The index such (key < arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<boolean>, key: boolean): int
```

Tries to find an upper bound of a key in sorted arr.The array has to be sorted before calling this function.Upper bound is an index of a first element, where (key < element) is true. If no such element is found than upper bound is endIndex

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<boolean>, key: boolean): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<boolean>, key: boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;boolean&gt; | 是 | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | boolean | 是 | The value to find upper bound of |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The index such (key < arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<byte>, key: byte, startIndex: int, endIndex: int): int
```

Tries to find an upper bound of a key in sorted arr.The array has to be sorted before calling this function.Upper bound is an index of a first element, where (key < element) is true. If no such element is found than upper bound is endIndex

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<byte>, key: byte, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<byte>, key: byte, startIndex: int, endIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;byte&gt; | 是 | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | byte | 是 | The value to find upper bound of |
| startIndex | int | 是 | The index of arr to begin search with &lt;br&gt;The value should be an integer. |
| endIndex | int | 是 | The last index to stop search in arr, i.e. arr[endIndex] is not checked &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The index such (key < arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<byte>, key: byte): int
```

Tries to find an upper bound of a key in sorted arr.The array has to be sorted before calling this function.Upper bound is an index of a first element, where (key < element) is true. If no such element is found than upper bound is endIndex

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<byte>, key: byte): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<byte>, key: byte): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;byte&gt; | 是 | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | byte | 是 | The value to find upper bound of |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The index such (key < arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<short>, key: short, startIndex: int, endIndex: int): int
```

Tries to find an upper bound of a key in sorted arr.The array has to be sorted before calling this function.Upper bound is an index of a first element, where (key < element) is true. If no such element is found than upper bound is endIndex

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<short>, key: short, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<short>, key: short, startIndex: int, endIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;short&gt; | 是 | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | short | 是 | The value to find upper bound of |
| startIndex | int | 是 | The index of arr to begin search with &lt;br&gt;The value should be an integer. |
| endIndex | int | 是 | The last index to stop search in arr, i.e. arr[endIndex] is not checked &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The index such (key < arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<short>, key: short): int
```

Tries to find an upper bound of a key in sorted arr.The array has to be sorted before calling this function.Upper bound is an index of a first element, where (key < element) is true. If no such element is found than upper bound is endIndex

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<short>, key: short): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<short>, key: short): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;short&gt; | 是 | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | short | 是 | The value to find upper bound of |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The index such (key < arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<int>, key: int, startIndex: int, endIndex: int): int
```

Tries to find an upper bound of a key in sorted arr.The array has to be sorted before calling this function.Upper bound is an index of a first element, where (key < element) is true. If no such element is found than upper bound is endIndex

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<int>, key: int, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<int>, key: int, startIndex: int, endIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;int&gt; | 是 | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | int | 是 | The value to find upper bound of &lt;br&gt;The value should be an integer. |
| startIndex | int | 是 | The index of arr to begin search with &lt;br&gt;The value should be an integer. |
| endIndex | int | 是 | The last index to stop search in arr, i.e. arr[endIndex] is not checked &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The index such (key < arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<int>, key: int): int
```

Tries to find an upper bound of a key in sorted arr.The array has to be sorted before calling this function.Upper bound is an index of a first element, where (key < element) is true. If no such element is found than upper bound is endIndex

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<int>, key: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<int>, key: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;int&gt; | 是 | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | int | 是 | The value to find upper bound of &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The index such (key < arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<long>, key: long, startIndex: int, endIndex: int): int
```

Tries to find an upper bound of a key in sorted arr.The array has to be sorted before calling this function.Upper bound is an index of a first element, where (key < element) is true. If no such element is found than upper bound is endIndex

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<long>, key: long, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<long>, key: long, startIndex: int, endIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;long&gt; | 是 | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | long | 是 | The value to find upper bound of |
| startIndex | int | 是 | The index of arr to begin search with &lt;br&gt;The value should be an integer. |
| endIndex | int | 是 | The last index to stop search in arr, i.e. arr[endIndex] is not checked &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The index such (key < arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<long>, key: long): int
```

Tries to find an upper bound of a key in sorted arr.The array has to be sorted before calling this function.Upper bound is an index of a first element, where (key < element) is true. If no such element is found than upper bound is endIndex

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<long>, key: long): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<long>, key: long): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;long&gt; | 是 | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | long | 是 | The value to find upper bound of |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The index such (key < arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<float>, key: float, startIndex: int, endIndex: int): int
```

Tries to find an upper bound of a key in sorted arr.The array has to be sorted before calling this function.Upper bound is an index of a first element, where (key < element) is true. If no such element is found than upper bound is endIndex

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<float>, key: float, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<float>, key: float, startIndex: int, endIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;float&gt; | 是 | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | float | 是 | The value to find upper bound of |
| startIndex | int | 是 | The index of arr to begin search with &lt;br&gt;The value should be an integer. |
| endIndex | int | 是 | The last index to stop search in arr, i.e. arr[endIndex] is not checked &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The index such (key < arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<float>, key: float): int
```

Tries to find an upper bound of a key in sorted arr.The array has to be sorted before calling this function.Upper bound is an index of a first element, where (key < element) is true. If no such element is found than upper bound is endIndex

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<float>, key: float): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<float>, key: float): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;float&gt; | 是 | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | float | 是 | The value to find upper bound of |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The index such (key < arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<double>, key: double, startIndex: int, endIndex: int): int
```

Tries to find an upper bound of a key in sorted arr.The array has to be sorted before calling this function.Upper bound is an index of a first element, where (key < element) is true. If no such element is found than upper bound is endIndex

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<double>, key: double, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<double>, key: double, startIndex: int, endIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;double&gt; | 是 | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | double | 是 | The value to find upper bound of |
| startIndex | int | 是 | The index of arr to begin search with &lt;br&gt;The value should be an integer. |
| endIndex | int | 是 | The last index to stop search in arr, i.e. arr[endIndex] is not checked &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The index such (key < arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<double>, key: double): int
```

Tries to find an upper bound of a key in sorted arr.The array has to be sorted before calling this function.Upper bound is an index of a first element, where (key < element) is true. If no such element is found than upper bound is endIndex

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<double>, key: double): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<double>, key: double): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;double&gt; | 是 | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | double | 是 | The value to find upper bound of |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The index such (key < arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<char>, key: char, startIndex: int, endIndex: int): int
```

Tries to find an upper bound of a key in sorted arr.The array has to be sorted before calling this function.Upper bound is an index of a first element, where (key < element) is true. If no such element is found than upper bound is endIndex

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<char>, key: char, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<char>, key: char, startIndex: int, endIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;char&gt; | 是 | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | char | 是 | The value to find upper bound of |
| startIndex | int | 是 | The index of arr to begin search with &lt;br&gt;The value should be an integer. |
| endIndex | int | 是 | The last index to stop search in arr, i.e. arr[endIndex] is not checked &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The index such (key < arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<char>, key: char): int
```

Tries to find an upper bound of a key in sorted arr.The array has to be sorted before calling this function.Upper bound is an index of a first element, where (key < element) is true. If no such element is found than upper bound is endIndex

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<char>, key: char): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<char>, key: char): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;char&gt; | 是 | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | char | 是 | The value to find upper bound of |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The index such (key < arr[index]) is true. If no such index is found than endIndex |

