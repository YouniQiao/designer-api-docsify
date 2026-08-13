# belongingDisplay

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from '@kit.TestKit';
```

## belongingDisplay

```TypeScript
export function belongingDisplay(displayId: number): On
```

Specifies the displayId to which the target Component belongs.

**Since:** 23

**Deprecated since:** -1

<!--Device-ON-export function belongingDisplay(displayId: int): On--><!--Device-ON-export function belongingDisplay(displayId: int): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [On](arkts-test-uitest-on-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |
