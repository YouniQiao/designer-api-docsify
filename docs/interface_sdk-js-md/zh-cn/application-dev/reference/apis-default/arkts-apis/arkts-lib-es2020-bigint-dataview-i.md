# DataView

**ArkTS模式：** 仅支持ArkTS-Dyn

## getBigInt64

```TypeScript
getBigInt64(byteOffset: number, littleEndian?: boolean): bigint
```

Gets the BigInt64 value at the specified byte offset from the start of the view. There is no alignment constraint; multi-byte values may be fetched from any offset.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-DataView-getBigInt64(byteOffset: number, littleEndian?: boolean): bigint--><!--Device-DataView-getBigInt64(byteOffset: number, littleEndian?: boolean): bigint-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | number | 是 |  |
| littleEndian | boolean | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint |  |

## getBigUint64

```TypeScript
getBigUint64(byteOffset: number, littleEndian?: boolean): bigint
```

Gets the BigUint64 value at the specified byte offset from the start of the view. There is no alignment constraint; multi-byte values may be fetched from any offset.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-DataView-getBigUint64(byteOffset: number, littleEndian?: boolean): bigint--><!--Device-DataView-getBigUint64(byteOffset: number, littleEndian?: boolean): bigint-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | number | 是 |  |
| littleEndian | boolean | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint |  |

## setBigInt64

```TypeScript
setBigInt64(byteOffset: number, value: bigint, littleEndian?: boolean): void
```

Stores a BigInt64 value at the specified byte offset from the start of the view.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-DataView-setBigInt64(byteOffset: number, value: bigint, littleEndian?: boolean): void--><!--Device-DataView-setBigInt64(byteOffset: number, value: bigint, littleEndian?: boolean): void-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | number | 是 |  |
| value | bigint | 是 |  |
| littleEndian | boolean | 否 |  |

## setBigUint64

```TypeScript
setBigUint64(byteOffset: number, value: bigint, littleEndian?: boolean): void
```

Stores a BigUint64 value at the specified byte offset from the start of the view.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-DataView-setBigUint64(byteOffset: number, value: bigint, littleEndian?: boolean): void--><!--Device-DataView-setBigUint64(byteOffset: number, value: bigint, littleEndian?: boolean): void-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteOffset | number | 是 |  |
| value | bigint | 是 |  |
| littleEndian | boolean | 否 |  |

