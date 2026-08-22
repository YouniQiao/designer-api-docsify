# RelativeTimeFormat

Provides the relative time formatting capability.

**Since:** 8

**Deprecated since:** 20

**Substitutes:** [Intl.RelativeTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat)

<!--Device-intl-export class RelativeTimeFormat--><!--Device-intl-export class RelativeTimeFormat-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { intl } from '@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor()
```

Creates a **RelativeTimeFormat** object.

**Since:** 8

**Deprecated since:** 20

**Substitutes:** [Intl.RelativeTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RelativeTimeFormat-constructor()--><!--Device-RelativeTimeFormat-constructor()-End-->

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
constructor(locale: string | Array<string>, options?: RelativeTimeFormatInputOptions)
```

Creates a **RelativeTimeFormat** object.

**Since:** 8

**Deprecated since:** 20

**Substitutes:** [Intl.RelativeTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RelativeTimeFormat-constructor(locale: string | Array<string>, options?: RelativeTimeFormatInputOptions)--><!--Device-RelativeTimeFormat-constructor(locale: string | Array<string>, options?: RelativeTimeFormatInputOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string \| Array&lt;string&gt; | Yes | Locale ID or locale ID array. If the input is a locale ID array, the first valid locale ID is used. |
| options | [RelativeTimeFormatInputOptions](arkts-localization-intl-relativetimeformatinputoptions-i.md) | No | Options for creating a **RelativeTimeFormat** object. |

**Examples**

See [constructor](#constructor)

## format

```TypeScript
format(value: double, unit: string): string
```

Formats a relative time.

**Since:** 8

**Deprecated since:** 20

**Substitutes:** [Intl.RelativeTimeFormat.format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RelativeTimeFormat-format(value: double, unit: string): string--><!--Device-RelativeTimeFormat-format(value: double, unit: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | Value to format. |
| unit | string | Yes | Unit of the relative time. The value can be any of the following: **year**, **quarter**, **month**, **week**, **day**, **hour**, **minute**, or **second**. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Relative time after formatting. |

**Examples**

```TypeScript
import { intl } from '@kit.LocalizationKit';

let date: Date = new Date(2021, 11, 17, 3, 24, 0); // The date and time is 2021.12.17 03:24:00.
// Create a DateTimeFormat object with the locale ID being en-GB.
let formatter: intl.DateTimeFormat = new intl.DateTimeFormat('en-GB');
let formattedDate: string = formatter.format(date); // formattedDate "17/12/2021"

// Create a DateTimeFormat object with locale ID being en-GB, dateStyle being full, and timeStyle being medium.
formatter = new intl.DateTimeFormat('en-GB', { dateStyle: 'full', timeStyle: 'medium' });
formattedDate = formatter.format(date); // formattedDate "Friday, 17 December 2021, 03:24:00"
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a NumberFormat object with a locale ID array. The locale ID en-GB is valid and therefore is used.
let formatter: intl.NumberFormat = new intl.NumberFormat(['en-GB', 'zh'], { style: 'decimal', notation: 'scientific' });
let formattedNumber: string = formatter.format(1223); // formattedNumber = 1.223E3
let options: intl.NumberOptions = {
  roundingPriority: 'lessPrecision',
  maximumFractionDigits: 3,
  maximumSignificantDigits: 3
}
formatter = new intl.NumberFormat('en', options);
let result: string = formatter.format(1.23456); // result = 1.23
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a RelativeTimeFormat object with the locale ID being zh-CN.
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat('zh-CN');
// Obtain the localized representation (in unit of quarter) of number 3 in locale zh-CN.
let formatResult: string = formatter.format(3, 'quarter'); // formatResult = '3 quarters later'
```

## formatToParts

```TypeScript
formatToParts(value: double, unit: string): Array<object>
```

Formats the relative time

**Since:** 8

**Deprecated since:** 20

**Substitutes:** [Intl.RelativeTimeFormat.formatToParts](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/formatToParts)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RelativeTimeFormat-formatToParts(value: double, unit: string): Array<object>--><!--Device-RelativeTimeFormat-formatToParts(value: double, unit: string): Array<object>-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | Value to format. |
| unit | string | Yes | Unit of the relative time. The value can be any of the following: **year**, **quarter**, **month**, **week**, **day**, **hour**, **minute**, or **second**. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;object&gt; | Components of the formatted result. |

**Examples**

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a RelativeTimeFormat object with the locale ID being en and numeric being auto.
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat('en', { numeric: 'auto' });
let parts: Array<object> = formatter.formatToParts(10, 'seconds'); // parts = [ {type: 'literal', value: 'in'}, {type: 'integer', value: 10, unit: 'second'}, {type: 'literal', value: 'seconds'} ]
```

## resolvedOptions

```TypeScript
resolvedOptions(): RelativeTimeFormatResolvedOptions
```

Defines the formatting options for a **RelativeTimeFormat** object.

**Since:** 8

**Deprecated since:** 20

**Substitutes:** [Intl.RelativeTimeFormat.resolvedOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/resolvedOptions)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RelativeTimeFormat-resolvedOptions(): RelativeTimeFormatResolvedOptions--><!--Device-RelativeTimeFormat-resolvedOptions(): RelativeTimeFormatResolvedOptions-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| [RelativeTimeFormatResolvedOptions](arkts-localization-intl-relativetimeformatresolvedoptions-i.md) | Options for the **RelativeTimeFormat** object. |

**Examples**

```TypeScript
import { intl } from '@kit.LocalizationKit';

let formatter: intl.DateTimeFormat = new intl.DateTimeFormat('en-GB', { dateStyle: 'full', timeStyle: 'medium' });
// Obtain the options of the DateTimeFormat object.
let options: intl.DateTimeOptions = formatter.resolvedOptions();
let dateStyle: string | undefined = options.dateStyle; // dateStyle = 'full'
let timeStyle: string | undefined = options.timeStyle; // timeStyle = 'medium'
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

let formatter: intl.NumberFormat = new intl.NumberFormat(['en-GB', 'zh'], { style: 'decimal', notation: 'scientific' });
// Obtain the options of the NumberFormat object.
let options: intl.NumberOptions = formatter.resolvedOptions();
let style: string | undefined = options.style; // style = 'decimal'
let notation: string | undefined = options.notation; // notation = 'scientific'
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

let collator = new intl.Collator('zh-Hans', { usage: 'sort', ignorePunctuation: true });
// Obtain the options of the Collator object.
let options = collator.resolvedOptions();
let usage = options.usage; // usage = 'sort'
let ignorePunctuation = options.ignorePunctuation; // ignorePunctuation = true
```

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a RelativeTimeFormat object with the locale ID being en-GB.
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat('en-GB', { style: 'short' });
// Obtain the options of the RelativeTimeFormat object.
let options: intl.RelativeTimeFormatResolvedOptions = formatter.resolvedOptions();
let style: string = options.style; // style = 'short'
```

