# ChineseCalendar

提供农历相关的能力，包括设置农历时间、判断指定年份某月是否存在闰月。继承自[Calendar](arkts-localization-i18n-calendar-c.md#Calendar)，支持[Calendar](arkts-localization-i18n-calendar-c.md#Calendar)的方法。

**继承/实现关系：** ChineseCalendar extends [Calendar](arkts-localization-i18n-calendar-c.md#Calendar)

**起始版本：** 26.0.0

<!--Device-i18n-export class ChineseCalendar extends Calendar--><!--Device-i18n-export class ChineseCalendar extends Calendar-End-->

**系统能力：** SystemCapability.Global.I18n

## checkLeapMonth

```TypeScript
public static checkLeapMonth(gregorianYear: number, cyclicalYear: number, month: number): boolean
```

判断指定年份某月是否存在闰月。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-ChineseCalendar-public static checkLeapMonth(gregorianYear: int, cyclicalYear: int, month: int): boolean--><!--Device-ChineseCalendar-public static checkLeapMonth(gregorianYear: int, cyclicalYear: int, month: int): boolean-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [gregorianYear](arkts-localization-i18n-chinesecalendartime-i.md) | number | 是 |
| [cyclicalYear](arkts-localization-i18n-chinesecalendartime-i.md) | number | 是 |
| month | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [8900001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-localization-kit/errorcode-i18n.md#8900001-参数校验错误) |

## setChineseCalendarTime

```TypeScript
public setChineseCalendarTime(chineseCalendarTime: ChineseCalendarTime): void
```

设置农历对象的时间日期。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-ChineseCalendar-public setChineseCalendarTime(chineseCalendarTime: ChineseCalendarTime): void--><!--Device-ChineseCalendar-public setChineseCalendarTime(chineseCalendarTime: ChineseCalendarTime): void-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| chineseCalendarTime | [ChineseCalendarTime](arkts-localization-i18n-chinesecalendartime-i.md) | 是 |
