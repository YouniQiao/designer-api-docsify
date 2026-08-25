# PointerMatrix

Implements a **PointerMatrix** object that stores coordinates and behaviors of each action of each finger in a multi-touch operation. After creating an object using create, use [setPoint](#setpoint) to set the coordinates of each finger at each step. Then pass the coordinates to [injectMultiPointerAction](arkts-test-uitest-driver-c.md#injectmultipointeraction) to perform a multi-finger operation.

**Since:** 9

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from 'kits/@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from 'kits/@kit.TestKit';
```

## create

```TypeScript
static create(fingers: number, steps: number): PointerMatrix
```

Creates a **PointerMatrix** object and returns the object created. This API is a static API.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fingers | number | Yes |
| steps | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PointerMatrix](arkts-test-uitest-pointermatrix-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setPoint

```TypeScript
setPoint(finger: number, step: number, point: Point): void
```

Sets the coordinates for the action corresponding to the specified finger and step in the **PointerMatrix** object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| finger | number | Yes |
| step | number | Yes |
| point | [Point](arkts-test-uitest-point-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
