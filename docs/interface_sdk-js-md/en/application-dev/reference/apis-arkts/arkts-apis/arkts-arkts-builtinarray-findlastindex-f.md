# findLastIndex

## Modules to Import

```TypeScript
```

## findLastIndex

```TypeScript
export function findLastIndex(self: FixedArray<boolean>, predicate: (element: boolean, index: int,
    array: FixedArray<boolean>) => boolean): int
```

Iterates the array in reverse order and returns the index of the first element that satisfies the provided testing function. If no elements satisfy the testing function, -1 is returned.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function findLastIndex(self: FixedArray<boolean>, predicate: (element: boolean, index: int,    array: FixedArray<boolean>) => boolean): int--><!--Device-unnamed-export function findLastIndex(self: FixedArray<boolean>, predicate: (element: boolean, index: int,    array: FixedArray<boolean>) => boolean): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | Yes | The array to operate `findLastIndex` on. |
| predicate | (element: boolean, index: int,     array: FixedArray&lt;boolean&gt;) =&gt; boolean | Yes | A function to execute on each value in the array. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index of the first element that satisfies the provided testing function; otherwise, -1. |


## findLastIndex

```TypeScript
export function findLastIndex(self: FixedArray<byte>, predicate: (element: byte, index: int, array: FixedArray<byte>) 
    => boolean): int
```

Iterates the array in reverse order and returns the index of the first element that satisfies the provided testing function. If no elements satisfy the testing function, -1 is returned.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function findLastIndex(self: FixedArray<byte>, predicate: (element: byte, index: int, array: FixedArray<byte>)     => boolean): int--><!--Device-unnamed-export function findLastIndex(self: FixedArray<byte>, predicate: (element: byte, index: int, array: FixedArray<byte>)     => boolean): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | Yes | The array to operate `findLastIndex` on. |
| predicate | (element: byte, index: int, array: FixedArray&lt;byte&gt;)      =&gt; boolean | Yes | A function to execute on each value in the array. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index of the first element that satisfies the provided testing function; otherwise, -1. |


## findLastIndex

```TypeScript
export function findLastIndex(self: FixedArray<short>, predicate: (element: short, index: int, array: 
    FixedArray<short>) => boolean): int
```

Iterates the array in reverse order and returns the index of the first element that satisfies the provided testing function. If no elements satisfy the testing function, -1 is returned.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function findLastIndex(self: FixedArray<short>, predicate: (element: short, index: int, array:     FixedArray<short>) => boolean): int--><!--Device-unnamed-export function findLastIndex(self: FixedArray<short>, predicate: (element: short, index: int, array:     FixedArray<short>) => boolean): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | Yes | The array to operate `findLastIndex` on. |
| predicate | (element: short, index: int, array:      FixedArray&lt;short&gt;) =&gt; boolean | Yes | A function to execute on each value in the array. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index of the first element that satisfies the provided testing function; otherwise, -1. |


## findLastIndex

```TypeScript
export function findLastIndex(self: FixedArray<int>, predicate: (element: int, index: int, array: FixedArray<int>) 
    => boolean): int
```

Iterates the array in reverse order and returns the index of the first element that satisfies the provided testing function. If no elements satisfy the testing function, -1 is returned.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function findLastIndex(self: FixedArray<int>, predicate: (element: int, index: int, array: FixedArray<int>)     => boolean): int--><!--Device-unnamed-export function findLastIndex(self: FixedArray<int>, predicate: (element: int, index: int, array: FixedArray<int>)     => boolean): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | Yes | The array to operate `findLastIndex` on. |
| predicate | (element: int, index: int, array: FixedArray&lt;int&gt;)      =&gt; boolean | Yes | A function to execute on each value in the array. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index of the first element that satisfies the provided testing function; otherwise, -1. |


## findLastIndex

```TypeScript
export function findLastIndex(self: FixedArray<long>, predicate: (element: long, index: int, array: FixedArray<long>) 
    => boolean): int
```

Iterates the array in reverse order and returns the index of the first element that satisfies the provided testing function. If no elements satisfy the testing function, -1 is returned.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function findLastIndex(self: FixedArray<long>, predicate: (element: long, index: int, array: FixedArray<long>)     => boolean): int--><!--Device-unnamed-export function findLastIndex(self: FixedArray<long>, predicate: (element: long, index: int, array: FixedArray<long>)     => boolean): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | Yes | The array to operate `findLastIndex` on. |
| predicate | (element: long, index: int, array: FixedArray&lt;long&gt;)      =&gt; boolean | Yes | A function to execute on each value in the array. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index of the first element that satisfies the provided testing function; otherwise, -1. |


## findLastIndex

```TypeScript
export function findLastIndex(self: FixedArray<float>, predicate: (element: float, index: int, 
    array: FixedArray<float>) => boolean): int
```

Iterates the array in reverse order and returns the index of the first element that satisfies the provided testing function. If no elements satisfy the testing function, -1 is returned.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function findLastIndex(self: FixedArray<float>, predicate: (element: float, index: int,     array: FixedArray<float>) => boolean): int--><!--Device-unnamed-export function findLastIndex(self: FixedArray<float>, predicate: (element: float, index: int,     array: FixedArray<float>) => boolean): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | Yes | The array to operate `findLastIndex` on. |
| predicate | (element: float, index: int,      array: FixedArray&lt;float&gt;) =&gt; boolean | Yes | A function to execute on each value in the array. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index of the first element that satisfies the provided testing function; otherwise, -1. |


## findLastIndex

```TypeScript
export function findLastIndex(self: FixedArray<double>, predicate: (element: double, index: int, 
    array: FixedArray<double>) => boolean): int
```

Iterates the array in reverse order and returns the index of the first element that satisfies the provided testing function. If no elements satisfy the testing function, -1 is returned.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function findLastIndex(self: FixedArray<double>, predicate: (element: double, index: int,     array: FixedArray<double>) => boolean): int--><!--Device-unnamed-export function findLastIndex(self: FixedArray<double>, predicate: (element: double, index: int,     array: FixedArray<double>) => boolean): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | Yes | The array to operate `findLastIndex` on. |
| predicate | (element: double, index: int,      array: FixedArray&lt;double&gt;) =&gt; boolean | Yes | A function to execute on each value in the array. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index of the first element that satisfies the provided testing function; otherwise, -1. |


## findLastIndex

```TypeScript
export function findLastIndex(self: FixedArray<char>, predicate: (element: char, index: int, array: FixedArray<char>) 
    => boolean): int
```

Iterates the array in reverse order and returns the index of the first element that satisfies the provided testing function. If no elements satisfy the testing function, -1 is returned.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function findLastIndex(self: FixedArray<char>, predicate: (element: char, index: int, array: FixedArray<char>)     => boolean): int--><!--Device-unnamed-export function findLastIndex(self: FixedArray<char>, predicate: (element: char, index: int, array: FixedArray<char>)     => boolean): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | Yes | The array to operate `findLastIndex` on. |
| predicate | (element: char, index: int, array: FixedArray&lt;char&gt;)      =&gt; boolean | Yes | A function to execute on each value in the array. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The index of the first element that satisfies the provided testing function; otherwise, -1. |

