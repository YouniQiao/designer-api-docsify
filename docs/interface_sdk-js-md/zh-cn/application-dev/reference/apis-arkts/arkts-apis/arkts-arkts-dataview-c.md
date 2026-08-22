# DataView

DataView类。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-export class DataView--><!--Device-unnamed-export class DataView-End-->

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

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public constructor(buffer: ArrayBuffer, byteOffset?: int, byteLength?: int)--><!--Device-DataView-public constructor(buffer: ArrayBuffer, byteOffset?: int, byteLength?: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 该DataView的底层ArrayBuffer。 |
| byteOffset | int | 否 | 在ArrayBuffer中的byte偏移量。 <br>取值约束：应为整数。 |
| byteLength | int | 否 | DataView的byte长度。 <br>取值约束：应为整数。 |

## getBigInt64

```TypeScript
public getBigInt64(byteOffset: int, littleEndian?: boolean): bigint
```

按指定类型从字节序列中读取值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getBigInt64(byteOffset: int, littleEndian?: boolean): bigint--><!--Device-DataView-public getBigInt64(byteOffset: int, littleEndian?: boolean): bigint-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 读取位置的起始索引。 <br>取值约束：应为整数。 |
| littleEndian | boolean | 否 | 是否按小端序读取，true表示小端序，false表示大端序。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | byteOffset处的BigInt64值。 |

## getBigInt64

```TypeScript
public getBigInt64(byteOffset: int): bigint
```

从字节序列中读取bigint64值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getBigInt64(byteOffset: int): bigint--><!--Device-DataView-public getBigInt64(byteOffset: int): bigint-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 读取位置的起始索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | 读取到的值（大端序）。 |

## getBigUint64

```TypeScript
public getBigUint64(byteOffset: int, littleEndian?: boolean): bigint
```

按指定类型从字节序列中读取值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getBigUint64(byteOffset: int, littleEndian?: boolean): bigint--><!--Device-DataView-public getBigUint64(byteOffset: int, littleEndian?: boolean): bigint-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 读取位置的起始索引。 <br>取值约束：应为整数。 |
| littleEndian | boolean | 否 | 是否按小端序读取，true表示小端序，false表示大端序。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | byteOffset处的BigUint64值。 |

## getBigUint64

```TypeScript
public getBigUint64(byteOffset: int): bigint
```

从字节序列中读取biguint64值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getBigUint64(byteOffset: int): bigint--><!--Device-DataView-public getBigUint64(byteOffset: int): bigint-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 读取位置的起始索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | 读取到的值（大端序）。 |

## getFloat32

```TypeScript
public getFloat32(byteOffset: int): double
```

从字节序列中读取float32值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getFloat32(byteOffset: int): double--><!--Device-DataView-public getFloat32(byteOffset: int): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 读取位置的起始索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 读取到的值（大端序）。 |

## getFloat32

```TypeScript
public getFloat32(byteOffset: int, littleEndian?: boolean): double
```

从字节序列中读取float32值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getFloat32(byteOffset: int, littleEndian?: boolean): double--><!--Device-DataView-public getFloat32(byteOffset: int, littleEndian?: boolean): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 读取位置的起始索引。 |
| littleEndian | boolean | 否 | true表示小端序，false表示大端序。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 读取到的值。 |

## getFloat64

```TypeScript
public getFloat64(byteOffset: int): double
```

从字节序列中读取float64值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getFloat64(byteOffset: int): double--><!--Device-DataView-public getFloat64(byteOffset: int): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 读取位置的起始索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 读取到的值（大端序）。 |

## getFloat64

```TypeScript
public getFloat64(byteOffset: int, littleEndian?: boolean): double
```

从字节序列中读取float64值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getFloat64(byteOffset: int, littleEndian?: boolean): double--><!--Device-DataView-public getFloat64(byteOffset: int, littleEndian?: boolean): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 读取位置的起始索引。 |
| littleEndian | boolean | 否 | true表示小端序，false表示大端序。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 读取到的值。 |

## getInt16

```TypeScript
public getInt16(byteOffset: int): int
```

按指定类型从字节序列中读取值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getInt16(byteOffset: int): int--><!--Device-DataView-public getInt16(byteOffset: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 读取位置的起始索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | byteOffset处的Int16值。 |

## getInt16

```TypeScript
public getInt16(byteOffset: int, littleEndian?: boolean): int
```

按指定类型从字节序列中读取值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getInt16(byteOffset: int, littleEndian?: boolean): int--><!--Device-DataView-public getInt16(byteOffset: int, littleEndian?: boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 读取位置的起始索引。 <br>取值约束：应为整数。 |
| littleEndian | boolean | 否 | 是否按小端序读取，true表示小端序，false表示大端序。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | byteOffset处的Int16值。 |

## getInt32

```TypeScript
public getInt32(byteOffset: int): int
```

按指定类型从字节序列中读取值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getInt32(byteOffset: int): int--><!--Device-DataView-public getInt32(byteOffset: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 读取位置的起始索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | byteOffset处的Int32值。 |

## getInt32

```TypeScript
public getInt32(byteOffset: int, littleEndian?: boolean): int
```

按指定类型从字节序列中读取值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getInt32(byteOffset: int, littleEndian?: boolean): int--><!--Device-DataView-public getInt32(byteOffset: int, littleEndian?: boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 读取位置的起始索引。 <br>取值约束：应为整数。 |
| littleEndian | boolean | 否 | 是否按小端序读取，true表示小端序，false表示大端序。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | byteOffset处的Int32值。 |

## getInt8

```TypeScript
public getInt8(byteOffset: int): int
```

按指定类型从字节序列中读取值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getInt8(byteOffset: int): int--><!--Device-DataView-public getInt8(byteOffset: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 读取位置的起始索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | byteOffset处的Int8值。 |

## getUint16

```TypeScript
public getUint16(byteOffset: int): int
```

按指定类型从字节序列中读取值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getUint16(byteOffset: int): int--><!--Device-DataView-public getUint16(byteOffset: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 读取位置的起始索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | byteOffset处的Uint16值。 |

## getUint16

```TypeScript
public getUint16(byteOffset: int, littleEndian?: boolean): int
```

按指定类型从字节序列中读取值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getUint16(byteOffset: int, littleEndian?: boolean): int--><!--Device-DataView-public getUint16(byteOffset: int, littleEndian?: boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 读取位置的起始索引。 <br>取值约束：应为整数。 |
| littleEndian | boolean | 否 | 是否按小端序读取，true表示小端序，false表示大端序。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | byteOffset处的Uint16值。 |

## getUint32

```TypeScript
public getUint32(byteOffset: int): double
```

从字节序列中读取uint32值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getUint32(byteOffset: int): double--><!--Device-DataView-public getUint32(byteOffset: int): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 读取位置的起始索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 读取到的值（大端序）。 |

## getUint32

```TypeScript
public getUint32(byteOffset: int, littleEndian?: boolean): double
```

从字节序列中读取uint32值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getUint32(byteOffset: int, littleEndian?: boolean): double--><!--Device-DataView-public getUint32(byteOffset: int, littleEndian?: boolean): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 读取位置的起始索引。 |
| littleEndian | boolean | 否 | true表示小端序，false表示大端序。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 读取到的值。 |

## getUint8

```TypeScript
public getUint8(byteOffset: int): int
```

按指定类型从字节序列中读取值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public getUint8(byteOffset: int): int--><!--Device-DataView-public getUint8(byteOffset: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 读取位置的起始索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | byteOffset处的Uint8值。 |

## setBigInt64

```TypeScript
public setBigInt64(byteOffset: int, value: bigint, littleEndian?: boolean): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setBigInt64(byteOffset: int, value: bigint, littleEndian?: boolean): void--><!--Device-DataView-public setBigInt64(byteOffset: int, value: bigint, littleEndian?: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 <br>取值约束：应为整数。 |
| value | bigint | 是 | 待写入的bigint值。 |
| littleEndian | boolean | 否 | 是否按小端序读取，true表示小端序，false表示大端序。 |

## setBigInt64

```TypeScript
public setBigInt64(byteOffset: int, value: long): void
```

将bigint64值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setBigInt64(byteOffset: int, value: long): void--><!--Device-DataView-public setBigInt64(byteOffset: int, value: long): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 <br>取值约束：应为整数。 |
| value | long | 是 | 待写入的long值。 |

## setBigInt64

```TypeScript
public setBigInt64(byteOffset: int, value: long, littleEndian: boolean): void
```

将bigint64值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setBigInt64(byteOffset: int, value: long, littleEndian: boolean): void--><!--Device-DataView-public setBigInt64(byteOffset: int, value: long, littleEndian: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 <br>取值约束：应为整数。 |
| value | long | 是 | 待写入的long值。 |
| littleEndian | boolean | 是 | true表示小端序，false表示大端序。 |

## setBigUint64

```TypeScript
public setBigUint64(byteOffset: int, value: long): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setBigUint64(byteOffset: int, value: long): void--><!--Device-DataView-public setBigUint64(byteOffset: int, value: long): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 <br>取值约束：应为整数。 |
| value | long | 是 | 待写入的long值。 |

## setBigUint64

```TypeScript
public setBigUint64(byteOffset: int, value: long, littleEndian: boolean): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setBigUint64(byteOffset: int, value: long, littleEndian: boolean): void--><!--Device-DataView-public setBigUint64(byteOffset: int, value: long, littleEndian: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 <br>取值约束：应为整数。 |
| value | long | 是 | 待写入的long值。 |
| littleEndian | boolean | 是 | 是否按小端序读取，true表示小端序，false表示大端序。 |

## setBigUint64

```TypeScript
public setBigUint64(byteOffset: int, value: bigint, littleEndian?: boolean): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setBigUint64(byteOffset: int, value: bigint, littleEndian?: boolean): void--><!--Device-DataView-public setBigUint64(byteOffset: int, value: bigint, littleEndian?: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 <br>取值约束：应为整数。 |
| value | bigint | 是 |  |
| littleEndian | boolean | 否 | 是否按小端序读取，true表示小端序，false表示大端序。 |

## setFloat32

```TypeScript
public setFloat32(byteOffset: int, value: float): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setFloat32(byteOffset: int, value: float): void--><!--Device-DataView-public setFloat32(byteOffset: int, value: float): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 <br>取值约束：应为整数。 |
| value | float | 是 | 待写入的float值。 |

## setFloat32

```TypeScript
public setFloat32(byteOffset: int, value: float, littleEndian: boolean): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setFloat32(byteOffset: int, value: float, littleEndian: boolean): void--><!--Device-DataView-public setFloat32(byteOffset: int, value: float, littleEndian: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 <br>取值约束：应为整数。 |
| value | float | 是 | 待写入的float值。 |
| littleEndian | boolean | 是 | 是否按小端序读取，true表示小端序，false表示大端序。 |

## setFloat32

```TypeScript
public setFloat32(byteOffset: int, value: double, littleEndian?: boolean): void
```

将float32值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setFloat32(byteOffset: int, value: double, littleEndian?: boolean): void--><!--Device-DataView-public setFloat32(byteOffset: int, value: double, littleEndian?: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 |
| value | double | 是 | 待写入的double值。 |
| littleEndian | boolean | 否 | true表示小端序，false表示大端序。 |

## setFloat64

```TypeScript
public setFloat64(byteOffset: int, value: double): void
```

将float64值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setFloat64(byteOffset: int, value: double): void--><!--Device-DataView-public setFloat64(byteOffset: int, value: double): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 |
| value | double | 是 | 待写入的double值。 |

## setFloat64

```TypeScript
public setFloat64(byteOffset: int, value: double, littleEndian?: boolean): void
```

将float64值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setFloat64(byteOffset: int, value: double, littleEndian?: boolean): void--><!--Device-DataView-public setFloat64(byteOffset: int, value: double, littleEndian?: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 |
| value | double | 是 | 待写入的double值。 |
| littleEndian | boolean | 否 | true表示小端序，false表示大端序。 |

## setInt16

```TypeScript
public setInt16(byteOffset: int, value: int): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setInt16(byteOffset: int, value: int): void--><!--Device-DataView-public setInt16(byteOffset: int, value: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 <br>取值约束：应为整数。 |
| value | int | 是 | <br>取值约束：应为整数。 |

## setInt16

```TypeScript
public setInt16(byteOffset: int, value: int, littleEndian: boolean): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setInt16(byteOffset: int, value: int, littleEndian: boolean): void--><!--Device-DataView-public setInt16(byteOffset: int, value: int, littleEndian: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 <br>取值约束：应为整数。 |
| value | int | 是 | <br>取值约束：应为整数。 |
| littleEndian | boolean | 是 | 是否按小端序读取，true表示小端序，false表示大端序。 |

## setInt16

```TypeScript
public setInt16(byteOffset: int, value: double, littleEndian?: boolean): void
```

将int16值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setInt16(byteOffset: int, value: double, littleEndian?: boolean): void--><!--Device-DataView-public setInt16(byteOffset: int, value: double, littleEndian?: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 |
| value | double | 是 | 待写入的值。 |
| littleEndian | boolean | 否 | true表示小端序，false表示大端序。 |

## setInt32

```TypeScript
public setInt32(byteOffset: int, value: int): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setInt32(byteOffset: int, value: int): void--><!--Device-DataView-public setInt32(byteOffset: int, value: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 <br>取值约束：应为整数。 |
| value | int | 是 | <br>取值约束：应为整数。 |

## setInt32

```TypeScript
public setInt32(byteOffset: int, value: int, littleEndian: boolean): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setInt32(byteOffset: int, value: int, littleEndian: boolean): void--><!--Device-DataView-public setInt32(byteOffset: int, value: int, littleEndian: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 <br>取值约束：应为整数。 |
| value | int | 是 | <br>取值约束：应为整数。 |
| littleEndian | boolean | 是 | 是否按小端序读取，true表示小端序，false表示大端序。 |

## setInt32

```TypeScript
public setInt32(byteOffset: int, value: double, littleEndian?: boolean): void
```

将int32值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setInt32(byteOffset: int, value: double, littleEndian?: boolean): void--><!--Device-DataView-public setInt32(byteOffset: int, value: double, littleEndian?: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 |
| value | double | 是 | 待写入的值。 |
| littleEndian | boolean | 否 | true表示小端序，false表示大端序。 |

## setInt8

```TypeScript
public setInt8(byteOffset: int, value: int): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setInt8(byteOffset: int, value: int): void--><!--Device-DataView-public setInt8(byteOffset: int, value: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 <br>取值约束：应为整数。 |
| value | int | 是 | <br>取值约束：应为整数。 |

## setInt8

```TypeScript
public setInt8(byteOffset: int, value: double): void
```

将int8值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setInt8(byteOffset: int, value: double): void--><!--Device-DataView-public setInt8(byteOffset: int, value: double): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 |
| value | double | 是 | 待写入的值。 |

## setUint16

```TypeScript
public setUint16(byteOffset: int, value: int): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setUint16(byteOffset: int, value: int): void--><!--Device-DataView-public setUint16(byteOffset: int, value: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 <br>取值约束：应为整数。 |
| value | int | 是 | <br>取值约束：应为整数。 |

## setUint16

```TypeScript
public setUint16(byteOffset: int, value: int, littleEndian: boolean): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setUint16(byteOffset: int, value: int, littleEndian: boolean): void--><!--Device-DataView-public setUint16(byteOffset: int, value: int, littleEndian: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 <br>取值约束：应为整数。 |
| value | int | 是 | <br>取值约束：应为整数。 |
| littleEndian | boolean | 是 | 是否按小端序读取，true表示小端序，false表示大端序。 |

## setUint16

```TypeScript
public setUint16(byteOffset: int, value: double, littleEndian?: boolean): void
```

将uint16值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setUint16(byteOffset: int, value: double, littleEndian?: boolean): void--><!--Device-DataView-public setUint16(byteOffset: int, value: double, littleEndian?: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 |
| value | double | 是 | 待写入的double值。 |
| littleEndian | boolean | 否 | true表示小端序，false表示大端序。 |

## setUint32

```TypeScript
public setUint32(byteOffset: int, value: long): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setUint32(byteOffset: int, value: long): void--><!--Device-DataView-public setUint32(byteOffset: int, value: long): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 <br>取值约束：应为整数。 |
| value | long | 是 | 待写入的long值。 |

## setUint32

```TypeScript
public setUint32(byteOffset: int, value: long, littleEndian: boolean): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setUint32(byteOffset: int, value: long, littleEndian: boolean): void--><!--Device-DataView-public setUint32(byteOffset: int, value: long, littleEndian: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 <br>取值约束：应为整数。 |
| value | long | 是 | 待写入的long值。 |
| littleEndian | boolean | 是 | 是否按小端序读取，true表示小端序，false表示大端序。 |

## setUint32

```TypeScript
public setUint32(byteOffset: int, value: double, littleEndian?: boolean): void
```

将uint32值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setUint32(byteOffset: int, value: double, littleEndian?: boolean): void--><!--Device-DataView-public setUint32(byteOffset: int, value: double, littleEndian?: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 |
| value | double | 是 | 待写入的值。 |
| littleEndian | boolean | 否 | true表示小端序，false表示大端序。 |

## setUint8

```TypeScript
public setUint8(byteOffset: int, value: int): void
```

按指定类型将值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setUint8(byteOffset: int, value: int): void--><!--Device-DataView-public setUint8(byteOffset: int, value: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 <br>取值约束：应为整数。 |
| value | int | 是 | <br>取值约束：应为整数。 |

## setUint8

```TypeScript
public setUint8(byteOffset: int, value: double): void
```

将uint8值写入字节序列。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataView-public setUint8(byteOffset: int, value: double): void--><!--Device-DataView-public setUint8(byteOffset: int, value: double): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | int | 是 | 写入位置的起始索引。 |
| value | double | 是 | 待写入的值。 |

