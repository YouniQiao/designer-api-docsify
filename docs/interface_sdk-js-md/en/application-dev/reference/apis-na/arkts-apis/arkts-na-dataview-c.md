# DataView

class DataView

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export class DataView--><!--Device-unnamed-export class DataView-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(buffer: ArrayBuffer, byteOffset?: int, byteLength?: int)
```

Creates a new DataView object.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public constructor(buffer: ArrayBuffer, byteOffset?: int, byteLength?: int)--><!--Device-DataView-public constructor(buffer: ArrayBuffer, byteOffset?: int, byteLength?: int)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | The underlying ArrayBuffer for this DataView. |
| byteOffset | int | No | The byte offset within the ArrayBuffer. <br>The value should be an integer. |
| byteLength | int | No | The byte length of the DataView. <br>The value should be an integer. |

## getBigInt64

```TypeScript
public getBigInt64(byteOffset: int, littleEndian?: boolean): bigint
```

Read bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public getBigInt64(byteOffset: int, littleEndian?: boolean): bigint--><!--Device-DataView-public getBigInt64(byteOffset: int, littleEndian?: boolean): bigint-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to read <br>The value should be an integer. |
| littleEndian | boolean | No | read as little or big endian |

**Return value:**

| Type | Description |
| --- | --- |
| bigint | byteOffset's BigInt64 value. |

## getBigInt64

```TypeScript
public getBigInt64(byteOffset: int): bigint
```

Read bytes as bigint64 value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public getBigInt64(byteOffset: int): bigint--><!--Device-DataView-public getBigInt64(byteOffset: int): bigint-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to read. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| bigint | read value (big endian). |

## getBigUint64

```TypeScript
public getBigUint64(byteOffset: int, littleEndian?: boolean): bigint
```

Read bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public getBigUint64(byteOffset: int, littleEndian?: boolean): bigint--><!--Device-DataView-public getBigUint64(byteOffset: int, littleEndian?: boolean): bigint-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to read <br>The value should be an integer. |
| littleEndian | boolean | No | read as little or big endian |

**Return value:**

| Type | Description |
| --- | --- |
| bigint | byteOffset's BigUint64 value. |

## getBigUint64

```TypeScript
public getBigUint64(byteOffset: int): bigint
```

Read bytes as biguint64 value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public getBigUint64(byteOffset: int): bigint--><!--Device-DataView-public getBigUint64(byteOffset: int): bigint-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to read. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| bigint | read value (big endian). |

## getFloat32

```TypeScript
public getFloat32(byteOffset: int): double
```

Read bytes as float32 value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public getFloat32(byteOffset: int): double--><!--Device-DataView-public getFloat32(byteOffset: int): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to read. |

**Return value:**

| Type | Description |
| --- | --- |
| double | read value (big endian). |

## getFloat32

```TypeScript
public getFloat32(byteOffset: int, littleEndian?: boolean): double
```

Read bytes as float32 value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public getFloat32(byteOffset: int, littleEndian?: boolean): double--><!--Device-DataView-public getFloat32(byteOffset: int, littleEndian?: boolean): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to read. |
| littleEndian | boolean | No | true for little endian, false for big endian. |

**Return value:**

| Type | Description |
| --- | --- |
| double | read value. |

## getFloat64

```TypeScript
public getFloat64(byteOffset: int): double
```

Read bytes as float64 value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public getFloat64(byteOffset: int): double--><!--Device-DataView-public getFloat64(byteOffset: int): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to read. |

**Return value:**

| Type | Description |
| --- | --- |
| double | read value (big endian). |

## getFloat64

```TypeScript
public getFloat64(byteOffset: int, littleEndian?: boolean): double
```

Read bytes as float64 value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public getFloat64(byteOffset: int, littleEndian?: boolean): double--><!--Device-DataView-public getFloat64(byteOffset: int, littleEndian?: boolean): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to read. |
| littleEndian | boolean | No | true for little endian, false for big endian. |

**Return value:**

| Type | Description |
| --- | --- |
| double | read value. |

## getInt16

```TypeScript
public getInt16(byteOffset: int): int
```

Read bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public getInt16(byteOffset: int): int--><!--Device-DataView-public getInt16(byteOffset: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to read <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | return byteOffset's Int16 value |

## getInt16

```TypeScript
public getInt16(byteOffset: int, littleEndian?: boolean): int
```

Read bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public getInt16(byteOffset: int, littleEndian?: boolean): int--><!--Device-DataView-public getInt16(byteOffset: int, littleEndian?: boolean): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to read <br>The value should be an integer. |
| littleEndian | boolean | No | read as little or big endian |

**Return value:**

| Type | Description |
| --- | --- |
| int | byteOffset's Int16 value. |

## getInt32

```TypeScript
public getInt32(byteOffset: int): int
```

Read bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public getInt32(byteOffset: int): int--><!--Device-DataView-public getInt32(byteOffset: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to read <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | return byteOffset's Int32 value. |

## getInt32

```TypeScript
public getInt32(byteOffset: int, littleEndian?: boolean): int
```

Read bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public getInt32(byteOffset: int, littleEndian?: boolean): int--><!--Device-DataView-public getInt32(byteOffset: int, littleEndian?: boolean): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to read <br>The value should be an integer. |
| littleEndian | boolean | No | read as little or big endian |

**Return value:**

| Type | Description |
| --- | --- |
| int | return byteOffset's Int32 value. |

## getInt8

```TypeScript
public getInt8(byteOffset: int): int
```

Read bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public getInt8(byteOffset: int): int--><!--Device-DataView-public getInt8(byteOffset: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to read <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | return byteOffset's Int8 value |

## getUint16

```TypeScript
public getUint16(byteOffset: int): int
```

Read bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public getUint16(byteOffset: int): int--><!--Device-DataView-public getUint16(byteOffset: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to read <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | return byteOffset's Uint16 value |

## getUint16

```TypeScript
public getUint16(byteOffset: int, littleEndian?: boolean): int
```

Read bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public getUint16(byteOffset: int, littleEndian?: boolean): int--><!--Device-DataView-public getUint16(byteOffset: int, littleEndian?: boolean): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to read. <br>The value should be an integer. |
| littleEndian | boolean | No | read as little or big endian |

**Return value:**

| Type | Description |
| --- | --- |
| int | byteOffset's Uint16 value. |

## getUint32

```TypeScript
public getUint32(byteOffset: int): double
```

Read bytes as uint32 value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public getUint32(byteOffset: int): double--><!--Device-DataView-public getUint32(byteOffset: int): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to read. |

**Return value:**

| Type | Description |
| --- | --- |
| double | read value (big endian). |

## getUint32

```TypeScript
public getUint32(byteOffset: int, littleEndian?: boolean): double
```

Read bytes as uint32 value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public getUint32(byteOffset: int, littleEndian?: boolean): double--><!--Device-DataView-public getUint32(byteOffset: int, littleEndian?: boolean): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to read. |
| littleEndian | boolean | No | true for little endian, false for big endian. |

**Return value:**

| Type | Description |
| --- | --- |
| double | read value. |

## getUint8

```TypeScript
public getUint8(byteOffset: int): int
```

Read bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public getUint8(byteOffset: int): int--><!--Device-DataView-public getUint8(byteOffset: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to read <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | return byteOffset's Uint8 value |

## setBigInt64

```TypeScript
public setBigInt64(byteOffset: int, value: bigint, littleEndian?: boolean): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setBigInt64(byteOffset: int, value: bigint, littleEndian?: boolean): void--><!--Device-DataView-public setBigInt64(byteOffset: int, value: bigint, littleEndian?: boolean): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write <br>The value should be an integer. |
| value | bigint | Yes | the bigint value to write. |
| littleEndian | boolean | No | read as little or big endian |

