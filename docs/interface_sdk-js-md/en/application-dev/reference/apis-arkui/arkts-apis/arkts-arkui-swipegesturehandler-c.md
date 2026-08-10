# SwipeGestureHandler

快滑手势处理器对象类型。

**Inheritance/Implementation:** SwipeGestureHandler extends [GestureHandler<SwipeGestureHandler>](GestureHandler<SwipeGestureHandler>)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class SwipeGestureHandler extends GestureHandler<SwipeGestureHandler>--><!--Device-unnamed-declare class SwipeGestureHandler extends GestureHandler<SwipeGestureHandler>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: SwipeGestureHandlerOptions)
```

快滑手势处理器的构造函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SwipeGestureHandler-constructor(options?: SwipeGestureHandlerOptions)--><!--Device-SwipeGestureHandler-constructor(options?: SwipeGestureHandlerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [SwipeGestureHandlerOptions](arkts-arkui-gesture-swipegesturehandleroptions-i.md) | No | 快滑手势处理器配置参数。 |

## onAction

```TypeScript
onAction(event: Callback<GestureEvent>): SwipeGestureHandler
```

设置快滑手势处理器识别成功回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SwipeGestureHandler-onAction(event: Callback<GestureEvent>): SwipeGestureHandler--><!--Device-SwipeGestureHandler-onAction(event: Callback<GestureEvent>): SwipeGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 快滑手势处理器识别成功回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SwipeGestureHandler](arkts-arkui-swipegesturehandler-c.md) | 返回当前快滑手势处理器对象。 |

