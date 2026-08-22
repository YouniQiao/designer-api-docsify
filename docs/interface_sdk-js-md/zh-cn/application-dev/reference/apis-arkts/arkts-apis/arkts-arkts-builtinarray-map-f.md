# map

## 导入模块

```TypeScript
```

## map

```TypeScript
export function map(self: FixedArray<boolean>, callbackfn: (value: boolean, index: int, array: FixedArray<boolean>) 
    => boolean): FixedArray<boolean>
```

对数组中的每个元素调用指定的回调函数，并返回包含各次调用结果的数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function map(self: FixedArray<boolean>, callbackfn: (value: boolean, index: int, array: FixedArray<boolean>)     => boolean): FixedArray<boolean>--><!--Device-unnamed-export function map(self: FixedArray<boolean>, callbackfn: (value: boolean, index: int, array: FixedArray<boolean>)     => boolean): FixedArray<boolean>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | 是 | 执行映射操作的数组。 |
| callbackfn | (value: boolean, index: int, array: FixedArray&lt;boolean&gt;)      =&gt; boolean | 是 | 最多接受三个参数的函数。map方法会对数组中的每个元素调用一次callbackfn 调用一次该函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;boolean&gt; | 由`this`与给定函数构造出的数组实例。 |


## map

```TypeScript
export function map(self: FixedArray<byte>, callbackfn: (value: byte, index: int, array: FixedArray<byte>) => byte): 
    FixedArray<byte>
```

对数组中的每个元素调用指定的回调函数，并返回包含各次调用结果的数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function map(self: FixedArray<byte>, callbackfn: (value: byte, index: int, array: FixedArray<byte>) => byte):     FixedArray<byte>--><!--Device-unnamed-export function map(self: FixedArray<byte>, callbackfn: (value: byte, index: int, array: FixedArray<byte>) => byte):     FixedArray<byte>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | 是 | 执行映射操作的数组。 |
| callbackfn | (value: byte, index: int, array: FixedArray&lt;byte&gt;) =&gt; byte | 是 | 最多接受三个参数的函数。map方法会对数组中的每个元素调用一次callbackfn 调用一次该函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;byte&gt; | 由`this`与给定函数构造出的数组实例。 |


## map

```TypeScript
export function map(self: FixedArray<short>, callbackfn: (value: short, index: int, array: FixedArray<short>) 
    => short): FixedArray<short>
```

对数组中的每个元素调用指定的回调函数，并返回包含各次调用结果的数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function map(self: FixedArray<short>, callbackfn: (value: short, index: int, array: FixedArray<short>)     => short): FixedArray<short>--><!--Device-unnamed-export function map(self: FixedArray<short>, callbackfn: (value: short, index: int, array: FixedArray<short>)     => short): FixedArray<short>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | 是 | 执行映射操作的数组。 |
| callbackfn | (value: short, index: int, array: FixedArray&lt;short&gt;)      =&gt; short | 是 | 最多接受三个参数的函数。map方法会对数组中的每个元素调用一次callbackfn 调用一次该函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;short&gt; | 由`this`与给定函数构造出的数组实例。 |


## map

```TypeScript
export function map(self: FixedArray<int>, callbackfn: (value: int, index: int, array: FixedArray<int>) => int): 
    FixedArray<int>
```

对数组中的每个元素调用指定的回调函数，并返回包含各次调用结果的数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function map(self: FixedArray<int>, callbackfn: (value: int, index: int, array: FixedArray<int>) => int):     FixedArray<int>--><!--Device-unnamed-export function map(self: FixedArray<int>, callbackfn: (value: int, index: int, array: FixedArray<int>) => int):     FixedArray<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | 是 | 执行映射操作的数组。 |
| callbackfn | (value: int, index: int, array: FixedArray&lt;int&gt;) =&gt; int | 是 | 最多接受三个参数的函数。map方法会对数组中的每个元素调用一次callbackfn 调用一次该函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;int&gt; | 由`this`与给定函数构造出的数组实例。 |


## map

```TypeScript
export function map(self: FixedArray<long>, callbackfn: (value: long, index: int, array: FixedArray<long>) => long): 
    FixedArray<long>
```

对数组中的每个元素调用指定的回调函数，并返回包含各次调用结果的数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function map(self: FixedArray<long>, callbackfn: (value: long, index: int, array: FixedArray<long>) => long):     FixedArray<long>--><!--Device-unnamed-export function map(self: FixedArray<long>, callbackfn: (value: long, index: int, array: FixedArray<long>) => long):     FixedArray<long>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | 是 | 执行映射操作的数组。 |
| callbackfn | (value: long, index: int, array: FixedArray&lt;long&gt;) =&gt; long | 是 | 最多接受三个参数的函数。map方法会对数组中的每个元素调用一次callbackfn 调用一次该函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;long&gt; | 由`this`与给定函数构造出的数组实例。 |


## map

```TypeScript
export function map(self: FixedArray<float>, callbackfn: (value: float, index: int, array: FixedArray<float>) 
    => float): FixedArray<float>
```

对数组中的每个元素调用指定的回调函数，并返回包含各次调用结果的数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function map(self: FixedArray<float>, callbackfn: (value: float, index: int, array: FixedArray<float>)     => float): FixedArray<float>--><!--Device-unnamed-export function map(self: FixedArray<float>, callbackfn: (value: float, index: int, array: FixedArray<float>)     => float): FixedArray<float>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | 是 | 执行映射操作的数组。 |
| callbackfn | (value: float, index: int, array: FixedArray&lt;float&gt;)      =&gt; float | 是 | 最多接受三个参数的函数。map方法会对数组中的每个元素调用一次callbackfn 调用一次该函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;float&gt; | 由`this`与给定函数构造出的数组实例。 |


## map

```TypeScript
export function map(self: FixedArray<double>, callbackfn: (value: double, index: int, array: FixedArray<double>) 
    => double): FixedArray<double>
```

对数组中的每个元素调用指定的回调函数，并返回包含各次调用结果的数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function map(self: FixedArray<double>, callbackfn: (value: double, index: int, array: FixedArray<double>)     => double): FixedArray<double>--><!--Device-unnamed-export function map(self: FixedArray<double>, callbackfn: (value: double, index: int, array: FixedArray<double>)     => double): FixedArray<double>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | 是 | 执行映射操作的数组。 |
| callbackfn | (value: double, index: int, array: FixedArray&lt;double&gt;)      =&gt; double | 是 | 最多接受三个参数的函数。map方法会对数组中的每个元素调用一次callbackfn 调用一次该函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;double&gt; | 由`this`与给定函数构造出的数组实例。 |


## map

```TypeScript
export function map(self: FixedArray<char>, callbackfn: (value: char, index: int, array: FixedArray<char>) => char): 
    FixedArray<char>
```

对数组中的每个元素调用指定的回调函数，并返回包含各次调用结果的数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function map(self: FixedArray<char>, callbackfn: (value: char, index: int, array: FixedArray<char>) => char):     FixedArray<char>--><!--Device-unnamed-export function map(self: FixedArray<char>, callbackfn: (value: char, index: int, array: FixedArray<char>) => char):     FixedArray<char>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | 是 | 执行映射操作的数组。 |
| callbackfn | (value: char, index: int, array: FixedArray&lt;char&gt;) =&gt; char | 是 | 最多接受三个参数的函数。map方法会对数组中的每个元素调用一次callbackfn 调用一次该函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;char&gt; | 由`this`与给定函数构造出的数组实例。 |

