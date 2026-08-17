# GesturePoint(Gesture Point)

GesturePoint represents a gesture touch point and is the basic unit that constitutes a gesture path (GesturePath). This module is used to create touch point information for gesture paths, for use by accessibility applications to inject gestures.

**Since:** 9

<!--Device-unnamed-export declare class GesturePoint--><!--Device-unnamed-export declare class GesturePoint-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## Modules to Import

```TypeScript
import { GesturePoint } from 'GesturePoint';
```

## constructor

```TypeScript
constructor(positionX: double, positionY: double)
```

Creates a **GesturePoint** instance based on the given X and Y coordinates.

**Since:** 9

**Deprecated since:** 12

<!--Device-GesturePoint-constructor(positionX: double, positionY: double)--><!--Device-GesturePoint-constructor(positionX: double, positionY: double)-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| positionX | double | Yes | X coordinate of the touch point, in pixels (px). |
| positionY | double | Yes | Y coordinate of the touch point, in pixels (px). |

**Examples**

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

<!--Device-GesturePoint-positionX: double--><!--Device-GesturePoint-positionX: double-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## positionY

```TypeScript
positionY: double
```

Y coordinate of the touch point, in pixels (px).

**Type:** double

**Since:** 9

<!--Device-GesturePoint-positionY: double--><!--Device-GesturePoint-positionY: double-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

