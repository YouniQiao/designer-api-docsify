# Unicode

Provides character attribute management capabilities, such as checking whether a character is a space, digit, or letter.

**Since:** 9

<!--Device-i18n-export class Unicode--><!--Device-i18n-export class Unicode-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## detectEncoding

```TypeScript
static detectEncoding(bytes: Uint8Array): EncodingInfo
```

Detects the encoding information of the input byte stream.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Unicode-static detectEncoding(bytes: Uint8Array): EncodingInfo--><!--Device-Unicode-static detectEncoding(bytes: Uint8Array): EncodingInfo-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bytes | Uint8Array | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [EncodingInfo](arkts-localization-i18n-encodinginfo-i.md) |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let uint8Array = new Uint8Array([0xEF, 0xBB, 0xBF, 0xE4, 0xB8, 0xAD]);
let info = i18n.Unicode.detectEncoding(uint8Array); // info.encodingName = 'UTF-8', info.confidence = 100
```

## getType

```TypeScript
static getType(ch: string): string
```

Obtains the type of the input character.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Unicode-static getType(ch: string): string--><!--Device-Unicode-static getType(ch: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ch | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let unicodeType: string = i18n.Unicode.getType('a'); // unicodeType = 'U_LOWERCASE_LETTER'
```

## isDigit

```TypeScript
static isDigit(ch: string): boolean
```

Checks whether the input character is a digit.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Unicode-static isDigit(ch: string): boolean--><!--Device-Unicode-static isDigit(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ch | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isDigit: boolean = i18n.Unicode.isDigit('1'); // isDigit = true
```

## isIdeograph

```TypeScript
static isIdeograph(ch: string): boolean
```

Checks whether the input character is an ideographic character.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Unicode-static isIdeograph(ch: string): boolean--><!--Device-Unicode-static isIdeograph(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ch | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isIdeograph: boolean = i18n.Unicode.isIdeograph('a'); // isIdeograph = false
```

## isLetter

```TypeScript
static isLetter(ch: string): boolean
```

Checks whether the input character is a letter.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Unicode-static isLetter(ch: string): boolean--><!--Device-Unicode-static isLetter(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ch | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isLetter: boolean = i18n.Unicode.isLetter('a'); // isLetter = true
```

## isLowerCase

```TypeScript
static isLowerCase(ch: string): boolean
```

Checks whether the input character is a lowercase letter.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Unicode-static isLowerCase(ch: string): boolean--><!--Device-Unicode-static isLowerCase(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ch | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isLowercase: boolean = i18n.Unicode.isLowerCase('a'); // isLowercase = true
```

## isRTL

```TypeScript
static isRTL(ch: string): boolean
```

Checks whether the input character is of the right to left (RTL) language.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Unicode-static isRTL(ch: string): boolean--><!--Device-Unicode-static isRTL(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ch | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isRtl: boolean = i18n.Unicode.isRTL('a'); // isRtl = false
```

## isSpaceChar

```TypeScript
static isSpaceChar(ch: string): boolean
```

Checks whether the input character is a space.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Unicode-static isSpaceChar(ch: string): boolean--><!--Device-Unicode-static isSpaceChar(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ch | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isSpacechar: boolean = i18n.Unicode.isSpaceChar('a'); // isSpacechar = false
```

## isUpperCase

```TypeScript
static isUpperCase(ch: string): boolean
```

Checks whether the input character is an uppercase letter.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Unicode-static isUpperCase(ch: string): boolean--><!--Device-Unicode-static isUpperCase(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ch | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isUppercase: boolean = i18n.Unicode.isUpperCase('a'); // isUppercase = false
```

## isWhitespace

```TypeScript
static isWhitespace(ch: string): boolean
```

Checks whether the input character is a whitespace.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Unicode-static isWhitespace(ch: string): boolean--><!--Device-Unicode-static isWhitespace(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ch | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isWhitespace: boolean = i18n.Unicode.isWhitespace('a'); // isWhitespace = false
```
