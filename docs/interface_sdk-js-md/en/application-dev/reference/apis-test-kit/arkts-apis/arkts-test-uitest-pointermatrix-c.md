# PointerMatrix

存储多指操作中每根手指每一步动作的坐标点及其行为的二维数组。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class PointerMatrix--><!--Device-unnamed-declare class PointerMatrix-End-->

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from 'kits/@kit.TestKit';
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

静态方法，构造一个PointerMatrix对象，并返回该对象。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PointerMatrix-static create(fingers: int, steps: int): PointerMatrix--><!--Device-PointerMatrix-static create(fingers: int, steps: int): PointerMatrix-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fingers | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 多指操作中注入的手指数，取值范围：[1,10]的整数。 |
| steps | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 每根手指操作的步骤数，取值范围：[1,1000]的整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PointerMatrix](arkts-test-uitest-pointermatrix-c.md) | 返回构造的PointerMatrix对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

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

设置PointerMatrix对象中指定手指和步骤对应动作的坐标点。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PointerMatrix-setPoint(finger: int, step: int, point: Point): void--><!--Device-PointerMatrix-setPoint(finger: int, step: int, point: Point): void-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| finger | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 手指的序号，取值大于等于0的整数，且不超过构造PointerMatrix对象时设置的手指数。 |
| step | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 步骤的序号，取值大于等于0的整数，且不超过构造PointerMatrix对象时设置的操作的步骤数。 |
| point | [Point](../../apis-camera-kit/arkts-apis/arkts-camera-camera-point-i.md) | Yes | 该行为的坐标点。建议相邻的坐标点距离在10px至80px范围内。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

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

