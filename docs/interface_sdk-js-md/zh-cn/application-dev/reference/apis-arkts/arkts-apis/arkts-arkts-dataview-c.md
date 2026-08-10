# DataView

class DataView

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class DataView--><!--Device-unnamed-export class DataView-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(buffer: ArrayBuffer, byteOffset?: int, byteLength?: int)
```

Creates a new DataView object.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public constructor(buffer: ArrayBuffer, byteOffset?: int, byteLength?: int)--><!--Device-DataView-public constructor(buffer: ArrayBuffer, byteOffset?: int, byteLength?: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | The underlying ArrayBuffer for this DataView. |
| byteOffset | int | 否 | The byte offset within the ArrayBuffer. &lt;br&gt;The value should be an integer. |
| byteLength | int | 否 | The byte length of the DataView. &lt;br&gt;The value should be an integer. |

## getBigInt64

```TypeScript
public getBigInt64(byteOffset: int, littleEndian?: boolean): bigint
```

Read bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getBigInt64(byteOffset: int, littleEndian?: boolean): bigint--><!--Device-DataView-public getBigInt64(byteOffset: int, littleEndian?: boolean): bigint-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to read &lt;br&gt;The value should be an integer. |
| littleEndian | boolean | 否 | read as little or big endian |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | byteOffset's BigInt64 value. |

## getBigInt64

```TypeScript
public getBigInt64(byteOffset: int): bigint
```

Read bytes as bigint64 value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getBigInt64(byteOffset: int): bigint--><!--Device-DataView-public getBigInt64(byteOffset: int): bigint-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to read. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | read value (big endian). |

## getBigUint64

```TypeScript
public getBigUint64(byteOffset: int, littleEndian?: boolean): bigint
```

Read bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getBigUint64(byteOffset: int, littleEndian?: boolean): bigint--><!--Device-DataView-public getBigUint64(byteOffset: int, littleEndian?: boolean): bigint-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to read &lt;br&gt;The value should be an integer. |
| littleEndian | boolean | 否 | read as little or big endian |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | byteOffset's BigUint64 value. |

## getBigUint64

```TypeScript
public getBigUint64(byteOffset: int): bigint
```

Read bytes as biguint64 value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getBigUint64(byteOffset: int): bigint--><!--Device-DataView-public getBigUint64(byteOffset: int): bigint-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to read. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | read value (big endian). |

## getFloat32

```TypeScript
public getFloat32(byteOffset: int): double
```

Read bytes as float32 value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getFloat32(byteOffset: int): double--><!--Device-DataView-public getFloat32(byteOffset: int): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to read. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | read value (big endian). |

## getFloat32

```TypeScript
public getFloat32(byteOffset: int, littleEndian?: boolean): double
```

Read bytes as float32 value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getFloat32(byteOffset: int, littleEndian?: boolean): double--><!--Device-DataView-public getFloat32(byteOffset: int, littleEndian?: boolean): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to read. |
| littleEndian | boolean | 否 | true for little endian, false for big endian. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | read value. |

## getFloat64

```TypeScript
public getFloat64(byteOffset: int): double
```

Read bytes as float64 value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getFloat64(byteOffset: int): double--><!--Device-DataView-public getFloat64(byteOffset: int): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to read. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | read value (big endian). |

## getFloat64

```TypeScript
public getFloat64(byteOffset: int, littleEndian?: boolean): double
```

Read bytes as float64 value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getFloat64(byteOffset: int, littleEndian?: boolean): double--><!--Device-DataView-public getFloat64(byteOffset: int, littleEndian?: boolean): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to read. |
| littleEndian | boolean | 否 | true for little endian, false for big endian. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | read value. |

## getInt16

```TypeScript
public getInt16(byteOffset: int): int
```

Read bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getInt16(byteOffset: int): int--><!--Device-DataView-public getInt16(byteOffset: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to read &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | return byteOffset's Int16 value |

## getInt16

```TypeScript
public getInt16(byteOffset: int, littleEndian?: boolean): int
```

Read bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getInt16(byteOffset: int, littleEndian?: boolean): int--><!--Device-DataView-public getInt16(byteOffset: int, littleEndian?: boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to read &lt;br&gt;The value should be an integer. |
| littleEndian | boolean | 否 | read as little or big endian |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | byteOffset's Int16 value. |

## getInt32

```TypeScript
public getInt32(byteOffset: int): int
```

Read bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getInt32(byteOffset: int): int--><!--Device-DataView-public getInt32(byteOffset: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to read &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | return byteOffset's Int32 value. |

## getInt32

```TypeScript
public getInt32(byteOffset: int, littleEndian?: boolean): int
```

Read bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getInt32(byteOffset: int, littleEndian?: boolean): int--><!--Device-DataView-public getInt32(byteOffset: int, littleEndian?: boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to read &lt;br&gt;The value should be an integer. |
| littleEndian | boolean | 否 | read as little or big endian |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | return byteOffset's Int32 value. |

## getInt8

```TypeScript
public getInt8(byteOffset: int): int
```

Read bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getInt8(byteOffset: int): int--><!--Device-DataView-public getInt8(byteOffset: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to read &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | return byteOffset's Int8 value |

## getUint16

```TypeScript
public getUint16(byteOffset: int): int
```

Read bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getUint16(byteOffset: int): int--><!--Device-DataView-public getUint16(byteOffset: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to read &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | return byteOffset's Uint16 value |

## getUint16

```TypeScript
public getUint16(byteOffset: int, littleEndian?: boolean): int
```

Read bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getUint16(byteOffset: int, littleEndian?: boolean): int--><!--Device-DataView-public getUint16(byteOffset: int, littleEndian?: boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to read. &lt;br&gt;The value should be an integer. |
| littleEndian | boolean | 否 | read as little or big endian |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | byteOffset's Uint16 value. |

## getUint32

```TypeScript
public getUint32(byteOffset: int): double
```

Read bytes as uint32 value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getUint32(byteOffset: int): double--><!--Device-DataView-public getUint32(byteOffset: int): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to read. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | read value (big endian). |

## getUint32

```TypeScript
public getUint32(byteOffset: int, littleEndian?: boolean): double
```

Read bytes as uint32 value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getUint32(byteOffset: int, littleEndian?: boolean): double--><!--Device-DataView-public getUint32(byteOffset: int, littleEndian?: boolean): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to read. |
| littleEndian | boolean | 否 | true for little endian, false for big endian. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | read value. |

## getUint8

```TypeScript
public getUint8(byteOffset: int): int
```

Read bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getUint8(byteOffset: int): int--><!--Device-DataView-public getUint8(byteOffset: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to read &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | return byteOffset's Uint8 value |

## setBigInt64

```TypeScript
public setBigInt64(byteOffset: int, value: bigint, littleEndian?: boolean): void
```

Sets bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setBigInt64(byteOffset: int, value: bigint, littleEndian?: boolean): void--><!--Device-DataView-public setBigInt64(byteOffset: int, value: bigint, littleEndian?: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write &lt;br&gt;The value should be an integer. |
| value | bigint | 是 | the bigint value to write. |
| littleEndian | boolean | 否 | read as little or big endian |

## setBigInt64

```TypeScript
public setBigInt64(byteOffset: int, value: long): void
```

Sets bytes as bigint64 value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setBigInt64(byteOffset: int, value: long): void--><!--Device-DataView-public setBigInt64(byteOffset: int, value: long): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write. &lt;br&gt;The value should be an integer. |
| value | long | 是 | the long value to write. |

## setBigInt64

```TypeScript
public setBigInt64(byteOffset: int, value: long, littleEndian: boolean): void
```

Sets bytes as bigint64 value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setBigInt64(byteOffset: int, value: long, littleEndian: boolean): void--><!--Device-DataView-public setBigInt64(byteOffset: int, value: long, littleEndian: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write. &lt;br&gt;The value should be an integer. |
| value | long | 是 | the long value to write. |
| littleEndian | boolean | 是 | true for little endian, false for big endian. |

## setBigUint64

```TypeScript
public setBigUint64(byteOffset: int, value: long): void
```

Sets bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setBigUint64(byteOffset: int, value: long): void--><!--Device-DataView-public setBigUint64(byteOffset: int, value: long): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write &lt;br&gt;The value should be an integer. |
| value | long | 是 | the long value to write. |

## setBigUint64

```TypeScript
public setBigUint64(byteOffset: int, value: long, littleEndian: boolean): void
```

Sets bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setBigUint64(byteOffset: int, value: long, littleEndian: boolean): void--><!--Device-DataView-public setBigUint64(byteOffset: int, value: long, littleEndian: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write &lt;br&gt;The value should be an integer. |
| value | long | 是 | the long value to write. |
| littleEndian | boolean | 是 | read as little or big endian |

## setBigUint64

```TypeScript
public setBigUint64(byteOffset: int, value: bigint, littleEndian?: boolean): void
```

Sets bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setBigUint64(byteOffset: int, value: bigint, littleEndian?: boolean): void--><!--Device-DataView-public setBigUint64(byteOffset: int, value: bigint, littleEndian?: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write &lt;br&gt;The value should be an integer. |
| value | bigint | 是 |  |
| littleEndian | boolean | 否 | read as little or big endian |

## setFloat32

```TypeScript
public setFloat32(byteOffset: int, value: float): void
```

Sets bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setFloat32(byteOffset: int, value: float): void--><!--Device-DataView-public setFloat32(byteOffset: int, value: float): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write &lt;br&gt;The value should be an integer. |
| value | float | 是 | the float value to write. |

## setFloat32

```TypeScript
public setFloat32(byteOffset: int, value: float, littleEndian: boolean): void
```

Sets bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setFloat32(byteOffset: int, value: float, littleEndian: boolean): void--><!--Device-DataView-public setFloat32(byteOffset: int, value: float, littleEndian: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write &lt;br&gt;The value should be an integer. |
| value | float | 是 | the float value to write. |
| littleEndian | boolean | 是 | read as little or big endian |

## setFloat32

```TypeScript
public setFloat32(byteOffset: int, value: double, littleEndian?: boolean): void
```

Sets bytes as float32 value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setFloat32(byteOffset: int, value: double, littleEndian?: boolean): void--><!--Device-DataView-public setFloat32(byteOffset: int, value: double, littleEndian?: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write. |
| value | double | 是 | the double value to write. |
| littleEndian | boolean | 否 | true for little endian, false for big endian. |

## setFloat64

```TypeScript
public setFloat64(byteOffset: int, value: double): void
```

Sets bytes as float64 value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setFloat64(byteOffset: int, value: double): void--><!--Device-DataView-public setFloat64(byteOffset: int, value: double): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write. |
| value | double | 是 | the double value to write. |

## setFloat64

```TypeScript
public setFloat64(byteOffset: int, value: double, littleEndian?: boolean): void
```

Sets bytes as float64 value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setFloat64(byteOffset: int, value: double, littleEndian?: boolean): void--><!--Device-DataView-public setFloat64(byteOffset: int, value: double, littleEndian?: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write. |
| value | double | 是 | the double value to write. |
| littleEndian | boolean | 否 | true for little endian, false for big endian. |

## setInt16

```TypeScript
public setInt16(byteOffset: int, value: int): void
```

Sets bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setInt16(byteOffset: int, value: int): void--><!--Device-DataView-public setInt16(byteOffset: int, value: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write &lt;br&gt;The value should be an integer. |
| value | int | 是 | &lt;br&gt;The value should be an integer. |

## setInt16

```TypeScript
public setInt16(byteOffset: int, value: int, littleEndian: boolean): void
```

Sets bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setInt16(byteOffset: int, value: int, littleEndian: boolean): void--><!--Device-DataView-public setInt16(byteOffset: int, value: int, littleEndian: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write &lt;br&gt;The value should be an integer. |
| value | int | 是 | &lt;br&gt;The value should be an integer. |
| littleEndian | boolean | 是 | read as little or big endian |

## setInt16

```TypeScript
public setInt16(byteOffset: int, value: double, littleEndian?: boolean): void
```

Sets bytes as int16 value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setInt16(byteOffset: int, value: double, littleEndian?: boolean): void--><!--Device-DataView-public setInt16(byteOffset: int, value: double, littleEndian?: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write. |
| value | double | 是 | value to write. |
| littleEndian | boolean | 否 | true for little endian, false for big endian. |

## setInt32

```TypeScript
public setInt32(byteOffset: int, value: int): void
```

Sets bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setInt32(byteOffset: int, value: int): void--><!--Device-DataView-public setInt32(byteOffset: int, value: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write &lt;br&gt;The value should be an integer. |
| value | int | 是 | &lt;br&gt;The value should be an integer. |

## setInt32

```TypeScript
public setInt32(byteOffset: int, value: int, littleEndian: boolean): void
```

Sets bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setInt32(byteOffset: int, value: int, littleEndian: boolean): void--><!--Device-DataView-public setInt32(byteOffset: int, value: int, littleEndian: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write &lt;br&gt;The value should be an integer. |
| value | int | 是 | &lt;br&gt;The value should be an integer. |
| littleEndian | boolean | 是 | read as little or big endian |

## setInt32

```TypeScript
public setInt32(byteOffset: int, value: double, littleEndian?: boolean): void
```

Sets bytes as int32 value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setInt32(byteOffset: int, value: double, littleEndian?: boolean): void--><!--Device-DataView-public setInt32(byteOffset: int, value: double, littleEndian?: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write. |
| value | double | 是 | value to write. |
| littleEndian | boolean | 否 | true for little endian, false for big endian. |

## setInt8

```TypeScript
public setInt8(byteOffset: int, value: int): void
```

Sets bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setInt8(byteOffset: int, value: int): void--><!--Device-DataView-public setInt8(byteOffset: int, value: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write &lt;br&gt;The value should be an integer. |
| value | int | 是 | &lt;br&gt;The value should be an integer. |

## setInt8

```TypeScript
public setInt8(byteOffset: int, value: double): void
```

Sets bytes as int8 value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setInt8(byteOffset: int, value: double): void--><!--Device-DataView-public setInt8(byteOffset: int, value: double): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write. |
| value | double | 是 | value to write. |

## setUint16

```TypeScript
public setUint16(byteOffset: int, value: int): void
```

Sets bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setUint16(byteOffset: int, value: int): void--><!--Device-DataView-public setUint16(byteOffset: int, value: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write &lt;br&gt;The value should be an integer. |
| value | int | 是 | &lt;br&gt;The value should be an integer. |

## setUint16

```TypeScript
public setUint16(byteOffset: int, value: int, littleEndian: boolean): void
```

Sets bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setUint16(byteOffset: int, value: int, littleEndian: boolean): void--><!--Device-DataView-public setUint16(byteOffset: int, value: int, littleEndian: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write &lt;br&gt;The value should be an integer. |
| value | int | 是 | &lt;br&gt;The value should be an integer. |
| littleEndian | boolean | 是 | read as little or big endian |

## setUint16

```TypeScript
public setUint16(byteOffset: int, value: double, littleEndian?: boolean): void
```

Sets bytes as uint16 value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setUint16(byteOffset: int, value: double, littleEndian?: boolean): void--><!--Device-DataView-public setUint16(byteOffset: int, value: double, littleEndian?: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write. |
| value | double | 是 | the double value to write. |
| littleEndian | boolean | 否 | true for little endian, false for big endian. |

## setUint32

```TypeScript
public setUint32(byteOffset: int, value: long): void
```

Sets bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setUint32(byteOffset: int, value: long): void--><!--Device-DataView-public setUint32(byteOffset: int, value: long): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write. &lt;br&gt;The value should be an integer. |
| value | long | 是 | the long value to write. |

## setUint32

```TypeScript
public setUint32(byteOffset: int, value: long, littleEndian: boolean): void
```

Sets bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setUint32(byteOffset: int, value: long, littleEndian: boolean): void--><!--Device-DataView-public setUint32(byteOffset: int, value: long, littleEndian: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write &lt;br&gt;The value should be an integer. |
| value | long | 是 | the long value to write. |
| littleEndian | boolean | 是 | read as little or big endian |

## setUint32

```TypeScript
public setUint32(byteOffset: int, value: double, littleEndian?: boolean): void
```

Sets bytes as uint32 value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setUint32(byteOffset: int, value: double, littleEndian?: boolean): void--><!--Device-DataView-public setUint32(byteOffset: int, value: double, littleEndian?: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write. |
| value | double | 是 | value to write. |
| littleEndian | boolean | 否 | true for little endian, false for big endian. |

## setUint8

```TypeScript
public setUint8(byteOffset: int, value: int): void
```

Sets bytes as they represent given type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setUint8(byteOffset: int, value: int): void--><!--Device-DataView-public setUint8(byteOffset: int, value: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write &lt;br&gt;The value should be an integer. |
| value | int | 是 | &lt;br&gt;The value should be an integer. |

## setUint8

```TypeScript
public setUint8(byteOffset: int, value: double): void
```

Sets bytes as uint8 value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setUint8(byteOffset: int, value: double): void--><!--Device-DataView-public setUint8(byteOffset: int, value: double): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | zero index to write. |
| value | double | 是 | value to write. |

## buffer

```TypeScript
public get buffer(): ArrayBuffer
```

Underlying buffer.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public get buffer(): ArrayBuffer--><!--Device-DataView-public get buffer(): ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

## byteLength

```TypeScript
public get byteLength(): int
```

Read-only property for the byte length of the DataView.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public get byteLength(): int--><!--Device-DataView-public get byteLength(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

## byteOffset

```TypeScript
public get byteOffset(): int
```

Read-only property for the byte offset of the DataView.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public get byteOffset(): int--><!--Device-DataView-public get byteOffset(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

