# ArrayBuffer

JS ArrayBuffer API-compatible class.Used to represent a generic, fixed-length raw binary data buffer.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

<!--Device-unnamed-export class ArrayBuffer--><!--Device-unnamed-export class ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

## at

```TypeScript
public at(pos: int): byte
```

Returns the byte at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public at(pos: int): byte--><!--Device-ArrayBuffer-public at(pos: int): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pos | int | 是 | The position in the buffer. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | The byte value. |

## atomicAddI16

```TypeScript
public atomicAddI16(index: int, byteOffset: int, value: short): long
```

Atomically adds a value to the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicAddI16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicAddI16(index: int, byteOffset: int, value: short): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | 是 | The value to add. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicAddI32

```TypeScript
public atomicAddI32(index: int, byteOffset: int, value: int): long
```

Atomically adds a value to the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicAddI32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicAddI32(index: int, byteOffset: int, value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | 是 | The value to add. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicAddI64

```TypeScript
public atomicAddI64(index: int, byteOffset: int, value: long): long
```

Atomically adds a value to the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicAddI64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicAddI64(index: int, byteOffset: int, value: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | 是 | The value to add. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicAddI8

```TypeScript
public atomicAddI8(index: int, byteOffset: int, value: byte): long
```

Atomically adds a value to the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicAddI8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicAddI8(index: int, byteOffset: int, value: byte): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | 是 | The value to add. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicAddU16

```TypeScript
public atomicAddU16(index: int, byteOffset: int, value: short): long
```

Atomically adds a value to the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicAddU16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicAddU16(index: int, byteOffset: int, value: short): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | 是 | The value to add. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicAddU32

```TypeScript
public atomicAddU32(index: int, byteOffset: int, value: int): long
```

Atomically adds a value to the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicAddU32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicAddU32(index: int, byteOffset: int, value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | 是 | The value to add. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicAddU64

```TypeScript
public atomicAddU64(index: int, byteOffset: int, value: long): long
```

Atomically adds a value to the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicAddU64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicAddU64(index: int, byteOffset: int, value: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | 是 | The value to add. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicAddU8

```TypeScript
public atomicAddU8(index: int, byteOffset: int, value: byte): long
```

Atomically adds a value to the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicAddU8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicAddU8(index: int, byteOffset: int, value: byte): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | 是 | The value to add. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicAndI16

```TypeScript
public atomicAndI16(index: int, byteOffset: int, value: short): long
```

Atomically performs a bitwise AND operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicAndI16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicAndI16(index: int, byteOffset: int, value: short): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | 是 | The value to AND with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicAndI32

```TypeScript
public atomicAndI32(index: int, byteOffset: int, value: int): long
```

Atomically performs a bitwise AND operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicAndI32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicAndI32(index: int, byteOffset: int, value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | 是 | The value to AND with. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicAndI64

```TypeScript
public atomicAndI64(index: int, byteOffset: int, value: long): long
```

Atomically performs a bitwise AND operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicAndI64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicAndI64(index: int, byteOffset: int, value: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | 是 | The value to AND with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicAndI8

```TypeScript
public atomicAndI8(index: int, byteOffset: int, value: byte): long
```

Atomically performs a bitwise AND operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicAndI8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicAndI8(index: int, byteOffset: int, value: byte): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | 是 | The value to AND with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicAndU16

```TypeScript
public atomicAndU16(index: int, byteOffset: int, value: short): long
```

Atomically performs a bitwise AND operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicAndU16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicAndU16(index: int, byteOffset: int, value: short): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | 是 | The value to AND with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicAndU32

```TypeScript
public atomicAndU32(index: int, byteOffset: int, value: int): long
```

Atomically performs a bitwise AND operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicAndU32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicAndU32(index: int, byteOffset: int, value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | 是 | The value to AND with. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicAndU64

```TypeScript
public atomicAndU64(index: int, byteOffset: int, value: long): long
```

Atomically performs a bitwise AND operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicAndU64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicAndU64(index: int, byteOffset: int, value: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | 是 | The value to AND with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicAndU8

```TypeScript
public atomicAndU8(index: int, byteOffset: int, value: byte): long
```

Atomically performs a bitwise AND operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicAndU8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicAndU8(index: int, byteOffset: int, value: byte): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | 是 | The value to AND with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicCompareExchangeI16

```TypeScript
public atomicCompareExchangeI16(index: int, byteOffset: int, expectedValue: short, replacementValue: short): long
```

Atomically compares and exchanges the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicCompareExchangeI16(index: int, byteOffset: int, expectedValue: short, replacementValue: short): long--><!--Device-ArrayBuffer-public atomicCompareExchangeI16(index: int, byteOffset: int, expectedValue: short, replacementValue: short): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| expectedValue | short | 是 | The expected value. |
| replacementValue | short | 是 | The replacement value. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicCompareExchangeI32

```TypeScript
public atomicCompareExchangeI32(index: int, byteOffset: int, expectedValue: int, replacementValue: int): long
```

Atomically compares and exchanges the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicCompareExchangeI32(index: int, byteOffset: int, expectedValue: int, replacementValue: int): long--><!--Device-ArrayBuffer-public atomicCompareExchangeI32(index: int, byteOffset: int, expectedValue: int, replacementValue: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| expectedValue | int | 是 | The expected value. &lt;br&gt;The value should be an integer. |
| replacementValue | int | 是 | The replacement value. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicCompareExchangeI64

```TypeScript
public atomicCompareExchangeI64(index: int, byteOffset: int, expectedValue: long, replacementValue: long): long
```

Atomically compares and exchanges the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicCompareExchangeI64(index: int, byteOffset: int, expectedValue: long, replacementValue: long): long--><!--Device-ArrayBuffer-public atomicCompareExchangeI64(index: int, byteOffset: int, expectedValue: long, replacementValue: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| expectedValue | long | 是 | The expected value. |
| replacementValue | long | 是 | The replacement value. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicCompareExchangeI8

```TypeScript
public atomicCompareExchangeI8(index: int, byteOffset: int, expectedValue: byte, replacementValue: byte): long
```

Atomically compares and exchanges the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicCompareExchangeI8(index: int, byteOffset: int, expectedValue: byte, replacementValue: byte): long--><!--Device-ArrayBuffer-public atomicCompareExchangeI8(index: int, byteOffset: int, expectedValue: byte, replacementValue: byte): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| expectedValue | byte | 是 | The expected value. |
| replacementValue | byte | 是 | The replacement value. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicCompareExchangeU16

```TypeScript
public atomicCompareExchangeU16(index: int, byteOffset: int, expectedValue: short, replacementValue: short): long
```

Atomically compares and exchanges the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicCompareExchangeU16(index: int, byteOffset: int, expectedValue: short, replacementValue: short): long--><!--Device-ArrayBuffer-public atomicCompareExchangeU16(index: int, byteOffset: int, expectedValue: short, replacementValue: short): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| expectedValue | short | 是 | The expected value. |
| replacementValue | short | 是 | The replacement value. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicCompareExchangeU32

```TypeScript
public atomicCompareExchangeU32(index: int, byteOffset: int, expectedValue: int, replacementValue: int): long
```

Atomically compares and exchanges the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicCompareExchangeU32(index: int, byteOffset: int, expectedValue: int, replacementValue: int): long--><!--Device-ArrayBuffer-public atomicCompareExchangeU32(index: int, byteOffset: int, expectedValue: int, replacementValue: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| expectedValue | int | 是 | The expected value. &lt;br&gt;The value should be an integer. |
| replacementValue | int | 是 | The replacement value. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicCompareExchangeU64

```TypeScript
public atomicCompareExchangeU64(index: int, byteOffset: int, expectedValue: long, replacementValue: long): long
```

Atomically compares and exchanges the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicCompareExchangeU64(index: int, byteOffset: int, expectedValue: long, replacementValue: long): long--><!--Device-ArrayBuffer-public atomicCompareExchangeU64(index: int, byteOffset: int, expectedValue: long, replacementValue: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| expectedValue | long | 是 | The expected value. |
| replacementValue | long | 是 | The replacement value. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicCompareExchangeU8

```TypeScript
public atomicCompareExchangeU8(index: int, byteOffset: int, expectedValue: byte, replacementValue: byte): long
```

Atomically compares and exchanges the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicCompareExchangeU8(index: int, byteOffset: int, expectedValue: byte, replacementValue: byte): long--><!--Device-ArrayBuffer-public atomicCompareExchangeU8(index: int, byteOffset: int, expectedValue: byte, replacementValue: byte): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| expectedValue | byte | 是 | The expected value. |
| replacementValue | byte | 是 | The replacement value. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicExchangeI16

```TypeScript
public atomicExchangeI16(index: int, byteOffset: int, value: short): long
```

Atomically exchanges the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicExchangeI16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicExchangeI16(index: int, byteOffset: int, value: short): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | 是 | The value to exchange. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicExchangeI32

```TypeScript
public atomicExchangeI32(index: int, byteOffset: int, value: int): long
```

Atomically exchanges the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicExchangeI32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicExchangeI32(index: int, byteOffset: int, value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | 是 | The value to exchange. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicExchangeI64

```TypeScript
public atomicExchangeI64(index: int, byteOffset: int, value: long): long
```

Atomically exchanges the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicExchangeI64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicExchangeI64(index: int, byteOffset: int, value: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | 是 | The value to exchange. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicExchangeI8

```TypeScript
public atomicExchangeI8(index: int, byteOffset: int, value: byte): long
```

Atomically exchanges the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicExchangeI8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicExchangeI8(index: int, byteOffset: int, value: byte): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | 是 | The value to exchange. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicExchangeU16

```TypeScript
public atomicExchangeU16(index: int, byteOffset: int, value: short): long
```

Atomically exchanges the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicExchangeU16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicExchangeU16(index: int, byteOffset: int, value: short): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | 是 | The value to exchange. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicExchangeU32

```TypeScript
public atomicExchangeU32(index: int, byteOffset: int, value: int): long
```

Atomically exchanges the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicExchangeU32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicExchangeU32(index: int, byteOffset: int, value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | 是 | The value to exchange. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicExchangeU64

```TypeScript
public atomicExchangeU64(index: int, byteOffset: int, value: long): long
```

Atomically exchanges the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicExchangeU64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicExchangeU64(index: int, byteOffset: int, value: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | 是 | The value to exchange. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicExchangeU8

```TypeScript
public atomicExchangeU8(index: int, byteOffset: int, value: byte): long
```

Atomically exchanges the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicExchangeU8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicExchangeU8(index: int, byteOffset: int, value: byte): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | 是 | The value to exchange. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicLoadI16

```TypeScript
public atomicLoadI16(index: int, byteOffset: int): long
```

Atomically loads the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicLoadI16(index: int, byteOffset: int): long--><!--Device-ArrayBuffer-public atomicLoadI16(index: int, byteOffset: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicLoadI32

```TypeScript
public atomicLoadI32(index: int, byteOffset: int): long
```

Atomically loads the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicLoadI32(index: int, byteOffset: int): long--><!--Device-ArrayBuffer-public atomicLoadI32(index: int, byteOffset: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicLoadI64

```TypeScript
public atomicLoadI64(index: int, byteOffset: int): long
```

Atomically loads the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicLoadI64(index: int, byteOffset: int): long--><!--Device-ArrayBuffer-public atomicLoadI64(index: int, byteOffset: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicLoadI8

```TypeScript
public atomicLoadI8(index: int, byteOffset: int): long
```

Atomically loads the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicLoadI8(index: int, byteOffset: int): long--><!--Device-ArrayBuffer-public atomicLoadI8(index: int, byteOffset: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicLoadU16

```TypeScript
public atomicLoadU16(index: int, byteOffset: int): long
```

Atomically loads the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicLoadU16(index: int, byteOffset: int): long--><!--Device-ArrayBuffer-public atomicLoadU16(index: int, byteOffset: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicLoadU32

```TypeScript
public atomicLoadU32(index: int, byteOffset: int): long
```

Atomically loads the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicLoadU32(index: int, byteOffset: int): long--><!--Device-ArrayBuffer-public atomicLoadU32(index: int, byteOffset: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicLoadU64

```TypeScript
public atomicLoadU64(index: int, byteOffset: int): long
```

Atomically loads the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicLoadU64(index: int, byteOffset: int): long--><!--Device-ArrayBuffer-public atomicLoadU64(index: int, byteOffset: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicLoadU8

```TypeScript
public atomicLoadU8(index: int, byteOffset: int): long
```

Atomically loads the value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicLoadU8(index: int, byteOffset: int): long--><!--Device-ArrayBuffer-public atomicLoadU8(index: int, byteOffset: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicOrI16

```TypeScript
public atomicOrI16(index: int, byteOffset: int, value: short): long
```

Atomically performs a bitwise OR operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicOrI16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicOrI16(index: int, byteOffset: int, value: short): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | 是 | The value to OR with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicOrI32

```TypeScript
public atomicOrI32(index: int, byteOffset: int, value: int): long
```

Atomically performs a bitwise OR operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicOrI32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicOrI32(index: int, byteOffset: int, value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | 是 | The value to OR with. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicOrI64

```TypeScript
public atomicOrI64(index: int, byteOffset: int, value: long): long
```

Atomically performs a bitwise OR operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicOrI64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicOrI64(index: int, byteOffset: int, value: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | 是 | The value to OR with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicOrI8

```TypeScript
public atomicOrI8(index: int, byteOffset: int, value: byte): long
```

Atomically performs a bitwise OR operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicOrI8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicOrI8(index: int, byteOffset: int, value: byte): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | 是 | The value to OR with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicOrU16

```TypeScript
public atomicOrU16(index: int, byteOffset: int, value: short): long
```

Atomically performs a bitwise OR operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicOrU16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicOrU16(index: int, byteOffset: int, value: short): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | 是 | The value to OR with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicOrU32

```TypeScript
public atomicOrU32(index: int, byteOffset: int, value: int): long
```

Atomically performs a bitwise OR operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicOrU32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicOrU32(index: int, byteOffset: int, value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | 是 | The value to OR with. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicOrU64

```TypeScript
public atomicOrU64(index: int, byteOffset: int, value: long): long
```

Atomically performs a bitwise OR operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicOrU64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicOrU64(index: int, byteOffset: int, value: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | 是 | The value to OR with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicOrU8

```TypeScript
public atomicOrU8(index: int, byteOffset: int, value: byte): long
```

Atomically performs a bitwise OR operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicOrU8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicOrU8(index: int, byteOffset: int, value: byte): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | 是 | The value to OR with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicStoreI16

```TypeScript
public atomicStoreI16(index: int, byteOffset: int, value: short): long
```

Atomically stores a value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicStoreI16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicStoreI16(index: int, byteOffset: int, value: short): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | 是 | The value to store. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The stored value. |

## atomicStoreI32

```TypeScript
public atomicStoreI32(index: int, byteOffset: int, value: int): long
```

Atomically stores a value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicStoreI32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicStoreI32(index: int, byteOffset: int, value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | 是 | The value to store. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The stored value. |

## atomicStoreI64

```TypeScript
public atomicStoreI64(index: int, byteOffset: int, value: long): long
```

Atomically stores a value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicStoreI64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicStoreI64(index: int, byteOffset: int, value: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | 是 | The value to store. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The stored value. |

## atomicStoreI8

```TypeScript
public atomicStoreI8(index: int, byteOffset: int, value: byte): long
```

Atomically stores a value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicStoreI8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicStoreI8(index: int, byteOffset: int, value: byte): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | 是 | The value to store. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The stored value. |

## atomicStoreU16

```TypeScript
public atomicStoreU16(index: int, byteOffset: int, value: short): long
```

Atomically stores a value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicStoreU16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicStoreU16(index: int, byteOffset: int, value: short): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | 是 | The value to store. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The stored value. |

## atomicStoreU32

```TypeScript
public atomicStoreU32(index: int, byteOffset: int, value: int): long
```

Atomically stores a value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicStoreU32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicStoreU32(index: int, byteOffset: int, value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | 是 | The value to store. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The stored value. |

## atomicStoreU64

```TypeScript
public atomicStoreU64(index: int, byteOffset: int, value: long): long
```

Atomically stores a value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicStoreU64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicStoreU64(index: int, byteOffset: int, value: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | 是 | The value to store. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The stored value. |

## atomicStoreU8

```TypeScript
public atomicStoreU8(index: int, byteOffset: int, value: byte): long
```

Atomically stores a value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicStoreU8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicStoreU8(index: int, byteOffset: int, value: byte): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | 是 | The value to store. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The stored value. |

## atomicSubI16

```TypeScript
public atomicSubI16(index: int, byteOffset: int, value: short): long
```

Atomically subtracts a value from the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicSubI16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicSubI16(index: int, byteOffset: int, value: short): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | 是 | The value to subtract. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicSubI32

```TypeScript
public atomicSubI32(index: int, byteOffset: int, value: int): long
```

Atomically subtracts a value from the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicSubI32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicSubI32(index: int, byteOffset: int, value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | 是 | The value to subtract. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicSubI64

```TypeScript
public atomicSubI64(index: int, byteOffset: int, value: long): long
```

Atomically subtracts a value from the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicSubI64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicSubI64(index: int, byteOffset: int, value: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | 是 | The value to subtract. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicSubI8

```TypeScript
public atomicSubI8(index: int, byteOffset: int, value: byte): long
```

Atomically subtracts a value from the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicSubI8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicSubI8(index: int, byteOffset: int, value: byte): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | 是 | The value to subtract. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicSubU16

```TypeScript
public atomicSubU16(index: int, byteOffset: int, value: short): long
```

Atomically subtracts a value from the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicSubU16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicSubU16(index: int, byteOffset: int, value: short): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | 是 | The value to subtract. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicSubU32

```TypeScript
public atomicSubU32(index: int, byteOffset: int, value: int): long
```

Atomically subtracts a value from the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicSubU32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicSubU32(index: int, byteOffset: int, value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | 是 | The value to subtract. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicSubU64

```TypeScript
public atomicSubU64(index: int, byteOffset: int, value: long): long
```

Atomically subtracts a value from the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicSubU64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicSubU64(index: int, byteOffset: int, value: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | 是 | The value to subtract. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicSubU8

```TypeScript
public atomicSubU8(index: int, byteOffset: int, value: byte): long
```

Atomically subtracts a value from the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicSubU8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicSubU8(index: int, byteOffset: int, value: byte): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | 是 | The value to subtract. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicXorI16

```TypeScript
public atomicXorI16(index: int, byteOffset: int, value: short): long
```

Atomically performs a bitwise XOR operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicXorI16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicXorI16(index: int, byteOffset: int, value: short): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | 是 | The value to XOR with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicXorI32

```TypeScript
public atomicXorI32(index: int, byteOffset: int, value: int): long
```

Atomically performs a bitwise XOR operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicXorI32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicXorI32(index: int, byteOffset: int, value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | 是 | The value to XOR with. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicXorI64

```TypeScript
public atomicXorI64(index: int, byteOffset: int, value: long): long
```

Atomically performs a bitwise XOR operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicXorI64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicXorI64(index: int, byteOffset: int, value: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | 是 | The value to XOR with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicXorI8

```TypeScript
public atomicXorI8(index: int, byteOffset: int, value: byte): long
```

Atomically performs a bitwise XOR operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicXorI8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicXorI8(index: int, byteOffset: int, value: byte): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | 是 | The value to XOR with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicXorU16

```TypeScript
public atomicXorU16(index: int, byteOffset: int, value: short): long
```

Atomically performs a bitwise XOR operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicXorU16(index: int, byteOffset: int, value: short): long--><!--Device-ArrayBuffer-public atomicXorU16(index: int, byteOffset: int, value: short): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | short | 是 | The value to XOR with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicXorU32

```TypeScript
public atomicXorU32(index: int, byteOffset: int, value: int): long
```

Atomically performs a bitwise XOR operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicXorU32(index: int, byteOffset: int, value: int): long--><!--Device-ArrayBuffer-public atomicXorU32(index: int, byteOffset: int, value: int): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | int | 是 | The value to XOR with. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicXorU64

```TypeScript
public atomicXorU64(index: int, byteOffset: int, value: long): long
```

Atomically performs a bitwise XOR operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicXorU64(index: int, byteOffset: int, value: long): long--><!--Device-ArrayBuffer-public atomicXorU64(index: int, byteOffset: int, value: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | long | 是 | The value to XOR with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## atomicXorU8

```TypeScript
public atomicXorU8(index: int, byteOffset: int, value: byte): long
```

Atomically performs a bitwise XOR operation on the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public atomicXorU8(index: int, byteOffset: int, value: byte): long--><!--Device-ArrayBuffer-public atomicXorU8(index: int, byteOffset: int, value: byte): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to access. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| byteOffset | int | 是 | The byte offset within the ArrayBuffer (unit: byte). &lt;br&gt;The value must be an integer greater than or equal to 0. |
| value | byte | 是 | The value to XOR with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The value after the operation. |

## bytesLength

```TypeScript
public static bytesLength(text: string, encoding: string): int
```

Returns the byte length of a string in a given encoding.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public static bytesLength(text: string, encoding: string): int--><!--Device-ArrayBuffer-public static bytesLength(text: string, encoding: string): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | Source string. |
| encoding | string | 是 | Encoding type. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | Calculated byte length. |

## constructor

```TypeScript
constructor(length: int, maxByteLength?: int)
```

Creates an ArrayBuffer with size equal to the length parameter.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-constructor(length: int, maxByteLength?: int)--><!--Device-ArrayBuffer-constructor(length: int, maxByteLength?: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | int | 是 | The size of the ArrayBuffer in bytes. &lt;br&gt;The value must be an integer greater than or equal to 0. |
| maxByteLength | int | 否 | Optional maximum size the ArrayBuffer can be resized to. &lt;br&gt;The value must be an integer greater than or equal to 0. |

## constructor

```TypeScript
public constructor(length: double, maxByteLength?: double)
```

Creates an ArrayBuffer with size equal to the length parameter.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public constructor(length: double, maxByteLength?: double)--><!--Device-ArrayBuffer-public constructor(length: double, maxByteLength?: double)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | double | 是 | The size of the ArrayBuffer in bytes. &lt;br&gt;The value must be greater than or equal to 0. |
| maxByteLength | double | 否 | Optional maximum size the ArrayBuffer can be resized to. &lt;br&gt;The value must be greater than or equal to 0. |

## from

```TypeScript
public static from(arr: FixedArray<byte>): ArrayBuffer
```

Creates a new ArrayBuffer from an array of bytes.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public static from(arr: FixedArray<byte>): ArrayBuffer--><!--Device-ArrayBuffer-public static from(arr: FixedArray<byte>): ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arr | FixedArray&lt;byte&gt; | 是 | Source byte array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | The new ArrayBuffer. |

## from

```TypeScript
public static from(u8arr: Uint8Array): ArrayBuffer
```

Creates a new ArrayBuffer from a Uint8Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public static from(u8arr: Uint8Array): ArrayBuffer--><!--Device-ArrayBuffer-public static from(u8arr: Uint8Array): ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| u8arr | Uint8Array | 是 | Source typed array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | The new ArrayBuffer. |

## from

```TypeScript
public static from(array: double[]): ArrayBuffer
```

Creates a new ArrayBuffer from an array of numbers.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public static from(array: double[]): ArrayBuffer--><!--Device-ArrayBuffer-public static from(array: double[]): ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | double[] | 是 | Source number array. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | The new ArrayBuffer. |

## from

```TypeScript
public static from(str: string, encoding: string): ArrayBuffer
```

Creates a new ArrayBuffer from a string with specific encoding.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public static from(str: string, encoding: string): ArrayBuffer--><!--Device-ArrayBuffer-public static from(str: string, encoding: string): ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| str | string | 是 | Source string. |
| encoding | string | 是 | String encoding (e.g., "utf8"). |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | The new ArrayBuffer. |

## from

```TypeScript
public static from(buff: ArrayBuffer, byteOffset: int, length: int): ArrayBuffer
```

Creates a new ArrayBuffer from a segment of an existing ArrayBuffer.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public static from(buff: ArrayBuffer, byteOffset: int, length: int): ArrayBuffer--><!--Device-ArrayBuffer-public static from(buff: ArrayBuffer, byteOffset: int, length: int): ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buff | ArrayBuffer | 是 | Source buffer. |
| byteOffset | int | 是 | Start offset in source. &lt;br&gt;The value should be an integer. |
| length | int | 是 | Number of bytes to copy. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | The new ArrayBuffer. |

## from

```TypeScript
public static from(buffer: ArrayBuffer, byteOffset?: double, length?: double): ArrayBuffer
```

Creates a new ArrayBuffer from a segment of an existing ArrayBuffer with number parameters.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public static from(buffer: ArrayBuffer, byteOffset?: double, length?: double): ArrayBuffer--><!--Device-ArrayBuffer-public static from(buffer: ArrayBuffer, byteOffset?: double, length?: double): ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | Source buffer. |
| byteOffset | double | 否 | Start offset. |
| length | double | 否 | Byte length. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | The new ArrayBuffer. |

## fromObject

```TypeScript
public static fromObject(obj: Object, byteOffsetOrEncoding: int | string, length: int): ArrayBuffer
```

Creates a new ArrayBuffer from an object.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public static fromObject(obj: Object, byteOffsetOrEncoding: int | string, length: int): ArrayBuffer--><!--Device-ArrayBuffer-public static fromObject(obj: Object, byteOffsetOrEncoding: int | string, length: int): ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Object | 是 | Source object (string or ArrayBuffer). |
| byteOffsetOrEncoding | int \| string | 是 | Byte offset or encoding string. |
| length | int | 是 | Length to copy. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | The new ArrayBuffer. |

## getByteLength

```TypeScript
public getByteLength(): int
```

Returns the length of the ArrayBuffer in bytes.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public getByteLength(): int--><!--Device-ArrayBuffer-public getByteLength(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The byte length. |

## isView

```TypeScript
public static isView(obj: Object): boolean
```

Checks if the passed object is one of the ArrayBuffer views.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public static isView(obj: Object): boolean--><!--Device-ArrayBuffer-public static isView(obj: Object): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Object | 是 | The object to check. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns true if the object is a view; otherwise false. |

## resize

```TypeScript
public resize(newLen : int): void
```

Resizes the ArrayBuffer to the specified length.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public resize(newLen : int): void--><!--Device-ArrayBuffer-public resize(newLen : int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| newLen | int | 是 | The new byte length. &lt;br&gt;The value must be an integer greater than or equal to 0. |

## set

```TypeScript
public set(pos: int, val: byte): void
```

Sets the byte value at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public set(pos: int, val: byte): void--><!--Device-ArrayBuffer-public set(pos: int, val: byte): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pos | int | 是 | The position in the buffer. &lt;br&gt;The value should be an integer. |
| val | byte | 是 | The byte value to set. |

## slice

```TypeScript
public slice(begin: int, end?: int): ArrayBuffer
```

Creates a new ArrayBuffer with a copy of bytes in the range [begin, end).

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public slice(begin: int, end?: int): ArrayBuffer--><!--Device-ArrayBuffer-public slice(begin: int, end?: int): ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | int | 是 | An inclusive index to start copying from. &lt;br&gt;The value should be an integer. |
| end | int | 否 | An exclusive index to stop copying. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | The new ArrayBuffer. |

## slice

```TypeScript
public slice(begin: double, end?: double): ArrayBuffer
```

Creates a new ArrayBuffer with a copy of bytes in the range [begin, end).

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public slice(begin: double, end?: double): ArrayBuffer--><!--Device-ArrayBuffer-public slice(begin: double, end?: double): ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | double | 是 | An inclusive index to start copying from. |
| end | double | 否 | An exclusive index to stop copying. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | The new ArrayBuffer. |

## stringify

```TypeScript
public static stringify(buffer: ArrayBuffer, encoding: string, start: int, end: int): string
```

Converts a segment of an ArrayBuffer to a string.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public static stringify(buffer: ArrayBuffer, encoding: string, start: int, end: int): string--><!--Device-ArrayBuffer-public static stringify(buffer: ArrayBuffer, encoding: string, start: int, end: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | Source buffer. |
| encoding | string | 是 | Encoding to use. |
| start | int | 是 | Start index. &lt;br&gt;The value should be an integer. |
| end | int | 是 | End index. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Decoded string. |

## toString

```TypeScript
public toString(): string
```

Returns the string representation of the ArrayBuffer.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-public toString(): string--><!--Device-ArrayBuffer-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | The string representation of the ArrayBuffer. |

## byteLength

```TypeScript
get byteLength(): int
```

Read-only property for the byte length of the ArrayBuffer.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-get byteLength(): int--><!--Device-ArrayBuffer-get byteLength(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

## detached

```TypeScript
get detached(): boolean
```

Returns true if the ArrayBuffer has been detached.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-get detached(): boolean--><!--Device-ArrayBuffer-get detached(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

## resizable

```TypeScript
get resizable(): boolean
```

Returns true if the ArrayBuffer can be resized.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBuffer-get resizable(): boolean--><!--Device-ArrayBuffer-get resizable(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

