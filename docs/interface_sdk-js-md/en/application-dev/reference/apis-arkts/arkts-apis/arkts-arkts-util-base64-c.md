# Base64

Decodes a string or Uint8Array containing Base64 data into a newly allocated Uint8Array.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [Base64Helper](arkts-arkts-util-base64helper-c.md)

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **Base64** object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [constructor](arkts-arkts-util-base64helper-c.md#constructor)

**System capability:** SystemCapability.Utils.Lang

## decode

```TypeScript
decode(src: Uint8Array | string): Promise<Uint8Array>
```

Decodes the input content into a Uint8Array object. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [decode](arkts-arkts-util-base64helper-c.md#decode)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | Uint8Array \| string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Uint8Array & gt; |

## decodeSync

```TypeScript
decodeSync(src: Uint8Array | string): Uint8Array
```

Decodes the input content into a Uint8Array object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [decodeSync](arkts-arkts-util-base64helper-c.md#decodesync)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | Uint8Array \| string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

## encode

```TypeScript
encode(src: Uint8Array): Promise<Uint8Array>
```

Encodes the input content into a Uint8Array object. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [encode](arkts-arkts-util-base64helper-c.md#encode)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | Uint8Array | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Uint8Array & gt; |

## encodeSync

```TypeScript
encodeSync(src: Uint8Array): Uint8Array
```

Performs Base64 encoding on the input Uint8Array byte array and returns the encoded Uint8Array.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [encodeSync](arkts-arkts-util-base64helper-c.md#encodesync)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | Uint8Array | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

## encodeToString

```TypeScript
encodeToString(src: Uint8Array): Promise<string>
```

Encodes the input content into a string. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [encodeToString](arkts-arkts-util-base64helper-c.md#encodetostring)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | Uint8Array | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## encodeToStringSync

```TypeScript
encodeToStringSync(src: Uint8Array): string
```

Performs Base64 encoding on the input Uint8Array byte array and returns the encoded string.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [encodeToStringSync](arkts-arkts-util-base64helper-c.md#encodetostringsync)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | Uint8Array | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |
