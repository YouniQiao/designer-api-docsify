# mergeSort

## 导入模块

```TypeScript
```

## mergeSort

```TypeScript
export function mergeSort(array: FixedArray<byte>, cmp: (lhs: byte, rhs: byte) => int,
    begin: int = 0, end: int = 0): FixedArray<byte>
```

对数组进行原地排序。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function mergeSort(array: FixedArray<byte>, cmp: (lhs: byte, rhs: byte) => int,    begin: int = 0, end: int = 0): FixedArray<byte>--><!--Device-unnamed-export function mergeSort(array: FixedArray<byte>, cmp: (lhs: byte, rhs: byte) => int,    begin: int = 0, end: int = 0): FixedArray<byte>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | FixedArray&lt;byte&gt; | 是 | 待排序的数组。 |
| cmp | (lhs: byte, rhs: byte) =&gt; int | 是 | 比较函数。 |
| begin | int | 是 | 开始排序的索引。 <br>取值约束：应为整数。 |
| end | int | 是 | 结束排序的索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;byte&gt; | 排序后的数组。 |


## mergeSort

```TypeScript
export function mergeSort(array: FixedArray<short>, cmp: (lhs: short, rhs: short) => int,
    begin: int = 0, end: int = 0): FixedArray<short>
```

对数组进行原地排序。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function mergeSort(array: FixedArray<short>, cmp: (lhs: short, rhs: short) => int,    begin: int = 0, end: int = 0): FixedArray<short>--><!--Device-unnamed-export function mergeSort(array: FixedArray<short>, cmp: (lhs: short, rhs: short) => int,    begin: int = 0, end: int = 0): FixedArray<short>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | FixedArray&lt;short&gt; | 是 | 待排序的数组。 |
| cmp | (lhs: short, rhs: short) =&gt; int | 是 | 比较函数。 |
| begin | int | 是 | 开始排序的索引。 |
| end | int | 是 | 结束排序的索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;short&gt; | 排序后的数组。 |


## mergeSort

```TypeScript
export function mergeSort(array: FixedArray<int>, cmp: (lhs: int, rhs: int) => int,
    begin: int = 0, end: int = 0): FixedArray<int>
```

对数组进行原地排序。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function mergeSort(array: FixedArray<int>, cmp: (lhs: int, rhs: int) => int,    begin: int = 0, end: int = 0): FixedArray<int>--><!--Device-unnamed-export function mergeSort(array: FixedArray<int>, cmp: (lhs: int, rhs: int) => int,    begin: int = 0, end: int = 0): FixedArray<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | FixedArray&lt;int&gt; | 是 | 待排序的数组。 |
| cmp | (lhs: int, rhs: int) =&gt; int | 是 | 比较函数。 |
| begin | int | 是 | 开始排序的索引。 |
| end | int | 是 | 结束排序的索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;int&gt; | 排序后的数组。 |


## mergeSort

```TypeScript
export function mergeSort(array: FixedArray<long>, cmp: (lhs: long, rhs: long) => int,
    begin: int = 0, end: int = 0): FixedArray<long>
```

对数组进行原地排序。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function mergeSort(array: FixedArray<long>, cmp: (lhs: long, rhs: long) => int,    begin: int = 0, end: int = 0): FixedArray<long>--><!--Device-unnamed-export function mergeSort(array: FixedArray<long>, cmp: (lhs: long, rhs: long) => int,    begin: int = 0, end: int = 0): FixedArray<long>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | FixedArray&lt;long&gt; | 是 | 待排序的数组。 |
| cmp | (lhs: long, rhs: long) =&gt; int | 是 | 比较函数。 |
| begin | int | 是 | 开始排序的索引。 |
| end | int | 是 | 结束排序的索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;long&gt; | 排序后的数组。 |


## mergeSort

```TypeScript
export function mergeSort(array: FixedArray<float>, cmp: (lhs: float, rhs: float) => int,
    begin: int = 0, end: int = 0): FixedArray<float>
```

对数组进行原地排序。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function mergeSort(array: FixedArray<float>, cmp: (lhs: float, rhs: float) => int,    begin: int = 0, end: int = 0): FixedArray<float>--><!--Device-unnamed-export function mergeSort(array: FixedArray<float>, cmp: (lhs: float, rhs: float) => int,    begin: int = 0, end: int = 0): FixedArray<float>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | FixedArray&lt;float&gt; | 是 | 待排序的数组。 |
| cmp | (lhs: float, rhs: float) =&gt; int | 是 | 比较函数。 |
| begin | int | 是 | 开始排序的索引。 |
| end | int | 是 | 结束排序的索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;float&gt; | 排序后的数组。 |


## mergeSort

```TypeScript
export function mergeSort(array: FixedArray<double>, cmp: (lhs: double, rhs: double) => int,
    begin: int = 0, end: int = 0): FixedArray<double>
```

对数组进行原地排序。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function mergeSort(array: FixedArray<double>, cmp: (lhs: double, rhs: double) => int,    begin: int = 0, end: int = 0): FixedArray<double>--><!--Device-unnamed-export function mergeSort(array: FixedArray<double>, cmp: (lhs: double, rhs: double) => int,    begin: int = 0, end: int = 0): FixedArray<double>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | FixedArray&lt;double&gt; | 是 | 待排序的数组。 |
| cmp | (lhs: double, rhs: double) =&gt; int | 是 | 比较函数。 |
| begin | int | 是 | 开始排序的索引。 |
| end | int | 是 | 结束排序的索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;double&gt; | 排序后的数组。 |

