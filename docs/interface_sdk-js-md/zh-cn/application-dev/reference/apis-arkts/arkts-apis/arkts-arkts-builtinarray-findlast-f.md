# findLast

## 导入模块

```TypeScript
```

## findLast

```TypeScript
export function findLast(self: FixedArray<boolean>, predicate: (elem: boolean, index: int, array: FixedArray<boolean>)
    => boolean): Boolean | undefined
```

按逆序遍历数组，返回第一个满足指定测试函数的 元素的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findLast(self: FixedArray<boolean>, predicate: (elem: boolean, index: int, array: FixedArray<boolean>)    => boolean): Boolean | undefined--><!--Device-unnamed-export function findLast(self: FixedArray<boolean>, predicate: (elem: boolean, index: int, array: FixedArray<boolean>)    => boolean): Boolean | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | 是 | 执行`findLast`操作的数组。 |
| predicate | (elem: boolean, index: int, array: FixedArray&lt;boolean&gt;)     =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Boolean \| undefined | 找到时返回该元素的值，否则返回undefined。 |


## findLast

```TypeScript
export function findLast(self: FixedArray<byte>, predicate: (elem: byte, index: int, array: FixedArray<byte>) 
    => boolean): Byte | undefined
```

按逆序遍历数组，返回第一个满足指定测试函数的 元素的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findLast(self: FixedArray<byte>, predicate: (elem: byte, index: int, array: FixedArray<byte>)     => boolean): Byte | undefined--><!--Device-unnamed-export function findLast(self: FixedArray<byte>, predicate: (elem: byte, index: int, array: FixedArray<byte>)     => boolean): Byte | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | 是 | 执行`findLast`操作的数组。 |
| predicate | (elem: byte, index: int, array: FixedArray&lt;byte&gt;)      =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Byte \| undefined | 找到时返回该元素的值，否则返回undefined。 |


## findLast

```TypeScript
export function findLast(self: FixedArray<short>, predicate: (elem: short, index: int, array: FixedArray<short>) 
    => boolean): Short | undefined
```

按逆序遍历数组，返回第一个满足指定测试函数的 元素的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findLast(self: FixedArray<short>, predicate: (elem: short, index: int, array: FixedArray<short>)     => boolean): Short | undefined--><!--Device-unnamed-export function findLast(self: FixedArray<short>, predicate: (elem: short, index: int, array: FixedArray<short>)     => boolean): Short | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | 是 | 执行`findLast`操作的数组。 |
| predicate | (elem: short, index: int, array: FixedArray&lt;short&gt;)      =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Short \| undefined | 找到时返回该元素的值，否则返回undefined。 |


## findLast

```TypeScript
export function findLast(self: FixedArray<int>, predicate: (elem: int, index: int, array: FixedArray<int>) 
    => boolean): Int | undefined
```

按逆序遍历数组，返回第一个满足指定测试函数的 元素的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findLast(self: FixedArray<int>, predicate: (elem: int, index: int, array: FixedArray<int>)     => boolean): Int | undefined--><!--Device-unnamed-export function findLast(self: FixedArray<int>, predicate: (elem: int, index: int, array: FixedArray<int>)     => boolean): Int | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | 是 | 执行`findLast`操作的数组。 |
| predicate | (elem: int, index: int, array: FixedArray&lt;int&gt;)      =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int \| undefined | 找到时返回该元素的值，否则返回undefined。 |


## findLast

```TypeScript
export function findLast(self: FixedArray<long>, predicate: (elem: long, index: int, array: FixedArray<long>) 
    => boolean): Long | undefined
```

按逆序遍历数组，返回第一个满足指定测试函数的 元素的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findLast(self: FixedArray<long>, predicate: (elem: long, index: int, array: FixedArray<long>)     => boolean): Long | undefined--><!--Device-unnamed-export function findLast(self: FixedArray<long>, predicate: (elem: long, index: int, array: FixedArray<long>)     => boolean): Long | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | 是 | 执行`findLast`操作的数组。 |
| predicate | (elem: long, index: int, array: FixedArray&lt;long&gt;)      =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Long \| undefined | 找到时返回该元素的值，否则返回undefined。 |


## findLast

```TypeScript
export function findLast(self: FixedArray<float>, predicate: (elem: float, index: int, array: FixedArray<float>) 
    => boolean): Float | undefined
```

按逆序遍历数组，返回第一个满足指定测试函数的 元素的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findLast(self: FixedArray<float>, predicate: (elem: float, index: int, array: FixedArray<float>)     => boolean): Float | undefined--><!--Device-unnamed-export function findLast(self: FixedArray<float>, predicate: (elem: float, index: int, array: FixedArray<float>)     => boolean): Float | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | 是 | 执行`findLast`操作的数组。 |
| predicate | (elem: float, index: int, array: FixedArray&lt;float&gt;)      =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Float \| undefined | 找到时返回该元素的值，否则返回undefined。 |


## findLast

```TypeScript
export function findLast(self: FixedArray<double>, predicate: (elem: double, index: int, array: FixedArray<double>) 
    => boolean): Double | undefined
```

按逆序遍历数组，返回第一个满足指定测试函数的 元素的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findLast(self: FixedArray<double>, predicate: (elem: double, index: int, array: FixedArray<double>)     => boolean): Double | undefined--><!--Device-unnamed-export function findLast(self: FixedArray<double>, predicate: (elem: double, index: int, array: FixedArray<double>)     => boolean): Double | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | 是 | 执行`findLast`操作的数组。 |
| predicate | (elem: double, index: int, array: FixedArray&lt;double&gt;)      =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Double \| undefined | 找到时返回该元素的值，否则返回undefined。 |


## findLast

```TypeScript
export function findLast(self: FixedArray<char>, predicate: (elem: char, index: int, array: FixedArray<char>) 
    => boolean): Char | undefined
```

按逆序遍历数组，返回第一个满足指定测试函数的 元素的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function findLast(self: FixedArray<char>, predicate: (elem: char, index: int, array: FixedArray<char>)     => boolean): Char | undefined--><!--Device-unnamed-export function findLast(self: FixedArray<char>, predicate: (elem: char, index: int, array: FixedArray<char>)     => boolean): Char | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | 是 | 执行`findLast`操作的数组。 |
| predicate | (elem: char, index: int, array: FixedArray&lt;char&gt;)      =&gt; boolean | 是 | 对数组中每个值执行的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Char \| undefined | 找到时返回该元素的值，否则返回undefined。 |

