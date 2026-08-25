# reduceRight

## 导入模块

```TypeScript
```

## reduceRight

```TypeScript
export function reduceRight<U>(self: FixedArray<boolean>, callbackfn: (previousValue: U, currentValue: boolean, 
    index: int, array: FixedArray<boolean>) => U, initialValue: U): U
```

按降序对数组中的所有元素调用指定的回调函数。回调函数的 返回值即为累加结果，并作为参数传入下一次回调调用的 函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;boolean & gt; | 是 |
| callbackfn | (previousValue: U, currentValue: boolean,      index: int, array: FixedArray & lt;boolean & gt;) = & gt; U | 是 |
| initialValue | U | 是 |

**返回值：**

| 类型 |
| --- |
| U |


## reduceRight

```TypeScript
export function reduceRight(self: FixedArray<boolean>, callbackfn: (previousValue: boolean, currentValue: boolean, 
    index: int, array: FixedArray<boolean>) => boolean): boolean
```

按降序对数组中的所有元素调用指定的回调函数。回调函数的 返回值即为累加结果，并作为参数传入下一次回调调用的 函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;boolean & gt; | 是 |
| callbackfn | (previousValue: boolean, currentValue: boolean,      index: int, array: FixedArray & lt;boolean & gt;) = & gt; boolean | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |


## reduceRight

```TypeScript
export function reduceRight<U>(self: FixedArray<byte>, callbackfn: (previousValue: U, currentValue: byte, index: int, 
    array: FixedArray<byte>) => U, initialValue: U): U
```

按降序对数组中的所有元素调用指定的回调函数。回调函数的 返回值即为累加结果，并作为参数传入下一次回调调用的 函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;byte & gt; | 是 |
| callbackfn | (previousValue: U, currentValue: byte, index: int,      array: FixedArray & lt;byte & gt;) = & gt; U | 是 |
| initialValue | U | 是 |

**返回值：**

| 类型 |
| --- |
| U |


## reduceRight

```TypeScript
export function reduceRight(self: FixedArray<byte>, callbackfn: (previousValue: byte, currentValue: byte, index: int, 
    array: FixedArray<byte>) => byte): byte
```

按降序对数组中的所有元素调用指定的回调函数。回调函数的 返回值即为累加结果，并作为参数传入下一次回调调用的 函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;byte & gt; | 是 |
| callbackfn | (previousValue: byte, currentValue: byte, index: int,      array: FixedArray & lt;byte & gt;) = & gt; byte | 是 |

**返回值：**

| 类型 |
| --- |
| byte |


## reduceRight

```TypeScript
export function reduceRight<U>(self: FixedArray<short>, callbackfn: (previousValue: U, currentValue: short, 
    index: int, array: FixedArray<short>) => U, initialValue: U): U
```

按降序对数组中的所有元素调用指定的回调函数。回调函数的 返回值即为累加结果，并作为参数传入下一次回调调用的 函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;short & gt; | 是 |
| callbackfn | (previousValue: U, currentValue: short,      index: int, array: FixedArray & lt;short & gt;) = & gt; U | 是 |
| initialValue | U | 是 |

**返回值：**

| 类型 |
| --- |
| U |


## reduceRight

```TypeScript
export function reduceRight(self: FixedArray<short>, callbackfn: (previousValue: short, currentValue: short, 
    index: int, array: FixedArray<short>) => short): short
```

按降序对数组中的所有元素调用指定的回调函数。回调函数的 返回值即为累加结果，并作为参数传入下一次回调调用的 函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;short & gt; | 是 |
| callbackfn | (previousValue: short, currentValue: short,      index: int, array: FixedArray & lt;short & gt;) = & gt; short | 是 |

**返回值：**

| 类型 |
| --- |
| short |


## reduceRight

```TypeScript
export function reduceRight<U>(self: FixedArray<int>, callbackfn: (previousValue: U, currentValue: int, index: int, 
    array: FixedArray<int>) => U, initialValue: U): U
```

按降序对数组中的所有元素调用指定的回调函数。回调函数的 返回值即为累加结果，并作为参数传入下一次回调调用的 函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;int & gt; | 是 |
| callbackfn | (previousValue: U, currentValue: int, index: int,      array: FixedArray & lt;int & gt;) = & gt; U | 是 |
| initialValue | U | 是 |

**返回值：**

| 类型 |
| --- |
| U |


## reduceRight

```TypeScript
export function reduceRight(self: FixedArray<int>, callbackfn: (previousValue: int, currentValue: int, 
    index: int, array: FixedArray<int>) => int): int
```

按降序对数组中的所有元素调用指定的回调函数。回调函数的 返回值即为累加结果，并作为参数传入下一次回调调用的 函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;int & gt; | 是 |
| callbackfn | (previousValue: int, currentValue: int,      index: int, array: FixedArray & lt;int & gt;) = & gt; int | 是 |

