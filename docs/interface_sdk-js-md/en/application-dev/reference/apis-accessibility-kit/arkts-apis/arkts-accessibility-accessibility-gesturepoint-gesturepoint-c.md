# GesturePoint

The **GesturePoint** module provides APIs for creating gesture touch point information required for an accessibility application to inject gestures.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-unnamed-export declare class GesturePoint--><!--Device-unnamed-export declare class GesturePoint-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## constructor

```TypeScript
constructor(positionX: double, positionY: double)
```

Defines a constructor used to create a **GesturePoint** instance.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

<!--Device-GesturePoint-constructor(positionX: double, positionY: double)--><!--Device-GesturePoint-constructor(positionX: double, positionY: double)-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| positionX | double | Yes | X coordinate of the touch point, in pixels (px). |
| positionY | double | Yes | Y coordinate of the touch point, in pixels (px). |

**Example**

```TypeScript
import { GesturePoint } from '@kit.AccessibilityKit';

let gesturePoint = new GesturePoint(1, 2);
```

## positionX

```TypeScript
positionX: double
```

X coordinate of the touch point, in pixels (px).

**Type:** double

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-GesturePoint-positionX: double--><!--Device-GesturePoint-positionX: double-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## positionY

```TypeScript
positionY: double
```

Y coordinate of the touch point, in pixels (px).

**Type:** double

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-GesturePoint-positionY: double--><!--Device-GesturePoint-positionY: double-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

