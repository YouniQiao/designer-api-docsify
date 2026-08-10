# InnerEvent

订阅或发送的事件，订阅事件时`EventPriority`不生效。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-emitter-export interface InnerEvent--><!--Device-emitter-export interface InnerEvent-End-->

**System capability:** SystemCapability.Notification.Emitter

## Modules to Import

```TypeScript
import { emitter } from 'kits/@kit.BasicServicesKit';
```

## eventId

```TypeScript
eventId: long
```

事件ID，由开发者定义，用于辨别事件。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-InnerEvent-eventId: long--><!--Device-InnerEvent-eventId: long-End-->

**System capability:** SystemCapability.Notification.Emitter

## priority

```TypeScript
priority?: EventPriority
```

事件的优先级，默认值为EventPriority.LOW。

**Type:** [EventPriority](arkts-basicservices-emitter-eventpriority-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-InnerEvent-priority?: EventPriority--><!--Device-InnerEvent-priority?: EventPriority-End-->

**System capability:** SystemCapability.Notification.Emitter