## setBigInt64

```TypeScript
public setBigInt64(byteOffset: int, value: long): void
```

Sets bytes as bigint64 value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setBigInt64(byteOffset: int, value: long): void--><!--Device-DataView-public setBigInt64(byteOffset: int, value: long): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write. <br>The value should be an integer. |
| value | long | Yes | the long value to write. |

## setBigInt64

```TypeScript
public setBigInt64(byteOffset: int, value: long, littleEndian: boolean): void
```

Sets bytes as bigint64 value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setBigInt64(byteOffset: int, value: long, littleEndian: boolean): void--><!--Device-DataView-public setBigInt64(byteOffset: int, value: long, littleEndian: boolean): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write. <br>The value should be an integer. |
| value | long | Yes | the long value to write. |
| littleEndian | boolean | Yes | true for little endian, false for big endian. |

## setBigUint64

```TypeScript
public setBigUint64(byteOffset: int, value: long): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setBigUint64(byteOffset: int, value: long): void--><!--Device-DataView-public setBigUint64(byteOffset: int, value: long): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write <br>The value should be an integer. |
| value | long | Yes | the long value to write. |

## setBigUint64

```TypeScript
public setBigUint64(byteOffset: int, value: long, littleEndian: boolean): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setBigUint64(byteOffset: int, value: long, littleEndian: boolean): void--><!--Device-DataView-public setBigUint64(byteOffset: int, value: long, littleEndian: boolean): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write <br>The value should be an integer. |
| value | long | Yes | the long value to write. |
| littleEndian | boolean | Yes | read as little or big endian |

