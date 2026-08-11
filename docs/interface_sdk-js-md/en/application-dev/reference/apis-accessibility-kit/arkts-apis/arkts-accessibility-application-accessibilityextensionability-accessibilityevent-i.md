# AccessibilityEvent

Defines an accessibility event.

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

Component ID for auto-focusing. The default value is **0**.

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

Event type.

**EventType**: accessibility event type.

**WindowUpdateType**: window update type.

**TouchGuideType**: touch guide type.

**GestureType**: gesture type.

**PageUpdateType**: page update type.

**Type:** accessibility.EventType \| accessibility.WindowUpdateType \| TouchGuideType \| GestureType \| PageUpdateType

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-AccessibilityEvent-eventType: accessibility.EventType | accessibility.WindowUpdateType |        TouchGuideType | GestureType | PageUpdateType--><!--Device-AccessibilityEvent-eventType: accessibility.EventType | accessibility.WindowUpdateType |        TouchGuideType | GestureType | PageUpdateType-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## extraInfo

```TypeScript
extraInfo?: string
```

Added or deleted text content carried by the **TextArea**, **TextInput**, **SearchField**, or **RichEdit** component. Set this parameter based on site requirements. No special restrictions.

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-AccessibilityEvent-extraInfo?: string--><!--Device-AccessibilityEvent-extraInfo?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## target

```TypeScript
target?: AccessibilityElement
```

Target component where the event occurs.

**Type:** [AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-AccessibilityEvent-target?: AccessibilityElement--><!--Device-AccessibilityEvent-target?: AccessibilityElement-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## textAnnouncedForAccessibility

```TypeScript
textAnnouncedForAccessibility?: string
```

Content for auto-broadcasting. Set the broadcast content based on the actual scenario. No special restrictions.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-AccessibilityEvent-textAnnouncedForAccessibility?: string--><!--Device-AccessibilityEvent-textAnnouncedForAccessibility?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## timeStamp

```TypeScript
timeStamp?: long
```

Timestamp of the event, in milliseconds. The default value is **0**.

**Type:** long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-AccessibilityEvent-timeStamp?: long--><!--Device-AccessibilityEvent-timeStamp?: long-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

