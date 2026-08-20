# concat

## 导入模块

```TypeScript
```

## concat

```TypeScript
export function concat(self: FixedArray<boolean>, fst: FixedArray<boolean>, ...more: FixedArray<FixedArray<boolean>>): 
    FixedArray<boolean>
```

将参数中提供的数组依次连接，合并两个或多个数组 为一个新数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function concat(self: FixedArray<boolean>, fst: FixedArray<boolean>, ...more: FixedArray<FixedArray<boolean>>):     FixedArray<boolean>--><!--Device-unnamed-export function concat(self: FixedArray<boolean>, fst: FixedArray<boolean>, ...more: FixedArray<FixedArray<boolean>>):     FixedArray<boolean>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | 是 | 执行`concat`操作的数组。 |
| fst | FixedArray&lt;boolean&gt; | 是 | 待连接的第一个数组。 |
| more | FixedArray&lt;FixedArray&lt;boolean&gt;&gt; | 是 | 待连接的其他数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;boolean&gt; | 由这些数组连接而成的新数组。 |


## concat

```TypeScript
export function concat(self: FixedArray<boolean>, ...items: FixedArray<ConcatArray<boolean>>): FixedArray<boolean>
```

根据当前数组实例与给定的数组实例创建新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function concat(self: FixedArray<boolean>, ...items: FixedArray<ConcatArray<boolean>>): FixedArray<boolean>--><!--Device-unnamed-export function concat(self: FixedArray<boolean>, ...items: FixedArray<ConcatArray<boolean>>): FixedArray<boolean>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | 是 | 执行`concat`操作的数组。 |
| items | FixedArray&lt;ConcatArray&lt;boolean&gt;&gt; | 是 | 待连接为新数组的 其他数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;boolean&gt; | 由`this`与给定的Array类实例`items` 构造出的新Array实例。 |


## concat

```TypeScript
export function concat(self: FixedArray<byte>, fst: FixedArray<byte>, ...more: FixedArray<FixedArray<byte>>): 
    FixedArray<byte>
```

将参数中提供的数组依次连接，合并两个或多个数组 为一个新数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function concat(self: FixedArray<byte>, fst: FixedArray<byte>, ...more: FixedArray<FixedArray<byte>>):     FixedArray<byte>--><!--Device-unnamed-export function concat(self: FixedArray<byte>, fst: FixedArray<byte>, ...more: FixedArray<FixedArray<byte>>):     FixedArray<byte>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | 是 | 执行`concat`操作的数组。 |
| fst | FixedArray&lt;byte&gt; | 是 | 待连接的第一个数组。 |
| more | FixedArray&lt;FixedArray&lt;byte&gt;&gt; | 是 | 待连接的其他数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;byte&gt; | 由这些数组连接而成的新数组。 |


## concat

```TypeScript
export function concat(self: FixedArray<byte>, ...items: FixedArray<ConcatArray<byte>>): FixedArray<byte>
```

根据当前数组实例与给定的数组实例创建新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function concat(self: FixedArray<byte>, ...items: FixedArray<ConcatArray<byte>>): FixedArray<byte>--><!--Device-unnamed-export function concat(self: FixedArray<byte>, ...items: FixedArray<ConcatArray<byte>>): FixedArray<byte>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | 是 | 执行`concat`操作的数组。 |
| items | FixedArray&lt;ConcatArray&lt;byte&gt;&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;byte&gt; | 由`this`与给定的Array类实例`items`构造出的新Array实例。 |


## concat

```TypeScript
export function concat(self: FixedArray<short>, fst: FixedArray<short>, ...more: FixedArray<FixedArray<short>>): 
    FixedArray<short>
```

将参数中提供的数组依次连接，合并两个或多个数组 为一个新数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function concat(self: FixedArray<short>, fst: FixedArray<short>, ...more: FixedArray<FixedArray<short>>):     FixedArray<short>--><!--Device-unnamed-export function concat(self: FixedArray<short>, fst: FixedArray<short>, ...more: FixedArray<FixedArray<short>>):     FixedArray<short>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | 是 | 执行`concat`操作的数组。 |
| fst | FixedArray&lt;short&gt; | 是 | 待连接的第一个数组。 |
| more | FixedArray&lt;FixedArray&lt;short&gt;&gt; | 是 | 待连接的其他数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;short&gt; | 由这些数组连接而成的新数组。 |


## concat

