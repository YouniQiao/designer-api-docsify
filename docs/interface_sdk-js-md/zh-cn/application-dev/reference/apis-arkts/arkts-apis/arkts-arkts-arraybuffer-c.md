# ArrayBuffer

与JS ArrayBuffer API兼容的类。 用于表示通用的、固定长度的原始二进制数据缓冲区。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## at

```TypeScript
public at(pos: int): byte
```

返回指定索引处的字节。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pos | int | 是 |

**返回值：**

| 类型 |
| --- |
| byte |

## atomicAddI16

```TypeScript
public atomicAddI16(index: int, byteOffset: int, value: short): long
```

以原子方式将一个值加到指定索引处的元素上。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | short | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicAddI32

```TypeScript
public atomicAddI32(index: int, byteOffset: int, value: int): long
```

以原子方式将一个值加到指定索引处的元素上。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicAddI64

```TypeScript
public atomicAddI64(index: int, byteOffset: int, value: long): long
```

以原子方式将一个值加到指定索引处的元素上。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | long | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicAddI8

```TypeScript
public atomicAddI8(index: int, byteOffset: int, value: byte): long
```

以原子方式将一个值加到指定索引处的元素上。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | byte | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicAddU16

```TypeScript
public atomicAddU16(index: int, byteOffset: int, value: short): long
```

以原子方式将一个值加到指定索引处的元素上。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | short | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicAddU32

```TypeScript
public atomicAddU32(index: int, byteOffset: int, value: int): long
```

以原子方式将一个值加到指定索引处的元素上。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicAddU64

```TypeScript
public atomicAddU64(index: int, byteOffset: int, value: long): long
```

以原子方式将一个值加到指定索引处的元素上。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | long | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicAddU8

```TypeScript
public atomicAddU8(index: int, byteOffset: int, value: byte): long
```

以原子方式将一个值加到指定索引处的元素上。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | byte | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicAndI16

```TypeScript
public atomicAndI16(index: int, byteOffset: int, value: short): long
```

以原子方式对指定索引处的元素执行按位与运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | short | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicAndI32

```TypeScript
public atomicAndI32(index: int, byteOffset: int, value: int): long
```

以原子方式对指定索引处的元素执行按位与运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicAndI64

```TypeScript
public atomicAndI64(index: int, byteOffset: int, value: long): long
```

以原子方式对指定索引处的元素执行按位与运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | long | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicAndI8

```TypeScript
public atomicAndI8(index: int, byteOffset: int, value: byte): long
```

以原子方式对指定索引处的元素执行按位与运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | byte | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicAndU16

```TypeScript
public atomicAndU16(index: int, byteOffset: int, value: short): long
```

以原子方式对指定索引处的元素执行按位与运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | short | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicAndU32

```TypeScript
public atomicAndU32(index: int, byteOffset: int, value: int): long
```

以原子方式对指定索引处的元素执行按位与运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicAndU64

```TypeScript
public atomicAndU64(index: int, byteOffset: int, value: long): long
```

以原子方式对指定索引处的元素执行按位与运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | long | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicAndU8

```TypeScript
public atomicAndU8(index: int, byteOffset: int, value: byte): long
```

以原子方式对指定索引处的元素执行按位与运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | byte | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicCompareExchangeI16

```TypeScript
public atomicCompareExchangeI16(index: int, byteOffset: int, expectedValue: short, replacementValue: short): long
```

以原子方式比较并交换指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| expectedValue | short | 是 |
| replacementValue | short | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicCompareExchangeI32

```TypeScript
public atomicCompareExchangeI32(index: int, byteOffset: int, expectedValue: int, replacementValue: int): long
```

以原子方式比较并交换指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| expectedValue | int | 是 |
| replacementValue | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicCompareExchangeI64

```TypeScript
public atomicCompareExchangeI64(index: int, byteOffset: int, expectedValue: long, replacementValue: long): long
```

以原子方式比较并交换指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| expectedValue | long | 是 |
| replacementValue | long | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicCompareExchangeI8

```TypeScript
public atomicCompareExchangeI8(index: int, byteOffset: int, expectedValue: byte, replacementValue: byte): long
```

以原子方式比较并交换指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| expectedValue | byte | 是 |
| replacementValue | byte | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicCompareExchangeU16

```TypeScript
public atomicCompareExchangeU16(index: int, byteOffset: int, expectedValue: short, replacementValue: short): long
```

以原子方式比较并交换指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| expectedValue | short | 是 |
| replacementValue | short | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicCompareExchangeU32

```TypeScript
public atomicCompareExchangeU32(index: int, byteOffset: int, expectedValue: int, replacementValue: int): long
```

以原子方式比较并交换指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| expectedValue | int | 是 |
| replacementValue | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicCompareExchangeU64

```TypeScript
public atomicCompareExchangeU64(index: int, byteOffset: int, expectedValue: long, replacementValue: long): long
```

以原子方式比较并交换指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| expectedValue | long | 是 |
| replacementValue | long | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicCompareExchangeU8

```TypeScript
public atomicCompareExchangeU8(index: int, byteOffset: int, expectedValue: byte, replacementValue: byte): long
```

以原子方式比较并交换指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| expectedValue | byte | 是 |
| replacementValue | byte | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicExchangeI16

```TypeScript
public atomicExchangeI16(index: int, byteOffset: int, value: short): long
```

以原子方式交换指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | short | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicExchangeI32

```TypeScript
public atomicExchangeI32(index: int, byteOffset: int, value: int): long
```

以原子方式交换指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicExchangeI64

```TypeScript
public atomicExchangeI64(index: int, byteOffset: int, value: long): long
```

以原子方式交换指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | long | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicExchangeI8

```TypeScript
public atomicExchangeI8(index: int, byteOffset: int, value: byte): long
```

以原子方式交换指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | byte | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicExchangeU16

```TypeScript
public atomicExchangeU16(index: int, byteOffset: int, value: short): long
```

以原子方式交换指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | short | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicExchangeU32

```TypeScript
public atomicExchangeU32(index: int, byteOffset: int, value: int): long
```

以原子方式交换指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicExchangeU64

```TypeScript
public atomicExchangeU64(index: int, byteOffset: int, value: long): long
```

以原子方式交换指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | long | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicExchangeU8

```TypeScript
public atomicExchangeU8(index: int, byteOffset: int, value: byte): long
```

以原子方式交换指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | byte | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicLoadI16

```TypeScript
public atomicLoadI16(index: int, byteOffset: int): long
```

以原子方式加载指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicLoadI32

```TypeScript
public atomicLoadI32(index: int, byteOffset: int): long
```

以原子方式加载指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicLoadI64

```TypeScript
public atomicLoadI64(index: int, byteOffset: int): long
```

以原子方式加载指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicLoadI8

```TypeScript
public atomicLoadI8(index: int, byteOffset: int): long
```

以原子方式加载指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicLoadU16

```TypeScript
public atomicLoadU16(index: int, byteOffset: int): long
```

以原子方式加载指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicLoadU32

```TypeScript
public atomicLoadU32(index: int, byteOffset: int): long
```

以原子方式加载指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicLoadU64

```TypeScript
public atomicLoadU64(index: int, byteOffset: int): long
```

以原子方式加载指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicLoadU8

```TypeScript
public atomicLoadU8(index: int, byteOffset: int): long
```

以原子方式加载指定索引处的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicOrI16

```TypeScript
public atomicOrI16(index: int, byteOffset: int, value: short): long
```

以原子方式对指定索引处的元素执行按位或运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | short | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicOrI32

```TypeScript
public atomicOrI32(index: int, byteOffset: int, value: int): long
```

以原子方式对指定索引处的元素执行按位或运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicOrI64

```TypeScript
public atomicOrI64(index: int, byteOffset: int, value: long): long
```

以原子方式对指定索引处的元素执行按位或运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | long | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicOrI8

```TypeScript
public atomicOrI8(index: int, byteOffset: int, value: byte): long
```

以原子方式对指定索引处的元素执行按位或运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | byte | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicOrU16

```TypeScript
public atomicOrU16(index: int, byteOffset: int, value: short): long
```

以原子方式对指定索引处的元素执行按位或运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | short | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicOrU32

```TypeScript
public atomicOrU32(index: int, byteOffset: int, value: int): long
```

以原子方式对指定索引处的元素执行按位或运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicOrU64

```TypeScript
public atomicOrU64(index: int, byteOffset: int, value: long): long
```

以原子方式对指定索引处的元素执行按位或运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | long | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicOrU8

```TypeScript
public atomicOrU8(index: int, byteOffset: int, value: byte): long
```

以原子方式对指定索引处的元素执行按位或运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | byte | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicStoreI16

```TypeScript
public atomicStoreI16(index: int, byteOffset: int, value: short): long
```

以原子方式在指定索引处存储一个值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | short | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicStoreI32

```TypeScript
public atomicStoreI32(index: int, byteOffset: int, value: int): long
```

以原子方式在指定索引处存储一个值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicStoreI64

```TypeScript
public atomicStoreI64(index: int, byteOffset: int, value: long): long
```

以原子方式在指定索引处存储一个值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | long | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicStoreI8

```TypeScript
public atomicStoreI8(index: int, byteOffset: int, value: byte): long
```

以原子方式在指定索引处存储一个值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | byte | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicStoreU16

```TypeScript
public atomicStoreU16(index: int, byteOffset: int, value: short): long
```

以原子方式在指定索引处存储一个值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | short | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicStoreU32

```TypeScript
public atomicStoreU32(index: int, byteOffset: int, value: int): long
```

以原子方式在指定索引处存储一个值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicStoreU64

```TypeScript
public atomicStoreU64(index: int, byteOffset: int, value: long): long
```

以原子方式在指定索引处存储一个值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | long | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicStoreU8

```TypeScript
public atomicStoreU8(index: int, byteOffset: int, value: byte): long
```

以原子方式在指定索引处存储一个值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | byte | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicSubI16

```TypeScript
public atomicSubI16(index: int, byteOffset: int, value: short): long
```

以原子方式从指定索引处的元素中减去一个值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | short | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicSubI32

```TypeScript
public atomicSubI32(index: int, byteOffset: int, value: int): long
```

以原子方式从指定索引处的元素中减去一个值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicSubI64

```TypeScript
public atomicSubI64(index: int, byteOffset: int, value: long): long
```

以原子方式从指定索引处的元素中减去一个值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | long | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicSubI8

```TypeScript
public atomicSubI8(index: int, byteOffset: int, value: byte): long
```

以原子方式从指定索引处的元素中减去一个值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | byte | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicSubU16

```TypeScript
public atomicSubU16(index: int, byteOffset: int, value: short): long
```

以原子方式从指定索引处的元素中减去一个值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | short | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicSubU32

```TypeScript
public atomicSubU32(index: int, byteOffset: int, value: int): long
```

以原子方式从指定索引处的元素中减去一个值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicSubU64

```TypeScript
public atomicSubU64(index: int, byteOffset: int, value: long): long
```

以原子方式从指定索引处的元素中减去一个值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | long | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicSubU8

```TypeScript
public atomicSubU8(index: int, byteOffset: int, value: byte): long
```

以原子方式从指定索引处的元素中减去一个值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | byte | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicXorI16

```TypeScript
public atomicXorI16(index: int, byteOffset: int, value: short): long
```

以原子方式对指定索引处的元素执行按位异或运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | short | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicXorI32

```TypeScript
public atomicXorI32(index: int, byteOffset: int, value: int): long
```

以原子方式对指定索引处的元素执行按位异或运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicXorI64

```TypeScript
public atomicXorI64(index: int, byteOffset: int, value: long): long
```

以原子方式对指定索引处的元素执行按位异或运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | long | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicXorI8

```TypeScript
public atomicXorI8(index: int, byteOffset: int, value: byte): long
```

以原子方式对指定索引处的元素执行按位异或运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | byte | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicXorU16

```TypeScript
public atomicXorU16(index: int, byteOffset: int, value: short): long
```

以原子方式对指定索引处的元素执行按位异或运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | short | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicXorU32

```TypeScript
public atomicXorU32(index: int, byteOffset: int, value: int): long
```

以原子方式对指定索引处的元素执行按位异或运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicXorU64

```TypeScript
public atomicXorU64(index: int, byteOffset: int, value: long): long
```

以原子方式对指定索引处的元素执行按位异或运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | long | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## atomicXorU8

```TypeScript
public atomicXorU8(index: int, byteOffset: int, value: byte): long
```

以原子方式对指定索引处的元素执行按位异或运算。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| byteOffset | int | 是 |
| value | byte | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## bytesLength

```TypeScript
public static bytesLength(text: string, encoding: string): int
```

返回字符串在给定编码下的字节长度。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| encoding | string | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## constructor

