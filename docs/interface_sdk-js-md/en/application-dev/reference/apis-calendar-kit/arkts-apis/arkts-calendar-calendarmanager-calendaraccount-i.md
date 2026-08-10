# CalendarAccount

日历账户信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-calendarManager-interface CalendarAccount--><!--Device-calendarManager-interface CalendarAccount-End-->

**System capability:** SystemCapability.Applications.CalendarData

## Modules to Import

```TypeScript
import { calendarManager } from 'kits/@kit.CalendarKit';
```

## displayName

```TypeScript
displayName?: string
```

账户显示在日历应用上的名称（面向用户）。不填时，默认为空字符串，长度限制为[0,64]字符，长度超限制会导致日历应用上账户名显示不全，被截断。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CalendarAccount-displayName?: string--><!--Device-CalendarAccount-displayName?: string-End-->

**System capability:** SystemCapability.Applications.CalendarData

## name

```TypeScript
readonly name: string
```

账户名称（面向开发者），长度建议为[0,5000]字符。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CalendarAccount-readonly name: string--><!--Device-CalendarAccount-readonly name: string-End-->

**System capability:** SystemCapability.Applications.CalendarData

## type

```TypeScript
type: CalendarType
```

账户类型。

**Type:** [CalendarType](arkts-calendar-calendarmanager-calendartype-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CalendarAccount-type: CalendarType--><!--Device-CalendarAccount-type: CalendarType-End-->

**System capability:** SystemCapability.Applications.CalendarData

