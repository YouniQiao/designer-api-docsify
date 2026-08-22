# filter

## 导入模块

```TypeScript
```

## filter

```TypeScript
export function filter(self: FixedArray<boolean>, fn: (v: boolean, k: int, array: FixedArray<boolean>) => boolean): 
    FixedArray<boolean>
```

构造新的Array实例，并以给定数组中通过指定函数测试的 元素填充该实例， 即仅保留通过测试的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function filter(self: FixedArray<boolean>, fn: (v: boolean, k: int, array: FixedArray<boolean>) => boolean):     FixedArray<boolean>--><!--Device-unnamed-export function filter(self: FixedArray<boolean>, fn: (v: boolean, k: int, array: FixedArray<boolean>) => boolean):     FixedArray<boolean>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | 是 | 执行`filter`操作的数组。 |
| fn | (v: boolean, k: int, array: FixedArray&lt;boolean&gt;) =&gt; boolean | 是 | 测试函数，对数组中的每个元素调用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;boolean&gt; | 由`this`构造出的新Array实例，其中的元素 已使用测试函数`fn`筛选。 |


## filter

```TypeScript
export function filter(self: FixedArray<byte>, fn: (v: byte, k: int, array: FixedArray<byte>) => boolean): 
    FixedArray<byte>
```

构造新的`Array`实例，并以给定数组中 通过指定函数测试的元素 填充该实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function filter(self: FixedArray<byte>, fn: (v: byte, k: int, array: FixedArray<byte>) => boolean):     FixedArray<byte>--><!--Device-unnamed-export function filter(self: FixedArray<byte>, fn: (v: byte, k: int, array: FixedArray<byte>) => boolean):     FixedArray<byte>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | 是 |  |
| fn | (v: byte, k: int, array: FixedArray&lt;byte&gt;) =&gt; boolean | 是 | 测试函数，对数组中的每个元素调用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;byte&gt; | 由`this`构造出的新`Array`实例，其中的元素已 使用测试函数`fn`筛选。 |


## filter

```TypeScript
export function filter(self: FixedArray<short>, fn: (v: short, k: int, array: FixedArray<short>) => boolean): 
    FixedArray<short>
```

构造新的Array实例，并以给定数组中通过指定函数测试的 元素填充该实例， 即仅保留通过测试的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function filter(self: FixedArray<short>, fn: (v: short, k: int, array: FixedArray<short>) => boolean):     FixedArray<short>--><!--Device-unnamed-export function filter(self: FixedArray<short>, fn: (v: short, k: int, array: FixedArray<short>) => boolean):     FixedArray<short>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | 是 | 执行`filter`操作的数组。 |
| fn | (v: short, k: int, array: FixedArray&lt;short&gt;) =&gt; boolean | 是 | 测试函数，对数组中的每个元素调用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;short&gt; | 由`this`构造出的新Array实例，其中的元素 已使用测试函数`fn`筛选。 |


## filter

```TypeScript
export function filter(self: FixedArray<int>, fn: (v: int, k: int, array: FixedArray<int>) => boolean): 
    FixedArray<int>
```

构造新的Array实例，并以给定数组中通过指定函数测试的 元素填充该实例， 即仅保留通过测试的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function filter(self: FixedArray<int>, fn: (v: int, k: int, array: FixedArray<int>) => boolean):     FixedArray<int>--><!--Device-unnamed-export function filter(self: FixedArray<int>, fn: (v: int, k: int, array: FixedArray<int>) => boolean):     FixedArray<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | 是 | 执行`filter`操作的数组。 |
| fn | (v: int, k: int, array: FixedArray&lt;int&gt;) =&gt; boolean | 是 | 测试函数，对数组中的每个元素调用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;int&gt; | 由`this`构造出的新Array实例，其中的元素 已使用测试函数`fn`筛选。 |


## filter

```TypeScript
export function filter(self: FixedArray<long>, fn: (v: long, k: int, array: FixedArray<long>) => boolean): 
    FixedArray<long>
```

构造新的Array实例，并以给定数组中通过指定函数测试的 元素填充该实例， 即仅保留通过测试的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function filter(self: FixedArray<long>, fn: (v: long, k: int, array: FixedArray<long>) => boolean):     FixedArray<long>--><!--Device-unnamed-export function filter(self: FixedArray<long>, fn: (v: long, k: int, array: FixedArray<long>) => boolean):     FixedArray<long>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | 是 | 执行`filter`操作的数组。 |
| fn | (v: long, k: int, array: FixedArray&lt;long&gt;) =&gt; boolean | 是 | 测试函数，对数组中的每个元素调用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;long&gt; | 由`this`构造出的新Array实例，其中的元素 已使用测试函数`fn`筛选。 |


## filter

```TypeScript
export function filter(self: FixedArray<float>, fn: (v: float, k: int, array: FixedArray<float>) => boolean): 
    FixedArray<float>
```

构造新的Array实例，并以给定数组中通过指定函数测试的 元素填充该实例， 即仅保留通过测试的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function filter(self: FixedArray<float>, fn: (v: float, k: int, array: FixedArray<float>) => boolean):     FixedArray<float>--><!--Device-unnamed-export function filter(self: FixedArray<float>, fn: (v: float, k: int, array: FixedArray<float>) => boolean):     FixedArray<float>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | 是 | 执行`filter`操作的数组。 |
| fn | (v: float, k: int, array: FixedArray&lt;float&gt;) =&gt; boolean | 是 | 测试函数，对数组中的每个元素调用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;float&gt; | 由`this`构造出的新Array实例，其中的元素 已使用测试函数`fn`筛选。 |


## filter

```TypeScript
export function filter(self: FixedArray<double>, fn: (v: double, k: int, array: FixedArray<double>) => boolean): 
    FixedArray<double>
```

构造新的Array实例，并以给定数组中通过指定函数测试的 元素填充该实例， 即仅保留通过测试的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function filter(self: FixedArray<double>, fn: (v: double, k: int, array: FixedArray<double>) => boolean):     FixedArray<double>--><!--Device-unnamed-export function filter(self: FixedArray<double>, fn: (v: double, k: int, array: FixedArray<double>) => boolean):     FixedArray<double>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | 是 | 执行`filter`操作的数组。 |
| fn | (v: double, k: int, array: FixedArray&lt;double&gt;) =&gt; boolean | 是 | 测试函数，对数组中的每个元素调用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;double&gt; | 由`this`构造出的新Array实例，其中的元素 已使用测试函数`fn`筛选。 |


## filter

```TypeScript
export function filter(self: FixedArray<char>, fn: (v: char, k: int, array: FixedArray<char>) => boolean): 
    FixedArray<char>
```

构造新的Array实例，并以给定数组中通过指定函数测试的 元素填充该实例， 即仅保留通过测试的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function filter(self: FixedArray<char>, fn: (v: char, k: int, array: FixedArray<char>) => boolean):     FixedArray<char>--><!--Device-unnamed-export function filter(self: FixedArray<char>, fn: (v: char, k: int, array: FixedArray<char>) => boolean):     FixedArray<char>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | 是 | 执行`filter`操作的数组。 |
| fn | (v: char, k: int, array: FixedArray&lt;char&gt;) =&gt; boolean | 是 | 测试函数，对数组中的每个元素调用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;char&gt; | 由`this`构造出的新Array实例，其中的元素 已使用测试函数`fn`筛选。 |

