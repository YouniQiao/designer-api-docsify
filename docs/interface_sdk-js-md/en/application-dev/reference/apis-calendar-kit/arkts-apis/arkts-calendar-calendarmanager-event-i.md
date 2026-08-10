# Event

日程对象，包含日程标题、开始时间、结束时间等信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-calendarManager-interface Event--><!--Device-calendarManager-interface Event-End-->

**System capability:** SystemCapability.Applications.CalendarData

## Modules to Import

```TypeScript
import { calendarManager } from 'kits/@kit.CalendarKit';
```

## attendee

```TypeScript
attendee?: Attendee[]
```

会议日程参与者。不填时，默认为null。

**Type:** [Attendee](arkts-calendar-calendarmanager-attendee-i.md)[]

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Event-attendee?: Attendee[]--><!--Device-Event-attendee?: Attendee[]-End-->

**System capability:** SystemCapability.Applications.CalendarData

## description

```TypeScript
description?: string
```

日程描述。长度建议为[0,5000]字符，不填时，默认为空字符串。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Event-description?: string--><!--Device-Event-description?: string-End-->

**System capability:** SystemCapability.Applications.CalendarData

## endTime

```TypeScript
endTime: number
```

日程结束时间，需要13位时间戳。全天日程时，该字段转换为传入日期24:00对应的时间戳。 *

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Event-endTime: number--><!--Device-Event-endTime: number-End-->

**System capability:** SystemCapability.Applications.CalendarData

## id

```TypeScript
id?: number
```

日程id。当调用[addEvent()](arkts-calendar-calendarmanager-calendar-i.md#addevent)、  
[addEvents()](arkts-calendar-calendarmanager-calendar-i.md#addevents)创建日程时，不填写此参数；当调用[deleteEvent()](arkts-calendar-calendarmanager-calendar-i.md#deleteevent)、  
[deleteEvents()](arkts-calendar-calendarmanager-calendar-i.md#deleteevents)删除日程时，日程id数组，日程id需为整数，传入其他非法入参会报错。

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Event-id?: number--><!--Device-Event-id?: number-End-->

**System capability:** SystemCapability.Applications.CalendarData

## identifier

```TypeScript
identifier?: string
```

写入方可指定日程唯一标识。长度建议为[0,5000]字符，不填时，默认为null。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Event-identifier?: string--><!--Device-Event-identifier?: string-End-->

**System capability:** SystemCapability.Applications.CalendarData

## instanceEndTime

```TypeScript
instanceEndTime?: number
```

日程实例结束时间，需要13位时间戳。当调用[addEvent()](arkts-calendar-calendarmanager-calendar-i.md#addevent)、  
[addEvents()](arkts-calendar-calendarmanager-calendar-i.md#addevents)创建日程时，不填写此参数。

**Type:** number

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Event-instanceEndTime?: number--><!--Device-Event-instanceEndTime?: number-End-->

**System capability:** SystemCapability.Applications.CalendarData

## instanceStartTime

```TypeScript
instanceStartTime?: number
```

日程实例开始时间，需要13位时间戳。当调用[addEvent()](arkts-calendar-calendarmanager-calendar-i.md#addevent)、  
[addEvents()](arkts-calendar-calendarmanager-calendar-i.md#addevents)创建日程时，不填写此参数。

**Type:** number

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Event-instanceStartTime?: number--><!--Device-Event-instanceStartTime?: number-End-->

**System capability:** SystemCapability.Applications.CalendarData

## isAllDay

```TypeScript
isAllDay?: boolean
```

是否为全天日程。当取值为true时，说明为全天日程；当取值为false时，说明不是全天日程，默认为非全天日程。

**Type:** boolean

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Event-isAllDay?: boolean--><!--Device-Event-isAllDay?: boolean-End-->

**System capability:** SystemCapability.Applications.CalendarData

## isLunar

```TypeScript
isLunar?: boolean
```

是否为农历日程。当取值为true时，说明为农历日程；当取值为false时，说明不是农历日程，默认为非农历日程。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Event-isLunar?: boolean--><!--Device-Event-isLunar?: boolean-End-->

**System capability:** SystemCapability.Applications.CalendarData

## location

```TypeScript
location?: Location
```

日程地点。不填时，默认为undefined。

**Type:** [Location](../../apis-location-kit/arkts-apis/arkts-location-geolocationmanager-location-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Event-location?: Location--><!--Device-Event-location?: Location-End-->

**System capability:** SystemCapability.Applications.CalendarData

## recurrenceRule

```TypeScript
recurrenceRule?: RecurrenceRule
```

日程重复规则，设置了此字段的日程为重复日程。不填时，默认为非重复日程。

**Type:** [RecurrenceRule](arkts-calendar-calendarmanager-recurrencerule-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Event-recurrenceRule?: RecurrenceRule--><!--Device-Event-recurrenceRule?: RecurrenceRule-End-->

**System capability:** SystemCapability.Applications.CalendarData

## reminderTime

```TypeScript
reminderTime?: number[]
```

日程提醒时间，单位为分钟。填写x分钟，即距开始时间提前x分钟提醒，不填时，默认为不提醒。为负值时表示延期多长时间提醒。全天日程时此字段表示上午9:00前x分钟提醒，可取负值，负值表示上午9:00后多长时间提醒。

**Type:** number[]

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Event-reminderTime?: number[]--><!--Device-Event-reminderTime?: number[]-End-->

**System capability:** SystemCapability.Applications.CalendarData

## service

```TypeScript
service?: EventService
```

&lt;!--RP1--&gt;日程服务。不填时，默认没有一键服务。暂不支持此功能。&lt;!--RP1End--&gt;

**Type:** [EventService](arkts-calendar-calendarmanager-eventservice-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Event-service?: EventService--><!--Device-Event-service?: EventService-End-->

**System capability:** SystemCapability.Applications.CalendarData

## startTime

```TypeScript
startTime: number
```

日程开始时间，需要13位时间戳。全天日程时，该字段转换为传入日期00:00对应的时间戳。

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Event-startTime: number--><!--Device-Event-startTime: number-End-->

**System capability:** SystemCapability.Applications.CalendarData

## timeZone

```TypeScript
timeZone?: string
```

日程时区。日程时区。长度建议为[0,5000]字符，不填或异常值时，默认为当前所在时区，当需要创建与当前不一样的时区时，可填入对应的时区。可通过  
[systemDateTime.getTimezone()](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-systemdatetime-gettimezone-f.md/arkts-basicservices-systemdatetime-gettimezone-f.md#gettimezone)获取当前系统时区。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Event-timeZone?: string--><!--Device-Event-timeZone?: string-End-->

**System capability:** SystemCapability.Applications.CalendarData

## title

```TypeScript
title?: string
```

日程标题。长度建议为[0,5000]字符，不填时，默认为空字符串。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Event-title?: string--><!--Device-Event-title?: string-End-->

**System capability:** SystemCapability.Applications.CalendarData

## type

```TypeScript
type: EventType
```

日程类型。

**Type:** [EventType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-screenlock-eventtype-t-sys.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Event-type: EventType--><!--Device-Event-type: EventType-End-->

**System capability:** SystemCapability.Applications.CalendarData

