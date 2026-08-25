# DataView

class DataView

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
public constructor(buffer: ArrayBuffer, byteOffset?: int, byteLength?: int)
```

Creates a new DataView object.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [buffer](#buffer) | ArrayBuffer | Yes |
| [byteOffset](#byteoffset) | int | No |
| [byteLength](#bytelength) | int | No |

## getBigInt64

```TypeScript
public getBigInt64(byteOffset: int, littleEndian?: boolean): bigint
```

Read bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| littleEndian | boolean | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| bigint |

## getBigInt64

```TypeScript
public getBigInt64(byteOffset: int): bigint
```

Read bytes as bigint64 value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| bigint |

## getBigUint64

```TypeScript
public getBigUint64(byteOffset: int, littleEndian?: boolean): bigint
```

Read bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| littleEndian | boolean | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| bigint |

## getBigUint64

```TypeScript
public getBigUint64(byteOffset: int): bigint
```

Read bytes as biguint64 value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| bigint |

## getFloat32

```TypeScript
public getFloat32(byteOffset: int): double
```

Read bytes as float32 value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| double |

## getFloat32

```TypeScript
public getFloat32(byteOffset: int, littleEndian?: boolean): double
```

Read bytes as float32 value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| littleEndian | boolean | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| double |

## getFloat64

```TypeScript
public getFloat64(byteOffset: int): double
```

Read bytes as float64 value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| double |

## getFloat64

```TypeScript
public getFloat64(byteOffset: int, littleEndian?: boolean): double
```

Read bytes as float64 value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| littleEndian | boolean | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| double |

## getInt16

```TypeScript
public getInt16(byteOffset: int): int
```

Read bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getInt16

```TypeScript
public getInt16(byteOffset: int, littleEndian?: boolean): int
```

Read bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| littleEndian | boolean | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getInt32

```TypeScript
public getInt32(byteOffset: int): int
```

Read bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getInt32

```TypeScript
public getInt32(byteOffset: int, littleEndian?: boolean): int
```

Read bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| littleEndian | boolean | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getInt8

```TypeScript
public getInt8(byteOffset: int): int
```

Read bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getUint16

```TypeScript
public getUint16(byteOffset: int): int
```

Read bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getUint16

```TypeScript
public getUint16(byteOffset: int, littleEndian?: boolean): int
```

Read bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| littleEndian | boolean | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getUint32

```TypeScript
public getUint32(byteOffset: int): double
```

Read bytes as uint32 value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| double |

## getUint32

```TypeScript
public getUint32(byteOffset: int, littleEndian?: boolean): double
```

Read bytes as uint32 value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| littleEndian | boolean | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| double |

## getUint8

```TypeScript
public getUint8(byteOffset: int): int
```

Read bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## setBigInt64

```TypeScript
public setBigInt64(byteOffset: int, value: bigint, littleEndian?: boolean): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | bigint | Yes |
| littleEndian | boolean | No |

## setBigInt64

```TypeScript
public setBigInt64(byteOffset: int, value: long): void
```

Sets bytes as bigint64 value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | long | Yes |

## setBigInt64

```TypeScript
public setBigInt64(byteOffset: int, value: long, littleEndian: boolean): void
```

Sets bytes as bigint64 value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | long | Yes |
| littleEndian | boolean | Yes |

## setBigUint64

```TypeScript
public setBigUint64(byteOffset: int, value: long): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | long | Yes |

## setBigUint64

```TypeScript
public setBigUint64(byteOffset: int, value: long, littleEndian: boolean): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | long | Yes |
| littleEndian | boolean | Yes |

## setBigUint64

```TypeScript
public setBigUint64(byteOffset: int, value: bigint, littleEndian?: boolean): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | bigint | Yes |
| littleEndian | boolean | No |

## setFloat32

```TypeScript
public setFloat32(byteOffset: int, value: float): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | float | Yes |

## setFloat32

```TypeScript
public setFloat32(byteOffset: int, value: float, littleEndian: boolean): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | float | Yes |
| littleEndian | boolean | Yes |

## setFloat32

```TypeScript
public setFloat32(byteOffset: int, value: double, littleEndian?: boolean): void
```

Sets bytes as float32 value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | double | Yes |
| littleEndian | boolean | No |

## setFloat64

```TypeScript
public setFloat64(byteOffset: int, value: double): void
```

Sets bytes as float64 value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | double | Yes |

## setFloat64

```TypeScript
public setFloat64(byteOffset: int, value: double, littleEndian?: boolean): void
```

Sets bytes as float64 value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | double | Yes |
| littleEndian | boolean | No |

## setInt16

```TypeScript
public setInt16(byteOffset: int, value: int): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | int | Yes |

## setInt16

```TypeScript
public setInt16(byteOffset: int, value: int, littleEndian: boolean): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | int | Yes |
| littleEndian | boolean | Yes |

## setInt16

```TypeScript
public setInt16(byteOffset: int, value: double, littleEndian?: boolean): void
```

Sets bytes as int16 value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | double | Yes |
| littleEndian | boolean | No |

## setInt32

```TypeScript
public setInt32(byteOffset: int, value: int): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | int | Yes |

## setInt32

```TypeScript
public setInt32(byteOffset: int, value: int, littleEndian: boolean): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | int | Yes |
| littleEndian | boolean | Yes |

## setInt32

```TypeScript
public setInt32(byteOffset: int, value: double, littleEndian?: boolean): void
```

Sets bytes as int32 value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | double | Yes |
| littleEndian | boolean | No |

## setInt8

```TypeScript
public setInt8(byteOffset: int, value: int): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | int | Yes |

## setInt8

```TypeScript
public setInt8(byteOffset: int, value: double): void
```

Sets bytes as int8 value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | double | Yes |

## setUint16

```TypeScript
public setUint16(byteOffset: int, value: int): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | int | Yes |

## setUint16

```TypeScript
public setUint16(byteOffset: int, value: int, littleEndian: boolean): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | int | Yes |
| littleEndian | boolean | Yes |

## setUint16

```TypeScript
public setUint16(byteOffset: int, value: double, littleEndian?: boolean): void
```

Sets bytes as uint16 value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | double | Yes |
| littleEndian | boolean | No |

## setUint32

```TypeScript
public setUint32(byteOffset: int, value: long): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | long | Yes |

## setUint32

```TypeScript
public setUint32(byteOffset: int, value: long, littleEndian: boolean): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | long | Yes |
| littleEndian | boolean | Yes |

## setUint32

```TypeScript
public setUint32(byteOffset: int, value: double, littleEndian?: boolean): void
```

Sets bytes as uint32 value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | double | Yes |
| littleEndian | boolean | No |

## setUint8

```TypeScript
public setUint8(byteOffset: int, value: int): void
```

Sets bytes as they represent given type

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | int | Yes |

## setUint8

```TypeScript
public setUint8(byteOffset: int, value: double): void
```

Sets bytes as uint8 value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | Yes |
| value | double | Yes |

## buffer

```TypeScript
public get buffer(): ArrayBuffer
```

Underlying buffer.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## byteLength

```TypeScript
public get byteLength(): int
```

Read-only property for the byte length of the DataView.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## byteOffset

```TypeScript
public get byteOffset(): int
```

Read-only property for the byte offset of the DataView.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang
