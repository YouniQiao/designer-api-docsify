# TextEncoder

The TextEncoder interface represents a text encoder. The encoder takes the byte stream as the input and outputs the String string.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-util-class TextEncoder--><!--Device-util-class TextEncoder-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(encoding?: string)
```

The textEncoder constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-TextEncoder-constructor(encoding?: string)--><!--Device-TextEncoder-constructor(encoding?: string)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| encoding | string | No | The string for encoding format. |

## create

```TypeScript
static create(encoding?: string): TextEncoder
```

Create a TextEncoder object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-TextEncoder-static create(encoding?: string): TextEncoder--><!--Device-TextEncoder-static create(encoding?: string): TextEncoder-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| encoding | string | No | The string for encoding format. |

**Return value:**

| Type | Description |
| --- | --- |
| [TextEncoder](arkts-util-textencoder-c.md) |  |

## encodeInto

```TypeScript
encodeInto(input?: string): Uint8Array
```

UTF-8 encodes the input string and returns a Uint8Array containing the encoded bytes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-TextEncoder-encodeInto(input?: string): Uint8Array--><!--Device-TextEncoder-encodeInto(input?: string): Uint8Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| input | string | No | The string to be encoded. |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | Returns the encoded text. |

## encodeIntoUint8Array

```TypeScript
encodeIntoUint8Array(input: string, dest: Uint8Array): EncodeIntoUint8ArrayInfo
```

Encode string, write the result to dest array.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-TextEncoder-encodeIntoUint8Array(input: string, dest: Uint8Array): EncodeIntoUint8ArrayInfo--><!--Device-TextEncoder-encodeIntoUint8Array(input: string, dest: Uint8Array): EncodeIntoUint8ArrayInfo-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| input | string | Yes | The string to be encoded. |
| dest | Uint8Array | Yes | Encoded numbers in accordance with the format |

**Return value:**

| Type | Description |
| --- | --- |
| [EncodeIntoUint8ArrayInfo](arkts-util-encodeintouint8arrayinfo-i.md) | Return the object, where read represents the number of characters that have been encoded, and written represents the number of bytes occupied by the encoded characters. |

