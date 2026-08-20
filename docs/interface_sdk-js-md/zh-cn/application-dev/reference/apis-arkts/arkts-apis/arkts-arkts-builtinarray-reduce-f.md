# reduce

## 导入模块

```TypeScript
```

## reduce

```TypeScript
export function reduce(self: FixedArray<boolean>, callbackfn: (previousValue: boolean, currentValue: boolean,
    index: int, array: FixedArray<boolean>) => boolean): boolean
```

对数组中的所有元素调用指定的回调函数。回调函数的返回值 即为累加结果，并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce(self: FixedArray<boolean>, callbackfn: (previousValue: boolean, currentValue: boolean,    index: int, array: FixedArray<boolean>) => boolean): boolean--><!--Device-unnamed-export function reduce(self: FixedArray<boolean>, callbackfn: (previousValue: boolean, currentValue: boolean,    index: int, array: FixedArray<boolean>) => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | 是 | 执行`reduce`操作的数组。 |
| callbackfn | (previousValue: boolean, currentValue: boolean,     index: int, array: FixedArray&lt;boolean&gt;) =&gt; boolean | 是 | 最多接受四个参数的函数。reduce方法会对稀疏数组中的每个元素 调用一次callbackfn函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 累加得到的结果。 |


## reduce

```TypeScript
export function reduce<U=boolean>(self: FixedArray<boolean>, callbackfn: (previousValue: U,
    currentValue: boolean, index: int, array: FixedArray<boolean>) => U, initialValue: U): U
```

对数组中的所有元素调用指定的回调函数。回调函数的返回值 即为累加结果，并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce<U=boolean>(self: FixedArray<boolean>, callbackfn: (previousValue: U,    currentValue: boolean, index: int, array: FixedArray<boolean>) => U, initialValue: U): U--><!--Device-unnamed-export function reduce<U=boolean>(self: FixedArray<boolean>, callbackfn: (previousValue: U,    currentValue: boolean, index: int, array: FixedArray<boolean>) => U, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | 是 | 执行`reduce`操作的数组。 |
| callbackfn | (previousValue: U,     currentValue: boolean, index: int, array: FixedArray&lt;boolean&gt;) =&gt; U | 是 | 最多接受四个参数的函数。reduce方法会对稀疏数组中的每个元素 调用一次callbackfn函数。 |
| initialValue | U | 是 | 累加器的初始值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | 累加得到的结果。 |


## reduce

```TypeScript
export function reduce(self: FixedArray<byte>, callbackfn: (previousValue: byte, currentValue: byte, index: int, 
    array: FixedArray<byte>) => byte): byte
```

对数组中的所有元素调用指定的回调函数。回调函数的返回值 即为累加结果，并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce(self: FixedArray<byte>, callbackfn: (previousValue: byte, currentValue: byte, index: int,     array: FixedArray<byte>) => byte): byte--><!--Device-unnamed-export function reduce(self: FixedArray<byte>, callbackfn: (previousValue: byte, currentValue: byte, index: int,     array: FixedArray<byte>) => byte): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | 是 | 执行`reduce`操作的数组。 |
| callbackfn | (previousValue: byte, currentValue: byte, index: int,      array: FixedArray&lt;byte&gt;) =&gt; byte | 是 | 最多接受四个参数的函数。reduce方法会对稀疏数组中的每个元素 调用一次callbackfn函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | 累加得到的结果。 |


## reduce

```TypeScript
export function reduce<U = byte>(self: FixedArray<byte>, callbackfn: (previousValue: U, currentValue: byte, 
    index: int, array: FixedArray<byte>) => U, initialValue: U): U
```

对数组中的所有元素调用指定的回调函数。回调函数的返回值 即为累加结果，并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce<U = byte>(self: FixedArray<byte>, callbackfn: (previousValue: U, currentValue: byte,     index: int, array: FixedArray<byte>) => U, initialValue: U): U--><!--Device-unnamed-export function reduce<U = byte>(self: FixedArray<byte>, callbackfn: (previousValue: U, currentValue: byte,     index: int, array: FixedArray<byte>) => U, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | 是 | 执行`reduce`操作的数组。 |
| callbackfn | (previousValue: U, currentValue: byte,      index: int, array: FixedArray&lt;byte&gt;) =&gt; U | 是 | 最多接受四个参数的函数。reduce方法会对稀疏数组中的每个元素 调用一次callbackfn函数。 |
| initialValue | U | 是 | 累加器的初始值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | 累加得到的结果。 |


## reduce

```TypeScript
export function reduce(self: FixedArray<short>, callbackfn: (previousValue: short, currentValue: short, index: int, 
    array: FixedArray<short>) => short): short
```

对数组中的所有元素调用指定的回调函数。回调函数的返回值 即为累加结果，并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce(self: FixedArray<short>, callbackfn: (previousValue: short, currentValue: short, index: int,     array: FixedArray<short>) => short): short--><!--Device-unnamed-export function reduce(self: FixedArray<short>, callbackfn: (previousValue: short, currentValue: short, index: int,     array: FixedArray<short>) => short): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | 是 | 执行`reduce`操作的数组。 |
| callbackfn | (previousValue: short, currentValue: short, index: int,      array: FixedArray&lt;short&gt;) =&gt; short | 是 | 最多接受四个参数的函数。reduce方法会对稀疏数组中的每个元素 调用一次callbackfn函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | 累加得到的结果。 |


## reduce

```TypeScript
export function reduce<U = short>(self: FixedArray<short>, callbackfn: (previousValue: U, currentValue: short, index: 
    int, array: FixedArray<short>) => U, initialValue: U): U
```

对数组中的所有元素调用指定的回调函数。回调函数的返回值 即为累加结果，并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce<U = short>(self: FixedArray<short>, callbackfn: (previousValue: U, currentValue: short, index:     int, array: FixedArray<short>) => U, initialValue: U): U--><!--Device-unnamed-export function reduce<U = short>(self: FixedArray<short>, callbackfn: (previousValue: U, currentValue: short, index:     int, array: FixedArray<short>) => U, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | 是 | 执行`reduce`操作的数组。 |
| callbackfn | (previousValue: U, currentValue: short, index:      int, array: FixedArray&lt;short&gt;) =&gt; U | 是 | 最多接受四个参数的函数。reduce方法会对稀疏数组中的每个元素 调用一次callbackfn函数。 |
| initialValue | U | 是 | 累加器的初始值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | 累加得到的结果。 |


## reduce

```TypeScript
export function reduce(self: FixedArray<int>, callbackfn: (previousValue: int, currentValue: int, index: int, 
    array: FixedArray<int>) => int): int
```

对数组中的所有元素调用指定的回调函数。回调函数的返回值 即为累加结果，并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce(self: FixedArray<int>, callbackfn: (previousValue: int, currentValue: int, index: int,     array: FixedArray<int>) => int): int--><!--Device-unnamed-export function reduce(self: FixedArray<int>, callbackfn: (previousValue: int, currentValue: int, index: int,     array: FixedArray<int>) => int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | 是 | 执行`reduce`操作的数组。 |
| callbackfn | (previousValue: int, currentValue: int, index: int,      array: FixedArray&lt;int&gt;) =&gt; int | 是 | 最多接受四个参数的函数。reduce方法会对稀疏数组中的每个元素 调用一次callbackfn函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 累加得到的结果。 |


## reduce

```TypeScript
export function reduce<U = int>(self: FixedArray<int>, callbackfn: (previousValue: U, currentValue: int, index: int, 
    array: FixedArray<int>) => U, initialValue: U): U
```

对数组中的所有元素调用指定的回调函数。回调函数的返回值 即为累加结果，并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce<U = int>(self: FixedArray<int>, callbackfn: (previousValue: U, currentValue: int, index: int,     array: FixedArray<int>) => U, initialValue: U): U--><!--Device-unnamed-export function reduce<U = int>(self: FixedArray<int>, callbackfn: (previousValue: U, currentValue: int, index: int,     array: FixedArray<int>) => U, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | 是 | 执行`reduce`操作的数组。 |
| callbackfn | (previousValue: U, currentValue: int, index: int,      array: FixedArray&lt;int&gt;) =&gt; U | 是 | 最多接受四个参数的函数。reduce方法会对稀疏数组中的每个元素 调用一次callbackfn函数。 |
| initialValue | U | 是 | 累加器的初始值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | 累加得到的结果。 |


## reduce

```TypeScript
export function reduce(self: FixedArray<long>, callbackfn: (previousValue: long, currentValue: long, index: int, 
    array: FixedArray<long>) => long): long
```

对数组中的所有元素调用指定的回调函数。回调函数的返回值 即为累加结果，并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce(self: FixedArray<long>, callbackfn: (previousValue: long, currentValue: long, index: int,     array: FixedArray<long>) => long): long--><!--Device-unnamed-export function reduce(self: FixedArray<long>, callbackfn: (previousValue: long, currentValue: long, index: int,     array: FixedArray<long>) => long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | 是 | 执行`reduce`操作的数组。 |
| callbackfn | (previousValue: long, currentValue: long, index: int,      array: FixedArray&lt;long&gt;) =&gt; long | 是 | 最多接受四个参数的函数。reduce方法会对稀疏数组中的每个元素 调用一次callbackfn函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 累加得到的结果。 |


## reduce

```TypeScript
export function reduce<U = long>(self: FixedArray<long>, callbackfn: (previousValue: U, currentValue: long, 
    index: int, array: FixedArray<long>) => U, initialValue: U): U
```

对数组中的所有元素调用指定的回调函数。回调函数的返回值 即为累加结果，并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce<U = long>(self: FixedArray<long>, callbackfn: (previousValue: U, currentValue: long,     index: int, array: FixedArray<long>) => U, initialValue: U): U--><!--Device-unnamed-export function reduce<U = long>(self: FixedArray<long>, callbackfn: (previousValue: U, currentValue: long,     index: int, array: FixedArray<long>) => U, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | 是 | 执行`reduce`操作的数组。 |
| callbackfn | (previousValue: U, currentValue: long,      index: int, array: FixedArray&lt;long&gt;) =&gt; U | 是 | 最多接受四个参数的函数。reduce方法会对稀疏数组中的每个元素 调用一次callbackfn函数。 |
| initialValue | U | 是 | 累加器的初始值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | 累加得到的结果。 |


## reduce

```TypeScript
export function reduce(self: FixedArray<float>, callbackfn: (previousValue: float, currentValue: float, 
    index: int, array: FixedArray<float>) => float): float
```

对数组中的所有元素调用指定的回调函数。回调函数的返回值 即为累加结果，并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce(self: FixedArray<float>, callbackfn: (previousValue: float, currentValue: float,     index: int, array: FixedArray<float>) => float): float--><!--Device-unnamed-export function reduce(self: FixedArray<float>, callbackfn: (previousValue: float, currentValue: float,     index: int, array: FixedArray<float>) => float): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | 是 | 执行`reduce`操作的数组。 |
| callbackfn | (previousValue: float, currentValue: float,      index: int, array: FixedArray&lt;float&gt;) =&gt; float | 是 | 最多接受四个参数的函数。reduce方法会对稀疏数组中的每个元素 调用一次callbackfn函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | 累加得到的结果。 |


## reduce

```TypeScript
export function reduce<U = float>(self: FixedArray<float>, callbackfn: (previousValue: U, currentValue: float, 
    index: int, array: FixedArray<float>) => U, initialValue: U): U
```

对数组中的所有元素调用指定的回调函数。回调函数的返回值 即为累加结果，并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce<U = float>(self: FixedArray<float>, callbackfn: (previousValue: U, currentValue: float,     index: int, array: FixedArray<float>) => U, initialValue: U): U--><!--Device-unnamed-export function reduce<U = float>(self: FixedArray<float>, callbackfn: (previousValue: U, currentValue: float,     index: int, array: FixedArray<float>) => U, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | 是 | 执行`reduce`操作的数组。 |
| callbackfn | (previousValue: U, currentValue: float,      index: int, array: FixedArray&lt;float&gt;) =&gt; U | 是 | 最多接受四个参数的函数。reduce方法会对稀疏数组中的每个元素 调用一次callbackfn函数。 |
| initialValue | U | 是 | 累加器的初始值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | 累加得到的结果。 |


## reduce

```TypeScript
export function reduce(self: FixedArray<double>, callbackfn: (previousValue: double, currentValue: double, 
    index: int, array: FixedArray<double>) => double): double
```

对数组中的所有元素调用指定的回调函数。回调函数的返回值 即为累加结果，并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce(self: FixedArray<double>, callbackfn: (previousValue: double, currentValue: double,     index: int, array: FixedArray<double>) => double): double--><!--Device-unnamed-export function reduce(self: FixedArray<double>, callbackfn: (previousValue: double, currentValue: double,     index: int, array: FixedArray<double>) => double): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | 是 | 执行`reduce`操作的数组。 |
| callbackfn | (previousValue: double, currentValue: double,      index: int, array: FixedArray&lt;double&gt;) =&gt; double | 是 | 最多接受四个参数的函数。reduce方法会对稀疏数组中的每个元素 调用一次callbackfn函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 累加得到的结果。 |


## reduce

```TypeScript
export function reduce<U = double>(self: FixedArray<double>, callbackfn: (previousValue: U, currentValue: double, 
    index: int, array: FixedArray<double>) => U, initialValue: U): U
```

对数组中的所有元素调用指定的回调函数。回调函数的返回值 即为累加结果，并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce<U = double>(self: FixedArray<double>, callbackfn: (previousValue: U, currentValue: double,     index: int, array: FixedArray<double>) => U, initialValue: U): U--><!--Device-unnamed-export function reduce<U = double>(self: FixedArray<double>, callbackfn: (previousValue: U, currentValue: double,     index: int, array: FixedArray<double>) => U, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | 是 | 执行`reduce`操作的数组。 |
| callbackfn | (previousValue: U, currentValue: double,      index: int, array: FixedArray&lt;double&gt;) =&gt; U | 是 | 最多接受四个参数的函数。reduce方法会对稀疏数组中的每个元素 调用一次callbackfn函数。 |
| initialValue | U | 是 | 累加器的初始值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | 累加得到的结果。 |


## reduce

```TypeScript
export function reduce(self: FixedArray<char>, callbackfn: (previousValue: char, currentValue: char, index: int, 
    array: FixedArray<char>) => char): char
```

对数组中的所有元素调用指定的回调函数。回调函数的返回值 即为累加结果，并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce(self: FixedArray<char>, callbackfn: (previousValue: char, currentValue: char, index: int,     array: FixedArray<char>) => char): char--><!--Device-unnamed-export function reduce(self: FixedArray<char>, callbackfn: (previousValue: char, currentValue: char, index: int,     array: FixedArray<char>) => char): char-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | 是 | 执行`reduce`操作的数组。 |
| callbackfn | (previousValue: char, currentValue: char, index: int,      array: FixedArray&lt;char&gt;) =&gt; char | 是 | 最多接受四个参数的函数。reduce方法会对稀疏数组中的每个元素 调用一次callbackfn函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| char | 累加得到的结果。 |


## reduce

```TypeScript
export function reduce<U = char>(self: FixedArray<char>, callbackfn: (previousValue: U, currentValue: char, 
    index: int, array: FixedArray<char>) => U, initialValue: U): U
```

对数组中的所有元素调用指定的回调函数。回调函数的返回值 即为累加结果，并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce<U = char>(self: FixedArray<char>, callbackfn: (previousValue: U, currentValue: char,     index: int, array: FixedArray<char>) => U, initialValue: U): U--><!--Device-unnamed-export function reduce<U = char>(self: FixedArray<char>, callbackfn: (previousValue: U, currentValue: char,     index: int, array: FixedArray<char>) => U, initialValue: U): U-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | 是 | 执行`reduce`操作的数组。 |
| callbackfn | (previousValue: U, currentValue: char,      index: int, array: FixedArray&lt;char&gt;) =&gt; U | 是 | 最多接受四个参数的函数。reduce方法会对稀疏数组中的每个元素 调用一次callbackfn函数。 |
| initialValue | U | 是 | 累加器的初始值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | 累加得到的结果。 |


## reduce

```TypeScript
export function reduce<U, T>(self: Array<U>, callbackfn: (previousValue: T, currentValue: U, index: int, 
    array: Array<U>) => T, initialValue: T): T
```

对数组中的所有元素调用指定的回调函数。回调函数的返回值 即为累加结果，并作为参数传入下一次回调调用。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function reduce<U, T>(self: Array<U>, callbackfn: (previousValue: T, currentValue: U, index: int,     array: Array<U>) => T, initialValue: T): T--><!--Device-unnamed-export function reduce<U, T>(self: Array<U>, callbackfn: (previousValue: T, currentValue: U, index: int,     array: Array<U>) => T, initialValue: T): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | Array&lt;U&gt; | 是 |  |
| callbackfn | (previousValue: T, currentValue: U, index: int,      array: Array&lt;U&gt;) =&gt; T | 是 | 最多接受四个参数的函数。 reduce方法会对数组中的每个元素调用一次callbackfn函数。 |
| initialValue | T | 是 | 如果指定了initialValue，则将其作为累加的初始值。 首次调用callbackfn时，将该值而非数组元素作为参数传入。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 对数组所有元素应用callbackfn后得到的结果。 |