```TypeScript
constructor(length: int, maxByteLength?: int)
```

创建一个大小等于length参数的ArrayBuffer。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | int | 是 |
| maxByteLength | int | 否 |

## constructor

```TypeScript
public constructor(length: double, maxByteLength?: double)
```

创建一个大小等于length参数的ArrayBuffer。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | double | 是 |
| maxByteLength | double | 否 |

## from

```TypeScript
public static from(arr: FixedArray<byte>): ArrayBuffer
```

根据字节数组创建一个新的ArrayBuffer。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arr | FixedArray & lt;byte & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| ArrayBuffer |

## from

```TypeScript
public static from(u8arr: Uint8Array): ArrayBuffer
```

根据Uint8Array创建一个新的ArrayBuffer。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| u8arr | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| ArrayBuffer |

## from

```TypeScript
public static from(array: double[]): ArrayBuffer
```

根据数字数组创建一个新的ArrayBuffer。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| array | double[] | 是 |

**返回值：**

| 类型 |
| --- |
| ArrayBuffer |

## from

```TypeScript
public static from(str: string, encoding: string): ArrayBuffer
```

根据指定编码的字符串创建一个新的ArrayBuffer。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| str | string | 是 |
| encoding | string | 是 |

**返回值：**

| 类型 |
| --- |
| ArrayBuffer |

## from

```TypeScript
public static from(buff: ArrayBuffer, byteOffset: int, length: int): ArrayBuffer
```

根据已有ArrayBuffer的一个片段创建一个新的ArrayBuffer。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buff | ArrayBuffer | 是 |
| byteOffset | int | 是 |
| length | int | 是 |

**返回值：**

| 类型 |
| --- |
| ArrayBuffer |

## from

```TypeScript
public static from(buffer: ArrayBuffer, byteOffset?: double, length?: double): ArrayBuffer
```

使用数字参数，根据已有ArrayBuffer的一个片段创建一个新的ArrayBuffer。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer | 是 |
| byteOffset | double | 否 |
| length | double | 否 |

**返回值：**

| 类型 |
| --- |
| ArrayBuffer |

## fromObject

```TypeScript
public static fromObject(obj: Object, byteOffsetOrEncoding: int | string, length: int): ArrayBuffer
```

根据对象创建一个新的ArrayBuffer。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | Object | 是 |
| byteOffsetOrEncoding | int \| string | 是 |
| length | int | 是 |

**返回值：**

| 类型 |
| --- |
| ArrayBuffer |

## getByteLength

```TypeScript
public getByteLength(): int
```

返回该ArrayBuffer的字节长度。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| int |

## isView

```TypeScript
public static isView(obj: Object): boolean
```

检查传入的对象是否为ArrayBuffer视图之一。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## resize

```TypeScript
public resize(newLen : int): void
```

将该ArrayBuffer调整为指定长度。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| newLen | int | 是 |

## set

```TypeScript
public set(pos: int, val: byte): void
```

设置指定索引处的字节值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pos | int | 是 |
| val | byte | 是 |

## slice

```TypeScript
public slice(begin: int, end?: int): ArrayBuffer
```

创建一个新的ArrayBuffer，包含[begin, end)范围内字节的副本。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| begin | int | 是 |
| end | int | 否 |

**返回值：**

| 类型 |
| --- |
| ArrayBuffer |

## slice

```TypeScript
public slice(begin: double, end?: double): ArrayBuffer
```

创建一个新的ArrayBuffer，包含[begin, end)范围内字节的副本。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| begin | double | 是 |
| end | double | 否 |

**返回值：**

| 类型 |
| --- |
| ArrayBuffer |

## stringify

```TypeScript
public static stringify(buffer: ArrayBuffer, encoding: string, start: int, end: int): string
```

将ArrayBuffer的一个片段转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer | 是 |
| encoding | string | 是 |
| start | int | 是 |
| end | int | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## toString

```TypeScript
public toString(): string
```

返回该ArrayBuffer的字符串表示。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## byteLength

```TypeScript
get byteLength(): int
```

该ArrayBuffer字节长度的只读属性。

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## detached

```TypeScript
get detached(): boolean
```

如果该ArrayBuffer已分离，则返回true。

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## resizable

```TypeScript
get resizable(): boolean
```

如果该ArrayBuffer可调整大小，则返回true。

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang
