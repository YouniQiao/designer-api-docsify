# Attendee

会议日程参与者。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-calendarManager-export interface Attendee--><!--Device-calendarManager-export interface Attendee-End-->

**System capability:** SystemCapability.Applications.CalendarData

## Modules to Import

```TypeScript
import { calendarManager } from 'kits/@kit.CalendarKit';
```

## email

```TypeScript
email: string
```

会议日程参与者的邮箱，邮箱格式为“用户名@域名.后缀”，用户名部分只能包含字母、数字、下划线“_”、点 “.”、连字符 “-”。不能以点 “.” 开头或结尾。 不能连续出现两个点（即“..”）。长度建议为[0,5000]字符。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Attendee-email: string--><!--Device-Attendee-email: string-End-->

**System capability:** SystemCapability.Applications.CalendarData

## name

```TypeScript
name: string
```

会议日程参与者的姓名。长度建议为[0,5000]字符。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Attendee-name: string--><!--Device-Attendee-name: string-End-->

**System capability:** SystemCapability.Applications.CalendarData

## role

```TypeScript
role?: AttendeeRole
```

会议日程参与者的角色，不填时默认为空。

**Type:** [AttendeeRole](arkts-calendar-calendarmanager-attendeerole-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Attendee-role?: AttendeeRole--><!--Device-Attendee-role?: AttendeeRole-End-->

**System capability:** SystemCapability.Applications.CalendarData

## status

```TypeScript
status?: AttendeeStatus
```

会议日程参与者的状态，不填时默认为空。

**Type:** [AttendeeStatus](arkts-calendar-calendarmanager-attendeestatus-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Attendee-status?: AttendeeStatus--><!--Device-Attendee-status?: AttendeeStatus-End-->

**System capability:** SystemCapability.Applications.CalendarData

## type

```TypeScript
type?: AttendeeType
```

会议日程参与者的类型，不填时默认为空。

**Type:** [AttendeeType](arkts-calendar-calendarmanager-attendeetype-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Attendee-type?: AttendeeType--><!--Device-Attendee-type?: AttendeeType-End-->

**System capability:** SystemCapability.Applications.CalendarData

