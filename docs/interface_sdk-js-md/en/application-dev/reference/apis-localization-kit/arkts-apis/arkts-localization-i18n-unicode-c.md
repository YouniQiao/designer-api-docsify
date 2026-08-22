# Unicode

Provides character attribute management capabilities, such as checking whether a character is a space, digit, or letter.

**Since:** 23

<!--Device-i18n-export class Unicode--><!--Device-i18n-export class Unicode-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bytes | Uint8Array | Yes | Input byte stream. To detect the encoding of a text string, convert the text to a byte stream first while preserving its original format. <br>Byte stream to be identified and encoded |

**Return value:**

| Type | Description |
| --- | --- |
| [EncodingInfo](arkts-localization-i18n-encodinginfo-i.md) | An object containing the detected encoding name and detection confidence level. |

## getType

```TypeScript
static getType(ch: string): string
```

Obtains the type of the input character.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Unicode-static getType(ch: string): string--><!--Device-Unicode-static getType(ch: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked.<br>**Since:** 12 |

**Return value:**

| Type | Description |
| --- | --- |
| string | Type of the input character.U_UNASSIGNED： Non-category for unassigned and non-character code points. The value can be |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let unicodeType: string = i18n.Unicode.getType('a'); // unicodeType = 'U_LOWERCASE_LETTER'
```

## isDigit

```TypeScript
static isDigit(ch: string): boolean
```

Checks whether the input character is a digit.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Unicode-static isDigit(ch: string): boolean--><!--Device-Unicode-static isDigit(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked.<br>**Since:** 12 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true** if the input character is a digit, and **false** otherwise. |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isDigit: boolean = i18n.Unicode.isDigit('1'); // isDigit = true
```

## isIdeograph

```TypeScript
static isIdeograph(ch: string): boolean
```

Checks whether the input character is an ideographic character.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Unicode-static isIdeograph(ch: string): boolean--><!--Device-Unicode-static isIdeograph(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked.<br>**Since:** 12 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true** if the input character an ideographic character, and **false** otherwise. |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isIdeograph: boolean = i18n.Unicode.isIdeograph('a'); // isIdeograph = false
```

## isLetter

```TypeScript
static isLetter(ch: string): boolean
```

Checks whether the input character is a letter.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Unicode-static isLetter(ch: string): boolean--><!--Device-Unicode-static isLetter(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked.<br>**Since:** 12 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true** if the input character a letter, and **false** otherwise. |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isLetter: boolean = i18n.Unicode.isLetter('a'); // isLetter = true
```

## isLowerCase

```TypeScript
static isLowerCase(ch: string): boolean
```

Checks whether the input character is a lowercase letter.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Unicode-static isLowerCase(ch: string): boolean--><!--Device-Unicode-static isLowerCase(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked.<br>**Since:** 12 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true** if the input character a lowercase letter, and **false** otherwise. |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isLowercase: boolean = i18n.Unicode.isLowerCase('a'); // isLowercase = true
```

## isRTL

```TypeScript
static isRTL(ch: string): boolean
```

Checks whether the input character is of the right to left (RTL) language.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Unicode-static isRTL(ch: string): boolean--><!--Device-Unicode-static isRTL(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked.<br>**Since:** 12 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true** if the input character is of the RTL language, and **false** otherwise. |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isZhRTL: boolean = i18n.isRTL('zh-CN'); // Since Chinese is not written from right to left, false is returned.
let isArRTL: boolean = i18n.isRTL('ar-EG'); // Since Arabic is written from right to left, true is returned.
```

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isRtl: boolean = i18n.Unicode.isRTL('a'); // isRtl = false
```

## isSpaceChar

```TypeScript
static isSpaceChar(ch: string): boolean
```

Checks whether the input character is a space.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Unicode-static isSpaceChar(ch: string): boolean--><!--Device-Unicode-static isSpaceChar(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked.<br>**Since:** 12 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true** if the input character is a space, and **false** otherwise. |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isSpacechar: boolean = i18n.Unicode.isSpaceChar('a'); // isSpacechar = false
```

## isUpperCase

```TypeScript
static isUpperCase(ch: string): boolean
```

Checks whether the input character is an uppercase letter.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Unicode-static isUpperCase(ch: string): boolean--><!--Device-Unicode-static isUpperCase(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked.<br>**Since:** 12 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true** if the input character an uppercase letter, and **false** otherwise. |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isUppercase: boolean = i18n.Unicode.isUpperCase('a'); // isUppercase = false
```

## isWhitespace

```TypeScript
static isWhitespace(ch: string): boolean
```

Checks whether the input character is a whitespace.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Unicode-static isWhitespace(ch: string): boolean--><!--Device-Unicode-static isWhitespace(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked.<br>**Since:** 12 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true** if the input character is a white space, and **false** otherwise. |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isWhitespace: boolean = i18n.Unicode.isWhitespace('a'); // isWhitespace = false
```

