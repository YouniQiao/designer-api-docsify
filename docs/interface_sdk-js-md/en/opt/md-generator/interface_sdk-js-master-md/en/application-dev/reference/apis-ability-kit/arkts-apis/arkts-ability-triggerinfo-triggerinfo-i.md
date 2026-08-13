# TriggerInfo

The module defines the information required for triggering the WantAgent. The information is used as an input parameter of trigger.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-export interface TriggerInfo--><!--Device-unnamed-export interface TriggerInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## code

```TypeScript
code: number
```

Common event code. This field is valid only when OperationType of the WantAgent instance is **'SEND_COMMON_EVENT'**. The meaning of this field is the same as that of the **code** field set in [CommonEventPublishData](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-commoneventpublishdata-commoneventpublishdata-i.md#CommonEventPublishData) when the publisher uses [commonEventManager.publish](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-commoneventmanager-publish-f.md#publish) to publish common events.

**Type:** number

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TriggerInfo-code: int--><!--Device-TriggerInfo-code: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## extraInfo

```TypeScript
extraInfo?: Record<string, RecordData>
```

Extra information.

**Type:** [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md)&gt;

**Since:** 23

**Deprecated since:** -1

<!--Device-TriggerInfo-extraInfo?: Record<string, RecordData>--><!--Device-TriggerInfo-extraInfo?: Record<string, RecordData>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## extraInfos

```TypeScript
extraInfos?: Record<string, RecordData>
```

Extra information. You are advised to use this property to replace extraInfo. When this property is set, extraInfo does not take effect.

**Type:** [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md)&gt;

**Since:** 23

**Deprecated since:** -1

<!--Device-TriggerInfo-extraInfos?: Record<string, RecordData>--><!--Device-TriggerInfo-extraInfos?: Record<string, RecordData>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## permission

```TypeScript
permission?: string
```

Permission required for a subscriber to receive the common event. This field is valid only when OperationType of the WantAgent instance is **'SEND_COMMON_EVENT'**.

**Type:** string

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TriggerInfo-permission?: string--><!--Device-TriggerInfo-permission?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## want

```TypeScript
want?: Want
```

Carrier for information transfer between objects (application components).

**Type:** [Want](arkts-ability-app-ability-want-want-c.md)

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TriggerInfo-want?: Want--><!--Device-TriggerInfo-want?: Want-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core
