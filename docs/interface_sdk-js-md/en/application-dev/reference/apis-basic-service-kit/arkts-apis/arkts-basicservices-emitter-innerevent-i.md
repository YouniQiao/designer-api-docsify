# InnerEvent

Describes an event to subscribe to or emit. The **EventPriority** settings do not take effect under event subscription.

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

Event ID.

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

Event priority. The default value is **EventPriority.LOW**.

**Type:** [EventPriority](arkts-basicservices-emitter-eventpriority-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-InnerEvent-priority?: EventPriority--><!--Device-InnerEvent-priority?: EventPriority-End-->

**System capability:** SystemCapability.Notification.Emitter

