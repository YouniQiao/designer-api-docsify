# toSpliced

## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<boolean>, start: int): FixedArray<boolean>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<boolean>, start: int): FixedArray<boolean>--><!--Device-unnamed-export function toSpliced(self: FixedArray<boolean>, start: int): FixedArray<boolean>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 是 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;boolean&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<boolean>, start: int, del: int, ...items: FixedArray<boolean>)
    : FixedArray<boolean>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<boolean>, start: int, del: int, ...items: FixedArray<boolean>)    : FixedArray<boolean>--><!--Device-unnamed-export function toSpliced(self: FixedArray<boolean>, start: int, del: int, ...items: FixedArray<boolean>)    : FixedArray<boolean>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 是 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |
| del | int | 是 | The number of elements to remove. &lt;br&gt;The value should be an integer. |
| items | FixedArray&lt;boolean&gt; | 是 | The elements to add to the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;boolean&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<boolean>, start?: int, del?: int): FixedArray<boolean>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<boolean>, start?: int, del?: int): FixedArray<boolean>--><!--Device-unnamed-export function toSpliced(self: FixedArray<boolean>, start?: int, del?: int): FixedArray<boolean>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;boolean&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 否 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |
| del | int | 否 | The number of elements to remove. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;boolean&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<byte>, start: int): FixedArray<byte>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<byte>, start: int): FixedArray<byte>--><!--Device-unnamed-export function toSpliced(self: FixedArray<byte>, start: int): FixedArray<byte>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 是 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;byte&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<byte>, start: int, del: int, ...items: FixedArray<byte>): 
    FixedArray<byte>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<byte>, start: int, del: int, ...items: FixedArray<byte>):     FixedArray<byte>--><!--Device-unnamed-export function toSpliced(self: FixedArray<byte>, start: int, del: int, ...items: FixedArray<byte>):     FixedArray<byte>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 是 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |
| del | int | 是 | The number of elements to remove. &lt;br&gt;The value should be an integer. |
| items | FixedArray&lt;byte&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;byte&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<byte>, start?: int, del?: int): FixedArray<byte>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<byte>, start?: int, del?: int): FixedArray<byte>--><!--Device-unnamed-export function toSpliced(self: FixedArray<byte>, start?: int, del?: int): FixedArray<byte>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;byte&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 否 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |
| del | int | 否 | The number of elements to remove. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;byte&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<short>, start: int): FixedArray<short>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<short>, start: int): FixedArray<short>--><!--Device-unnamed-export function toSpliced(self: FixedArray<short>, start: int): FixedArray<short>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 是 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;short&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<short>, start: int, del: int, ...items: FixedArray<short>): 
    FixedArray<short>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<short>, start: int, del: int, ...items: FixedArray<short>):     FixedArray<short>--><!--Device-unnamed-export function toSpliced(self: FixedArray<short>, start: int, del: int, ...items: FixedArray<short>):     FixedArray<short>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 是 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |
| del | int | 是 | The number of elements to remove. &lt;br&gt;The value should be an integer. |
| items | FixedArray&lt;short&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;short&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<short>, start?: int, del?: int): FixedArray<short>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<short>, start?: int, del?: int): FixedArray<short>--><!--Device-unnamed-export function toSpliced(self: FixedArray<short>, start?: int, del?: int): FixedArray<short>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;short&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 否 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |
| del | int | 否 | The number of elements to remove. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;short&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<int>, start: int): FixedArray<int>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<int>, start: int): FixedArray<int>--><!--Device-unnamed-export function toSpliced(self: FixedArray<int>, start: int): FixedArray<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 是 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;int&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<int>, start: int, del: int, ...items: FixedArray<int>): FixedArray<int>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<int>, start: int, del: int, ...items: FixedArray<int>): FixedArray<int>--><!--Device-unnamed-export function toSpliced(self: FixedArray<int>, start: int, del: int, ...items: FixedArray<int>): FixedArray<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 是 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |
| del | int | 是 | The number of elements to remove. &lt;br&gt;The value should be an integer. |
| items | FixedArray&lt;int&gt; | 是 | The elements to add to the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;int&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<int>, start?: int, del?: int): FixedArray<int>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<int>, start?: int, del?: int): FixedArray<int>--><!--Device-unnamed-export function toSpliced(self: FixedArray<int>, start?: int, del?: int): FixedArray<int>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;int&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 否 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |
| del | int | 否 | The number of elements to remove. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;int&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<long>, start: int): FixedArray<long>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<long>, start: int): FixedArray<long>--><!--Device-unnamed-export function toSpliced(self: FixedArray<long>, start: int): FixedArray<long>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 是 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;long&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<long>, start: int, del: int, ...items: FixedArray<long>): 
    FixedArray<long>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<long>, start: int, del: int, ...items: FixedArray<long>):     FixedArray<long>--><!--Device-unnamed-export function toSpliced(self: FixedArray<long>, start: int, del: int, ...items: FixedArray<long>):     FixedArray<long>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 是 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |
