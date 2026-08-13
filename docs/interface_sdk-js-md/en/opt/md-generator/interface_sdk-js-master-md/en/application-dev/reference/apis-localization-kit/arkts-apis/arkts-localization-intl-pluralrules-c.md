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

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a PluralRules object using the current system locale ID.
let pluralRules = new intl.PluralRules();
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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locale | string \| Array & lt;string & gt; | Yes |
| options | [PluralRulesOptions](../../apis-na/arkts-apis/arkts-na-intl-pluralrulesoptions-i.md) | No |

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a PluralRules object with the locale ID being zh-CN, localeMatcher being lookup, and type being cardinal.
let pluralRules: intl.PluralRules = new intl.PluralRules('zh-CN', { localeMatcher: 'lookup', type: 'cardinal' });
```

## select

```TypeScript
select(n: number): string
```

Obtains the singular-plural type of the specified number.

**Since:** 8

**Deprecated since:** 20

**Substitutes:** [Intl.PluralRules.select](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/select)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PluralRules-select(n: double): string--><!--Device-PluralRules-select(n: double): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

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
