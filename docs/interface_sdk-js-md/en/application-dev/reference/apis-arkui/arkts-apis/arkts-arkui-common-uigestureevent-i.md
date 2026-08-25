# UIGestureEvent

Defines a UIGestureEvent which is used to set different gestures to target component.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addGesture

```TypeScript
addGesture(gesture: GestureHandler, priority?: GesturePriority, mask?: GestureMask): void
```

Add a gesture bound to the component.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| gesture | [GestureHandler](arkts-arkui-gesturehandler-c.md) | Yes |
| priority | [GesturePriority](arkts-arkui-gesturepriority-e.md) | No |
| mask | [GestureMask](arkts-arkui-gesturemask-e.md) | No |

## addParallelGesture

```TypeScript
addParallelGesture(gesture: GestureHandler, mask?: GestureMask): void
```

Add a parallel gesture bound to the component.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| gesture | [GestureHandler](arkts-arkui-gesturehandler-c.md) | Yes |
| mask | [GestureMask](arkts-arkui-gesturemask-e.md) | No |

## clearGestures

```TypeScript
clearGestures(): void
```

Clear gestures bound to the component.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## removeGestureByTag

```TypeScript
removeGestureByTag(tag: string): void
```

Remove a gesture from a component that has been bound with a specific tag through a modifier.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tag | string | Yes |
