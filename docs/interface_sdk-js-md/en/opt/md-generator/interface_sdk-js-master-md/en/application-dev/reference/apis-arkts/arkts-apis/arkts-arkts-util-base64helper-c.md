# Base64Helper

Provides encoding and decoding for Base64 and Base64URL. The Base64 encoding table contains 64 characters, which are the uppercase letters (A-Z), lowercase letters (a-z), digits (0-9), and the special characters plus sign (+)and slash (/). During encoding, the original data is divided into groups of three bytes, and each group contains a6-bit number. Then, the corresponding characters in the Base64 encoding table are used to represent these numbers.If the last group contains only one or two bytes, the equal sign (=) is used for padding. The Base64URL encoding table contains 64 characters, which are the uppercase letters (A-Z), lowercase letters (a-z), digits (0-9), and the special characters plus sign (+) and slash (/). The Base64URL encoding result does not contain equal signs (=).

**Since:** 9

<!--Device-util-class Base64Helper--><!--Device-util-class Base64Helper-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **Base64Helper** instance.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Base64Helper-constructor()--><!--Device-Base64Helper-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## decode

```TypeScript
decode(src: Uint8Array | string, options?: Type): Promise<Uint8Array>
```

Decodes the input content into a Uint8Array object. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Base64Helper-decode(src: Uint8Array | string, options?: Type): Promise<Uint8Array>--><!--Device-Base64Helper-decode(src: Uint8Array | string, options?: Type): Promise<Uint8Array>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | Uint8Array \| string | Yes |
| options | [Type](arkts-arkts-util-type-e.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Uint8Array&gt; |

## decodeSync

```TypeScript
decodeSync(src: Uint8Array | string, options?: Type): Uint8Array
```

Decodes a string into a Uint8Array object. This API returns the result synchronously.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Base64Helper-decodeSync(src: Uint8Array | string, options?: Type): Uint8Array--><!--Device-Base64Helper-decodeSync(src: Uint8Array | string, options?: Type): Uint8Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | Uint8Array \| string | Yes |
| options | [Type](arkts-arkts-util-type-e.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

## encode

```TypeScript
encode(src: Uint8Array, options?: Type): Promise<Uint8Array>
```

Encodes the input content into a Uint8Array object. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Base64Helper-encode(src: Uint8Array, options?: Type): Promise<Uint8Array>--><!--Device-Base64Helper-encode(src: Uint8Array, options?: Type): Promise<Uint8Array>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | Uint8Array | Yes |
| options | [Type](arkts-arkts-util-type-e.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Uint8Array&gt; |

## encodeSync

```TypeScript
encodeSync(src: Uint8Array, options?: Type): Uint8Array
```

Encodes the input content into a Uint8Array object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Base64Helper-encodeSync(src: Uint8Array, options?: Type): Uint8Array--><!--Device-Base64Helper-encodeSync(src: Uint8Array, options?: Type): Uint8Array-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | Uint8Array | Yes |
| options | [Type](arkts-arkts-util-type-e.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

## encodeToString

```TypeScript
encodeToString(src: Uint8Array, options?: Type): Promise<string>
```

Encodes the input content into a string. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Base64Helper-encodeToString(src: Uint8Array, options?: Type): Promise<string>--><!--Device-Base64Helper-encodeToString(src: Uint8Array, options?: Type): Promise<string>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | Uint8Array | Yes |
| options | [Type](arkts-arkts-util-type-e.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

## encodeToStringSync

```TypeScript
encodeToStringSync(src: Uint8Array, options?: Type): string
```

Performs Base64 encoding on the input Uint8Array byte array and returns a string. This method supports multiple encoding formats, including standard Base64 encoding, MIME-compliant Base64 encoding (with line breaks), and URL-safe Base64 encoding.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Base64Helper-encodeToStringSync(src: Uint8Array, options?: Type): string--><!--Device-Base64Helper-encodeToStringSync(src: Uint8Array, options?: Type): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | Uint8Array | Yes |
| options | [Type](arkts-arkts-util-type-e.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |
