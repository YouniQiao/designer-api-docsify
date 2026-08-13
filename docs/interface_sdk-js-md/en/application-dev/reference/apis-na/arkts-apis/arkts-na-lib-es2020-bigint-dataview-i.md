# DataView

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-unnamed-interface DataView--><!--Device-unnamed-interface DataView-End-->

## getBigInt64

```TypeScript
getBigInt64(byteOffset: number, littleEndian?: boolean): bigint
```

Gets the BigInt64 value at the specified byte offset from the start of the view. There is no alignment constraint; multi-byte values may be fetched from any offset.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-DataView-getBigInt64(byteOffset: number, littleEndian?: boolean): bigint--><!--Device-DataView-getBigInt64(byteOffset: number, littleEndian?: boolean): bigint-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | number | Yes |  |
| littleEndian | boolean | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| bigint |  |

## getBigUint64

```TypeScript
getBigUint64(byteOffset: number, littleEndian?: boolean): bigint
```

Gets the BigUint64 value at the specified byte offset from the start of the view. There is no alignment constraint; multi-byte values may be fetched from any offset.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-DataView-getBigUint64(byteOffset: number, littleEndian?: boolean): bigint--><!--Device-DataView-getBigUint64(byteOffset: number, littleEndian?: boolean): bigint-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | number | Yes |  |
| littleEndian | boolean | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| bigint |  |

## setBigInt64

```TypeScript
setBigInt64(byteOffset: number, value: bigint, littleEndian?: boolean): void
```

Stores a BigInt64 value at the specified byte offset from the start of the view.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-DataView-setBigInt64(byteOffset: number, value: bigint, littleEndian?: boolean): void--><!--Device-DataView-setBigInt64(byteOffset: number, value: bigint, littleEndian?: boolean): void-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | number | Yes |  |
| value | bigint | Yes |  |
| littleEndian | boolean | No |  |

## setBigUint64

```TypeScript
setBigUint64(byteOffset: number, value: bigint, littleEndian?: boolean): void
```

Stores a BigUint64 value at the specified byte offset from the start of the view.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-DataView-setBigUint64(byteOffset: number, value: bigint, littleEndian?: boolean): void--><!--Device-DataView-setBigUint64(byteOffset: number, value: bigint, littleEndian?: boolean): void-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| byteOffset | number | Yes |  |
| value | bigint | Yes |  |
| littleEndian | boolean | No |  |

