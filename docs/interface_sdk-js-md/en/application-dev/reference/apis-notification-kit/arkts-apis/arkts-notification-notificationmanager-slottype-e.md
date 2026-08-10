# SlotType

通知渠道类型。

不同类型对应不同的SlotLevel，决定通知的提醒行为。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-notificationManager-export enum SlotType--><!--Device-notificationManager-export enum SlotType-End-->

**System capability:** SystemCapability.Notification.Notification

## UNKNOWN_TYPE

```TypeScript
UNKNOWN_TYPE = 0
```

未知类型。该类型对应SlotLevel为LEVEL_MIN。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SlotType-UNKNOWN_TYPE = 0--><!--Device-SlotType-UNKNOWN_TYPE = 0-End-->

**System capability:** SystemCapability.Notification.Notification

## SOCIAL_COMMUNICATION

```TypeScript
SOCIAL_COMMUNICATION = 1
```

社交通讯。该类型对应SlotLevel为LEVEL_HIGH。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SlotType-SOCIAL_COMMUNICATION = 1--><!--Device-SlotType-SOCIAL_COMMUNICATION = 1-End-->

**System capability:** SystemCapability.Notification.Notification

## SERVICE_INFORMATION

```TypeScript
SERVICE_INFORMATION = 2
```

服务提醒。该类型对应SlotLevel为LEVEL_HIGH。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SlotType-SERVICE_INFORMATION = 2--><!--Device-SlotType-SERVICE_INFORMATION = 2-End-->

**System capability:** SystemCapability.Notification.Notification

## CONTENT_INFORMATION

```TypeScript
CONTENT_INFORMATION = 3
```

内容资讯。该类型对应SlotLevel为LEVEL_MIN。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SlotType-CONTENT_INFORMATION = 3--><!--Device-SlotType-CONTENT_INFORMATION = 3-End-->

**System capability:** SystemCapability.Notification.Notification

## LIVE_VIEW

```TypeScript
LIVE_VIEW = 4
```

实况窗。不支持三方应用直接创建该渠道类型通知，可以由系统代理创建后， 三方应用发布同ID的通知来更新指定内容。该类型对应SlotLevel为LEVEL_DEFAULT。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SlotType-LIVE_VIEW = 4--><!--Device-SlotType-LIVE_VIEW = 4-End-->

**System capability:** SystemCapability.Notification.Notification

## CUSTOMER_SERVICE

```TypeScript
CUSTOMER_SERVICE = 5
```

客服消息。该类型用于用户与商家之间的客服消息，需由用户主动发起。 该类型对应SlotLevel为LEVEL_DEFAULT。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SlotType-CUSTOMER_SERVICE = 5--><!--Device-SlotType-CUSTOMER_SERVICE = 5-End-->

**System capability:** SystemCapability.Notification.Notification

## OTHER_TYPES

```TypeScript
OTHER_TYPES = 0xFFFF
```

其他。该类型对应SlotLevel为LEVEL_MIN。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SlotType-OTHER_TYPES = 0xFFFF--><!--Device-SlotType-OTHER_TYPES = 0xFFFF-End-->

**System capability:** SystemCapability.Notification.Notification

