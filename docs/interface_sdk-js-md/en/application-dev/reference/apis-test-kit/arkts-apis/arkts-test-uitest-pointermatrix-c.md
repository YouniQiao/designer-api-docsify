# PointerMatrix

Implements a **PointerMatrix** object that stores coordinates and behaviors of each action of each finger in a multi-touch operation. After creating an object using [create](create), use [setPoint](#setPoint) to set the coordinates of each finger at each step. Then pass the coordinates to [injectMultiPointerAction](arkts-test-uitest-driver-c.md#injectMultiPointerAction) to perform a multi-finger operation.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class PointerMatrix--><!--Device-unnamed-declare class PointerMatrix-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from '@kit.TestKit';
```

## create

ArkTS-Dyn:
```TypeScript
static create(fingers: number, steps: number): PointerMatrix
```

ArkTS-Sta:
```TypeScript
static create(fingers: int, steps: int): PointerMatrix
```

Creates a **PointerMatrix** object and returns the object created. This API is a static API.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PointerMatrix-static create(fingers: int, steps: int): PointerMatrix--><!--Device-PointerMatrix-static create(fingers: int, steps: int): PointerMatrix-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fingers | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Number of fingers injected during the multi-finger operation. The value is an integer ranging from 1 to 10. If the value is out of range, error code 401 is thrown. |
| steps | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Number of steps performed by a finger. The value is an integer ranging from 1 to 1000. If the value is out of range, error code 401 is thrown. |

**Return value:**

| Type | Description |
| --- | --- |
| [PointerMatrix](arkts-test-uitest-pointermatrix-c.md) | PointerMatrix** object created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { PointerMatrix } from '@kit.TestKit';

async function demo() {
  let pointerMatrix: PointerMatrix = PointerMatrix.create(2, 3);
}
```

## setPoint

ArkTS-Dyn:
```TypeScript
setPoint(finger: number, step: number, point: Point): void
```

ArkTS-Sta:
```TypeScript
setPoint(finger: int, step: int, point: Point): void
```

Sets the coordinates for the action corresponding to the specified finger and step in the **PointerMatrix**object.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PointerMatrix-setPoint(finger: int, step: int, point: Point): void--><!--Device-PointerMatrix-setPoint(finger: int, step: int, point: Point): void-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| finger | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Number of fingers. The value is an integer greater than or equal to 0 and cannot exceed the number of fingers set when the **PointerMatrix** object is constructed. |
| step | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Number of steps. The value is an integer greater than or equal to 0 and cannot exceed the number of steps set when the **PointerMatrix** object is constructed. |
| point | [Point](arkts-test-uitest-point-i.md) | Yes | Coordinates of the action. It is recommended that the distance between adjacent coordinates be within the range of 10 px to 80 px. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
// xxx.test.ets
import { PointerMatrix } from '@kit.TestKit';

async function demo() {
  let pointers: PointerMatrix = PointerMatrix.create(2, 5);
  pointers.setPoint(0, 0, { x: 250, y: 480 });
  pointers.setPoint(0, 1, { x: 250, y: 440 });
  pointers.setPoint(0, 2, { x: 250, y: 400 });
  pointers.setPoint(0, 3, { x: 250, y: 360 });
  pointers.setPoint(0, 4, { x: 250, y: 320 });
  pointers.setPoint(1, 0, { x: 250, y: 480 });
  pointers.setPoint(1, 1, { x: 250, y: 440 });
  pointers.setPoint(1, 2, { x: 250, y: 400 });
  pointers.setPoint(1, 3, { x: 250, y: 360 });
  pointers.setPoint(1, 4, { x: 250, y: 320 });
}
```

