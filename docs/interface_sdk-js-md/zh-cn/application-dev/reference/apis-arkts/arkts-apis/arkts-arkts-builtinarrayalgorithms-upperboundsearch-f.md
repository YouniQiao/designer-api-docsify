# upperBoundSearch

## 导入模块

```TypeScript
```

## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<boolean>, key: boolean, startIndex: int, endIndex: int): int
```

尝试在已排序的arr中查找键的上界。 调用该函数前必须先对数组排序。 上界是第一个使(key &lt; element)成立的元素的索引。 若不存在这样的元素，则上界为endIndex。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<boolean>, key: boolean, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<boolean>, key: boolean, startIndex: int, endIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;boolean&gt; | 是 | 待查找键上界的数组。该数组必须已排序， 否则结果由实现决定，可能不正确。 |
| key | boolean | 是 | 待查找上界的值。 |
| startIndex | int | 是 | 在arr中开始查找的索引。 <br>取值约束：应为整数。 |
| endIndex | int | 是 | 在arr中停止查找的索引，即不检查arr[endIndex]。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 使(key &lt; arr[index])成立的索引；若不存在这样的索引，则返回endIndex。 |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<boolean>, key: boolean): int
```

尝试在已排序的arr中查找键的上界。 调用该函数前必须先对数组排序。 上界是第一个使(key &lt; element)成立的元素的索引。 若不存在这样的元素，则上界为endIndex。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<boolean>, key: boolean): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<boolean>, key: boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;boolean&gt; | 是 | 待查找键上界的数组。该数组必须已排序， 否则结果由实现决定，可能不正确。 |
| key | boolean | 是 | 待查找上界的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 使(key &lt; arr[index])成立的索引；若不存在这样的索引，则返回endIndex。 |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<byte>, key: byte, startIndex: int, endIndex: int): int
```

尝试在已排序的arr中查找键的上界。 调用该函数前必须先对数组排序。 上界是第一个使(key &lt; element)成立的元素的索引。 若不存在这样的元素，则上界为endIndex。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<byte>, key: byte, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<byte>, key: byte, startIndex: int, endIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;byte&gt; | 是 | 待查找键上界的数组。该数组必须已排序， 否则结果由实现决定，可能不正确。 |
| key | byte | 是 | 待查找上界的值。 |
| startIndex | int | 是 | 在arr中开始查找的索引。 <br>取值约束：应为整数。 |
| endIndex | int | 是 | 在arr中停止查找的索引，即不检查arr[endIndex]。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 使(key &lt; arr[index])成立的索引；若不存在这样的索引，则返回endIndex。 |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<byte>, key: byte): int
```

尝试在已排序的arr中查找键的上界。 调用该函数前必须先对数组排序。 上界是第一个使(key &lt; element)成立的元素的索引。 若不存在这样的元素，则上界为endIndex。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<byte>, key: byte): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<byte>, key: byte): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;byte&gt; | 是 | 待查找键上界的数组。 该数组必须已排序，否则结果由实现决定，可能不正确。 |
| key | byte | 是 | 待查找上界的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 使(key &lt; arr[index])成立的索引；若不存在这样的索引，则返回endIndex。 |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<short>, key: short, startIndex: int, endIndex: int): int
```

尝试在已排序的arr中查找键的上界。 调用该函数前必须先对数组排序。 上界是第一个使(key &lt; element)成立的元素的索引。 若不存在这样的元素，则上界为endIndex。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<short>, key: short, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<short>, key: short, startIndex: int, endIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;short&gt; | 是 | 待查找键上界的数组。该数组必须已排序， 否则结果由实现决定，可能不正确。 |
| key | short | 是 | 待查找上界的值。 |
| startIndex | int | 是 | 在arr中开始查找的索引。 <br>取值约束：应为整数。 |
| endIndex | int | 是 | 在arr中停止查找的索引，即不检查arr[endIndex]。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 使(key &lt; arr[index])成立的索引；若不存在这样的索引，则返回endIndex。 |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<short>, key: short): int
```

