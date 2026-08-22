# toSpliced

## 导入模块

```TypeScript
```

## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<boolean>, start: int): FixedArray<boolean>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<boolean>, start: int): FixedArray<boolean>--><!--Device-unnamed-export function toSpliced(self: FixedArray<boolean>, start: int): FixedArray<boolean>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 是 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;boolean&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<boolean>, start: int, del: int, ...items: FixedArray<boolean>)
    : FixedArray<boolean>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<boolean>, start: int, del: int, ...items: FixedArray<boolean>)    : FixedArray<boolean>--><!--Device-unnamed-export function toSpliced(self: FixedArray<boolean>, start: int, del: int, ...items: FixedArray<boolean>)    : FixedArray<boolean>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 是 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |
| del | int | 是 | 待移除元素的number。 <br>取值约束：应为整数。 |
| items | FixedArray&lt;boolean&gt; | 是 | 待添加到数组中的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;boolean&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<boolean>, start?: int, del?: int): FixedArray<boolean>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<boolean>, start?: int, del?: int): FixedArray<boolean>--><!--Device-unnamed-export function toSpliced(self: FixedArray<boolean>, start?: int, del?: int): FixedArray<boolean>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 否 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |
| del | int | 否 | 待移除元素的number。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;boolean&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<byte>, start: int): FixedArray<byte>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<byte>, start: int): FixedArray<byte>--><!--Device-unnamed-export function toSpliced(self: FixedArray<byte>, start: int): FixedArray<byte>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 是 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;byte&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<byte>, start: int, del: int, ...items: FixedArray<byte>): 
    FixedArray<byte>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<byte>, start: int, del: int, ...items: FixedArray<byte>):     FixedArray<byte>--><!--Device-unnamed-export function toSpliced(self: FixedArray<byte>, start: int, del: int, ...items: FixedArray<byte>):     FixedArray<byte>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 是 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |
| del | int | 是 | 待移除元素的number。 <br>取值约束：应为整数。 |
| items | FixedArray&lt;byte&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;byte&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<byte>, start?: int, del?: int): FixedArray<byte>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<byte>, start?: int, del?: int): FixedArray<byte>--><!--Device-unnamed-export function toSpliced(self: FixedArray<byte>, start?: int, del?: int): FixedArray<byte>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 否 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |
| del | int | 否 | 待移除元素的number。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;byte&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<short>, start: int): FixedArray<short>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<short>, start: int): FixedArray<short>--><!--Device-unnamed-export function toSpliced(self: FixedArray<short>, start: int): FixedArray<short>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 是 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;short&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<short>, start: int, del: int, ...items: FixedArray<short>): 
    FixedArray<short>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<short>, start: int, del: int, ...items: FixedArray<short>):     FixedArray<short>--><!--Device-unnamed-export function toSpliced(self: FixedArray<short>, start: int, del: int, ...items: FixedArray<short>):     FixedArray<short>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 是 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |
| del | int | 是 | 待移除元素的number。 <br>取值约束：应为整数。 |
| items | FixedArray&lt;short&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;short&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<short>, start?: int, del?: int): FixedArray<short>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<short>, start?: int, del?: int): FixedArray<short>--><!--Device-unnamed-export function toSpliced(self: FixedArray<short>, start?: int, del?: int): FixedArray<short>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 否 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |
| del | int | 否 | 待移除元素的number。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;short&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<int>, start: int): FixedArray<int>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<int>, start: int): FixedArray<int>--><!--Device-unnamed-export function toSpliced(self: FixedArray<int>, start: int): FixedArray<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 是 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;int&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<int>, start: int, del: int, ...items: FixedArray<int>): FixedArray<int>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<int>, start: int, del: int, ...items: FixedArray<int>): FixedArray<int>--><!--Device-unnamed-export function toSpliced(self: FixedArray<int>, start: int, del: int, ...items: FixedArray<int>): FixedArray<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 是 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |
| del | int | 是 | 待移除元素的number。 <br>取值约束：应为整数。 |
| items | FixedArray&lt;int&gt; | 是 | 待添加到数组中的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;int&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<int>, start?: int, del?: int): FixedArray<int>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<int>, start?: int, del?: int): FixedArray<int>--><!--Device-unnamed-export function toSpliced(self: FixedArray<int>, start?: int, del?: int): FixedArray<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 否 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |
| del | int | 否 | 待移除元素的number。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;int&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<long>, start: int): FixedArray<long>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<long>, start: int): FixedArray<long>--><!--Device-unnamed-export function toSpliced(self: FixedArray<long>, start: int): FixedArray<long>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 是 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;long&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<long>, start: int, del: int, ...items: FixedArray<long>): 
    FixedArray<long>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<long>, start: int, del: int, ...items: FixedArray<long>):     FixedArray<long>--><!--Device-unnamed-export function toSpliced(self: FixedArray<long>, start: int, del: int, ...items: FixedArray<long>):     FixedArray<long>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 是 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |
