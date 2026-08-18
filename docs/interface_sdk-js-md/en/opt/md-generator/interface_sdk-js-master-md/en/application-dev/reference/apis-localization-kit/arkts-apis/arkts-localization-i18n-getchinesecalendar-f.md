# getChineseCalendar

## Modules to Import

```TypeScript
```

## getChineseCalendar

```TypeScript
export function getChineseCalendar(locale?: Intl.Locale): ChineseCalendar
```

Obtains the ChineseCalendar object for the specified locale.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-i18n-export function getChineseCalendar(locale?: Intl.Locale): ChineseCalendar--><!--Device-i18n-export function getChineseCalendar(locale?: Intl.Locale): ChineseCalendar-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locale | Intl.Locale | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ChineseCalendar](arkts-localization-i18n-chinesecalendar-c.md) |

**Examples**

```TypeScript
let locale: Intl.Locale = i18n.System.getSystemLocaleInstance();
let calendar: i18n.ChineseCalendar = i18n.getChineseCalendar(locale);
```
