# upperBoundSearch

## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<boolean>, key: boolean, startIndex: int, endIndex: int): int
```

Tries to find an upper bound of a key in sorted arr. The array has to be sorted before calling this function. Upper bound is an index of a first element, where (key &lt; element) is true. If no such element is found than upper bound is endIndex

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<boolean>, key: boolean, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<boolean>, key: boolean, startIndex: int, endIndex: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | FixedArray&lt;boolean&gt; | Yes | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | boolean | Yes | The value to find upper bound of |
| startIndex | int | Yes | The index of arr to begin search with <br>The value should be an integer. |
| endIndex | int | Yes | The last index to stop search in arr, i.e. arr[endIndex] is not checked <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index such (key &lt; arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<boolean>, key: boolean): int
```

Tries to find an upper bound of a key in sorted arr. The array has to be sorted before calling this function. Upper bound is an index of a first element, where (key &lt; element) is true. If no such element is found than upper bound is endIndex

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<boolean>, key: boolean): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<boolean>, key: boolean): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | FixedArray&lt;boolean&gt; | Yes | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | boolean | Yes | The value to find upper bound of |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index such (key &lt; arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<byte>, key: byte, startIndex: int, endIndex: int): int
```

Tries to find an upper bound of a key in sorted arr. The array has to be sorted before calling this function. Upper bound is an index of a first element, where (key &lt; element) is true. If no such element is found than upper bound is endIndex

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<byte>, key: byte, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<byte>, key: byte, startIndex: int, endIndex: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | FixedArray&lt;byte&gt; | Yes | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | byte | Yes | The value to find upper bound of |
| startIndex | int | Yes | The index of arr to begin search with <br>The value should be an integer. |
| endIndex | int | Yes | The last index to stop search in arr, i.e. arr[endIndex] is not checked <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index such (key &lt; arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<byte>, key: byte): int
```

Tries to find an upper bound of a key in sorted arr. The array has to be sorted before calling this function. Upper bound is an index of a first element, where (key &lt; element) is true. If no such element is found than upper bound is endIndex

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<byte>, key: byte): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<byte>, key: byte): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | FixedArray&lt;byte&gt; | Yes | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | byte | Yes | The value to find upper bound of |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index such (key &lt; arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<short>, key: short, startIndex: int, endIndex: int): int
```

Tries to find an upper bound of a key in sorted arr. The array has to be sorted before calling this function. Upper bound is an index of a first element, where (key &lt; element) is true. If no such element is found than upper bound is endIndex

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<short>, key: short, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<short>, key: short, startIndex: int, endIndex: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | FixedArray&lt;short&gt; | Yes | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | short | Yes | The value to find upper bound of |
| startIndex | int | Yes | The index of arr to begin search with <br>The value should be an integer. |
| endIndex | int | Yes | The last index to stop search in arr, i.e. arr[endIndex] is not checked <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index such (key &lt; arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<short>, key: short): int
```

Tries to find an upper bound of a key in sorted arr. The array has to be sorted before calling this function. Upper bound is an index of a first element, where (key &lt; element) is true. If no such element is found than upper bound is endIndex

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<short>, key: short): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<short>, key: short): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | FixedArray&lt;short&gt; | Yes | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | short | Yes | The value to find upper bound of |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index such (key &lt; arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<int>, key: int, startIndex: int, endIndex: int): int
```

Tries to find an upper bound of a key in sorted arr. The array has to be sorted before calling this function. Upper bound is an index of a first element, where (key &lt; element) is true. If no such element is found than upper bound is endIndex

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<int>, key: int, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<int>, key: int, startIndex: int, endIndex: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | FixedArray&lt;int&gt; | Yes | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | int | Yes | The value to find upper bound of <br>The value should be an integer. |
| startIndex | int | Yes | The index of arr to begin search with <br>The value should be an integer. |
| endIndex | int | Yes | The last index to stop search in arr, i.e. arr[endIndex] is not checked <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index such (key &lt; arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<int>, key: int): int
```

