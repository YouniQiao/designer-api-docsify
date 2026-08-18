# getInstance

## Modules to Import

```TypeScript
```

## getInstance

```TypeScript
export function getInstance(locale?:string): IndexUtil
```

Creates an IndexUtil object.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-i18n-export function getInstance(locale?:string): IndexUtil--><!--Device-i18n-export function getInstance(locale?:string): IndexUtil-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | No | System locale, which consists of the language, script, and country/region. The default value is the current system locale. |

**Return value:**

| Type | Description |
| --- | --- |
| [IndexUtil](arkts-na-i18n-indexutil-c.md) | IndexUtil object created based on the specified locale ID. |

