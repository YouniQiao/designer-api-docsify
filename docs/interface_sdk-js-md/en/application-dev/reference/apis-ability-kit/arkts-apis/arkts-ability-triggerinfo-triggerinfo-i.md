# TriggerInfo

作为[trigger](../../../reference/apis-ability-kit/js-apis-app-ability-wantAgent.md#wantagenttrigger)的入参定义触发WantAgent所需要的信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface TriggerInfo--><!--Device-unnamed-export interface TriggerInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## code

```TypeScript
code: int
```

表示传递的公共事件数据，仅当WantAgent实例的  
[OperationType](../../../reference/apis-ability-kit/js-apis-app-ability-wantAgent.md#operationtype)类型是'SEND_COMMON_EVENT'时有效。该字段与发布者使用  
[commonEventManager.publish](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-commoneventmanager-publish-f.md/arkts-basicservices-commoneventmanager-publish-f.md#publish)发布公共事件时，传递  
[CommonEventPublishData](../../../reference/apis-basic-services-kit/js-apis-inner-commonEvent-commonEventPublishData.md#属性)公共事件数据中的`code`字段含义一致。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TriggerInfo-code: int--><!--Device-TriggerInfo-code: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## extraInfo

```TypeScript
extraInfo?: { [key: string]: any }
```

额外数据。

**Type:** { [key: string]: any }

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TriggerInfo-extraInfo?: { [key: string]: any }--><!--Device-TriggerInfo-extraInfo?: { [key: string]: any }-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## extraInfos

```TypeScript
extraInfos?: Record<string, Object>
```

额外数据。推荐使用该属性替代extraInfo，设置该属性后，extraInfo不再生效。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TriggerInfo-extraInfos?: Record<string, Object>--><!--Device-TriggerInfo-extraInfos?: Record<string, Object>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## permission

```TypeScript
permission?: string
```

表示公共事件订阅者的权限。仅当WantAgent实例的  
[OperationType](../../../reference/apis-ability-kit/js-apis-app-ability-wantAgent.md#operationtype)类型是'SEND_COMMON_EVENT'时，该字段生效。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TriggerInfo-permission?: string--><!--Device-TriggerInfo-permission?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## want

```TypeScript
want?: Want
```

对象间信息传递的载体，可以用于应用组件间的信息传递。

**Type:** [Want](arkts-ability-app-ability-want-want-c.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TriggerInfo-want?: Want--><!--Device-TriggerInfo-want?: Want-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

