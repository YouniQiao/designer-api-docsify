# findIndex

## 导入模块

```TypeScript
```

## findIndex

```TypeScript
export function findIndex(self: FixedArray<boolean>, predicate: (value: boolean, index: int, 
    array: FixedArray<boolean>) => boolean): int
```

返回数组中第一个使predicate返回true的元素的索引，若不存在则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findIndex(self: FixedArray<boolean>, predicate: (value: boolean, index: int,     array: FixedArray<boolean>) => boolean): int--><!--Device-unnamed-export function findIndex(self: FixedArray<boolean>, predicate: (value: boolean, index: int,     array: FixedArray<boolean>) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | 是 | 执行`findIndex`操作的数组。 |
| predicate | (value: boolean, index: int,      array: FixedArray&lt;boolean&gt;) =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 第一个满足指定测试函数的元素的索引，若不存在则返回-1。 |


## findIndex

```TypeScript
export function findIndex(self: FixedArray<byte>, predicate: (value: byte, index: int, array: FixedArray<byte>) 
    => boolean): int
```

返回数组中第一个使predicate返回true的元素的索引，若不存在则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findIndex(self: FixedArray<byte>, predicate: (value: byte, index: int, array: FixedArray<byte>)     => boolean): int--><!--Device-unnamed-export function findIndex(self: FixedArray<byte>, predicate: (value: byte, index: int, array: FixedArray<byte>)     => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | 是 | 执行`findIndex`操作的数组。 |
| predicate | (value: byte, index: int, array: FixedArray&lt;byte&gt;)      =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 第一个满足指定测试函数的元素的索引，若不存在则返回-1。 |


## findIndex

```TypeScript
export function findIndex(self: FixedArray<short>, predicate: (value: short, index: int, array: FixedArray<short>) 
    => boolean): int
```

返回数组中第一个使predicate返回true的元素的索引，若不存在则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findIndex(self: FixedArray<short>, predicate: (value: short, index: int, array: FixedArray<short>)     => boolean): int--><!--Device-unnamed-export function findIndex(self: FixedArray<short>, predicate: (value: short, index: int, array: FixedArray<short>)     => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | 是 | 执行`findIndex`操作的数组。 |
| predicate | (value: short, index: int, array: FixedArray&lt;short&gt;)      =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 第一个满足指定测试函数的元素的索引，若不存在则返回-1。 |


## findIndex

```TypeScript
export function findIndex(self: FixedArray<int>, predicate: (value: int, index: int, array: FixedArray<int>) 
    => boolean): int
```

返回数组中第一个使predicate返回true的元素的索引，若不存在则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findIndex(self: FixedArray<int>, predicate: (value: int, index: int, array: FixedArray<int>)     => boolean): int--><!--Device-unnamed-export function findIndex(self: FixedArray<int>, predicate: (value: int, index: int, array: FixedArray<int>)     => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | 是 | 执行`findIndex`操作的数组。 |
| predicate | (value: int, index: int, array: FixedArray&lt;int&gt;)      =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 第一个满足指定测试函数的元素的索引，若不存在则返回-1。 |


## findIndex

```TypeScript
export function findIndex(self: FixedArray<long>, predicate: (value: long, index: int, array: FixedArray<long>) 
    => boolean): int
```

返回数组中第一个使predicate返回true的元素的索引，若不存在则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findIndex(self: FixedArray<long>, predicate: (value: long, index: int, array: FixedArray<long>)     => boolean): int--><!--Device-unnamed-export function findIndex(self: FixedArray<long>, predicate: (value: long, index: int, array: FixedArray<long>)     => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | 是 | 执行`findIndex`操作的数组。 |
| predicate | (value: long, index: int, array: FixedArray&lt;long&gt;)      =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 第一个满足指定测试函数的元素的索引，若不存在则返回-1。 |


## findIndex

```TypeScript
export function findIndex(self: FixedArray<float>, predicate: (value: float, index: int, array: FixedArray<float>) 
    => boolean): int
```

返回数组中第一个使predicate返回true的元素的索引，若不存在则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findIndex(self: FixedArray<float>, predicate: (value: float, index: int, array: FixedArray<float>)     => boolean): int--><!--Device-unnamed-export function findIndex(self: FixedArray<float>, predicate: (value: float, index: int, array: FixedArray<float>)     => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | 是 | 执行`findIndex`操作的数组。 |
| predicate | (value: float, index: int, array: FixedArray&lt;float&gt;)      =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 第一个满足指定测试函数的元素的索引，若不存在则返回-1。 |


## findIndex

```TypeScript
export function findIndex(self: FixedArray<double>, predicate: (value: double, index: int, array: FixedArray<double>) 
    => boolean): int
```

返回数组中第一个使predicate返回true的元素的索引，若不存在则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findIndex(self: FixedArray<double>, predicate: (value: double, index: int, array: FixedArray<double>)     => boolean): int--><!--Device-unnamed-export function findIndex(self: FixedArray<double>, predicate: (value: double, index: int, array: FixedArray<double>)     => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | 是 | 执行`findIndex`操作的数组。 |
| predicate | (value: double, index: int, array: FixedArray&lt;double&gt;)      =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 第一个满足指定测试函数的元素的索引，若不存在则返回-1。 |


## findIndex

```TypeScript
export function findIndex(self: FixedArray<char>, predicate: (value: char, index: int, array: FixedArray<char>) 
    => boolean): int
```

返回数组中第一个使predicate返回true的元素的索引，若不存在则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findIndex(self: FixedArray<char>, predicate: (value: char, index: int, array: FixedArray<char>)     => boolean): int--><!--Device-unnamed-export function findIndex(self: FixedArray<char>, predicate: (value: char, index: int, array: FixedArray<char>)     => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | 是 | 执行`findIndex`操作的数组。 |
| predicate | (value: char, index: int, array: FixedArray&lt;char&gt;)      =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 第一个满足指定测试函数的元素的索引，若不存在则返回-1。 |

