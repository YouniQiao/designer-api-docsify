# UIGestureEvent

Defines a UIGestureEvent which is used to set different gestures to target component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface UIGestureEvent--><!--Device-unnamed-export declare interface UIGestureEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addGesture

```TypeScript
addGesture(gesture: GestureHandler, priority?: GesturePriority, mask?: GestureMask): void
```

Add a gesture bound to the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIGestureEvent-addGesture(gesture: GestureHandler, priority?: GesturePriority, mask?: GestureMask): void--><!--Device-UIGestureEvent-addGesture(gesture: GestureHandler, priority?: GesturePriority, mask?: GestureMask): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| gesture | [GestureHandler](arkts-arkui-gesturehandler-c.md) | Yes | gesture indicates the gesture bound to a component. |
| priority | [GesturePriority](arkts-arkui-gesturepriority-e.md) | No | priority indicates the gesture's priority. |
| mask | [GestureMask](arkts-arkui-gesturemask-e.md) | No | mask indicates the gesture's GestureMask value. |

## addParallelGesture

```TypeScript
addParallelGesture(gesture: GestureHandler, mask?: GestureMask): void
```

Add a parallel gesture bound to the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIGestureEvent-addParallelGesture(gesture: GestureHandler, mask?: GestureMask): void--><!--Device-UIGestureEvent-addParallelGesture(gesture: GestureHandler, mask?: GestureMask): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| gesture | [GestureHandler](arkts-arkui-gesturehandler-c.md) | Yes | gesture indicates the gesture bound to a component. |
| mask | [GestureMask](arkts-arkui-gesturemask-e.md) | No | mask indicates the gesture's GestureMask value. |

## clearGestures

```TypeScript
clearGestures(): void
```

Clear gestures bound to the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIGestureEvent-clearGestures(): void--><!--Device-UIGestureEvent-clearGestures(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## removeGestureByTag

```TypeScript
removeGestureByTag(tag: string): void
```

Remove a gesture from a component that has been bound with a specific tag through a modifier.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIGestureEvent-removeGestureByTag(tag: string): void--><!--Device-UIGestureEvent-removeGestureByTag(tag: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tag | string | Yes | tag indicates the gesture's tag. |