**返回值：**

| 类型 |
| --- |
| int |


## reduceRight

```TypeScript
export function reduceRight<U>(self: FixedArray<long>, callbackfn: (previousValue: U, currentValue: long, index: int, 
    array: FixedArray<long>) => U, initialValue: U): U
```

按降序对数组中的所有元素调用指定的回调函数。回调函数的 返回值即为累加结果，并作为参数传入下一次回调调用的 函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;long & gt; | 是 |
| callbackfn | (previousValue: U, currentValue: long, index: int,      array: FixedArray & lt;long & gt;) = & gt; U | 是 |
| initialValue | U | 是 |

**返回值：**

| 类型 |
| --- |
| U |


## reduceRight

```TypeScript
export function reduceRight(self: FixedArray<long>, callbackfn: (previousValue: long, currentValue: long, index: int, 
    array: FixedArray<long>) => long): long
```

按降序对数组中的所有元素调用指定的回调函数。回调函数的 返回值即为累加结果，并作为参数传入下一次回调调用的 函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;long & gt; | 是 |
| callbackfn | (previousValue: long, currentValue: long, index: int,      array: FixedArray & lt;long & gt;) = & gt; long | 是 |

**返回值：**

| 类型 |
| --- |
| long |


## reduceRight

```TypeScript
export function reduceRight<U>(self: FixedArray<float>, callbackfn: (previousValue: U, currentValue: float, 
    index: int, array: FixedArray<float>) => U, initialValue: U): U
```

按降序对数组中的所有元素调用指定的回调函数。回调函数的 返回值即为累加结果，并作为参数传入下一次回调调用的 函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;float & gt; | 是 |
| callbackfn | (previousValue: U, currentValue: float,      index: int, array: FixedArray & lt;float & gt;) = & gt; U | 是 |
| initialValue | U | 是 |

**返回值：**

| 类型 |
| --- |
| U |


## reduceRight

```TypeScript
export function reduceRight(self: FixedArray<float>, callbackfn: (previousValue: float, currentValue: float, 
    index: int, array: FixedArray<float>) => float): float
```

按降序对数组中的所有元素调用指定的回调函数。回调函数的 返回值即为累加结果，并作为参数传入下一次回调调用的 函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;float & gt; | 是 |
| callbackfn | (previousValue: float, currentValue: float,      index: int, array: FixedArray & lt;float & gt;) = & gt; float | 是 |

**返回值：**

| 类型 |
| --- |
| float |


## reduceRight

```TypeScript
export function reduceRight<U>(self: FixedArray<double>, callbackfn: (previousValue: U, currentValue: double, 
    index: int, array: FixedArray<double>) => U, initialValue: U): U
```

按降序对数组中的所有元素调用指定的回调函数。回调函数的 返回值即为累加结果，并作为参数传入下一次回调调用的 函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;double & gt; | 是 |
| callbackfn | (previousValue: U, currentValue: double,      index: int, array: FixedArray & lt;double & gt;) = & gt; U | 是 |
| initialValue | U | 是 |

**返回值：**

| 类型 |
| --- |
| U |


## reduceRight

```TypeScript
export function reduceRight(self: FixedArray<double>, callbackfn: (previousValue: double, currentValue: double, 
    index: int, array: FixedArray<double>) => double): double
```

按降序对数组中的所有元素调用指定的回调函数。回调函数的 返回值即为累加结果，并作为参数传入下一次回调调用的 函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;double & gt; | 是 |
| callbackfn | (previousValue: double, currentValue: double,      index: int, array: FixedArray & lt;double & gt;) = & gt; double | 是 |

**返回值：**

| 类型 |
| --- |
| double |


## reduceRight

```TypeScript
export function reduceRight<U>(self: FixedArray<char>, callbackfn: (previousValue: U, currentValue: char, index: int, 
    array: FixedArray<char>) => U, initialValue: U): U
```

按降序对数组中的所有元素调用指定的回调函数。回调函数的 返回值即为累加结果，并作为参数传入下一次回调调用的 函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;char & gt; | 是 |
| callbackfn | (previousValue: U, currentValue: char, index: int,      array: FixedArray & lt;char & gt;) = & gt; U | 是 |
| initialValue | U | 是 |

**返回值：**

| 类型 |
| --- |
| U |


## reduceRight

```TypeScript
export function reduceRight(self: FixedArray<char>, callbackfn: (previousValue: char, currentValue: char, 
    index: int, array: FixedArray<char>) => char): char
```

按降序对数组中的所有元素调用指定的回调函数。回调函数的 返回值即为累加结果，并作为参数传入下一次回调调用的 函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| self | FixedArray & lt;char & gt; | 是 |
| callbackfn | (previousValue: char, currentValue: char,      index: int, array: FixedArray & lt;char & gt;) = & gt; char | 是 |

**返回值：**

| 类型 |
| --- |
| char |
