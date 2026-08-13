# reduceRight

## reduceRight

```TypeScript
export function reduceRight<U>(self: FixedArray<boolean>, callbackfn: (previousValue: U, currentValue: boolean, 
    index: int, array: FixedArray<boolean>) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function reduceRight<U>(self: FixedArray<boolean>, callbackfn: (previousValue: U, currentValue: boolean,     index: int, array: FixedArray<boolean>) => U, initialValue: U): U--><!--Device-unnamed-export function reduceRight<U>(self: FixedArray<boolean>, callbackfn: (previousValue: U, currentValue: boolean,     index: int, array: FixedArray<boolean>) => U, initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | Yes | The array to operate `reduce` on. |
| callbackfn | (previousValue: U, currentValue: boolean,      index: int, array: FixedArray&lt;boolean&gt;) =&gt; U | Yes | A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. |
| initialValue | U | Yes | The initial value of the accumulator. |

**Return value:**

| Type | Description |
| --- | --- |
| U | The accumulated result. |


## reduceRight

```TypeScript
export function reduceRight(self: FixedArray<boolean>, callbackfn: (previousValue: boolean, currentValue: boolean, 
    index: int, array: FixedArray<boolean>) => boolean): boolean
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function reduceRight(self: FixedArray<boolean>, callbackfn: (previousValue: boolean, currentValue: boolean,     index: int, array: FixedArray<boolean>) => boolean): boolean--><!--Device-unnamed-export function reduceRight(self: FixedArray<boolean>, callbackfn: (previousValue: boolean, currentValue: boolean,     index: int, array: FixedArray<boolean>) => boolean): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | Yes | The array to reduce. |
| callbackfn | (previousValue: boolean, currentValue: boolean,      index: int, array: FixedArray&lt;boolean&gt;) =&gt; boolean | Yes | A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | A result after applying callbackfn over all elements of the Array. |


## reduceRight

```TypeScript
export function reduceRight<U>(self: FixedArray<byte>, callbackfn: (previousValue: U, currentValue: byte, index: int, 
    array: FixedArray<byte>) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function reduceRight<U>(self: FixedArray<byte>, callbackfn: (previousValue: U, currentValue: byte, index: int,     array: FixedArray<byte>) => U, initialValue: U): U--><!--Device-unnamed-export function reduceRight<U>(self: FixedArray<byte>, callbackfn: (previousValue: U, currentValue: byte, index: int,     array: FixedArray<byte>) => U, initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | Yes | The array to operate `reduce` on. |
| callbackfn | (previousValue: U, currentValue: byte, index: int,      array: FixedArray&lt;byte&gt;) =&gt; U | Yes | A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. |
| initialValue | U | Yes | The initial value of the accumulator. |

**Return value:**

| Type | Description |
| --- | --- |
| U | The accumulated result. |


## reduceRight

```TypeScript
export function reduceRight(self: FixedArray<byte>, callbackfn: (previousValue: byte, currentValue: byte, index: int, 
    array: FixedArray<byte>) => byte): byte
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function reduceRight(self: FixedArray<byte>, callbackfn: (previousValue: byte, currentValue: byte, index: int,     array: FixedArray<byte>) => byte): byte--><!--Device-unnamed-export function reduceRight(self: FixedArray<byte>, callbackfn: (previousValue: byte, currentValue: byte, index: int,     array: FixedArray<byte>) => byte): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | Yes | The array to reduce. |
| callbackfn | (previousValue: byte, currentValue: byte, index: int,      array: FixedArray&lt;byte&gt;) =&gt; byte | Yes | A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. |

**Return value:**

| Type | Description |
| --- | --- |
| byte | A result after applying callbackfn over all elements of the Array. |


## reduceRight

```TypeScript
export function reduceRight<U>(self: FixedArray<short>, callbackfn: (previousValue: U, currentValue: short, 
    index: int, array: FixedArray<short>) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function reduceRight<U>(self: FixedArray<short>, callbackfn: (previousValue: U, currentValue: short,     index: int, array: FixedArray<short>) => U, initialValue: U): U--><!--Device-unnamed-export function reduceRight<U>(self: FixedArray<short>, callbackfn: (previousValue: U, currentValue: short,     index: int, array: FixedArray<short>) => U, initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | Yes | The array to operate `reduce` on. |
| callbackfn | (previousValue: U, currentValue: short,      index: int, array: FixedArray&lt;short&gt;) =&gt; U | Yes | A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. |
| initialValue | U | Yes | The initial value of the accumulator. |

**Return value:**

| Type | Description |
| --- | --- |
| U | The accumulated result. |


## reduceRight

```TypeScript
export function reduceRight(self: FixedArray<short>, callbackfn: (previousValue: short, currentValue: short, 
    index: int, array: FixedArray<short>) => short): short
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function reduceRight(self: FixedArray<short>, callbackfn: (previousValue: short, currentValue: short,     index: int, array: FixedArray<short>) => short): short--><!--Device-unnamed-export function reduceRight(self: FixedArray<short>, callbackfn: (previousValue: short, currentValue: short,     index: int, array: FixedArray<short>) => short): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | Yes | The array to reduce. |
| callbackfn | (previousValue: short, currentValue: short,      index: int, array: FixedArray&lt;short&gt;) =&gt; short | Yes | A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. |

