# reduce

## reduce

```TypeScript
export function reduce(self: FixedArray<boolean>, callbackfn: (previousValue: boolean, currentValue: boolean,
    index: int, array: FixedArray<boolean>) => boolean): boolean
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce(self: FixedArray<boolean>, callbackfn: (previousValue: boolean, currentValue: boolean,    index: int, array: FixedArray<boolean>) => boolean): boolean--><!--Device-unnamed-export function reduce(self: FixedArray<boolean>, callbackfn: (previousValue: boolean, currentValue: boolean,    index: int, array: FixedArray<boolean>) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | 是 | The array to operate `reduce` on. |
| callbackfn | (previousValue: boolean, currentValue: boolean,     index: int, array: FixedArray&lt;boolean&gt;) =&gt; boolean | 是 | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | The accumulated result. |


## reduce

```TypeScript
export function reduce<U=boolean>(self: FixedArray<boolean>, callbackfn: (previousValue: U,
    currentValue: boolean, index: int, array: FixedArray<boolean>) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce<U=boolean>(self: FixedArray<boolean>, callbackfn: (previousValue: U,    currentValue: boolean, index: int, array: FixedArray<boolean>) => U, initialValue: U): U--><!--Device-unnamed-export function reduce<U=boolean>(self: FixedArray<boolean>, callbackfn: (previousValue: U,    currentValue: boolean, index: int, array: FixedArray<boolean>) => U, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | 是 | The array to operate `reduce` on. |
| callbackfn | (previousValue: U,     currentValue: boolean, index: int, array: FixedArray&lt;boolean&gt;) =&gt; U | 是 | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array. |
| initialValue | U | 是 | The initial value of the accumulator. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | The accumulated result. |


## reduce

```TypeScript
export function reduce(self: FixedArray<byte>, callbackfn: (previousValue: byte, currentValue: byte, index: int, 
    array: FixedArray<byte>) => byte): byte
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce(self: FixedArray<byte>, callbackfn: (previousValue: byte, currentValue: byte, index: int,     array: FixedArray<byte>) => byte): byte--><!--Device-unnamed-export function reduce(self: FixedArray<byte>, callbackfn: (previousValue: byte, currentValue: byte, index: int,     array: FixedArray<byte>) => byte): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | 是 | The array to operate `reduce` on. |
| callbackfn | (previousValue: byte, currentValue: byte, index: int,      array: FixedArray&lt;byte&gt;) =&gt; byte | 是 | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | The accumulated result. |


## reduce

```TypeScript
export function reduce<U = byte>(self: FixedArray<byte>, callbackfn: (previousValue: U, currentValue: byte, 
    index: int, array: FixedArray<byte>) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce<U = byte>(self: FixedArray<byte>, callbackfn: (previousValue: U, currentValue: byte,     index: int, array: FixedArray<byte>) => U, initialValue: U): U--><!--Device-unnamed-export function reduce<U = byte>(self: FixedArray<byte>, callbackfn: (previousValue: U, currentValue: byte,     index: int, array: FixedArray<byte>) => U, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | 是 | The array to operate `reduce` on. |
| callbackfn | (previousValue: U, currentValue: byte,      index: int, array: FixedArray&lt;byte&gt;) =&gt; U | 是 | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array. |
| initialValue | U | 是 | The initial value of the accumulator. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | The accumulated result. |


## reduce

```TypeScript
export function reduce(self: FixedArray<short>, callbackfn: (previousValue: short, currentValue: short, index: int, 
    array: FixedArray<short>) => short): short
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce(self: FixedArray<short>, callbackfn: (previousValue: short, currentValue: short, index: int,     array: FixedArray<short>) => short): short--><!--Device-unnamed-export function reduce(self: FixedArray<short>, callbackfn: (previousValue: short, currentValue: short, index: int,     array: FixedArray<short>) => short): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | 是 | The array to operate `reduce` on. |
| callbackfn | (previousValue: short, currentValue: short, index: int,      array: FixedArray&lt;short&gt;) =&gt; short | 是 | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | The accumulated result. |


## reduce

```TypeScript
export function reduce<U = short>(self: FixedArray<short>, callbackfn: (previousValue: U, currentValue: short, index: 
    int, array: FixedArray<short>) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce<U = short>(self: FixedArray<short>, callbackfn: (previousValue: U, currentValue: short, index:     int, array: FixedArray<short>) => U, initialValue: U): U--><!--Device-unnamed-export function reduce<U = short>(self: FixedArray<short>, callbackfn: (previousValue: U, currentValue: short, index:     int, array: FixedArray<short>) => U, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | 是 | The array to operate `reduce` on. |
| callbackfn | (previousValue: U, currentValue: short, index:      int, array: FixedArray&lt;short&gt;) =&gt; U | 是 | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array. |
| initialValue | U | 是 | The initial value of the accumulator. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | The accumulated result. |


## reduce

```TypeScript
export function reduce(self: FixedArray<int>, callbackfn: (previousValue: int, currentValue: int, index: int, 
    array: FixedArray<int>) => int): int
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce(self: FixedArray<int>, callbackfn: (previousValue: int, currentValue: int, index: int,     array: FixedArray<int>) => int): int--><!--Device-unnamed-export function reduce(self: FixedArray<int>, callbackfn: (previousValue: int, currentValue: int, index: int,     array: FixedArray<int>) => int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | 是 | The array to operate `reduce` on. |
| callbackfn | (previousValue: int, currentValue: int, index: int,      array: FixedArray&lt;int&gt;) =&gt; int | 是 | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The accumulated result. |


## reduce

```TypeScript
export function reduce<U = int>(self: FixedArray<int>, callbackfn: (previousValue: U, currentValue: int, index: int, 
    array: FixedArray<int>) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce<U = int>(self: FixedArray<int>, callbackfn: (previousValue: U, currentValue: int, index: int,     array: FixedArray<int>) => U, initialValue: U): U--><!--Device-unnamed-export function reduce<U = int>(self: FixedArray<int>, callbackfn: (previousValue: U, currentValue: int, index: int,     array: FixedArray<int>) => U, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | 是 | The array to operate `reduce` on. |
| callbackfn | (previousValue: U, currentValue: int, index: int,      array: FixedArray&lt;int&gt;) =&gt; U | 是 | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array. |
| initialValue | U | 是 | The initial value of the accumulator. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | The accumulated result. |


## reduce

```TypeScript
export function reduce(self: FixedArray<long>, callbackfn: (previousValue: long, currentValue: long, index: int, 
    array: FixedArray<long>) => long): long
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce(self: FixedArray<long>, callbackfn: (previousValue: long, currentValue: long, index: int,     array: FixedArray<long>) => long): long--><!--Device-unnamed-export function reduce(self: FixedArray<long>, callbackfn: (previousValue: long, currentValue: long, index: int,     array: FixedArray<long>) => long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | 是 | The array to operate `reduce` on. |
| callbackfn | (previousValue: long, currentValue: long, index: int,      array: FixedArray&lt;long&gt;) =&gt; long | 是 | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The accumulated result. |


## reduce

```TypeScript
export function reduce<U = long>(self: FixedArray<long>, callbackfn: (previousValue: U, currentValue: long, 
    index: int, array: FixedArray<long>) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce<U = long>(self: FixedArray<long>, callbackfn: (previousValue: U, currentValue: long,     index: int, array: FixedArray<long>) => U, initialValue: U): U--><!--Device-unnamed-export function reduce<U = long>(self: FixedArray<long>, callbackfn: (previousValue: U, currentValue: long,     index: int, array: FixedArray<long>) => U, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | 是 | The array to operate `reduce` on. |
| callbackfn | (previousValue: U, currentValue: long,      index: int, array: FixedArray&lt;long&gt;) =&gt; U | 是 | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array. |
| initialValue | U | 是 | The initial value of the accumulator. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | The accumulated result. |


## reduce

```TypeScript
export function reduce(self: FixedArray<float>, callbackfn: (previousValue: float, currentValue: float, 
    index: int, array: FixedArray<float>) => float): float
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce(self: FixedArray<float>, callbackfn: (previousValue: float, currentValue: float,     index: int, array: FixedArray<float>) => float): float--><!--Device-unnamed-export function reduce(self: FixedArray<float>, callbackfn: (previousValue: float, currentValue: float,     index: int, array: FixedArray<float>) => float): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | 是 | The array to operate `reduce` on. |
| callbackfn | (previousValue: float, currentValue: float,      index: int, array: FixedArray&lt;float&gt;) =&gt; float | 是 | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | The accumulated result. |


## reduce

```TypeScript
export function reduce<U = float>(self: FixedArray<float>, callbackfn: (previousValue: U, currentValue: float, 
    index: int, array: FixedArray<float>) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce<U = float>(self: FixedArray<float>, callbackfn: (previousValue: U, currentValue: float,     index: int, array: FixedArray<float>) => U, initialValue: U): U--><!--Device-unnamed-export function reduce<U = float>(self: FixedArray<float>, callbackfn: (previousValue: U, currentValue: float,     index: int, array: FixedArray<float>) => U, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | 是 | The array to operate `reduce` on. |
| callbackfn | (previousValue: U, currentValue: float,      index: int, array: FixedArray&lt;float&gt;) =&gt; U | 是 | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array. |
| initialValue | U | 是 | The initial value of the accumulator. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | The accumulated result. |


## reduce

```TypeScript
export function reduce(self: FixedArray<double>, callbackfn: (previousValue: double, currentValue: double, 
    index: int, array: FixedArray<double>) => double): double
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce(self: FixedArray<double>, callbackfn: (previousValue: double, currentValue: double,     index: int, array: FixedArray<double>) => double): double--><!--Device-unnamed-export function reduce(self: FixedArray<double>, callbackfn: (previousValue: double, currentValue: double,     index: int, array: FixedArray<double>) => double): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | 是 | The array to operate `reduce` on. |
| callbackfn | (previousValue: double, currentValue: double,      index: int, array: FixedArray&lt;double&gt;) =&gt; double | 是 | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | The accumulated result. |


## reduce

```TypeScript
export function reduce<U = double>(self: FixedArray<double>, callbackfn: (previousValue: U, currentValue: double, 
    index: int, array: FixedArray<double>) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce<U = double>(self: FixedArray<double>, callbackfn: (previousValue: U, currentValue: double,     index: int, array: FixedArray<double>) => U, initialValue: U): U--><!--Device-unnamed-export function reduce<U = double>(self: FixedArray<double>, callbackfn: (previousValue: U, currentValue: double,     index: int, array: FixedArray<double>) => U, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | 是 | The array to operate `reduce` on. |
| callbackfn | (previousValue: U, currentValue: double,      index: int, array: FixedArray&lt;double&gt;) =&gt; U | 是 | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array. |
| initialValue | U | 是 | The initial value of the accumulator. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | The accumulated result. |


## reduce

```TypeScript
export function reduce(self: FixedArray<char>, callbackfn: (previousValue: char, currentValue: char, index: int, 
    array: FixedArray<char>) => char): char
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce(self: FixedArray<char>, callbackfn: (previousValue: char, currentValue: char, index: int,     array: FixedArray<char>) => char): char--><!--Device-unnamed-export function reduce(self: FixedArray<char>, callbackfn: (previousValue: char, currentValue: char, index: int,     array: FixedArray<char>) => char): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | 是 | The array to operate `reduce` on. |
| callbackfn | (previousValue: char, currentValue: char, index: int,      array: FixedArray&lt;char&gt;) =&gt; char | 是 | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | The accumulated result. |


## reduce

```TypeScript
export function reduce<U = char>(self: FixedArray<char>, callbackfn: (previousValue: U, currentValue: char, 
    index: int, array: FixedArray<char>) => U, initialValue: U): U
```

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce<U = char>(self: FixedArray<char>, callbackfn: (previousValue: U, currentValue: char,     index: int, array: FixedArray<char>) => U, initialValue: U): U--><!--Device-unnamed-export function reduce<U = char>(self: FixedArray<char>, callbackfn: (previousValue: U, currentValue: char,     index: int, array: FixedArray<char>) => U, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | 是 | The array to operate `reduce` on. |
| callbackfn | (previousValue: U, currentValue: char,      index: int, array: FixedArray&lt;char&gt;) =&gt; U | 是 | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array. |
| initialValue | U | 是 | The initial value of the accumulator. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | The accumulated result. |


## reduce

```TypeScript
export function reduce<U, T>(self: Array<U>, callbackfn: (previousValue: T, currentValue: U, index: int, 
    array: Array<U>) => T, initialValue: T): T
```

Calls the specified callback function for all the elements in an array. The return value of the callback function  is the accumulated result, and is provided as an argument in the next call to the callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce<U, T>(self: Array<U>, callbackfn: (previousValue: T, currentValue: U, index: int,     array: Array<U>) => T, initialValue: T): T--><!--Device-unnamed-export function reduce<U, T>(self: Array<U>, callbackfn: (previousValue: T, currentValue: U, index: int,     array: Array<U>) => T, initialValue: T): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | Array&lt;U&gt; | 是 |  |
| callbackfn | (previousValue: T, currentValue: U, index: int,      array: Array&lt;U&gt;) =&gt; T | 是 | A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array. |
| initialValue | T | 是 | If initialValue is specified, it is used as the initial value to start the accumulation. The first call to the callbackfn function provides this value as an argument instead of an array value. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | a result after applying callbackfn over all elements of the Array |

