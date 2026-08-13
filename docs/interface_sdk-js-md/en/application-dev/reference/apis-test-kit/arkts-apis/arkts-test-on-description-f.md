# description

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from '@kit.TestKit';
```

## description

```TypeScript
export function description(val: string, pattern?: MatchPattern): On
```

Specifies the description for the target Component.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ON-export function description(val: string, pattern?: MatchPattern): On--><!--Device-ON-export function description(val: string, pattern?: MatchPattern): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | string | Yes | the description value. |
| pattern | [MatchPattern](arkts-test-uitest-matchpattern-e.md) | No | the [MatchPattern](arkts-test-uitest-matchpattern-e.md#MatchPattern) of description value. &lt;br&gt;Default value: [EQUALS](arkts-test-uitest-matchpattern-e.md#EQUALS) |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | this { |

