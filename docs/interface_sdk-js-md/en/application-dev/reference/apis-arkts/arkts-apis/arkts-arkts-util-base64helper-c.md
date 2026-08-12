# Base64Helper

Decodes a Base64 encoded String or input u8 array into a newly-allocated u8 array using the Base64 encoding scheme.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-util-class Base64Helper--><!--Device-util-class Base64Helper-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from '@kit.ArkTS';
```

## constructor

```TypeScript
constructor()
```

Constructor for creating base64 encoding and decoding

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Base64Helper-constructor()--><!--Device-Base64Helper-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## decode

```TypeScript
decode(src: Uint8Array | string, options?: Type): Promise<Uint8Array>
```

Use the Base64 encoding scheme to asynchronously decode a Base64-encoded string or input u8 array into a newly allocated u8 array.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Base64Helper-decode(src: Uint8Array | string, options?: Type): Promise<Uint8Array>--><!--Device-Base64Helper-decode(src: Uint8Array | string, options?: Type): Promise<Uint8Array>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | Uint8Array \| string | Yes | A Uint8Array value or a string value |
| options | [Type](arkts-arkts-util-type-e.md) | No | one of the Type enumeration |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Uint8Array&gt; | Return the decoded asynchronous Uint8Array. |

## decodeSync

```TypeScript
decodeSync(src: Uint8Array | string, options?: Type): Uint8Array
```

Decodes a Base64 encoded String or input u8 array into a newly-allocated u8 array using the Base64 encoding scheme.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Base64Helper-decodeSync(src: Uint8Array | string, options?: Type): Uint8Array--><!--Device-Base64Helper-decodeSync(src: Uint8Array | string, options?: Type): Uint8Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | Uint8Array \| string | Yes | A Uint8Array value or a string value |
| options | [Type](arkts-arkts-util-type-e.md) | No | one of the Type enumeration |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | Return the decoded Uint8Array. |

## encode

```TypeScript
encode(src: Uint8Array, options?: Type): Promise<Uint8Array>
```

Asynchronously encodes all bytes in the specified u8 array into the newly allocated u8 array using the Base64 encoding scheme.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Base64Helper-encode(src: Uint8Array, options?: Type): Promise<Uint8Array>--><!--Device-Base64Helper-encode(src: Uint8Array, options?: Type): Promise<Uint8Array>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | Uint8Array | Yes | A Uint8Array value |
| options | [Type](arkts-arkts-util-type-e.md) | No | Enumerating input parameters includes two encoding formats: BASIC and BASIC_URL_SAFE |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Uint8Array&gt; | Return the encodes asynchronous new Uint8Array. |

## encodeSync

```TypeScript
encodeSync(src: Uint8Array, options?: Type): Uint8Array
```

Encodes all bytes from the specified u8 array into a newly-allocated u8 array using the Base64 encoding scheme.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Base64Helper-encodeSync(src: Uint8Array, options?: Type): Uint8Array--><!--Device-Base64Helper-encodeSync(src: Uint8Array, options?: Type): Uint8Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | Uint8Array | Yes | A Uint8Array value |
| options | [Type](arkts-arkts-util-type-e.md) | No | Enumerating input parameters includes two encoding formats: BASIC and BASIC_URL_SAFE |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | Return the encoded new Uint8Array. |

## encodeToString

```TypeScript
encodeToString(src: Uint8Array, options?: Type): Promise<string>
```

Asynchronously encodes the specified byte array into a String using the Base64 encoding scheme.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Base64Helper-encodeToString(src: Uint8Array, options?: Type): Promise<string>--><!--Device-Base64Helper-encodeToString(src: Uint8Array, options?: Type): Promise<string>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | Uint8Array | Yes | A Uint8Array value |
| options | [Type](arkts-arkts-util-type-e.md) | No | one of the Type enumeration |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Returns the encoded asynchronous string. |

## encodeToStringSync

```TypeScript
encodeToStringSync(src: Uint8Array, options?: Type): string
```

Encodes the specified byte array into a String using the Base64 encoding scheme.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Base64Helper-encodeToStringSync(src: Uint8Array, options?: Type): string--><!--Device-Base64Helper-encodeToStringSync(src: Uint8Array, options?: Type): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | Uint8Array | Yes | A Uint8Array value |
| options | [Type](arkts-arkts-util-type-e.md) | No | one of the Type enumeration |

**Return value:**

| Type | Description |
| --- | --- |
| string | Return the encoded string. |

