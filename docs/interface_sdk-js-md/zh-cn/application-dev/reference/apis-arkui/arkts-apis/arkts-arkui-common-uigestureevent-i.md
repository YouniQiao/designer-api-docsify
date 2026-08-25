# UIGestureEvent

Defines a UIGestureEvent which is used to set different gestures to target component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## addGesture

```TypeScript
addGesture(gesture: GestureHandler, priority?: GesturePriority, mask?: GestureMask): void
```

Add a gesture bound to the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| gesture | [GestureHandler](arkts-arkui-gesturehandler-c.md) | 是 |
| priority | [GesturePriority](arkts-arkui-gesturepriority-e.md) | 否 |
| mask | [GestureMask](arkts-arkui-gesturemask-e.md) | 否 |

## addParallelGesture

```TypeScript
addParallelGesture(gesture: GestureHandler, mask?: GestureMask): void
```

Add a parallel gesture bound to the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| gesture | [GestureHandler](arkts-arkui-gesturehandler-c.md) | 是 |
| mask | [GestureMask](arkts-arkui-gesturemask-e.md) | 否 |

## clearGestures

```TypeScript
clearGestures(): void
```

Clear gestures bound to the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## removeGestureByTag

```TypeScript
removeGestureByTag(tag: string): void
```

Remove a gesture from a component that has been bound with a specific tag through a modifier.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tag | string | 是 |
