# getCalendar

## getCalendar

```TypeScript
export function getCalendar(locale: string, type?: string): Calendar
```

Obtains the Calendar object for the specified locale and calendar type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-i18n-export function getCalendar(locale: string, type?: string): Calendar--><!--Device-i18n-export function getCalendar(locale: string, type?: string): Calendar-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | Yes | Locale ID, which consists of the language, script, and country/region, for example, zh-Hans-CN. |
| type | string | No | Calendar. The value can be: "buddhist", "chinese", "coptic", "ethiopic", "hebrew", "gregory", "indian", "islamic\_\_\_ESCAPED\_UNDERSCORE\_\_\_civil", "islamic\_\_\_ESCAPED\_UNDERSCORE\_\_\_tbla", "islamic\_\_\_ESCAPED\_UNDERSCORE\_\_\_umalqura", "japanese", or "persian". The default value is the default calendar of the locale. For details about the meanings and application scenarios of different values, see Calendar Setting. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Calendar object |

