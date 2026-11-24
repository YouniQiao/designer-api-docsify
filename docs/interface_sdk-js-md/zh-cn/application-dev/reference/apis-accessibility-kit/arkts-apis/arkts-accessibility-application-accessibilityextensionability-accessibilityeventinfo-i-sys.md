# AccessibilityEventInfo（系统接口）

```TypeScript
export declare interface AccessibilityEventInfo
```

无障碍事件信息。

**起始版本：** 20

<!--Device-unnamed-export declare interface AccessibilityEventInfo--><!--Device-unnamed-export declare interface AccessibilityEventInfo-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { AccessibilityExtensionAbility, AccessibilityElement, AccessibilityExtensionContext, ElementAttributeKeys, ElementAttributeValues, FocusDirection, FocusType, Rect, WindowType, AccessibilityEvent, AccessibilityEventInfo, Parameter, FocusRule, FocusCondition, FocusMoveResult, AccessibilityVirtualNode, TouchPosition } from '@kit.AccessibilityKit';
```

## eventType

```TypeScript
eventType: AccessibilityEventType
```

无障碍事件类型。

**类型：** [AccessibilityEventType](arkts-accessibility-accessibility-accessibilityeventtype-e-sys.md)

**起始版本：** 20

<!--Device-AccessibilityEventInfo-eventType: AccessibilityEventType--><!--Device-AccessibilityEventInfo-eventType: AccessibilityEventType-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## extraInfo

```TypeScript
extraInfo?: string
```

默认值为空字符串。

事件附加信息，值为JSON字符串，根据实际事件场景设置，无对应信息时为空字符串。包含以下字段：  
- addText：文本内容新增时，新增的具体文本内容。  
- removeText：文本内容删除时，删除的具体文本内容。  
- beforeText：文本内容发生变化前的文本内容。  
- addedCount：文本内容新增的字符数量。  
- removedCount：文本内容删除的字符数量。  
- startIndex：列表滚动前后的索引项，或编辑框的起始索引。  
- endIndex：列表滚动前后的索引项，或编辑框的结束索引。  
- scrollX：滚动事件发生时水平方向的滚动偏移量，单位为像素（px）  
- scrollY：滚动事件发生时垂直方向的滚动偏移量，单位为像素（px）。  
- scrollSource：滚动事件的触发来源。  
- itemCounts：列表或翻页类组件的总项数。  
- currentIndex：列表或翻页类组件当前项的索引。  
- candidateIds：焦点不可见时事件携带的候选焦点ID。  
- touchGuideGestureType：触摸浏览手势的类型。

**类型：** string

**起始版本：** 20

<!--Device-AccessibilityEventInfo-extraInfo?: string--><!--Device-AccessibilityEventInfo-extraInfo?: string-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## target

```TypeScript
target?: AccessibilityElement
```

发生事件的目标组件。当无障碍事件涉及具体组件时，此属性包含该组件信息。

**类型：** [AccessibilityElement](arkts-accessibility-accessibilityelement-t.md)

**起始版本：** 20

<!--Device-AccessibilityEventInfo-target?: AccessibilityElement--><!--Device-AccessibilityEventInfo-target?: AccessibilityElement-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## timestamp

```TypeScript
timestamp?: number
```

事件时间戳，单位为毫秒，默认值为0。

**类型：** number

**起始版本：** 20

<!--Device-AccessibilityEventInfo-timestamp?: long--><!--Device-AccessibilityEventInfo-timestamp?: long-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。
