# AccessibilityEvent

辅助事件信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-unnamed-export declare interface AccessibilityEvent--><!--Device-unnamed-export declare interface AccessibilityEvent-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## Modules to Import

```TypeScript
import { Rect, TouchPosition, AccessibilityVirtualNode, ElementAttributeKeys, FocusCondition, AccessibilityExtensionContext, ElementAttributeValues, AccessibilityEventInfo, AccessibilityEvent, AccessibilityElement, FocusRule, FocusMoveResult, FocusType, Parameter, FocusDirection, WindowType } from 'kits/@kit.AccessibilityKit';
```

## elementId

```TypeScript
elementId?: long
```

主动聚焦的组件ID。默认值为0。

**Type:** long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-AccessibilityEvent-elementId?: long--><!--Device-AccessibilityEvent-elementId?: long-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## eventType

```TypeScript
eventType: accessibility.EventType | accessibility.WindowUpdateType |
        TouchGuideType | GestureType | PageUpdateType
```

具体事件类型。

EventType：无障碍事件类型；

WindowUpdateType：窗口变化类型；

TouchGuideType：触摸浏览事件类型；

GestureType：手势事件类型；

PageUpdateType：页面刷新类型。

**Type:** accessibility.EventType \| accessibility.WindowUpdateType \| TouchGuideType \| GestureType \| PageUpdateType

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-AccessibilityEvent-eventType: accessibility.EventType | accessibility.WindowUpdateType |        TouchGuideType | GestureType | PageUpdateType--><!--Device-AccessibilityEvent-eventType: accessibility.EventType | accessibility.WindowUpdateType |        TouchGuideType | GestureType | PageUpdateType-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## extraInfo

```TypeScript
extraInfo?: string
```

针对TextArea、TextInput、SearchField、RichEdit组件，当文本内容有新增或删除时，携带的文本内容。根据实际场景设置，无特殊限制。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-AccessibilityEvent-extraInfo?: string--><!--Device-AccessibilityEvent-extraInfo?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## target

```TypeScript
target?: AccessibilityElement
```

发生事件的目标组件。

**Type:** [AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-AccessibilityEvent-target?: AccessibilityElement--><!--Device-AccessibilityEvent-target?: AccessibilityElement-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## textAnnouncedForAccessibility

```TypeScript
textAnnouncedForAccessibility?: string
```

主动播报的内容。当应用需要主动播报时根据实际场景设置播报内容，无特殊限制。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-AccessibilityEvent-textAnnouncedForAccessibility?: string--><!--Device-AccessibilityEvent-textAnnouncedForAccessibility?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## timeStamp

```TypeScript
timeStamp?: long
```

事件时间戳，单位是毫秒。默认值为0。

**Type:** long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-AccessibilityEvent-timeStamp?: long--><!--Device-AccessibilityEvent-timeStamp?: long-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