## setBigUint64

```TypeScript
public setBigUint64(byteOffset: int, value: bigint, littleEndian?: boolean): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setBigUint64(byteOffset: int, value: bigint, littleEndian?: boolean): void--><!--Device-DataView-public setBigUint64(byteOffset: int, value: bigint, littleEndian?: boolean): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write <br>The value should be an integer. |
| value | bigint | Yes |  |
| littleEndian | boolean | No | read as little or big endian |

## setFloat32

```TypeScript
public setFloat32(byteOffset: int, value: float): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setFloat32(byteOffset: int, value: float): void--><!--Device-DataView-public setFloat32(byteOffset: int, value: float): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write <br>The value should be an integer. |
| value | float | Yes | the float value to write. |

## setFloat32

```TypeScript
public setFloat32(byteOffset: int, value: float, littleEndian: boolean): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setFloat32(byteOffset: int, value: float, littleEndian: boolean): void--><!--Device-DataView-public setFloat32(byteOffset: int, value: float, littleEndian: boolean): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write <br>The value should be an integer. |
| value | float | Yes | the float value to write. |
| littleEndian | boolean | Yes | read as little or big endian |

## setFloat32

```TypeScript
public setFloat32(byteOffset: int, value: double, littleEndian?: boolean): void
```

Sets bytes as float32 value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setFloat32(byteOffset: int, value: double, littleEndian?: boolean): void--><!--Device-DataView-public setFloat32(byteOffset: int, value: double, littleEndian?: boolean): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write. |
| value | double | Yes | the double value to write. |
| littleEndian | boolean | No | true for little endian, false for big endian. |

## setFloat64

```TypeScript
public setFloat64(byteOffset: int, value: double): void
```

Sets bytes as float64 value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setFloat64(byteOffset: int, value: double): void--><!--Device-DataView-public setFloat64(byteOffset: int, value: double): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write. |
| value | double | Yes | the double value to write. |

## setFloat64

```TypeScript
public setFloat64(byteOffset: int, value: double, littleEndian?: boolean): void
```

Sets bytes as float64 value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setFloat64(byteOffset: int, value: double, littleEndian?: boolean): void--><!--Device-DataView-public setFloat64(byteOffset: int, value: double, littleEndian?: boolean): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write. |
| value | double | Yes | the double value to write. |
| littleEndian | boolean | No | true for little endian, false for big endian. |

## setInt16

```TypeScript
public setInt16(byteOffset: int, value: int): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setInt16(byteOffset: int, value: int): void--><!--Device-DataView-public setInt16(byteOffset: int, value: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write <br>The value should be an integer. |
| value | int | Yes | <br>The value should be an integer. |

## setInt16

```TypeScript
public setInt16(byteOffset: int, value: int, littleEndian: boolean): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setInt16(byteOffset: int, value: int, littleEndian: boolean): void--><!--Device-DataView-public setInt16(byteOffset: int, value: int, littleEndian: boolean): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write <br>The value should be an integer. |
| value | int | Yes | <br>The value should be an integer. |
| littleEndian | boolean | Yes | read as little or big endian |

## setInt16

```TypeScript
public setInt16(byteOffset: int, value: double, littleEndian?: boolean): void
```

Sets bytes as int16 value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setInt16(byteOffset: int, value: double, littleEndian?: boolean): void--><!--Device-DataView-public setInt16(byteOffset: int, value: double, littleEndian?: boolean): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write. |
| value | double | Yes | value to write. |
| littleEndian | boolean | No | true for little endian, false for big endian. |

## setInt32

```TypeScript
public setInt32(byteOffset: int, value: int): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setInt32(byteOffset: int, value: int): void--><!--Device-DataView-public setInt32(byteOffset: int, value: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write <br>The value should be an integer. |
| value | int | Yes | <br>The value should be an integer. |

## setInt32

```TypeScript
public setInt32(byteOffset: int, value: int, littleEndian: boolean): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setInt32(byteOffset: int, value: int, littleEndian: boolean): void--><!--Device-DataView-public setInt32(byteOffset: int, value: int, littleEndian: boolean): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write <br>The value should be an integer. |
| value | int | Yes | <br>The value should be an integer. |
| littleEndian | boolean | Yes | read as little or big endian |

## setInt32

```TypeScript
public setInt32(byteOffset: int, value: double, littleEndian?: boolean): void
```

Sets bytes as int32 value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setInt32(byteOffset: int, value: double, littleEndian?: boolean): void--><!--Device-DataView-public setInt32(byteOffset: int, value: double, littleEndian?: boolean): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write. |
| value | double | Yes | value to write. |
| littleEndian | boolean | No | true for little endian, false for big endian. |

## setInt8

```TypeScript
public setInt8(byteOffset: int, value: int): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setInt8(byteOffset: int, value: int): void--><!--Device-DataView-public setInt8(byteOffset: int, value: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write <br>The value should be an integer. |
| value | int | Yes | <br>The value should be an integer. |

## setInt8

```TypeScript
public setInt8(byteOffset: int, value: double): void
```

Sets bytes as int8 value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setInt8(byteOffset: int, value: double): void--><!--Device-DataView-public setInt8(byteOffset: int, value: double): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write. |
| value | double | Yes | value to write. |

## setUint16

```TypeScript
public setUint16(byteOffset: int, value: int): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setUint16(byteOffset: int, value: int): void--><!--Device-DataView-public setUint16(byteOffset: int, value: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write <br>The value should be an integer. |
| value | int | Yes | <br>The value should be an integer. |

## setUint16

```TypeScript
public setUint16(byteOffset: int, value: int, littleEndian: boolean): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setUint16(byteOffset: int, value: int, littleEndian: boolean): void--><!--Device-DataView-public setUint16(byteOffset: int, value: int, littleEndian: boolean): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write <br>The value should be an integer. |
| value | int | Yes | <br>The value should be an integer. |
| littleEndian | boolean | Yes | read as little or big endian |

## setUint16

```TypeScript
public setUint16(byteOffset: int, value: double, littleEndian?: boolean): void
```

Sets bytes as uint16 value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setUint16(byteOffset: int, value: double, littleEndian?: boolean): void--><!--Device-DataView-public setUint16(byteOffset: int, value: double, littleEndian?: boolean): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write. |
| value | double | Yes | the double value to write. |
| littleEndian | boolean | No | true for little endian, false for big endian. |

## setUint32

```TypeScript
public setUint32(byteOffset: int, value: long): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setUint32(byteOffset: int, value: long): void--><!--Device-DataView-public setUint32(byteOffset: int, value: long): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write. <br>The value should be an integer. |
| value | long | Yes | the long value to write. |

## setUint32

```TypeScript
public setUint32(byteOffset: int, value: long, littleEndian: boolean): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setUint32(byteOffset: int, value: long, littleEndian: boolean): void--><!--Device-DataView-public setUint32(byteOffset: int, value: long, littleEndian: boolean): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write <br>The value should be an integer. |
| value | long | Yes | the long value to write. |
| littleEndian | boolean | Yes | read as little or big endian |

## setUint32

```TypeScript
public setUint32(byteOffset: int, value: double, littleEndian?: boolean): void
```

Sets bytes as uint32 value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setUint32(byteOffset: int, value: double, littleEndian?: boolean): void--><!--Device-DataView-public setUint32(byteOffset: int, value: double, littleEndian?: boolean): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write. |
| value | double | Yes | value to write. |
| littleEndian | boolean | No | true for little endian, false for big endian. |

## setUint8

```TypeScript
public setUint8(byteOffset: int, value: int): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setUint8(byteOffset: int, value: int): void--><!--Device-DataView-public setUint8(byteOffset: int, value: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write <br>The value should be an integer. |
| value | int | Yes | <br>The value should be an integer. |

## setUint8

```TypeScript
public setUint8(byteOffset: int, value: double): void
```

Sets bytes as uint8 value.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataView-public setUint8(byteOffset: int, value: double): void--><!--Device-DataView-public setUint8(byteOffset: int, value: double): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | int | Yes | zero index to write. |
| value | double | Yes | value to write. |

