# sort

## 导入模块

```TypeScript
```

## sort

```TypeScript
export function sort(self: FixedArray<boolean>, comparator: (a: boolean, b: boolean) => int, start?: int, end?: int): 
    FixedArray<boolean>
```

使用比较函数重新排列当前数组中的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function sort(self: FixedArray<boolean>, comparator: (a: boolean, b: boolean) => int, start?: int, end?: int):     FixedArray<boolean>--><!--Device-unnamed-export function sort(self: FixedArray<boolean>, comparator: (a: boolean, b: boolean) => int, start?: int, end?: int):     FixedArray<boolean>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | 是 | 执行`sort`操作的数组。 |
| comparator | (a: boolean, b: boolean) =&gt; int | 是 | 用于定义排序顺序的函数。 |
| start | int | 否 | 开始排序的索引。 <br>取值约束：应为整数。 |
| end | int | 否 | 结束排序的索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;boolean&gt; | 排序后的数组。 |


## sort

```TypeScript
export function sort(self: FixedArray<boolean>): FixedArray<boolean>
```

使用比较函数重新排列`this`中的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function sort(self: FixedArray<boolean>): FixedArray<boolean>--><!--Device-unnamed-export function sort(self: FixedArray<boolean>): FixedArray<boolean>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | 是 | 用于定义排序顺序的比较函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;boolean&gt; | 新的Array迭代器对象。 |


## sort

```TypeScript
export function sort(self: FixedArray<byte>, comparator: (a: byte, b: byte) => int, start?: int, end?: int): 
    FixedArray<byte>
```

使用比较函数重新排列当前数组中的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function sort(self: FixedArray<byte>, comparator: (a: byte, b: byte) => int, start?: int, end?: int):     FixedArray<byte>--><!--Device-unnamed-export function sort(self: FixedArray<byte>, comparator: (a: byte, b: byte) => int, start?: int, end?: int):     FixedArray<byte>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | 是 | 执行`sort`操作的数组。 |
| comparator | (a: byte, b: byte) =&gt; int | 是 | 用于定义排序顺序的函数。 |
| start | int | 否 | 开始排序的索引。 <br>取值约束：应为整数。 |
| end | int | 否 | 结束排序的索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;byte&gt; | 排序后的数组。 |


## sort

```TypeScript
export function sort(self: FixedArray<byte>): FixedArray<byte>
```

使用比较函数重新排列`this`中的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function sort(self: FixedArray<byte>): FixedArray<byte>--><!--Device-unnamed-export function sort(self: FixedArray<byte>): FixedArray<byte>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | 是 | 用于定义排序顺序的比较函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;byte&gt; | 新的Array迭代器对象。 |


## sort

```TypeScript
export function sort(self: FixedArray<short>, comparator: (a: short, b: short) => int, start?: int, end?: int): 
    FixedArray<short>
```

使用比较函数重新排列当前数组中的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function sort(self: FixedArray<short>, comparator: (a: short, b: short) => int, start?: int, end?: int):     FixedArray<short>--><!--Device-unnamed-export function sort(self: FixedArray<short>, comparator: (a: short, b: short) => int, start?: int, end?: int):     FixedArray<short>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | 是 | 执行`sort`操作的数组。 |
| comparator | (a: short, b: short) =&gt; int | 是 | 用于定义排序顺序的函数。 |
| start | int | 否 | 开始排序的索引。 |
| end | int | 否 | 结束排序的索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;short&gt; | 排序后的数组。 |


## sort

```TypeScript
export function sort(self: FixedArray<short>): FixedArray<short>
```

使用比较函数重新排列`this`中的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function sort(self: FixedArray<short>): FixedArray<short>--><!--Device-unnamed-export function sort(self: FixedArray<short>): FixedArray<short>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | 是 | 用于定义排序顺序的比较函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;short&gt; | 新的Array迭代器对象。 |


## sort

```TypeScript
export function sort(self: FixedArray<int>, comparator: (a: int, b: int) => int, start?: int, end?: int): 
    FixedArray<int>
```

使用比较函数重新排列当前数组中的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function sort(self: FixedArray<int>, comparator: (a: int, b: int) => int, start?: int, end?: int):     FixedArray<int>--><!--Device-unnamed-export function sort(self: FixedArray<int>, comparator: (a: int, b: int) => int, start?: int, end?: int):     FixedArray<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | 是 | 执行`sort`操作的数组。 |
| comparator | (a: int, b: int) =&gt; int | 是 | 用于定义排序顺序的函数。 |
| start | int | 否 | 开始排序的索引。 <br>取值约束：应为整数。 |
| end | int | 否 | 结束排序的索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;int&gt; | 排序后的数组。 |


## sort

```TypeScript
export function sort(self: FixedArray<int>): FixedArray<int>
```

使用比较函数重新排列`this`中的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function sort(self: FixedArray<int>): FixedArray<int>--><!--Device-unnamed-export function sort(self: FixedArray<int>): FixedArray<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | 是 | 用于定义排序顺序的比较函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;int&gt; | 新的Array迭代器对象。 |


## sort

```TypeScript
export function sort(self: FixedArray<long>, comparator: (a: long, b: long) => int, start?: int, end?: int): 
    FixedArray<long>
```

使用比较函数重新排列当前数组中的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function sort(self: FixedArray<long>, comparator: (a: long, b: long) => int, start?: int, end?: int):     FixedArray<long>--><!--Device-unnamed-export function sort(self: FixedArray<long>, comparator: (a: long, b: long) => int, start?: int, end?: int):     FixedArray<long>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | 是 | 执行`sort`操作的数组。 |
| comparator | (a: long, b: long) =&gt; int | 是 | 用于定义排序顺序的函数。 |
| start | int | 否 | 开始排序的索引。 <br>取值约束：应为整数。 |
| end | int | 否 | 结束排序的索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;long&gt; | 排序后的数组。 |


## sort

```TypeScript
export function sort(self: FixedArray<long>): FixedArray<long>
```

使用比较函数重新排列`this`中的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function sort(self: FixedArray<long>): FixedArray<long>--><!--Device-unnamed-export function sort(self: FixedArray<long>): FixedArray<long>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | 是 | 用于定义排序顺序的比较函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;long&gt; | 新的Array迭代器对象。 |


## sort

```TypeScript
export function sort(self: FixedArray<float>, comparator: (a: float, b: float) => int, start?: int, end?: int): 
    FixedArray<float>
```

使用比较函数重新排列当前数组中的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function sort(self: FixedArray<float>, comparator: (a: float, b: float) => int, start?: int, end?: int):     FixedArray<float>--><!--Device-unnamed-export function sort(self: FixedArray<float>, comparator: (a: float, b: float) => int, start?: int, end?: int):     FixedArray<float>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | 是 | 执行`sort`操作的数组。 |
| comparator | (a: float, b: float) =&gt; int | 是 | 用于定义排序顺序的函数。 |
| start | int | 否 | 开始排序的索引。 <br>取值约束：应为整数。 |
| end | int | 否 | 结束排序的索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;float&gt; | 排序后的数组。 |


## sort

```TypeScript
export function sort(self: FixedArray<float>): FixedArray<float>
```

使用比较函数重新排列`this`中的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function sort(self: FixedArray<float>): FixedArray<float>--><!--Device-unnamed-export function sort(self: FixedArray<float>): FixedArray<float>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | 是 | 用于定义排序顺序的比较函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;float&gt; | 新的Array迭代器对象。 |


## sort

```TypeScript
export function sort(self: FixedArray<double>, comparator: (a: double, b: double) => int, start?: int, end?: int): 
    FixedArray<double>
```

使用比较函数重新排列当前数组中的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function sort(self: FixedArray<double>, comparator: (a: double, b: double) => int, start?: int, end?: int):     FixedArray<double>--><!--Device-unnamed-export function sort(self: FixedArray<double>, comparator: (a: double, b: double) => int, start?: int, end?: int):     FixedArray<double>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | 是 | 执行`sort`操作的数组。 |
| comparator | (a: double, b: double) =&gt; int | 是 | 用于定义排序顺序的函数。 |
| start | int | 否 | 开始排序的索引。 <br>取值约束：应为整数。 |
| end | int | 否 | 结束排序的索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;double&gt; | 排序后的数组。 |


## sort

```TypeScript
export function sort(self: FixedArray<double>): FixedArray<double>
```

使用比较函数重新排列`this`中的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function sort(self: FixedArray<double>): FixedArray<double>--><!--Device-unnamed-export function sort(self: FixedArray<double>): FixedArray<double>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | 是 | 用于定义排序顺序的比较函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;double&gt; | 新的Array迭代器对象。 |


## sort

```TypeScript
export function sort(self: FixedArray<char>, comparator: (a: char, b: char) => int, start?: int, end?: int): 
    FixedArray<char>
```

使用比较函数重新排列当前数组中的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function sort(self: FixedArray<char>, comparator: (a: char, b: char) => int, start?: int, end?: int):     FixedArray<char>--><!--Device-unnamed-export function sort(self: FixedArray<char>, comparator: (a: char, b: char) => int, start?: int, end?: int):     FixedArray<char>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | 是 | 执行`sort`操作的数组。 |
| comparator | (a: char, b: char) =&gt; int | 是 | 用于定义排序顺序的函数。 |
| start | int | 否 | 开始排序的索引。 <br>取值约束：应为整数。 |
| end | int | 否 | 结束排序的索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;char&gt; | 排序后的数组。 |


## sort

```TypeScript
export function sort(self: FixedArray<char>): FixedArray<char>
```

使用比较函数重新排列`this`中的元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function sort(self: FixedArray<char>): FixedArray<char>--><!--Device-unnamed-export function sort(self: FixedArray<char>): FixedArray<char>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | 是 | 用于定义排序顺序的比较函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;char&gt; | 新的Array迭代器对象。 |