尝试在已排序的arr中查找键的上界。 调用该函数前必须先对数组排序。 上界是第一个使(key &lt; element)成立的元素的索引。 若不存在这样的元素，则上界为endIndex。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<short>, key: short): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<short>, key: short): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;short&gt; | 是 | 待查找键上界的数组。该数组必须已排序， 否则结果由实现决定，可能不正确。 |
| key | short | 是 | 待查找上界的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 使(key &lt; arr[index])成立的索引；若不存在这样的索引，则返回endIndex。 |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<int>, key: int, startIndex: int, endIndex: int): int
```

尝试在已排序的arr中查找键的上界。 调用该函数前必须先对数组排序。 上界是第一个使(key &lt; element)成立的元素的索引。 若不存在这样的元素，则上界为endIndex。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<int>, key: int, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<int>, key: int, startIndex: int, endIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;int&gt; | 是 | 待查找键上界的数组。该数组必须已排序， 否则结果由实现决定，可能不正确。 |
| key | int | 是 | 待查找上界的值。 <br>取值约束：应为整数。 |
| startIndex | int | 是 | 在arr中开始查找的索引。 <br>取值约束：应为整数。 |
| endIndex | int | 是 | 在arr中停止查找的索引，即不检查arr[endIndex]。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 使(key &lt; arr[index])成立的索引；若不存在这样的索引，则返回endIndex。 |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<int>, key: int): int
```

尝试在已排序的arr中查找键的上界。 调用该函数前必须先对数组排序。 上界是第一个使(key &lt; element)成立的元素的索引。 若不存在这样的元素，则上界为endIndex。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<int>, key: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<int>, key: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;int&gt; | 是 | 待查找键上界的数组。该数组必须已排序， 否则结果由实现决定，可能不正确。 |
| key | int | 是 | 待查找上界的值。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 使(key &lt; arr[index])成立的索引；若不存在这样的索引，则返回endIndex。 |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<long>, key: long, startIndex: int, endIndex: int): int
```

尝试在已排序的arr中查找键的上界。 调用该函数前必须先对数组排序。 上界是第一个使(key &lt; element)成立的元素的索引。 若不存在这样的元素，则上界为endIndex。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<long>, key: long, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<long>, key: long, startIndex: int, endIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;long&gt; | 是 | 待查找键上界的数组。该数组必须已排序， 否则结果由实现决定，可能不正确。 |
| key | long | 是 | 待查找上界的值。 |
| startIndex | int | 是 | 在arr中开始查找的索引。 <br>取值约束：应为整数。 |
| endIndex | int | 是 | 在arr中停止查找的索引，即不检查arr[endIndex]。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 使(key &lt; arr[index])成立的索引；若不存在这样的索引，则返回endIndex。 |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<long>, key: long): int
```

尝试在已排序的arr中查找键的上界。 调用该函数前必须先对数组排序。 上界是第一个使(key &lt; element)成立的元素的索引。 若不存在这样的元素，则上界为endIndex。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<long>, key: long): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<long>, key: long): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;long&gt; | 是 | 待查找键上界的数组。该数组必须已排序， 否则结果由实现决定，可能不正确。 |
| key | long | 是 | 待查找上界的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 使(key &lt; arr[index])成立的索引；若不存在这样的索引，则返回endIndex。 |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<float>, key: float, startIndex: int, endIndex: int): int
```

尝试在已排序的arr中查找键的上界。 调用该函数前必须先对数组排序。 上界是第一个使(key &lt; element)成立的元素的索引。 若不存在这样的元素，则上界为endIndex。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<float>, key: float, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<float>, key: float, startIndex: int, endIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;float&gt; | 是 | 待查找键上界的数组。该数组必须已排序， 否则结果由实现决定，可能不正确。 |
| key | float | 是 | 待查找上界的值。 |
| startIndex | int | 是 | 在arr中开始查找的索引。 <br>取值约束：应为整数。 |
| endIndex | int | 是 | 在arr中停止查找的索引，即不检查arr[endIndex]。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 使(key &lt; arr[index])成立的索引；若不存在这样的索引，则返回endIndex。 |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<float>, key: float): int
```

