# findLastIndex

## 导入模块

```TypeScript
```

## findLastIndex

```TypeScript
export function findLastIndex(self: FixedArray<boolean>, predicate: (element: boolean, index: int,
    array: FixedArray<boolean>) => boolean): int
```

按逆序遍历数组，返回第一个满足指定测试函数的元素的索引； 如果没有元素满足该测试函数，则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findLastIndex(self: FixedArray<boolean>, predicate: (element: boolean, index: int,    array: FixedArray<boolean>) => boolean): int--><!--Device-unnamed-export function findLastIndex(self: FixedArray<boolean>, predicate: (element: boolean, index: int,    array: FixedArray<boolean>) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | 是 | 执行`findLastIndex`操作的数组。 |
| predicate | (element: boolean, index: int,     array: FixedArray&lt;boolean&gt;) =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 第一个满足指定测试函数的元素的索引，若不存在则返回-1。 |


## findLastIndex

```TypeScript
export function findLastIndex(self: FixedArray<byte>, predicate: (element: byte, index: int, array: FixedArray<byte>) 
    => boolean): int
```

按逆序遍历数组，返回第一个满足指定测试函数的元素的索引； 如果没有元素满足该测试函数，则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findLastIndex(self: FixedArray<byte>, predicate: (element: byte, index: int, array: FixedArray<byte>)     => boolean): int--><!--Device-unnamed-export function findLastIndex(self: FixedArray<byte>, predicate: (element: byte, index: int, array: FixedArray<byte>)     => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | 是 | 执行`findLastIndex`操作的数组。 |
| predicate | (element: byte, index: int, array: FixedArray&lt;byte&gt;)      =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 第一个满足指定测试函数的元素的索引，若不存在则返回-1。 |


## findLastIndex

```TypeScript
export function findLastIndex(self: FixedArray<short>, predicate: (element: short, index: int, array: 
    FixedArray<short>) => boolean): int
```

按逆序遍历数组，返回第一个满足指定测试函数的元素的索引； 如果没有元素满足该测试函数，则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findLastIndex(self: FixedArray<short>, predicate: (element: short, index: int, array:     FixedArray<short>) => boolean): int--><!--Device-unnamed-export function findLastIndex(self: FixedArray<short>, predicate: (element: short, index: int, array:     FixedArray<short>) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | 是 | 执行`findLastIndex`操作的数组。 |
| predicate | (element: short, index: int, array:      FixedArray&lt;short&gt;) =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 第一个满足指定测试函数的元素的索引，若不存在则返回-1。 |


## findLastIndex

```TypeScript
export function findLastIndex(self: FixedArray<int>, predicate: (element: int, index: int, array: FixedArray<int>) 
    => boolean): int
```

按逆序遍历数组，返回第一个满足指定测试函数的元素的索引； 如果没有元素满足该测试函数，则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findLastIndex(self: FixedArray<int>, predicate: (element: int, index: int, array: FixedArray<int>)     => boolean): int--><!--Device-unnamed-export function findLastIndex(self: FixedArray<int>, predicate: (element: int, index: int, array: FixedArray<int>)     => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | 是 | 执行`findLastIndex`操作的数组。 |
| predicate | (element: int, index: int, array: FixedArray&lt;int&gt;)      =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 第一个满足指定测试函数的元素的索引，若不存在则返回-1。 |


## findLastIndex

```TypeScript
export function findLastIndex(self: FixedArray<long>, predicate: (element: long, index: int, array: FixedArray<long>) 
    => boolean): int
```

按逆序遍历数组，返回第一个满足指定测试函数的元素的索引； 如果没有元素满足该测试函数，则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findLastIndex(self: FixedArray<long>, predicate: (element: long, index: int, array: FixedArray<long>)     => boolean): int--><!--Device-unnamed-export function findLastIndex(self: FixedArray<long>, predicate: (element: long, index: int, array: FixedArray<long>)     => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | 是 | 执行`findLastIndex`操作的数组。 |
| predicate | (element: long, index: int, array: FixedArray&lt;long&gt;)      =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 第一个满足指定测试函数的元素的索引，若不存在则返回-1。 |


## findLastIndex

```TypeScript
export function findLastIndex(self: FixedArray<float>, predicate: (element: float, index: int, 
    array: FixedArray<float>) => boolean): int
```

按逆序遍历数组，返回第一个满足指定测试函数的元素的索引； 如果没有元素满足该测试函数，则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findLastIndex(self: FixedArray<float>, predicate: (element: float, index: int,     array: FixedArray<float>) => boolean): int--><!--Device-unnamed-export function findLastIndex(self: FixedArray<float>, predicate: (element: float, index: int,     array: FixedArray<float>) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | 是 | 执行`findLastIndex`操作的数组。 |
| predicate | (element: float, index: int,      array: FixedArray&lt;float&gt;) =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 第一个满足指定测试函数的元素的索引，若不存在则返回-1。 |


## findLastIndex

```TypeScript
export function findLastIndex(self: FixedArray<double>, predicate: (element: double, index: int, 
    array: FixedArray<double>) => boolean): int
```

按逆序遍历数组，返回第一个满足指定测试函数的元素的索引； 如果没有元素满足该测试函数，则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findLastIndex(self: FixedArray<double>, predicate: (element: double, index: int,     array: FixedArray<double>) => boolean): int--><!--Device-unnamed-export function findLastIndex(self: FixedArray<double>, predicate: (element: double, index: int,     array: FixedArray<double>) => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | 是 | 执行`findLastIndex`操作的数组。 |
| predicate | (element: double, index: int,      array: FixedArray&lt;double&gt;) =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 第一个满足指定测试函数的元素的索引，若不存在则返回-1。 |


## findLastIndex

```TypeScript
export function findLastIndex(self: FixedArray<char>, predicate: (element: char, index: int, array: FixedArray<char>) 
    => boolean): int
```

按逆序遍历数组，返回第一个满足指定测试函数的元素的索引； 如果没有元素满足该测试函数，则返回-1。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findLastIndex(self: FixedArray<char>, predicate: (element: char, index: int, array: FixedArray<char>)     => boolean): int--><!--Device-unnamed-export function findLastIndex(self: FixedArray<char>, predicate: (element: char, index: int, array: FixedArray<char>)     => boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | 是 | 执行`findLastIndex`操作的数组。 |
| predicate | (element: char, index: int, array: FixedArray&lt;char&gt;)      =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 第一个满足指定测试函数的元素的索引，若不存在则返回-1。 |

