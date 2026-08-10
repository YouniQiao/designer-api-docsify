# DataView

**ArkTS模式：** 仅支持ArkTS-Dyn

## getFloat32

```TypeScript
getFloat32(byteOffset: number, littleEndian?: boolean): number
```

Gets the Float32 value at the specified byte offset from the start of the view. There is no alignment constraint; multi-byte values may be fetched from any offset.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-DataView-getFloat32(byteOffset: number, littleEndian?: boolean): number--><!--Device-DataView-getFloat32(byteOffset: number, littleEndian?: boolean): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | number | 是 |  |
| littleEndian | boolean | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## getFloat64

```TypeScript
getFloat64(byteOffset: number, littleEndian?: boolean): number
```

Gets the Float64 value at the specified byte offset from the start of the view. There is no alignment constraint; multi-byte values may be fetched from any offset.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-DataView-getFloat64(byteOffset: number, littleEndian?: boolean): number--><!--Device-DataView-getFloat64(byteOffset: number, littleEndian?: boolean): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | number | 是 |  |
| littleEndian | boolean | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## getInt16

```TypeScript
getInt16(byteOffset: number, littleEndian?: boolean): number
```

Gets the Int16 value at the specified byte offset from the start of the view. There is no alignment constraint; multi-byte values may be fetched from any offset.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-DataView-getInt16(byteOffset: number, littleEndian?: boolean): number--><!--Device-DataView-getInt16(byteOffset: number, littleEndian?: boolean): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | number | 是 |  |
| littleEndian | boolean | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## getInt32

```TypeScript
getInt32(byteOffset: number, littleEndian?: boolean): number
```

Gets the Int32 value at the specified byte offset from the start of the view. There is no alignment constraint; multi-byte values may be fetched from any offset.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-DataView-getInt32(byteOffset: number, littleEndian?: boolean): number--><!--Device-DataView-getInt32(byteOffset: number, littleEndian?: boolean): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | number | 是 |  |
| littleEndian | boolean | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## getInt8

```TypeScript
getInt8(byteOffset: number): number
```

Gets the Int8 value at the specified byte offset from the start of the view. There is no alignment constraint; multi-byte values may be fetched from any offset.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-DataView-getInt8(byteOffset: number): number--><!--Device-DataView-getInt8(byteOffset: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## getUint16

```TypeScript
getUint16(byteOffset: number, littleEndian?: boolean): number
```

Gets the Uint16 value at the specified byte offset from the start of the view. There is no alignment constraint; multi-byte values may be fetched from any offset.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-DataView-getUint16(byteOffset: number, littleEndian?: boolean): number--><!--Device-DataView-getUint16(byteOffset: number, littleEndian?: boolean): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | number | 是 |  |
| littleEndian | boolean | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## getUint32

```TypeScript
getUint32(byteOffset: number, littleEndian?: boolean): number
```

Gets the Uint32 value at the specified byte offset from the start of the view. There is no alignment constraint; multi-byte values may be fetched from any offset.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-DataView-getUint32(byteOffset: number, littleEndian?: boolean): number--><!--Device-DataView-getUint32(byteOffset: number, littleEndian?: boolean): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | number | 是 |  |
| littleEndian | boolean | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## getUint8

```TypeScript
getUint8(byteOffset: number): number
```

Gets the Uint8 value at the specified byte offset from the start of the view. There is no alignment constraint; multi-byte values may be fetched from any offset.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-DataView-getUint8(byteOffset: number): number--><!--Device-DataView-getUint8(byteOffset: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## setFloat32

```TypeScript
setFloat32(byteOffset: number, value: number, littleEndian?: boolean): void
```

Stores an Float32 value at the specified byte offset from the start of the view.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-DataView-setFloat32(byteOffset: number, value: number, littleEndian?: boolean): void--><!--Device-DataView-setFloat32(byteOffset: number, value: number, littleEndian?: boolean): void-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | number | 是 |  |
| value | number | 是 |  |
| littleEndian | boolean | 否 |  |

## setFloat64

```TypeScript
setFloat64(byteOffset: number, value: number, littleEndian?: boolean): void
```

Stores an Float64 value at the specified byte offset from the start of the view.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-DataView-setFloat64(byteOffset: number, value: number, littleEndian?: boolean): void--><!--Device-DataView-setFloat64(byteOffset: number, value: number, littleEndian?: boolean): void-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | number | 是 |  |
| value | number | 是 |  |
| littleEndian | boolean | 否 |  |

## setInt16

```TypeScript
setInt16(byteOffset: number, value: number, littleEndian?: boolean): void
```

Stores an Int16 value at the specified byte offset from the start of the view.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-DataView-setInt16(byteOffset: number, value: number, littleEndian?: boolean): void--><!--Device-DataView-setInt16(byteOffset: number, value: number, littleEndian?: boolean): void-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | number | 是 |  |
| value | number | 是 |  |
| littleEndian | boolean | 否 |  |

## setInt32

```TypeScript
setInt32(byteOffset: number, value: number, littleEndian?: boolean): void
```

Stores an Int32 value at the specified byte offset from the start of the view.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-DataView-setInt32(byteOffset: number, value: number, littleEndian?: boolean): void--><!--Device-DataView-setInt32(byteOffset: number, value: number, littleEndian?: boolean): void-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | number | 是 |  |
| value | number | 是 |  |
| littleEndian | boolean | 否 |  |

## setInt8

```TypeScript
setInt8(byteOffset: number, value: number): void
```

Stores an Int8 value at the specified byte offset from the start of the view.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-DataView-setInt8(byteOffset: number, value: number): void--><!--Device-DataView-setInt8(byteOffset: number, value: number): void-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | number | 是 |  |
| value | number | 是 |  |

## setUint16

```TypeScript
setUint16(byteOffset: number, value: number, littleEndian?: boolean): void
```

Stores an Uint16 value at the specified byte offset from the start of the view.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-DataView-setUint16(byteOffset: number, value: number, littleEndian?: boolean): void--><!--Device-DataView-setUint16(byteOffset: number, value: number, littleEndian?: boolean): void-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | number | 是 |  |
| value | number | 是 |  |
| littleEndian | boolean | 否 |  |

## setUint32

```TypeScript
setUint32(byteOffset: number, value: number, littleEndian?: boolean): void
```

Stores an Uint32 value at the specified byte offset from the start of the view.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-DataView-setUint32(byteOffset: number, value: number, littleEndian?: boolean): void--><!--Device-DataView-setUint32(byteOffset: number, value: number, littleEndian?: boolean): void-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | number | 是 |  |
| value | number | 是 |  |
| littleEndian | boolean | 否 |  |

## setUint8

```TypeScript
setUint8(byteOffset: number, value: number): void
```

Stores an Uint8 value at the specified byte offset from the start of the view.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-DataView-setUint8(byteOffset: number, value: number): void--><!--Device-DataView-setUint8(byteOffset: number, value: number): void-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | number | 是 |  |
| value | number | 是 |  |

## buffer

```TypeScript
readonly buffer: ArrayBuffer
```

**类型：** ArrayBuffer

**ArkTS模式：** 仅支持ArkTS-Dyn

## byteLength

```TypeScript
readonly byteLength: number
```

**类型：** number

**ArkTS模式：** 仅支持ArkTS-Dyn

## byteOffset

```TypeScript
readonly byteOffset: number
```

**类型：** number

**ArkTS模式：** 仅支持ArkTS-Dyn

