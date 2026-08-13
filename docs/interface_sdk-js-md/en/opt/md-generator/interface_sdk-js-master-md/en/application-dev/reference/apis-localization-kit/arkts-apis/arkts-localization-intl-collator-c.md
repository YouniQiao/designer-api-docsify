# Collator

Provides the string collation capability.

**Since:** 23

**Deprecated since:** -1

<!--Device-intl-export class Collator--><!--Device-intl-export class Collator-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { intl } from '@kit.LocalizationKit';
```

## compare

```TypeScript
compare(first: string, second: string): number
```

Compares two strings based on the specified collation rules.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Collator-compare(first: string, second: string): int--><!--Device-Collator-compare(first: string, second: string): int-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| first | string | Yes |
| second | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a Collator object with the locale ID being en-GB.
let collator = new intl.Collator('en-GB');
// Compare the sequence of the first and second strings.
let compareResult = collator.compare('first', 'second'); // compareResult = -1
```

## constructor

```TypeScript
constructor()
```

Creates a **Collator** object for the current system locale.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Collator-constructor()--><!--Device-Collator-constructor()-End-->

**System capability:** SystemCapability.Global.I18n

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a Collator object using the current system locale ID.
let collator = new intl.Collator();
```

## constructor

```TypeScript
constructor(locale: string | Array<string>, options?: CollatorOptions)
```

Creates a **Collator** object based on the specified locale and options.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Collator-constructor(locale: string | Array<string>, options?: CollatorOptions)--><!--Device-Collator-constructor(locale: string | Array<string>, options?: CollatorOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locale | string \| Array & lt;string & gt; | Yes |
| options | [CollatorOptions](../../apis-na/arkts-apis/arkts-na-intl-collatoroptions-i.md) | No |

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

// Create a Collator object with the locale ID being zh-CN, localeMatcher being lookup, and usage being sort.
let collator = new intl.Collator('zh-CN', {localeMatcher: 'lookup', usage: 'sort'});
```

## resolvedOptions

```TypeScript
resolvedOptions(): CollatorOptions
```

Obtains the options for creating a **Collator** object.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Collator-resolvedOptions(): CollatorOptions--><!--Device-Collator-resolvedOptions(): CollatorOptions-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CollatorOptions](../../apis-na/arkts-apis/arkts-na-intl-collatoroptions-i.md) |

## Examples

```TypeScript
import { intl } from '@kit.LocalizationKit';

let collator = new intl.Collator('zh-Hans', { usage: 'sort', ignorePunctuation: true });
// Obtain the options of the Collator object.
let options = collator.resolvedOptions();
let usage = options.usage; // usage = 'sort'
let ignorePunctuation = options.ignorePunctuation; // ignorePunctuation = true
```
