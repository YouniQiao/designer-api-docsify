# getChineseCalendar

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## getChineseCalendar

```TypeScript
export function getChineseCalendar(locale?: Intl.Locale): ChineseCalendar
```

获取指定区域的农历对象。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-i18n-export function getChineseCalendar(locale?: Intl.Locale): ChineseCalendar--><!--Device-i18n-export function getChineseCalendar(locale?: Intl.Locale): ChineseCalendar-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | Intl.Locale | No | 区域对象，默认值：系统区域对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ChineseCalendar](arkts-localization-i18n-chinesecalendar-c.md) | 农历对象。 |

