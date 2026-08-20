# GesturePath

GesturePath represents gesture path information.

This module is used to create gesture path information for accessibility gesture injection.

**Since:** 9

<!--Device-unnamed-export declare class GesturePath--><!--Device-unnamed-export declare class GesturePath-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## Modules to Import

```TypeScript
import { GesturePath } from '@kit.AccessibilityKit';
```

## constructor

```TypeScript
constructor(durationTime: long)
```

Creates a gesture path object by passing in the total gesture duration. After creating a GesturePath instance, you must also set the required property points.

**Since:** 9

**Deprecated since:** 12

<!--Device-GesturePath-constructor(durationTime: long)--><!--Device-GesturePath-constructor(durationTime: long)-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| durationTime | long | Yes | Total gesture duration, in ms. The value must be greater than 0. |

**Examples**

```TypeScript
import { GesturePath } from '@kit.AccessibilityKit';

let gesturePath = new GesturePath(20);
```

## durationTime

```TypeScript
durationTime: long
```

Total gesture duration, in ms. The value must be greater than 0.

**Type:** long

**Since:** 9

<!--Device-GesturePath-durationTime: long--><!--Device-GesturePath-durationTime: long-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## points

```TypeScript
points: Array<GesturePoint>
```

Sequence of touch points on the gesture path, used to form the movement trajectory of the gesture. Each touch point represents a coordinate position on the path. The array length must be greater than 0.

**Type:** Array&lt;[GesturePoint](arkts-accessibility-accessibility-gesturepoint-gesturepoint-c.md)&gt;

**Since:** 9

<!--Device-GesturePath-points: Array<GesturePoint>--><!--Device-GesturePath-points: Array<GesturePoint>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

