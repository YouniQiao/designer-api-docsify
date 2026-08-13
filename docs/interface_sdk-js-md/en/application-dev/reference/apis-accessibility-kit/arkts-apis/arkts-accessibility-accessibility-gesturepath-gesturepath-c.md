# GesturePath

The **GesturePath** module provides APIs for creating gesture path information required for an accessibility application to inject gestures.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

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

Defines a constructor used to create a **GesturePath** instance.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

<!--Device-GesturePath-constructor(durationTime: long)--><!--Device-GesturePath-constructor(durationTime: long)-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| durationTime | long | Yes | Total gesture duration, in milliseconds. |

## Examples

```TypeScript
import { GesturePath } from '@kit.AccessibilityKit';

let gesturePath = new GesturePath(20);
```

## durationTime

```TypeScript
durationTime: long
```

Total gesture duration, in milliseconds.

**Type:** long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

<!--Device-GesturePath-durationTime: long--><!--Device-GesturePath-durationTime: long-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## points

```TypeScript
points: Array<GesturePoint>
```

Gesture touch point.

**Type:** Array&lt;[GesturePoint](arkts-accessibility-accessibility-gesturepoint-gesturepoint-c.md)&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

<!--Device-GesturePath-points: Array<GesturePoint>--><!--Device-GesturePath-points: Array<GesturePoint>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

