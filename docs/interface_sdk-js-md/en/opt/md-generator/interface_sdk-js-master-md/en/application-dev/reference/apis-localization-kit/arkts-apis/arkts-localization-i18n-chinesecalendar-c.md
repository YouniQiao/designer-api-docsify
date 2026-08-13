# ChineseCalendar

Provide a ChineseCalendar interface which could handle unique characteristics of the chinese calendar, such as leap month.

**Inheritance/Implementation:** ChineseCalendar extends [Calendar](arkts-localization-i18n-calendar-c.md#Calendar)

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-i18n-export class ChineseCalendar--><!--Device-i18n-export class ChineseCalendar-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## checkLeapMonth

```TypeScript
public static checkLeapMonth(gregorianYear: number, cyclicalYear: number, month: number): boolean
```

Checks whether a given month exist leap month in gregorianYear and cyclicalYear.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChineseCalendar-public static checkLeapMonth(gregorianYear: int, cyclicalYear: int, month: int): boolean--><!--Device-ChineseCalendar-public static checkLeapMonth(gregorianYear: int, cyclicalYear: int, month: int): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [gregorianYear](../../apis-na/arkts-apis/arkts-na-i18n-chinesecalendartime-i.md) | number | Yes |
| [cyclicalYear](../../apis-na/arkts-apis/arkts-na-i18n-chinesecalendartime-i.md) | number | Yes |
| month | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [8900001](../errorcode-i18n.md#8900001-parameter-verification-error) |

## setChineseCalendarTime

```TypeScript
public setChineseCalendarTime(chineseCalendarTime: ChineseCalendarTime): void
```

Sets the year, month, day, hour, minute, second, isLeapMonth for this ChineseCalendar object.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChineseCalendar-public setChineseCalendarTime(chineseCalendarTime: ChineseCalendarTime): void--><!--Device-ChineseCalendar-public setChineseCalendarTime(chineseCalendarTime: ChineseCalendarTime): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| chineseCalendarTime | [ChineseCalendarTime](arkts-localization-i18n-chinesecalendartime-i.md) | Yes |
