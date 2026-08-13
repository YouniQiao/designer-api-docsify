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

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a RelativeTimeFormat object using the current system locale ID.
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat();
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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locale | string \| Array & lt;string & gt; | Yes |
| options | [RelativeTimeFormatInputOptions](arkts-localization-intl-relativetimeformatinputoptions-i.md) | No |

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Use locale ID zh-CN to create a RelativeTimeFormat object with the localeMatcher set to lookup, numeric set to always, and style set to long.
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat('zh-CN', {
  localeMatcher: 'lookup',
  numeric: 'always',
  style: 'long'
});
```

## format

```TypeScript
format(value: number, unit: string): string
```

Formats a relative time.

**Since:** 8

**Deprecated since:** 20

**Substitutes:** [Intl.RelativeTimeFormat.format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RelativeTimeFormat-format(value: double, unit: string): string--><!--Device-RelativeTimeFormat-format(value: double, unit: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| unit | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a RelativeTimeFormat object with the locale ID being zh-CN.
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat('zh-CN');
// Obtain the localized representation (in unit of quarter) of number 3 in locale zh-CN.
let formatResult: string = formatter.format(3, 'quarter'); // formatResult = '3 quarters later'
```

## formatToParts

```TypeScript
formatToParts(value: number, unit: string): Array<object>
```

Formats the relative time

**Since:** 8

**Deprecated since:** 20

**Substitutes:** [Intl.RelativeTimeFormat.formatToParts](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/formatToParts)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RelativeTimeFormat-formatToParts(value: double, unit: string): Array<object>--><!--Device-RelativeTimeFormat-formatToParts(value: double, unit: string): Array<object>-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| unit | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;object & gt; |

## Examples

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

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RelativeTimeFormatResolvedOptions](arkts-localization-intl-relativetimeformatresolvedoptions-i.md) |

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a RelativeTimeFormat object with the locale ID being en-GB.
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat('en-GB', { style: 'short' });
// Obtain the options of the RelativeTimeFormat object.
let options: intl.RelativeTimeFormatResolvedOptions = formatter.resolvedOptions();
let style: string = options.style; // style = 'short'
```
