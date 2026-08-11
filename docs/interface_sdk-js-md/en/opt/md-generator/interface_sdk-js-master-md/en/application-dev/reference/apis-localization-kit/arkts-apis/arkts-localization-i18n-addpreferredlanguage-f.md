# addPreferredLanguage

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## addPreferredLanguage

```TypeScript
export function addPreferredLanguage(language: string, index?: number): boolean
```

Adds a preferred language to the specified position on the preferred language list.

**Since:** 8

**Deprecated since:** 9

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-i18n-export function addPreferredLanguage(language: string, index?: int): boolean--><!--Device-i18n-export function addPreferredLanguage(language: string, index?: int): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| language | string | Yes |
| index | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
