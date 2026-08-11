# getLineInstance

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## getLineInstance

```TypeScript
export function getLineInstance(locale: string): BreakIterator
```

Obtains a **BreakIterator** object. The **BreakIterator** object maintains an internal break iterator that can be used to access various line break points.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-i18n-export function getLineInstance(locale: string): BreakIterator--><!--Device-i18n-export function getLineInstance(locale: string): BreakIterator-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locale | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BreakIterator](arkts-localization-i18n-breakiterator-c.md) |
