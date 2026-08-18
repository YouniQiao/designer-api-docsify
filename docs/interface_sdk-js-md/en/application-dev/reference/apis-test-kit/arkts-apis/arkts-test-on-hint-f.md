# hint

## Modules to Import

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from '@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from '@kit.TestKit';
```

## hint

```TypeScript
export function hint(val: string, pattern?: MatchPattern): On
```

Specifies the hint for the target Component.

**Since:** 23

<!--Device-ON-export function hint(val: string, pattern?: MatchPattern): On--><!--Device-ON-export function hint(val: string, pattern?: MatchPattern): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | string | Yes | the hint value. |
| pattern | [MatchPattern](arkts-test-uitest-matchpattern-e.md) | No | the [MatchPattern](arkts-test-uitest-matchpattern-e.md) of the text value. <br>Default value: [EQUALS](arkts-test-uitest-matchpattern-e.md#equals) |

**Return value:**

| Type | Description |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | this { |

