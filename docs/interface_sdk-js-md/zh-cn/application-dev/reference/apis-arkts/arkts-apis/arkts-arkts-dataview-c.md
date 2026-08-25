# DataView

DataView类。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## constructor

```TypeScript
public constructor(buffer: ArrayBuffer, byteOffset?: int, byteLength?: int)
```

创建新的DataView对象。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [buffer](#buffer) | ArrayBuffer | 是 |
| [byteOffset](#byteoffset) | int | 否 |
| [byteLength](#bytelength) | int | 否 |

## getBigInt64

```TypeScript
public getBigInt64(byteOffset: int, littleEndian?: boolean): bigint
```

按指定类型从字节序列中读取值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| littleEndian | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| bigint |

## getBigInt64

```TypeScript
public getBigInt64(byteOffset: int): bigint
```

从字节序列中读取bigint64值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |

**返回值：**

| 类型 |
| --- |
| bigint |

## getBigUint64

```TypeScript
public getBigUint64(byteOffset: int, littleEndian?: boolean): bigint
```

按指定类型从字节序列中读取值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| littleEndian | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| bigint |

## getBigUint64

```TypeScript
public getBigUint64(byteOffset: int): bigint
```

从字节序列中读取biguint64值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |

**返回值：**

| 类型 |
| --- |
| bigint |

## getFloat32

```TypeScript
public getFloat32(byteOffset: int): double
```

从字节序列中读取float32值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |

**返回值：**

| 类型 |
| --- |
| double |

## getFloat32

```TypeScript
public getFloat32(byteOffset: int, littleEndian?: boolean): double
```

从字节序列中读取float32值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| littleEndian | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| double |

## getFloat64

```TypeScript
public getFloat64(byteOffset: int): double
```

从字节序列中读取float64值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |

**返回值：**

| 类型 |
| --- |
| double |

## getFloat64

```TypeScript
public getFloat64(byteOffset: int, littleEndian?: boolean): double
```

从字节序列中读取float64值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| littleEndian | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| double |

## getInt16

```TypeScript
public getInt16(byteOffset: int): int
```

按指定类型从字节序列中读取值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## getInt16

```TypeScript
public getInt16(byteOffset: int, littleEndian?: boolean): int
```

按指定类型从字节序列中读取值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| littleEndian | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| int |

## getInt32

```TypeScript
public getInt32(byteOffset: int): int
```

按指定类型从字节序列中读取值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## getInt32

```TypeScript
public getInt32(byteOffset: int, littleEndian?: boolean): int
```

按指定类型从字节序列中读取值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| littleEndian | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| int |

## getInt8

```TypeScript
public getInt8(byteOffset: int): int
```

按指定类型从字节序列中读取值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## getUint16

```TypeScript
public getUint16(byteOffset: int): int
```

按指定类型从字节序列中读取值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## getUint16

```TypeScript
public getUint16(byteOffset: int, littleEndian?: boolean): int
```

按指定类型从字节序列中读取值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| littleEndian | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| int |

## getUint32

```TypeScript
public getUint32(byteOffset: int): double
```

从字节序列中读取uint32值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |

**返回值：**

| 类型 |
| --- |
| double |

## getUint32

```TypeScript
public getUint32(byteOffset: int, littleEndian?: boolean): double
```

从字节序列中读取uint32值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| littleEndian | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| double |

## getUint8

```TypeScript
public getUint8(byteOffset: int): int
```

按指定类型从字节序列中读取值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## setBigInt64

```TypeScript
public setBigInt64(byteOffset: int, value: bigint, littleEndian?: boolean): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | bigint | 是 |
| littleEndian | boolean | 否 |

## setBigInt64

```TypeScript
public setBigInt64(byteOffset: int, value: long): void
```

将bigint64值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | long | 是 |

## setBigInt64

```TypeScript
public setBigInt64(byteOffset: int, value: long, littleEndian: boolean): void
```

将bigint64值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | long | 是 |
| littleEndian | boolean | 是 |

## setBigUint64

```TypeScript
public setBigUint64(byteOffset: int, value: long): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | long | 是 |

## setBigUint64

```TypeScript
public setBigUint64(byteOffset: int, value: long, littleEndian: boolean): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | long | 是 |
| littleEndian | boolean | 是 |

## setBigUint64

```TypeScript
public setBigUint64(byteOffset: int, value: bigint, littleEndian?: boolean): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | bigint | 是 |
| littleEndian | boolean | 否 |

## setFloat32

```TypeScript
public setFloat32(byteOffset: int, value: float): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | float | 是 |

## setFloat32

```TypeScript
public setFloat32(byteOffset: int, value: float, littleEndian: boolean): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | float | 是 |
| littleEndian | boolean | 是 |

## setFloat32

```TypeScript
public setFloat32(byteOffset: int, value: double, littleEndian?: boolean): void
```

将float32值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | double | 是 |
| littleEndian | boolean | 否 |

## setFloat64

```TypeScript
public setFloat64(byteOffset: int, value: double): void
```

将float64值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | double | 是 |

## setFloat64

```TypeScript
public setFloat64(byteOffset: int, value: double, littleEndian?: boolean): void
```

将float64值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | double | 是 |
| littleEndian | boolean | 否 |

## setInt16

```TypeScript
public setInt16(byteOffset: int, value: int): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | int | 是 |

## setInt16

```TypeScript
public setInt16(byteOffset: int, value: int, littleEndian: boolean): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | int | 是 |
| littleEndian | boolean | 是 |

## setInt16

```TypeScript
public setInt16(byteOffset: int, value: double, littleEndian?: boolean): void
```

将int16值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | double | 是 |
| littleEndian | boolean | 否 |

## setInt32

```TypeScript
public setInt32(byteOffset: int, value: int): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | int | 是 |

## setInt32

```TypeScript
public setInt32(byteOffset: int, value: int, littleEndian: boolean): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | int | 是 |
| littleEndian | boolean | 是 |

## setInt32

```TypeScript
public setInt32(byteOffset: int, value: double, littleEndian?: boolean): void
```

将int32值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | double | 是 |
| littleEndian | boolean | 否 |

## setInt8

```TypeScript
public setInt8(byteOffset: int, value: int): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | int | 是 |

## setInt8

```TypeScript
public setInt8(byteOffset: int, value: double): void
```

将int8值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | double | 是 |

## setUint16

```TypeScript
public setUint16(byteOffset: int, value: int): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | int | 是 |

## setUint16

```TypeScript
public setUint16(byteOffset: int, value: int, littleEndian: boolean): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | int | 是 |
| littleEndian | boolean | 是 |

## setUint16

```TypeScript
public setUint16(byteOffset: int, value: double, littleEndian?: boolean): void
```

将uint16值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | double | 是 |
| littleEndian | boolean | 否 |

## setUint32

```TypeScript
public setUint32(byteOffset: int, value: long): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | long | 是 |

## setUint32

```TypeScript
public setUint32(byteOffset: int, value: long, littleEndian: boolean): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | long | 是 |
| littleEndian | boolean | 是 |

## setUint32

```TypeScript
public setUint32(byteOffset: int, value: double, littleEndian?: boolean): void
```

将uint32值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | double | 是 |
| littleEndian | boolean | 否 |

## setUint8

```TypeScript
public setUint8(byteOffset: int, value: int): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | int | 是 |

## setUint8

```TypeScript
public setUint8(byteOffset: int, value: double): void
```

将uint8值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteOffset](#byteoffset) | int | 是 |
| value | double | 是 |

## buffer

```TypeScript
public get buffer(): ArrayBuffer
```

底层缓冲区。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## byteLength

```TypeScript
public get byteLength(): int
```

只读属性，表示DataView的byte长度。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## byteOffset

```TypeScript
public get byteOffset(): int
```

只读属性，表示DataView的byte偏移量。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang
