# PluralRules

Provides the capability for obtaining the plural rule type.

**Since:** 8

**Deprecated since:** 20

**Substitutes:** [Intl.PluralRules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules)

<!--Device-intl-export class PluralRules--><!--Device-intl-export class PluralRules-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { intl } from '@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor()
```

Creates a **PluralRules** object to obtain the singular-plural type of numbers.

**Since:** 8

**Deprecated since:** 20

**Substitutes:** [Intl.PluralRules.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PluralRules-constructor()--><!--Device-PluralRules-constructor()-End-->

**System capability:** SystemCapability.Global.I18n

**Examples**

```TypeScript
import { intl } from '@kit.LocalizationKit';

// The current system locale is used by the default constructor.
let locale = new intl.Locale();
// Return the current system locale ID.
let localeID = locale.toString();
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a zh-CN locale object.
let locale = new intl.Locale('zh-CN');
let localeID = locale.toString(); // localeID = 'zh-CN'
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a DateTimeFormat object using the current system locale ID.
let formatter: intl.DateTimeFormat = new intl.DateTimeFormat();
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a DateTimeFormat object with locale ID being zh-CN, dateStyle being full, and timeStyle being medium.
let formatter: intl.DateTimeFormat = new intl.DateTimeFormat('zh-CN', { dateStyle: 'full', timeStyle: 'medium' });

// Create a DateTimeFormat object with a locale ID array. The locale ID ban is invalid and therefore locale ID zh is used.
formatter = new intl.DateTimeFormat(['ban', 'zh'], { dateStyle: 'full', timeStyle: 'medium' });
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a NumberFormat object using the current system locale ID.
let formatter: intl.NumberFormat = new intl.NumberFormat();
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a NumberFormat object with locale ID being en-GB, style being decimal, and notation being scientific.
let formatter: intl.NumberFormat = new intl.NumberFormat('en-GB', { style: 'decimal', notation: 'scientific' });
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a Collator object using the current system locale ID.
let collator = new intl.Collator();
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a Collator object with the locale ID being zh-CN, localeMatcher being lookup, and usage being sort.
let collator = new intl.Collator('zh-CN', {localeMatcher: 'lookup', usage: 'sort'});
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a PluralRules object using the current system locale ID.
let pluralRules = new intl.PluralRules();
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a PluralRules object with the locale ID being zh-CN, localeMatcher being lookup, and type being cardinal.
let pluralRules: intl.PluralRules = new intl.PluralRules('zh-CN', { localeMatcher: 'lookup', type: 'cardinal' });
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a RelativeTimeFormat object using the current system locale ID.
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat();
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a RelativeTimeFormat object with the locale ID being zh-CN, localeMatcher being lookup, and style being long.
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat('zh-CN', {
  localeMatcher: 'lookup',
  numeric: 'always',
  style: 'long'
});
```

## constructor

```TypeScript
constructor(locale: string | Array<string>, options?: PluralRulesOptions)
```

Creates a **PluralRules** object to obtain the singular-plural type of numbers.

**Since:** 8

**Deprecated since:** 20

**Substitutes:** [Intl.PluralRules.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PluralRules-constructor(locale: string | Array<string>, options?: PluralRulesOptions)--><!--Device-PluralRules-constructor(locale: string | Array<string>, options?: PluralRulesOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string \| Array&lt;string&gt; | Yes | Locale ID or locale ID array. If the input is a locale ID array, the first valid locale ID is used. |
| options | PluralRulesOptions | No | Options for creating a **PluralRules** object. |

**Examples**

See [constructor](#constructor)

## select

```TypeScript
select(n: double): string
```

Obtains the singular-plural type of the specified number.

**Since:** 8

**Deprecated since:** 20

**Substitutes:** [Intl.PluralRules.select](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/select)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PluralRules-select(n: double): string--><!--Device-PluralRules-select(n: double): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| n | double | Yes | Number for which the singular-plural type is to be obtained. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Singular-plural type. The value can be any of the following: **zero**, **one**, **two**, **few**, **many**, **others**. For details about the meanings of different values, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html). |

**Examples**

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a PluralRules object with the locale ID being zh-Hans.
let zhPluralRules = new intl.PluralRules('zh-Hans');
// Determine the singular-plural type corresponding to number 1 in locale zh-Hans.
let plural = zhPluralRules.select(1); // plural = 'other'

// Create a PluralRules object with the locale ID being en-US.
let enPluralRules = new intl.PluralRules('en-US');
// Determine the singular-plural type corresponding to number 1 in locale en-US.
plural = enPluralRules.select(1); // plural = 'one'
```