```TypeScript
export function concat(self: FixedArray<short>, ...items: FixedArray<ConcatArray<short>>): FixedArray<short>
```

根据当前数组实例与给定的数组实例创建新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function concat(self: FixedArray<short>, ...items: FixedArray<ConcatArray<short>>): FixedArray<short>--><!--Device-unnamed-export function concat(self: FixedArray<short>, ...items: FixedArray<ConcatArray<short>>): FixedArray<short>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | 是 | 执行`concat`操作的数组。 |
| items | FixedArray&lt;ConcatArray&lt;short&gt;&gt; | 是 | 待连接为新数组的 其他数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;short&gt; | 由`this`与给定的Array类实例`items` 构造出的新Array实例。 |


## concat

```TypeScript
export function concat(self: FixedArray<int>, fst: FixedArray<int>, ...more: FixedArray<FixedArray<int>>): 
    FixedArray<int>
```

将参数中提供的数组依次连接，合并两个或多个数组 为一个新数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function concat(self: FixedArray<int>, fst: FixedArray<int>, ...more: FixedArray<FixedArray<int>>):     FixedArray<int>--><!--Device-unnamed-export function concat(self: FixedArray<int>, fst: FixedArray<int>, ...more: FixedArray<FixedArray<int>>):     FixedArray<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | 是 | 执行`concat`操作的数组。 |
| fst | FixedArray&lt;int&gt; | 是 | 待连接的第一个数组。 |
| more | FixedArray&lt;FixedArray&lt;int&gt;&gt; | 是 | 待连接的其他数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;int&gt; | 由这些数组连接而成的新数组。 |


## concat

```TypeScript
export function concat(self: FixedArray<int>, ...items: FixedArray<ConcatArray<int>>): FixedArray<int>
```

根据当前数组实例与给定的数组实例创建新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function concat(self: FixedArray<int>, ...items: FixedArray<ConcatArray<int>>): FixedArray<int>--><!--Device-unnamed-export function concat(self: FixedArray<int>, ...items: FixedArray<ConcatArray<int>>): FixedArray<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | 是 | 执行`concat`操作的数组。 |
| items | FixedArray&lt;ConcatArray&lt;int&gt;&gt; | 是 | 待连接为新数组的 其他数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;int&gt; | 由`this`与给定的Array类实例`items` 构造出的新Array实例。 |


## concat

```TypeScript
export function concat(self: FixedArray<long>, fst: FixedArray<long>, ...more: FixedArray<FixedArray<long>>): 
    FixedArray<long>
```

将参数中提供的数组依次连接，合并两个或多个数组 为一个新数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function concat(self: FixedArray<long>, fst: FixedArray<long>, ...more: FixedArray<FixedArray<long>>):     FixedArray<long>--><!--Device-unnamed-export function concat(self: FixedArray<long>, fst: FixedArray<long>, ...more: FixedArray<FixedArray<long>>):     FixedArray<long>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | 是 | 执行`concat`操作的数组。 |
| fst | FixedArray&lt;long&gt; | 是 | 待连接的第一个数组。 |
| more | FixedArray&lt;FixedArray&lt;long&gt;&gt; | 是 | 待连接的其他数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;long&gt; | 由这些数组连接而成的新数组。 |


## concat

```TypeScript
export function concat(self: FixedArray<long>, ...items: FixedArray<ConcatArray<long>>): FixedArray<long>
```

根据当前数组实例与给定的数组实例创建新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function concat(self: FixedArray<long>, ...items: FixedArray<ConcatArray<long>>): FixedArray<long>--><!--Device-unnamed-export function concat(self: FixedArray<long>, ...items: FixedArray<ConcatArray<long>>): FixedArray<long>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | 是 | 执行`concat`操作的数组。 |
| items | FixedArray&lt;ConcatArray&lt;long&gt;&gt; | 是 | 待连接为新数组的 其他数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;long&gt; | 由`this`与给定的Array类实例`items` 构造出的新Array实例。 |


## concat

```TypeScript
export function concat(self: FixedArray<float>, fst: FixedArray<float>, ...more: FixedArray<FixedArray<float>>): 
    FixedArray<float>
```

将参数中提供的数组依次连接，合并两个或多个数组 为一个新数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function concat(self: FixedArray<float>, fst: FixedArray<float>, ...more: FixedArray<FixedArray<float>>):     FixedArray<float>--><!--Device-unnamed-export function concat(self: FixedArray<float>, fst: FixedArray<float>, ...more: FixedArray<FixedArray<float>>):     FixedArray<float>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | 是 | 执行`concat`操作的数组。 |
| fst | FixedArray&lt;float&gt; | 是 | 待连接的第一个数组。 |
| more | FixedArray&lt;FixedArray&lt;float&gt;&gt; | 是 | 待连接的其他数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;float&gt; | 由这些数组连接而成的新数组。 |


## concat

```TypeScript
export function concat(self: FixedArray<float>, ...items: FixedArray<ConcatArray<float>>): FixedArray<float>
```

根据当前数组实例与给定的数组实例创建新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function concat(self: FixedArray<float>, ...items: FixedArray<ConcatArray<float>>): FixedArray<float>--><!--Device-unnamed-export function concat(self: FixedArray<float>, ...items: FixedArray<ConcatArray<float>>): FixedArray<float>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | 是 | 执行`concat`操作的数组。 |
| items | FixedArray&lt;ConcatArray&lt;float&gt;&gt; | 是 | 待连接为新数组的 其他数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;float&gt; | 由`this`与给定的Array类实例`items` 构造出的新Array实例。 |


## concat

```TypeScript
export function concat(self: FixedArray<double>, fst: FixedArray<double>, ...more: FixedArray<FixedArray<double>>): 
    FixedArray<double>
```

将参数中提供的数组依次连接，合并两个或多个数组 为一个新数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function concat(self: FixedArray<double>, fst: FixedArray<double>, ...more: FixedArray<FixedArray<double>>):     FixedArray<double>--><!--Device-unnamed-export function concat(self: FixedArray<double>, fst: FixedArray<double>, ...more: FixedArray<FixedArray<double>>):     FixedArray<double>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | 是 | 执行`concat`操作的数组。 |
| fst | FixedArray&lt;double&gt; | 是 | 待连接的第一个数组。 |
| more | FixedArray&lt;FixedArray&lt;double&gt;&gt; | 是 | 待连接的其他数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;double&gt; | 由这些数组连接而成的新数组。 |


## concat

```TypeScript
export function concat(self: FixedArray<double>, ...items: FixedArray<ConcatArray<double>>): FixedArray<double>
```

根据当前数组实例与给定的数组实例创建新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function concat(self: FixedArray<double>, ...items: FixedArray<ConcatArray<double>>): FixedArray<double>--><!--Device-unnamed-export function concat(self: FixedArray<double>, ...items: FixedArray<ConcatArray<double>>): FixedArray<double>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | 是 | 执行`concat`操作的数组。 |
| items | FixedArray&lt;ConcatArray&lt;double&gt;&gt; | 是 | 待连接为新数组的 其他数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;double&gt; | 由`this`与给定的Array类实例`items` 构造出的新Array实例。 |


## concat

```TypeScript
export function concat(self: FixedArray<char>, fst: FixedArray<char>, ...more: FixedArray<FixedArray<char>>): 
    FixedArray<char>
```

将参数中提供的数组依次连接，合并两个或多个数组 为一个新数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function concat(self: FixedArray<char>, fst: FixedArray<char>, ...more: FixedArray<FixedArray<char>>):     FixedArray<char>--><!--Device-unnamed-export function concat(self: FixedArray<char>, fst: FixedArray<char>, ...more: FixedArray<FixedArray<char>>):     FixedArray<char>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | 是 | 执行`concat`操作的数组。 |
| fst | FixedArray&lt;char&gt; | 是 | 待连接的第一个数组。 |
| more | FixedArray&lt;FixedArray&lt;char&gt;&gt; | 是 | 待连接的其他数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;char&gt; | 由这些数组连接而成的新数组。 |


## concat

```TypeScript
export function concat(self: FixedArray<char>, ...items: FixedArray<ConcatArray<char>>): FixedArray<char>
```

根据当前数组实例与给定的数组实例创建新的数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function concat(self: FixedArray<char>, ...items: FixedArray<ConcatArray<char>>): FixedArray<char>--><!--Device-unnamed-export function concat(self: FixedArray<char>, ...items: FixedArray<ConcatArray<char>>): FixedArray<char>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | 是 | 执行`concat`操作的数组。 |
| items | FixedArray&lt;ConcatArray&lt;char&gt;&gt; | 是 | 待连接为新数组的 其他数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;char&gt; | 由`this`与给定的Array类实例`items` 构造出的新Array实例。 |

