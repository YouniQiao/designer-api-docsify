# GesturePath

GesturePath represents gesture path information. This module is used to create gesture path information for accessibility gesture injection.

**Since:** 9

<!--Device-unnamed-export declare class GesturePath--><!--Device-unnamed-export declare class GesturePath-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(durationTime: number)
```

Creates a gesture path object by passing in the total gesture duration. After creating a GesturePath instance, you must also set the required property points.

**Since:** 9

**Deprecated since:** 12

<!--Device-GesturePath-constructor(durationTime: long)--><!--Device-GesturePath-constructor(durationTime: long)-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [durationTime](arkts-accessibility-accessibility-gesturepath-gesturepath-c.md) | number | Yes |

**Examples**

```TypeScript
import { GesturePath, GesturePoint } from '@kit.AccessibilityKit';

let gesturePath = new GesturePath(20);
let startPoint = new GesturePoint(100, 100);
let endPoint = new GesturePoint(200, 200);
gesturePath.points = [startPoint, endPoint];
```

## durationTime

```TypeScript
durationTime: number
```

Total gesture duration, in ms. The value must be greater than 0.

**Type:** number

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
