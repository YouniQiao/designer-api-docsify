# EventFilter

日程过滤器，查询日程时进行筛选过滤，获取符合条件的日程。

**起始版本：** 10

**系统能力：** SystemCapability.Applications.CalendarData

## 导入模块

```TypeScript
import { calendarManager } from 'kits/@kit.CalendarKit';
```

## filterById

```TypeScript
static filterById(ids: number[]): EventFilter
```

根据日程id过滤日程。

**起始版本：** 10

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ids | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| [EventFilter](arkts-calendar-calendarmanager-eventfilter-c.md) |

## filterByTime

```TypeScript
static filterByTime(start: number, end: number): EventFilter
```

根据日程时间过滤日程。

**起始版本：** 10

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | number | 是 |
| end | number | 是 |

**返回值：**

| 类型 |
| --- |
| [EventFilter](arkts-calendar-calendarmanager-eventfilter-c.md) |

## filterByTitle

```TypeScript
static filterByTitle(title: string): EventFilter
```

根据日程标题过滤日程，该条件为模糊匹配。

**起始版本：** 10

**系统能力：** SystemCapability.Applications.CalendarData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| title | string | 是 |

**返回值：**

| 类型 |
| --- |
| [EventFilter](arkts-calendar-calendarmanager-eventfilter-c.md) |
