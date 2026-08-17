# isRTL

## isRTL

```TypeScript
export function isRTL(locale: string): boolean
```

Checks whether the input character is of the right to left (RTL) language.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-i18n-export function isRTL(locale: string): boolean--><!--Device-i18n-export function isRTL(locale: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the input character is of the RTL language, and false otherwise. |

