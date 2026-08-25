# TextDecoder

Provides APIs to decode byte arrays into strings. It supports multiple formats, including UTF-8, UTF-16LE, UTF-16BE, ISO-8859, and Windows-1251.

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

A constructor used to create a **TextDecoder** object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(encoding?: string, options?: { fatal?: boolean; ignoreBOM?: boolean })
```

A constructor used to create a **TextDecoder** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [create](#create)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [encoding](#encoding) | string | No |
| options | { fatal?: boolean; ignoreBOM?: boolean } | No |

## create

```TypeScript
static create(encoding?: string, options?: TextDecoderOptions): TextDecoder
```

Creates a **TextDecoder** object. It provides the same function as the deprecated argument constructor.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [encoding](#encoding) | string | No |
| options | [TextDecoderOptions](arkts-arkts-util-textdecoderoptions-i.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [TextDecoder](arkts-arkts-util-textdecoder-c.md) |

## decode

```TypeScript
decode(input: Uint8Array, options?: { stream?: false }): string
```

Decodes the input content into a string.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [decodeToString](#decodetostring)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| input | Uint8Array | Yes |
| options | { stream?: false } | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## decodeToString

```TypeScript
decodeToString(input: Uint8Array, options?: DecodeToStringOptions): string
```

Decodes the input content into a string.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| input | Uint8Array | Yes |
| options | [DecodeToStringOptions](arkts-arkts-util-decodetostringoptions-i.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## decodeWithStream

```TypeScript
decodeWithStream(input: Uint8Array, options?: DecodeWithStreamOptions): string
```

Decodes the input content into a string. If **input** is an empty array, **undefined** is returned.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [decodeToString](#decodetostring)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| input | Uint8Array | Yes |
| options | [DecodeWithStreamOptions](arkts-arkts-util-decodewithstreamoptions-i.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## encoding

```TypeScript
readonly encoding: string
```

Encoding format.The following formats are supported: utf-8, ibm866, iso-8859-2, iso-8859-3, iso-8859-4, iso-8 859-5, iso-8859-6, iso-8859-7, iso-8859-8, iso-8859-8-i, iso-8859-10, iso-8859-13, iso-8859-14, iso-8859-15, koi8 -r, koi8-u, macintosh, windows-874, windows-1250, windows-1251, windows-1252, windows-1253, windows-1254, windows -1255, windows-1256, windows-1257, windows-1258, x-mac-cyrillic, gbk, gb18030, big5, euc-jp, iso-2022-jp, shift_jis, euc-kr, utf-16be, utf-16le, gb2312, and iso-8859-1.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## fatal

```TypeScript
readonly fatal: boolean
```

Whether to display fatal errors. The value **true** means to display fatal errors, and **false** means the opposite.

**Type:** boolean

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

## ignoreBOM

```TypeScript
readonly ignoreBOM = false
```

Whether to ignore the byte order marker (BOM). The default value is **false**, which indicates that the result contains the BOM.

**Type:** false

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang
