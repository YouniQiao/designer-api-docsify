# every

## 导入模块

```TypeScript
```

## every

```TypeScript
export function every(self: FixedArray<boolean>, predicate: (value: boolean, index: int, array: FixedArray<boolean>)
    => boolean): boolean
```

判断数组中的所有元素是否都满足指定的测试条件。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function every(self: FixedArray<boolean>, predicate: (value: boolean, index: int, array: FixedArray<boolean>)    => boolean): boolean--><!--Device-unnamed-export function every(self: FixedArray<boolean>, predicate: (value: boolean, index: int, array: FixedArray<boolean>)    => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | 是 | 执行`every`操作的数组。 |
| predicate | (value: boolean, index: int, array: FixedArray&lt;boolean&gt;)     =&gt; boolean | 是 | 最多接受三个参数的函数。every方法会对数组中的每个元素调用predicate 函数，直到predicate返回的值可转换为 Boolean值false，或遍历完整个数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果predicate对数组中所有元素都返回true则返回true，否则返回false。 |


## every

```TypeScript
export function every(self: FixedArray<byte>, predicate: (value: byte, index: int, array: FixedArray<byte>) 
    => boolean): boolean
```

判断数组中的所有元素是否都满足指定的测试条件。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function every(self: FixedArray<byte>, predicate: (value: byte, index: int, array: FixedArray<byte>)     => boolean): boolean--><!--Device-unnamed-export function every(self: FixedArray<byte>, predicate: (value: byte, index: int, array: FixedArray<byte>)     => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | 是 | 执行`every`操作的数组。 |
| predicate | (value: byte, index: int, array: FixedArray&lt;byte&gt;)      =&gt; boolean | 是 | 最多接受三个参数的函数。every方法会对数组中的每个元素调用predicate 函数，直到predicate返回的值可转换为 Boolean值false，或遍历完整个数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果predicate对数组中所有元素都返回true则返回true，否则返回false。 |


## every

```TypeScript
export function every(self: FixedArray<short>, predicate: (value: short, index: int, array: FixedArray<short>) 
    => boolean): boolean
```

判断数组中的所有元素是否都满足指定的测试条件。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function every(self: FixedArray<short>, predicate: (value: short, index: int, array: FixedArray<short>)     => boolean): boolean--><!--Device-unnamed-export function every(self: FixedArray<short>, predicate: (value: short, index: int, array: FixedArray<short>)     => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | 是 | 执行`every`操作的数组。 |
| predicate | (value: short, index: int, array: FixedArray&lt;short&gt;)      =&gt; boolean | 是 | 最多接受三个参数的函数。every方法会对数组中的每个元素调用predicate 函数，直到predicate返回的值可转换为 Boolean值false，或遍历完整个数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果predicate对数组中所有元素都返回true则返回true，否则返回false。 |


## every

```TypeScript
export function every(self: FixedArray<int>, predicate: (value: int, index: int, array: FixedArray<int>) 
    => boolean): boolean
```

判断数组中的所有元素是否都满足指定的测试条件。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function every(self: FixedArray<int>, predicate: (value: int, index: int, array: FixedArray<int>)     => boolean): boolean--><!--Device-unnamed-export function every(self: FixedArray<int>, predicate: (value: int, index: int, array: FixedArray<int>)     => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | 是 | 执行`every`操作的数组。 |
| predicate | (value: int, index: int, array: FixedArray&lt;int&gt;)      =&gt; boolean | 是 | 最多接受三个参数的函数。every方法会对数组中的每个元素调用predicate 函数，直到predicate返回的值可转换为 Boolean值false，或遍历完整个数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果predicate对数组中所有元素都返回true则返回true，否则返回false。 |


## every

```TypeScript
export function every(self: FixedArray<long>, predicate: (value: long, index: int, array: FixedArray<long>) 
    => boolean): boolean
```

判断数组中的所有元素是否都满足指定的测试条件。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function every(self: FixedArray<long>, predicate: (value: long, index: int, array: FixedArray<long>)     => boolean): boolean--><!--Device-unnamed-export function every(self: FixedArray<long>, predicate: (value: long, index: int, array: FixedArray<long>)     => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | 是 | 执行`every`操作的数组。 |
| predicate | (value: long, index: int, array: FixedArray&lt;long&gt;)      =&gt; boolean | 是 | 最多接受三个参数的函数。every方法会对数组中的每个元素调用predicate 函数，直到predicate返回的值可转换为 Boolean值false，或遍历完整个数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果predicate对数组中所有元素都返回true则返回true，否则返回false。 |


## every

```TypeScript
export function every(self: FixedArray<float>, predicate: (value: float, index: int, array: FixedArray<float>) 
    => boolean): boolean
```

判断数组中的所有元素是否都满足指定的测试条件。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function every(self: FixedArray<float>, predicate: (value: float, index: int, array: FixedArray<float>)     => boolean): boolean--><!--Device-unnamed-export function every(self: FixedArray<float>, predicate: (value: float, index: int, array: FixedArray<float>)     => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | 是 | 执行`every`操作的数组。 |
| predicate | (value: float, index: int, array: FixedArray&lt;float&gt;)      =&gt; boolean | 是 | 最多接受三个参数的函数。every方法会对数组中的每个元素调用predicate 函数，直到predicate返回的值可转换为 Boolean值false，或遍历完整个数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果predicate对数组中所有元素都返回true则返回true，否则返回false。 |


## every

```TypeScript
export function every(self: FixedArray<double>, predicate: (value: double, index: int, array: FixedArray<double>) 
    => boolean): boolean
```

判断数组中的所有元素是否都满足指定的测试条件。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function every(self: FixedArray<double>, predicate: (value: double, index: int, array: FixedArray<double>)     => boolean): boolean--><!--Device-unnamed-export function every(self: FixedArray<double>, predicate: (value: double, index: int, array: FixedArray<double>)     => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | 是 | 执行`every`操作的数组。 |
| predicate | (value: double, index: int, array: FixedArray&lt;double&gt;)      =&gt; boolean | 是 | 最多接受三个参数的函数。every方法会对数组中的每个元素调用predicate 函数，直到predicate返回的值可转换为 Boolean值false，或遍历完整个数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果predicate对数组中所有元素都返回true则返回true，否则返回false。 |


## every

```TypeScript
export function every(self: FixedArray<char>, predicate: (value: char, index: int, array: FixedArray<char>) 
    => boolean): boolean
```

判断数组中的所有元素是否都满足指定的测试条件。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function every(self: FixedArray<char>, predicate: (value: char, index: int, array: FixedArray<char>)     => boolean): boolean--><!--Device-unnamed-export function every(self: FixedArray<char>, predicate: (value: char, index: int, array: FixedArray<char>)     => boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | 是 | 执行`every`操作的数组。 |
| predicate | (value: char, index: int, array: FixedArray&lt;char&gt;)      =&gt; boolean | 是 | 最多接受三个参数的函数。every方法会对数组中的每个元素调用predicate 函数，直到predicate返回的值可转换为 Boolean值false，或遍历完整个数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果predicate对数组中所有元素都返回true则返回true，否则返回false。 |

