# AccessibilityEventInfo (System API)

Describes the accessibility event information.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface AccessibilityEventInfo--><!--Device-unnamed-export declare interface AccessibilityEventInfo-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { Rect, TouchPosition, AccessibilityVirtualNode, ElementAttributeKeys, FocusCondition, AccessibilityExtensionContext, ElementAttributeValues, AccessibilityEventInfo, AccessibilityEvent, AccessibilityElement, FocusRule, FocusMoveResult, FocusType, Parameter, FocusDirection, WindowType } from '@kit.AccessibilityKit';
```

## eventType

```TypeScript
eventType: AccessibilityEventType
```

Event type.

**Type:** [AccessibilityEventType](arkts-accessibility-accessibility-accessibilityeventtype-e-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-AccessibilityEventInfo-eventType: AccessibilityEventType--><!--Device-AccessibilityEventInfo-eventType: AccessibilityEventType-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## extraInfo

```TypeScript
extraInfo?: string
```

Added or deleted text content carried by the **TextArea**, **TextInput**, **SearchField**, or **RichEdit** component.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-AccessibilityEventInfo-extraInfo?: string--><!--Device-AccessibilityEventInfo-extraInfo?: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## target

```TypeScript
target?: AccessibilityElement
```

Target component where the event occurs.

**Type:** [AccessibilityElement](arkts-accessibility-accessibilityelement-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-AccessibilityEventInfo-target?: AccessibilityElement--><!--Device-AccessibilityEventInfo-target?: AccessibilityElement-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## timestamp

```TypeScript
timestamp?: long
```

Timestamp of the event, in milliseconds. The default value is **0**.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-AccessibilityEventInfo-timestamp?: long--><!--Device-AccessibilityEventInfo-timestamp?: long-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

