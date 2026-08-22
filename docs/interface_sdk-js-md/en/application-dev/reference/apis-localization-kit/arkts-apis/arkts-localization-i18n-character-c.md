# Character

Provides the API for accessing unicode character properties. For example, determine whether a character is a number.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [Unicode](arkts-localization-i18n-unicode-c.md)

<!--Device-i18n-export class Character--><!--Device-i18n-export class Character-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## getType

```TypeScript
getType(ch: string): string
```

Obtains the type of the input character.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getType](arkts-localization-i18n-unicode-c.md#gettype)

<!--Device-Character-getType(ch: string): string--><!--Device-Character-getType(ch: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Type of the input character. |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let unicodeType: string = i18n.Unicode.getType('a'); // unicodeType = 'U_LOWERCASE_LETTER'
```

## isDigit

```TypeScript
isDigit(ch: string): boolean
```

Checks whether the input character is a digit.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isDigit](arkts-localization-i18n-unicode-c.md#isdigit)

<!--Device-Character-isDigit(ch: string): boolean--><!--Device-Character-isDigit(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

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
isIdeograph(ch: string): boolean
```

Checks whether the input character is an ideographic character.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isIdeograph](arkts-localization-i18n-unicode-c.md#isideograph)

<!--Device-Character-isIdeograph(ch: string): boolean--><!--Device-Character-isIdeograph(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

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
isLetter(ch: string): boolean
```

Checks whether the input character is a letter.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isLetter](arkts-localization-i18n-unicode-c.md#isletter)

<!--Device-Character-isLetter(ch: string): boolean--><!--Device-Character-isLetter(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

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
isLowerCase(ch: string): boolean
```

Checks whether the input character is a lowercase letter.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isLowerCase](arkts-localization-i18n-unicode-c.md#islowercase)

<!--Device-Character-isLowerCase(ch: string): boolean--><!--Device-Character-isLowerCase(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

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
isRTL(ch: string): boolean
```

Checks whether the input character is of the right to left (RTL) language.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isRTL](arkts-localization-i18n-unicode-c.md#isrtl)

<!--Device-Character-isRTL(ch: string): boolean--><!--Device-Character-isRTL(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

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
isSpaceChar(ch: string): boolean
```

Checks whether the input character is a space.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isSpaceChar](arkts-localization-i18n-unicode-c.md#isspacechar)

<!--Device-Character-isSpaceChar(ch: string): boolean--><!--Device-Character-isSpaceChar(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

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
isUpperCase(ch: string): boolean
```

Checks whether the input character is an uppercase letter.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isUpperCase](arkts-localization-i18n-unicode-c.md#isuppercase)

<!--Device-Character-isUpperCase(ch: string): boolean--><!--Device-Character-isUpperCase(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

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
isWhitespace(ch: string): boolean
```

Checks whether the input character is a whitespace.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isWhitespace](arkts-localization-i18n-unicode-c.md#iswhitespace)

<!--Device-Character-isWhitespace(ch: string): boolean--><!--Device-Character-isWhitespace(ch: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true** if the input character is a white space, and **false** otherwise. |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isWhitespace: boolean = i18n.Unicode.isWhitespace('a'); // isWhitespace = false
```

