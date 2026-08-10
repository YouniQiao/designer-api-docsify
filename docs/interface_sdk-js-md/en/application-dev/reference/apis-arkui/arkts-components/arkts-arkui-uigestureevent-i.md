# UIGestureEvent

用于设置组件绑定的手势。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface UIGestureEvent--><!--Device-unnamed-declare interface UIGestureEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addGesture

```TypeScript
addGesture<T>(gesture: GestureHandler<T>, priority?: GesturePriority, mask?: GestureMask): void
```

添加手势。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-UIGestureEvent-addGesture<T>(gesture: GestureHandler<T>, priority?: GesturePriority, mask?: GestureMask): void--><!--Device-UIGestureEvent-addGesture<T>(gesture: GestureHandler<T>, priority?: GesturePriority, mask?: GestureMask): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| gesture | [GestureHandler](../arkts-apis/arkts-arkui-gesturehandler-c.md)&lt;T&gt; | Yes | 手势处理器对象。 |
| priority | [GesturePriority](../arkts-apis/arkts-arkui-gesturepriority-e.md) | No | 绑定手势的优先级。&lt;br&gt;默认值：GesturePriority.NORMAL |
| mask | [GestureMask](../arkts-apis/arkts-arkui-gesturemask-e.md) | No | 事件响应设置。&lt;br&gt;默认值：GestureMask.Normal |

## addParallelGesture

```TypeScript
addParallelGesture<T>(gesture: GestureHandler<T>, mask?: GestureMask): void
```

绑定可与子组件手势同时触发的手势。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-UIGestureEvent-addParallelGesture<T>(gesture: GestureHandler<T>, mask?: GestureMask): void--><!--Device-UIGestureEvent-addParallelGesture<T>(gesture: GestureHandler<T>, mask?: GestureMask): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| gesture | [GestureHandler](../arkts-apis/arkts-arkui-gesturehandler-c.md)&lt;T&gt; | Yes | 手势处理器对象。 |
| mask | [GestureMask](../arkts-apis/arkts-arkui-gesturemask-e.md) | No | 事件响应设置。&lt;br&gt;默认值：GestureMask.Normal |

## clearGestures

```TypeScript
clearGestures(): void
```

清除该组件上通过modifier绑定的所有手势。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-UIGestureEvent-clearGestures(): void--><!--Device-UIGestureEvent-clearGestures(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## removeGestureByTag

```TypeScript
removeGestureByTag(tag: string): void
```

移除该组件上通过modifier绑定的设置为指定标志的手势。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-UIGestureEvent-removeGestureByTag(tag: string): void--><!--Device-UIGestureEvent-removeGestureByTag(tag: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tag | string | Yes | 手势处理器标志。 |