尝试在已排序的arr中查找键的上界。 调用该函数前必须先对数组排序。 上界是第一个使(key &lt; element)成立的元素的索引。 若不存在这样的元素，则上界为endIndex。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<float>, key: float): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<float>, key: float): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;float&gt; | 是 | 待查找键上界的数组。该数组必须已排序， 否则结果由实现决定，可能不正确。 |
| key | float | 是 | 待查找上界的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 使(key &lt; arr[index])成立的索引；若不存在这样的索引，则返回endIndex。 |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<double>, key: double, startIndex: int, endIndex: int): int
```

尝试在已排序的arr中查找键的上界。 调用该函数前必须先对数组排序。 上界是第一个使(key &lt; element)成立的元素的索引。 若不存在这样的元素，则上界为endIndex。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<double>, key: double, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<double>, key: double, startIndex: int, endIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;double&gt; | 是 | 待查找键上界的数组。该数组必须已排序， 否则结果由实现决定，可能不正确。 |
| key | double | 是 | 待查找上界的值。 |
| startIndex | int | 是 | 在arr中开始查找的索引。 <br>取值约束：应为整数。 |
| endIndex | int | 是 | 在arr中停止查找的索引，即不检查arr[endIndex]。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 使(key &lt; arr[index])成立的索引；若不存在这样的索引，则返回endIndex。 |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<double>, key: double): int
```

尝试在已排序的arr中查找键的上界。 调用该函数前必须先对数组排序。 上界是第一个使(key &lt; element)成立的元素的索引。 若不存在这样的元素，则上界为endIndex。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<double>, key: double): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<double>, key: double): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;double&gt; | 是 | 待查找键上界的数组。该数组必须已排序， 否则结果由实现决定，可能不正确。 |
| key | double | 是 | 待查找上界的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 使(key &lt; arr[index])成立的索引；若不存在这样的索引，则返回endIndex。 |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<char>, key: char, startIndex: int, endIndex: int): int
```

尝试在已排序的arr中查找键的上界。 调用该函数前必须先对数组排序。 上界是第一个使(key &lt; element)成立的元素的索引。 若不存在这样的元素，则上界为endIndex。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<char>, key: char, startIndex: int, endIndex: int): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<char>, key: char, startIndex: int, endIndex: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;char&gt; | 是 | 待查找键上界的数组。该数组必须已排序， 否则结果由实现决定，可能不正确。 |
| key | char | 是 | 待查找上界的值。 |
| startIndex | int | 是 | 在arr中开始查找的索引。 <br>取值约束：应为整数。 |
| endIndex | int | 是 | 在arr中停止查找的索引，即不检查arr[endIndex]。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 使(key &lt; arr[index])成立的索引；若不存在这样的索引，则返回endIndex。 |


## upperBoundSearch

```TypeScript
export function upperBoundSearch(arr: FixedArray<char>, key: char): int
```

尝试在已排序的arr中查找键的上界。 调用该函数前必须先对数组排序。 上界是第一个使(key &lt; element)成立的元素的索引。 若不存在这样的元素，则上界为endIndex。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<char>, key: char): int--><!--Device-unnamed-export function upperBoundSearch(arr: FixedArray<char>, key: char): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;char&gt; | 是 | 待查找键上界的数组。该数组必须已排序， 否则结果由实现决定，可能不正确。 |
| key | char | 是 | 待查找上界的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 使(key &lt; arr[index])成立的索引；若不存在这样的索引，则返回endIndex。 |

