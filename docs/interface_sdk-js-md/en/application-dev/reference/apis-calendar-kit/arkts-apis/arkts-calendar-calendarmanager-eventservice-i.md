# EventService

日程服务。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-calendarManager-export interface EventService--><!--Device-calendarManager-export interface EventService-End-->

**System capability:** SystemCapability.Applications.CalendarData

## Modules to Import

```TypeScript
import { calendarManager } from 'kits/@kit.CalendarKit';
```

## description

```TypeScript
description?: string
```

服务辅助描述。长度建议为[0,5000]字符，不填时，默认为空字符串。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-EventService-description?: string--><!--Device-EventService-description?: string-End-->

**System capability:** SystemCapability.Applications.CalendarData

## type

```TypeScript
type: ServiceType
```

服务类型。

**Type:** [ServiceType](arkts-calendar-calendarmanager-servicetype-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-EventService-type: ServiceType--><!--Device-EventService-type: ServiceType-End-->

**System capability:** SystemCapability.Applications.CalendarData

## uri

```TypeScript
uri: string
```

服务的uri，格式为DeepLink类型。可以跳转到三方应用相应界面。长度建议为[0,5000]字符。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-EventService-uri: string--><!--Device-EventService-uri: string-End-->

**System capability:** SystemCapability.Applications.CalendarData

