# within

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from '@kit.TestKit';
```

## within

```TypeScript
export function within(on: On): On
```

Requires that the target Component which is inside of another Component that specified by the given [On](arkts-test-uitest-on-c.md#On) object,used to locate Component relatively.

**Since:** 23

**Deprecated since:** -1

<!--Device-ON-export function within(on: On): On--><!--Device-ON-export function within(on: On): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| on | [On](arkts-test-uitest-on-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [On](arkts-test-uitest-on-c.md) |
