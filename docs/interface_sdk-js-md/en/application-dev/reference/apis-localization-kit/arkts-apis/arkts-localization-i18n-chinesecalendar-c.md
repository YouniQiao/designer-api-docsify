# ChineseCalendar

提供农历相关的能力，包括设置农历时间、判断指定年份某月是否存在闰月。继承自[Calendar](arkts-localization-i18n-calendar-c.md)，支持[Calendar](arkts-localization-i18n-calendar-c.md)的方法。

**Inheritance/Implementation:** ChineseCalendar extends [Calendar](arkts-localization-i18n-calendar-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-i18n-export class ChineseCalendar extends Calendar--><!--Device-i18n-export class ChineseCalendar extends Calendar-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## checkLeapMonth

```TypeScript
public static checkLeapMonth(gregorianYear: int, cyclicalYear: int, month: int): boolean
```

判断指定年份某月是否存在闰月。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChineseCalendar-public static checkLeapMonth(gregorianYear: int, cyclicalYear: int, month: int): boolean--><!--Device-ChineseCalendar-public static checkLeapMonth(gregorianYear: int, cyclicalYear: int, month: int): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| gregorianYear | int | Yes | 公历的年。 &lt;br&gt;取值范围：[1900, 2100]。 |
| cyclicalYear | int | Yes | 农历的干支年。 &lt;br&gt;取值范围：[1, 60]。 |
| month | int | Yes | 农历的月。 &lt;br&gt;**说明：** &lt;br&gt;月份从0开始计数，0表示一月。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 是否存在闰月。true表示该月存在闰月，false表示该月不存在闰月。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 8900001 | Invalid parameter. Possible causes: Parameter verification failed. |

## setChineseCalendarTime

```TypeScript
public setChineseCalendarTime(chineseCalendarTime: ChineseCalendarTime): void
```

设置农历对象的时间日期。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChineseCalendar-public setChineseCalendarTime(chineseCalendarTime: ChineseCalendarTime): void--><!--Device-ChineseCalendar-public setChineseCalendarTime(chineseCalendarTime: ChineseCalendarTime): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| chineseCalendarTime | [ChineseCalendarTime](arkts-localization-i18n-chinesecalendartime-i.md) | Yes | 农历时间对象。 |