Tries to find an upper bound of a key in sorted arr. The array has to be sorted before calling this function. Upper bound is an index of a first element, where (key &lt; element) is true. If no such element is found than upper bound is endIndex

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<int>, key: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<int>, key: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | FixedArray&lt;int&gt; | Yes | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | int | Yes | The value to find upper bound of <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index such (key &lt; arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<long>, key: long, startIndex: int, endIndex: int): int
```

Tries to find an upper bound of a key in sorted arr. The array has to be sorted before calling this function. Upper bound is an index of a first element, where (key &lt; element) is true. If no such element is found than upper bound is endIndex

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<long>, key: long, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<long>, key: long, startIndex: int, endIndex: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | FixedArray&lt;long&gt; | Yes | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | long | Yes | The value to find upper bound of |
| startIndex | int | Yes | The index of arr to begin search with <br>The value should be an integer. |
| endIndex | int | Yes | The last index to stop search in arr, i.e. arr[endIndex] is not checked <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index such (key &lt; arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<long>, key: long): int
```

Tries to find an upper bound of a key in sorted arr. The array has to be sorted before calling this function. Upper bound is an index of a first element, where (key &lt; element) is true. If no such element is found than upper bound is endIndex

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<long>, key: long): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<long>, key: long): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | FixedArray&lt;long&gt; | Yes | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | long | Yes | The value to find upper bound of |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index such (key &lt; arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<float>, key: float, startIndex: int, endIndex: int): int
```

Tries to find an upper bound of a key in sorted arr. The array has to be sorted before calling this function. Upper bound is an index of a first element, where (key &lt; element) is true. If no such element is found than upper bound is endIndex

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<float>, key: float, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<float>, key: float, startIndex: int, endIndex: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | FixedArray&lt;float&gt; | Yes | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | float | Yes | The value to find upper bound of |
| startIndex | int | Yes | The index of arr to begin search with <br>The value should be an integer. |
| endIndex | int | Yes | The last index to stop search in arr, i.e. arr[endIndex] is not checked <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index such (key &lt; arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<float>, key: float): int
```

Tries to find an upper bound of a key in sorted arr. The array has to be sorted before calling this function. Upper bound is an index of a first element, where (key &lt; element) is true. If no such element is found than upper bound is endIndex

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<float>, key: float): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<float>, key: float): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | FixedArray&lt;float&gt; | Yes | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | float | Yes | The value to find upper bound of |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index such (key &lt; arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<double>, key: double, startIndex: int, endIndex: int): int
```

Tries to find an upper bound of a key in sorted arr. The array has to be sorted before calling this function. Upper bound is an index of a first element, where (key &lt; element) is true. If no such element is found than upper bound is endIndex

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<double>, key: double, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<double>, key: double, startIndex: int, endIndex: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | FixedArray&lt;double&gt; | Yes | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | double | Yes | The value to find upper bound of |
| startIndex | int | Yes | The index of arr to begin search with <br>The value should be an integer. |
| endIndex | int | Yes | The last index to stop search in arr, i.e. arr[endIndex] is not checked <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index such (key &lt; arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<double>, key: double): int
```

Tries to find an upper bound of a key in sorted arr. The array has to be sorted before calling this function. Upper bound is an index of a first element, where (key &lt; element) is true. If no such element is found than upper bound is endIndex

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<double>, key: double): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<double>, key: double): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | FixedArray&lt;double&gt; | Yes | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | double | Yes | The value to find upper bound of |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index such (key &lt; arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<char>, key: char, startIndex: int, endIndex: int): int
```

Tries to find an upper bound of a key in sorted arr. The array has to be sorted before calling this function. Upper bound is an index of a first element, where (key &lt; element) is true. If no such element is found than upper bound is endIndex

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<char>, key: char, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<char>, key: char, startIndex: int, endIndex: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | FixedArray&lt;char&gt; | Yes | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | char | Yes | The value to find upper bound of |
| startIndex | int | Yes | The index of arr to begin search with <br>The value should be an integer. |
| endIndex | int | Yes | The last index to stop search in arr, i.e. arr[endIndex] is not checked <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index such (key &lt; arr[index]) is true. If no such index is found than endIndex |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<char>, key: char): int
```

Tries to find an upper bound of a key in sorted arr. The array has to be sorted before calling this function. Upper bound is an index of a first element, where (key &lt; element) is true. If no such element is found than upper bound is endIndex

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<char>, key: char): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<char>, key: char): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arr | FixedArray&lt;char&gt; | Yes | The array to find an upper bound of a key. Has to be sorted, otherwise the answer is implementation-defined and may be incorrect |
| key | char | Yes | The value to find upper bound of |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index such (key &lt; arr[index]) is true. If no such index is found than endIndex |

