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
import { AccessibilityElement } from 'AccessibilityElement';
import { AccessibilityExtensionContext } from 'AccessibilityExtensionContext';
import { ElementAttributeKeys } from 'ElementAttributeKeys';
import { ElementAttributeValues } from 'ElementAttributeValues';
import { FocusDirection } from 'FocusDirection';
import { FocusType } from 'FocusType';
import { Rect } from 'Rect';
import { WindowType } from 'WindowType';
import { AccessibilityEvent } from 'AccessibilityEvent';
import { AccessibilityEventInfo } from 'AccessibilityEventInfo';
import { Parameter } from 'Parameter';
import { FocusRule } from 'FocusRule';
import { FocusCondition } from 'FocusCondition';
import { FocusMoveResult } from 'FocusMoveResult';
import { AccessibilityVirtualNode } from 'AccessibilityVirtualNode';
import { TouchPosition } from 'TouchPosition';
```

## eventType

```TypeScript
eventType: AccessibilityEventType
```

Accessibility event type.

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

For TextArea, TextInput, SearchField, and RichEdit components, when text content is added or deleted, this property indicates the specific text content added or deleted. The default value is an empty string.

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

Target component where the event occurs. When the accessibility event involves a specific component, this property contains the component information.

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

Event timestamp, in milliseconds. The default value is **0**.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-AccessibilityEventInfo-timestamp?: long--><!--Device-AccessibilityEventInfo-timestamp?: long-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