| del | int | 是 | The number of elements to remove. &lt;br&gt;The value should be an integer. |
| items | FixedArray&lt;long&gt; | 是 | The elements to add to the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;long&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<long>, start?: int, del?: int): FixedArray<long>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<long>, start?: int, del?: int): FixedArray<long>--><!--Device-unnamed-export function toSpliced(self: FixedArray<long>, start?: int, del?: int): FixedArray<long>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;long&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 否 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |
| del | int | 否 | The number of elements to remove. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;long&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<float>, start: int): FixedArray<float>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<float>, start: int): FixedArray<float>--><!--Device-unnamed-export function toSpliced(self: FixedArray<float>, start: int): FixedArray<float>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 是 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;float&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<float>, start: int, del: int, ...items: FixedArray<float>): 
    FixedArray<float>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<float>, start: int, del: int, ...items: FixedArray<float>):     FixedArray<float>--><!--Device-unnamed-export function toSpliced(self: FixedArray<float>, start: int, del: int, ...items: FixedArray<float>):     FixedArray<float>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 是 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |
| del | int | 是 | The number of elements to remove. &lt;br&gt;The value should be an integer. |
| items | FixedArray&lt;float&gt; | 是 | The elements to add to the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;float&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<float>, start?: int, del?: int): FixedArray<float>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<float>, start?: int, del?: int): FixedArray<float>--><!--Device-unnamed-export function toSpliced(self: FixedArray<float>, start?: int, del?: int): FixedArray<float>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;float&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 否 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |
| del | int | 否 | The number of elements to remove. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;float&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<double>, start: int): FixedArray<double>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<double>, start: int): FixedArray<double>--><!--Device-unnamed-export function toSpliced(self: FixedArray<double>, start: int): FixedArray<double>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 是 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;double&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<double>, start: int, del: int, ...items: FixedArray<double>): 
    FixedArray<double>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<double>, start: int, del: int, ...items: FixedArray<double>):     FixedArray<double>--><!--Device-unnamed-export function toSpliced(self: FixedArray<double>, start: int, del: int, ...items: FixedArray<double>):     FixedArray<double>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 是 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |
| del | int | 是 | The number of elements to remove. &lt;br&gt;The value should be an integer. |
| items | FixedArray&lt;double&gt; | 是 | The elements to add to the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;double&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<double>, start?: int, del?: int): FixedArray<double>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<double>, start?: int, del?: int): FixedArray<double>--><!--Device-unnamed-export function toSpliced(self: FixedArray<double>, start?: int, del?: int): FixedArray<double>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;double&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 否 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |
| del | int | 否 | The number of elements to remove. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;double&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<char>, start: int): FixedArray<char>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<char>, start: int): FixedArray<char>--><!--Device-unnamed-export function toSpliced(self: FixedArray<char>, start: int): FixedArray<char>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 是 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;char&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<char>, start: int, del: int, ...items: FixedArray<char>): 
    FixedArray<char>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<char>, start: int, del: int, ...items: FixedArray<char>):     FixedArray<char>--><!--Device-unnamed-export function toSpliced(self: FixedArray<char>, start: int, del: int, ...items: FixedArray<char>):     FixedArray<char>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 是 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |
| del | int | 是 | The number of elements to remove. &lt;br&gt;The value should be an integer. |
| items | FixedArray&lt;char&gt; | 是 | The elements to add to the array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;char&gt; | A new array with the changes applied. |


## toSpliced

```TypeScript
export function toSpliced(self: FixedArray<char>, start?: int, del?: int): FixedArray<char>
```

Returns a new array with some elements removed and/or replaced at a given index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function toSpliced(self: FixedArray<char>, start?: int, del?: int): FixedArray<char>--><!--Device-unnamed-export function toSpliced(self: FixedArray<char>, start?: int, del?: int): FixedArray<char>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| self | FixedArray&lt;char&gt; | 是 | The array to operate `toSpliced` on. |
| start | int | 否 | The zero-based index at which to start changing the array. &lt;br&gt;The value should be an integer. |
| del | int | 否 | The number of elements to remove. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;char&gt; | A new array with the changes applied. |

