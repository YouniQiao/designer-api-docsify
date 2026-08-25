# TextEncoder

Provides APIs to encode strings into byte arrays. Multiple encoding formats are supported. When **TextEncoder** is used for encoding, the number of bytes occupied by a character varies according to the encoding format. You must explicitly specify the encoding format to obtain the required encoding result.

**Since:** 7

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **TextEncoder** object.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(encoding?: string)
```

A constructor used to create a **TextEncoder** object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [encoding](#encoding) | string | No |

## create

```TypeScript
static create(encoding?: string): TextEncoder
```

Creates a **TextEncoder** object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [encoding](#encoding) | string | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [TextEncoder](arkts-arkts-util-textencoder-c.md) |

## encode

```TypeScript
encode(input?: string): Uint8Array
```

Encodes the input content in to a Uint8Array object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [encodeInto](#encodeinto)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| input | string | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

## encodeInto

```TypeScript
encodeInto(input?: string): Uint8Array
```

Encodes the input content into a Uint8Array object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| input | string | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

## encodeInto

```TypeScript
encodeInto(input: string, dest: Uint8Array): { read: number; written: number }
```

Writes the generated UTF-8 encoded text to an array.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [encodeIntoUint8Array](#encodeintouint8array)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| input | string | Yes |
| dest | Uint8Array | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| object |

## encodeIntoUint8Array

```TypeScript
encodeIntoUint8Array(input: string, dest: Uint8Array): EncodeIntoUint8ArrayInfo
```

Encodes the input content and stores the result into a Uint8Array object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| input | string | Yes |
| dest | Uint8Array | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| object |
| [EncodeIntoUint8ArrayInfo](arkts-arkts-util-encodeintouint8arrayinfo-i.md) |

## encoding

```TypeScript
readonly encoding = 'utf-8'
```

Encoding format.The following formats are supported: utf-8, gb2312, gb18030, ibm866, iso-8859-1, iso-8859-2, iso-8859-3, iso-8859-4, iso-8859-5, iso-8859-6, iso-8859-7, iso-8859-8, iso-8859-8-i, iso-8859-10, iso-8859-13, iso-8859-14, iso-8859-15, koi8-r, koi8-u, macintosh, windows-874, windows-1250, windows-1251, windows-1252, windows-1253, windows-1254, windows-1255, windows-1256, windows-1257, windows-1258, gbk, big5, euc-jp, iso-2022- jp, shift_jis, euc-kr, x-mac-cyrillic, utf-16be, and utf-16le.The default value is **'utf-8'**.

**Type:** 'utf-8'

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang
