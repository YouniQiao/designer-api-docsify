# EventPriority

表示事件的优先级。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-emitter-export enum EventPriority--><!--Device-emitter-export enum EventPriority-End-->

**System capability:** SystemCapability.Notification.Emitter

## IMMEDIATE

```TypeScript
IMMEDIATE = 0
```

表示事件先于HIGH优先级投递。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-EventPriority-IMMEDIATE = 0--><!--Device-EventPriority-IMMEDIATE = 0-End-->

**System capability:** SystemCapability.Notification.Emitter

## HIGH

```TypeScript
HIGH
```

表示事件先于LOW优先级投递。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-EventPriority-HIGH--><!--Device-EventPriority-HIGH-End-->

**System capability:** SystemCapability.Notification.Emitter

## LOW

```TypeScript
LOW
```

表示事件先于IDLE优先级投递，事件的默认优先级是LOW。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-EventPriority-LOW--><!--Device-EventPriority-LOW-End-->

**System capability:** SystemCapability.Notification.Emitter

## IDLE

```TypeScript
IDLE
```

表示在没有其他事件的情况下，才投递该事件。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-EventPriority-IDLE--><!--Device-EventPriority-IDLE-End-->

**System capability:** SystemCapability.Notification.Emitter

