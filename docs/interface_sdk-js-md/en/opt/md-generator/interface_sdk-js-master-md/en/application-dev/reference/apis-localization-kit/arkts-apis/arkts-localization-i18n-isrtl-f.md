# isRTL

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## isRTL

```TypeScript
export function isRTL(locale: string): boolean
```

Checks whether a language is an RTL language. For an RTL language,  
[UI mirroring](../../../internationalization/i18n-ui-design.md#ui-mirroring) is required.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-i18n-export function isRTL(locale: string): boolean--><!--Device-i18n-export function isRTL(locale: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locale | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