**Return value:**

| Type | Description |
| --- | --- |
| short | A result after applying callbackfn over all elements of the Array. |


## reduceRight

```TypeScript
export function reduceRight<U>(self: FixedArray<int>, callbackfn: (previousValue: U, currentValue: int, index: int, 
    array: FixedArray<int>) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function reduceRight<U>(self: FixedArray<int>, callbackfn: (previousValue: U, currentValue: int, index: int,     array: FixedArray<int>) => U, initialValue: U): U--><!--Device-unnamed-export function reduceRight<U>(self: FixedArray<int>, callbackfn: (previousValue: U, currentValue: int, index: int,     array: FixedArray<int>) => U, initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | Yes | The array to operate `reduce` on. |
| callbackfn | (previousValue: U, currentValue: int, index: int,      array: FixedArray&lt;int&gt;) =&gt; U | Yes | A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. |
| initialValue | U | Yes | The initial value of the accumulator. |

**Return value:**

| Type | Description |
| --- | --- |
| U | The accumulated result. |


## reduceRight

```TypeScript
export function reduceRight(self: FixedArray<int>, callbackfn: (previousValue: int, currentValue: int, 
    index: int, array: FixedArray<int>) => int): int
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function reduceRight(self: FixedArray<int>, callbackfn: (previousValue: int, currentValue: int,     index: int, array: FixedArray<int>) => int): int--><!--Device-unnamed-export function reduceRight(self: FixedArray<int>, callbackfn: (previousValue: int, currentValue: int,     index: int, array: FixedArray<int>) => int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | Yes | The array to reduce. |
| callbackfn | (previousValue: int, currentValue: int,      index: int, array: FixedArray&lt;int&gt;) =&gt; int | Yes | A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. |

**Return value:**

| Type | Description |
| --- | --- |
| int | A result after applying callbackfn over all elements of the Array. |


## reduceRight

```TypeScript
export function reduceRight<U>(self: FixedArray<long>, callbackfn: (previousValue: U, currentValue: long, index: int, 
    array: FixedArray<long>) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function reduceRight<U>(self: FixedArray<long>, callbackfn: (previousValue: U, currentValue: long, index: int,     array: FixedArray<long>) => U, initialValue: U): U--><!--Device-unnamed-export function reduceRight<U>(self: FixedArray<long>, callbackfn: (previousValue: U, currentValue: long, index: int,     array: FixedArray<long>) => U, initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | Yes | The array to operate `reduce` on. |
| callbackfn | (previousValue: U, currentValue: long, index: int,      array: FixedArray&lt;long&gt;) =&gt; U | Yes | A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. |
| initialValue | U | Yes | The initial value of the accumulator. |

**Return value:**

| Type | Description |
| --- | --- |
| U | The accumulated result. |


## reduceRight

```TypeScript
export function reduceRight(self: FixedArray<long>, callbackfn: (previousValue: long, currentValue: long, index: int, 
    array: FixedArray<long>) => long): long
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function reduceRight(self: FixedArray<long>, callbackfn: (previousValue: long, currentValue: long, index: int,     array: FixedArray<long>) => long): long--><!--Device-unnamed-export function reduceRight(self: FixedArray<long>, callbackfn: (previousValue: long, currentValue: long, index: int,     array: FixedArray<long>) => long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | Yes | The array to reduce. |
| callbackfn | (previousValue: long, currentValue: long, index: int,      array: FixedArray&lt;long&gt;) =&gt; long | Yes | A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. |

**Return value:**

| Type | Description |
| --- | --- |
| long | A result after applying callbackfn over all elements of the Array. |


## reduceRight

```TypeScript
export function reduceRight<U>(self: FixedArray<float>, callbackfn: (previousValue: U, currentValue: float, 
    index: int, array: FixedArray<float>) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function reduceRight<U>(self: FixedArray<float>, callbackfn: (previousValue: U, currentValue: float,     index: int, array: FixedArray<float>) => U, initialValue: U): U--><!--Device-unnamed-export function reduceRight<U>(self: FixedArray<float>, callbackfn: (previousValue: U, currentValue: float,     index: int, array: FixedArray<float>) => U, initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | Yes | The array to operate `reduce` on. |
| callbackfn | (previousValue: U, currentValue: float,      index: int, array: FixedArray&lt;float&gt;) =&gt; U | Yes | A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. |
| initialValue | U | Yes | The initial value of the accumulator. |

**Return value:**

| Type | Description |
| --- | --- |
| U | The accumulated result. |


## reduceRight

```TypeScript
export function reduceRight(self: FixedArray<float>, callbackfn: (previousValue: float, currentValue: float, 
    index: int, array: FixedArray<float>) => float): float
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function reduceRight(self: FixedArray<float>, callbackfn: (previousValue: float, currentValue: float,     index: int, array: FixedArray<float>) => float): float--><!--Device-unnamed-export function reduceRight(self: FixedArray<float>, callbackfn: (previousValue: float, currentValue: float,     index: int, array: FixedArray<float>) => float): float-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | Yes | The array to reduce. |
| callbackfn | (previousValue: float, currentValue: float,      index: int, array: FixedArray&lt;float&gt;) =&gt; float | Yes | A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. |

**Return value:**

| Type | Description |
| --- | --- |
| float | A result after applying callbackfn over all elements of the Array. |


## reduceRight

```TypeScript
export function reduceRight<U>(self: FixedArray<double>, callbackfn: (previousValue: U, currentValue: double, 
    index: int, array: FixedArray<double>) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function reduceRight<U>(self: FixedArray<double>, callbackfn: (previousValue: U, currentValue: double,     index: int, array: FixedArray<double>) => U, initialValue: U): U--><!--Device-unnamed-export function reduceRight<U>(self: FixedArray<double>, callbackfn: (previousValue: U, currentValue: double,     index: int, array: FixedArray<double>) => U, initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | Yes | The array to operate `reduce` on. |
| callbackfn | (previousValue: U, currentValue: double,      index: int, array: FixedArray&lt;double&gt;) =&gt; U | Yes | A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. |
| initialValue | U | Yes | The initial value of the accumulator. |

**Return value:**

| Type | Description |
| --- | --- |
| U | The accumulated result. |


## reduceRight

```TypeScript
export function reduceRight(self: FixedArray<double>, callbackfn: (previousValue: double, currentValue: double, 
    index: int, array: FixedArray<double>) => double): double
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function reduceRight(self: FixedArray<double>, callbackfn: (previousValue: double, currentValue: double,     index: int, array: FixedArray<double>) => double): double--><!--Device-unnamed-export function reduceRight(self: FixedArray<double>, callbackfn: (previousValue: double, currentValue: double,     index: int, array: FixedArray<double>) => double): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | Yes | The array to reduce. |
| callbackfn | (previousValue: double, currentValue: double,      index: int, array: FixedArray&lt;double&gt;) =&gt; double | Yes | A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. |

**Return value:**

| Type | Description |
| --- | --- |
| double | A result after applying callbackfn over all elements of the Array. |


## reduceRight

```TypeScript
export function reduceRight<U>(self: FixedArray<char>, callbackfn: (previousValue: U, currentValue: char, index: int, 
    array: FixedArray<char>) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function reduceRight<U>(self: FixedArray<char>, callbackfn: (previousValue: U, currentValue: char, index: int,     array: FixedArray<char>) => U, initialValue: U): U--><!--Device-unnamed-export function reduceRight<U>(self: FixedArray<char>, callbackfn: (previousValue: U, currentValue: char, index: int,     array: FixedArray<char>) => U, initialValue: U): U-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | Yes | The array to operate `reduce` on. |
| callbackfn | (previousValue: U, currentValue: char, index: int,      array: FixedArray&lt;char&gt;) =&gt; U | Yes | A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. |
| initialValue | U | Yes | The initial value of the accumulator. |

**Return value:**

| Type | Description |
| --- | --- |
| U | The accumulated result. |


## reduceRight

```TypeScript
export function reduceRight(self: FixedArray<char>, callbackfn: (previousValue: char, currentValue: char, 
    index: int, array: FixedArray<char>) => char): char
```

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export function reduceRight(self: FixedArray<char>, callbackfn: (previousValue: char, currentValue: char,     index: int, array: FixedArray<char>) => char): char--><!--Device-unnamed-export function reduceRight(self: FixedArray<char>, callbackfn: (previousValue: char, currentValue: char,     index: int, array: FixedArray<char>) => char): char-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | Yes | The array to reduce. |
| callbackfn | (previousValue: char, currentValue: char,      index: int, array: FixedArray&lt;char&gt;) =&gt; char | Yes | A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the array. |

**Return value:**

| Type | Description |
| --- | --- |
| char | A result after applying callbackfn over all elements of the Array. |

