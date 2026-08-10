# EventInfo

界面变更事件。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-accessibility-class EventInfo--><!--Device-accessibility-class EventInfo-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## Modules to Import

```TypeScript
import { accessibility } from 'kits/@kit.AccessibilityKit';
```

## constructor

```TypeScript
constructor(jsonObject: Object)
```

构造函数，通过JSON对象构造EventInfo实例。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-EventInfo-constructor(jsonObject: Object)--><!--Device-EventInfo-constructor(jsonObject: Object)-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| jsonObject | Object | Yes | 包含 type、bundleName 和 triggerAction 三个字段的 JSON对象，详见示例。 |

## Examples

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'click',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'click',
});
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a EventInfo object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-EventInfo-constructor()--><!--Device-EventInfo-constructor()-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## constructor

```TypeScript
constructor(type: EventType, bundleName: string, triggerAction: Action)
```

构造函数，通过独立参数构造EventInfo实例。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-EventInfo-constructor(type: EventType, bundleName: string, triggerAction: Action)--><!--Device-EventInfo-constructor(type: EventType, bundleName: string, triggerAction: Action)-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [EventType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-screenlock-eventtype-t-sys.md) | Yes | 无障碍事件类型。 |
| bundleName | string | Yes | 目标应用名。 |
| triggerAction | [Action](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-action-e.md) | Yes | 触发事件的 Action。 |

## Examples

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';

let eventInfo = new accessibility.EventInfo('click', 'com.example.MyApplication', 'click');
```

## beginIndex

```TypeScript
beginIndex?: int
```

画面显示条目的开始序号，默认值为0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-EventInfo-beginIndex?: int--><!--Device-EventInfo-beginIndex?: int-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## bundleName

```TypeScript
bundleName: string
```

目标应用名；不可缺省。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-EventInfo-bundleName: string--><!--Device-EventInfo-bundleName: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## componentType

```TypeScript
componentType?: string
```

应与事件源组件类型对应，默认值为空。

例如：

- 按钮Button类型->'Button'。  
- 图片Image类型->'Image'。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-EventInfo-componentType?: string--><!--Device-EventInfo-componentType?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## contents

```TypeScript
contents?: Array<string>
```

内容列表，根据实际场景设置，无特殊限制，默认值为空。

**Type:** Array&lt;string&gt;

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-EventInfo-contents?: Array<string>--><!--Device-EventInfo-contents?: Array<string>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## currentIndex

```TypeScript
currentIndex?: int
```

当前条目序号，默认值为0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-EventInfo-currentIndex?: int--><!--Device-EventInfo-currentIndex?: int-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## customId

```TypeScript
customId?: string
```

主动聚焦的组件ID，默认值为空。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-EventInfo-customId?: string--><!--Device-EventInfo-customId?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## description

```TypeScript
description?: string
```

事件描述，根据实际场景设置，无特殊限制，默认值为空。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-EventInfo-description?: string--><!--Device-EventInfo-description?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## elementId

```TypeScript
elementId?: int
```

组件elementId，默认值为0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-EventInfo-elementId?: int--><!--Device-EventInfo-elementId?: int-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## endIndex

```TypeScript
endIndex?: int
```

画面显示条目的结束序号，默认值为0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-EventInfo-endIndex?: int--><!--Device-EventInfo-endIndex?: int-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## itemCount

```TypeScript
itemCount?: int
```

条目总数，默认值为0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-EventInfo-itemCount?: int--><!--Device-EventInfo-itemCount?: int-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## lastContent

```TypeScript
lastContent?: string
```

最新内容，根据实际场景设置，无特殊限制，默认值为空。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-EventInfo-lastContent?: string--><!--Device-EventInfo-lastContent?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## pageId

```TypeScript
pageId ?: int
```

事件源的页面ID，默认值为0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-EventInfo-pageId ?: int--><!--Device-EventInfo-pageId ?: int-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## textAnnouncedForAccessibility

```TypeScript
textAnnouncedForAccessibility?: string
```

主动播报的内容。当应用需要主动播报时，根据实际场景设置播报内容，无特殊限制，默认值为空。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-EventInfo-textAnnouncedForAccessibility?: string--><!--Device-EventInfo-textAnnouncedForAccessibility?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## textMoveUnit

```TypeScript
textMoveUnit?: TextMoveUnit
```

文本移动粒度，默认值为char。

**Type:** [TextMoveUnit](arkts-accessibility-accessibility-textmoveunit-t.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-EventInfo-textMoveUnit?: TextMoveUnit--><!--Device-EventInfo-textMoveUnit?: TextMoveUnit-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## textResourceAnnouncedForAccessibility

```TypeScript
textResourceAnnouncedForAccessibility?: Resource
```

主动播报的内容支持传入Resource类型，且只能传入string。

**Type:** [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-EventInfo-textResourceAnnouncedForAccessibility?: Resource--><!--Device-EventInfo-textResourceAnnouncedForAccessibility?: Resource-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## triggerAction

```TypeScript
triggerAction: Action
```

触发事件的Action，不可缺省。

**Type:** [Action](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-action-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-EventInfo-triggerAction: Action--><!--Device-EventInfo-triggerAction: Action-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## type

```TypeScript
type: EventType
```

无障碍事件类型，不可缺省。

**Type:** [EventType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-screenlock-eventtype-t-sys.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-EventInfo-type: EventType--><!--Device-EventInfo-type: EventType-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## windowUpdateType

```TypeScript
windowUpdateType?: WindowUpdateType
```

窗口变化类型。

**Type:** [WindowUpdateType](arkts-accessibility-accessibility-windowupdatetype-t.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-EventInfo-windowUpdateType?: WindowUpdateType--><!--Device-EventInfo-windowUpdateType?: WindowUpdateType-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

