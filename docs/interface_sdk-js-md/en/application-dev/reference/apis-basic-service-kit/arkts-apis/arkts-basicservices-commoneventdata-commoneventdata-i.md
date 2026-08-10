# CommonEventData

表示公共事件的数据。CommonEventData用于在公共事件订阅场景中承载订阅者接收到的公共事件数据，包含事件名称、发布者包名、code数据、data数据及附加参数等信息，适用于应用订阅并处理公共事件、解析事件携带数据的场景。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface CommonEventData--><!--Device-unnamed-export interface CommonEventData-End-->

**System capability:** SystemCapability.Notification.CommonEvent

## bundleName

```TypeScript
bundleName?: string
```

表示发布公共事件的应用包名，默认为空字符串。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventData-bundleName?: string--><!--Device-CommonEventData-bundleName?: string-End-->

**System capability:** SystemCapability.Notification.CommonEvent

## code

```TypeScript
code?: int
```

表示订阅者接收到的公共事件数据。该字段取值与发布者使用  
[commonEventManager.publish](arkts-basicservices-commoneventmanager-publish-f.md#publish)发布公共事件时，通过[CommonEventPublishData](arkts-basicservices-commoneventpublishdata-commoneventpublishdata-i.md)中的`code`字段传递的数据一致。取值范围[-2147483648, 2147483647]，默认值为0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** 0

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventData-code?: int--><!--Device-CommonEventData-code?: int-End-->

**System capability:** SystemCapability.Notification.CommonEvent

## data

```TypeScript
data?: string
```

表示订阅者接收到的公共事件数据，数据大小不超过64KB。该字段取值与发布者使用  
[commonEventManager.publish](arkts-basicservices-commoneventmanager-publish-f.md#publish)发布公共事件时，通过[CommonEventPublishData](arkts-basicservices-commoneventpublishdata-commoneventpublishdata-i.md)中的`data`字段传递的数据一致。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventData-data?: string--><!--Device-CommonEventData-data?: string-End-->

**System capability:** SystemCapability.Notification.CommonEvent

## event

```TypeScript
event: string
```

表示当前接收的公共事件名称。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventData-event: string--><!--Device-CommonEventData-event: string-End-->

**System capability:** SystemCapability.Notification.CommonEvent

## parameters

```TypeScript
parameters?: { [key: string]: any }
```

表示订阅者接收到的公共事件的附加信息。该字段取值与发布者使用  
[commonEventManager.publish](arkts-basicservices-commoneventmanager-publish-f.md#publish)发布公共事件时，通过[CommonEventPublishData](arkts-basicservices-commoneventpublishdata-commoneventpublishdata-i.md)中的`parameters`字段传递的数据一致。

**Type:** { [key: string]: any }

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonEventData-parameters?: { [key: string]: any }--><!--Device-CommonEventData-parameters?: { [key: string]: any }-End-->

**System capability:** SystemCapability.Notification.CommonEvent

