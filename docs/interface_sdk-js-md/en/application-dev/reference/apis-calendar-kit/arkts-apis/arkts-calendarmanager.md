# @ohos.calendarManager

本模块提供日历与日程管理能力，包括日历和日程的创建、删除、修改、查询等。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare namespace calendarManager--><!--Device-unnamed-declare namespace calendarManager-End-->

**System capability:** SystemCapability.Applications.CalendarData

## Modules to Import

```TypeScript
import { calendarManager } from 'kits/@kit.CalendarKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getCalendarManager](arkts-calendar-calendarmanager-getcalendarmanager-f.md#getcalendarmanager) | 根据上下文获取CalendarManager对象，用于管理日历。 |

### Classes

| Name | Description |
| --- | --- |
| [EventFilter](arkts-calendar-calendarmanager-eventfilter-c.md) | 日程过滤器，查询日程时进行筛选过滤，获取符合条件的日程。 |

### Interfaces

| Name | Description |
| --- | --- |
| [Attendee](arkts-calendar-calendarmanager-attendee-i.md) | 会议日程参与者。 |
| [Calendar](arkts-calendar-calendarmanager-calendar-i.md) | 下列API示例中需先通过  [createCalendar()](arkts-calendar-calendarmanager-calendarmanager-i.md#createcalendar)、[getCalendar()](arkts-calendar-calendarmanager-calendarmanager-i.md#getcalendar)中任一方法获取Calendar对象，再通过此对象调用对应方法，对该Calendar下的日程进行创建、删除、修改、查询等操作。 |
| [CalendarAccount](arkts-calendar-calendarmanager-calendaraccount-i.md) | 日历账户信息。 |
| [CalendarConfig](arkts-calendar-calendarmanager-calendarconfig-i.md) | 日历配置信息。 |
| [CalendarManager](arkts-calendar-calendarmanager-calendarmanager-i.md) | 下列API示例中需先通过[getCalendarManager()](arkts-calendar-calendarmanager-getcalendarmanager-f.md#getcalendarmanager)方法获取CalendarManager对象，再通过此对象调用对应方法，进行Calendar的创建、删除、修改、查询等操作。 |
| [Event](arkts-calendar-calendarmanager-event-i.md) | 日程对象，包含日程标题、开始时间、结束时间等信息。 |
| [EventService](arkts-calendar-calendarmanager-eventservice-i.md) | 日程服务。 |
| [Location](arkts-calendar-calendarmanager-location-i.md) | 日程地点。 |
| [RecurrenceRule](arkts-calendar-calendarmanager-recurrencerule-i.md) | 重复日程重复规则。 |

### Enums

| Name | Description |
| --- | --- |
| [AttendeeRole](arkts-calendar-calendarmanager-attendeerole-e.md) | 会议日程参与者角色类型枚举。 |
| [AttendeeStatus](arkts-calendar-calendarmanager-attendeestatus-e.md) | 会议日程参与者状态类型枚举。 |
| [AttendeeType](arkts-calendar-calendarmanager-attendeetype-e.md) | 会议日程参与者受邀类型枚举。 |
| [CalendarType](arkts-calendar-calendarmanager-calendartype-e.md) | 账户类型枚举。 |
| [EventType](arkts-calendar-calendarmanager-eventtype-e.md) | 日程类型枚举。 |
| [RecurrenceFrequency](arkts-calendar-calendarmanager-recurrencefrequency-e.md) | 日程重复规则类型枚举。 |
| [ServiceType](arkts-calendar-calendarmanager-servicetype-e.md) | 日程服务类型枚举。 |