| del | int | 是 | 待移除元素的number。 <br>取值约束：应为整数。 |
| items | FixedArray&lt;long&gt; | 是 | 待添加到数组中的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;long&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<long>, start?: int, del?: int): FixedArray<long>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<long>, start?: int, del?: int): FixedArray<long>--><!--Device-unnamed-export function toSpliced(self: FixedArray<long>, start?: int, del?: int): FixedArray<long>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 否 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |
| del | int | 否 | 待移除元素的number。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;long&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<float>, start: int): FixedArray<float>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<float>, start: int): FixedArray<float>--><!--Device-unnamed-export function toSpliced(self: FixedArray<float>, start: int): FixedArray<float>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 是 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;float&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<float>, start: int, del: int, ...items: FixedArray<float>): 
    FixedArray<float>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<float>, start: int, del: int, ...items: FixedArray<float>):     FixedArray<float>--><!--Device-unnamed-export function toSpliced(self: FixedArray<float>, start: int, del: int, ...items: FixedArray<float>):     FixedArray<float>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 是 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |
| del | int | 是 | 待移除元素的number。 <br>取值约束：应为整数。 |
| items | FixedArray&lt;float&gt; | 是 | 待添加到数组中的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;float&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<float>, start?: int, del?: int): FixedArray<float>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<float>, start?: int, del?: int): FixedArray<float>--><!--Device-unnamed-export function toSpliced(self: FixedArray<float>, start?: int, del?: int): FixedArray<float>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 否 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |
| del | int | 否 | 待移除元素的number。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;float&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<double>, start: int): FixedArray<double>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<double>, start: int): FixedArray<double>--><!--Device-unnamed-export function toSpliced(self: FixedArray<double>, start: int): FixedArray<double>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 是 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;double&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<double>, start: int, del: int, ...items: FixedArray<double>): 
    FixedArray<double>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<double>, start: int, del: int, ...items: FixedArray<double>):     FixedArray<double>--><!--Device-unnamed-export function toSpliced(self: FixedArray<double>, start: int, del: int, ...items: FixedArray<double>):     FixedArray<double>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 是 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |
| del | int | 是 | 待移除元素的number。 <br>取值约束：应为整数。 |
| items | FixedArray&lt;double&gt; | 是 | 待添加到数组中的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;double&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<double>, start?: int, del?: int): FixedArray<double>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<double>, start?: int, del?: int): FixedArray<double>--><!--Device-unnamed-export function toSpliced(self: FixedArray<double>, start?: int, del?: int): FixedArray<double>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 否 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |
| del | int | 否 | 待移除元素的number。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;double&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<char>, start: int): FixedArray<char>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<char>, start: int): FixedArray<char>--><!--Device-unnamed-export function toSpliced(self: FixedArray<char>, start: int): FixedArray<char>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 是 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;char&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<char>, start: int, del: int, ...items: FixedArray<char>): 
    FixedArray<char>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<char>, start: int, del: int, ...items: FixedArray<char>):     FixedArray<char>--><!--Device-unnamed-export function toSpliced(self: FixedArray<char>, start: int, del: int, ...items: FixedArray<char>):     FixedArray<char>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 是 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |
| del | int | 是 | 待移除元素的number。 <br>取值约束：应为整数。 |
| items | FixedArray&lt;char&gt; | 是 | 待添加到数组中的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;char&gt; | 应用修改后的新数组。 |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<char>, start?: int, del?: int): FixedArray<char>
```

返回在指定索引处移除或替换部分元素后的新数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<char>, start?: int, del?: int): FixedArray<char>--><!--Device-unnamed-export function toSpliced(self: FixedArray<char>, start?: int, del?: int): FixedArray<char>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | 是 | 执行`toSpliced`操作的数组。 |
| start | int | 否 | 开始修改数组的索引，从0开始计数。 <br>取值约束：应为整数。 |
| del | int | 否 | 待移除元素的number。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;char&gt; | 应用修改后的新数组。 |

