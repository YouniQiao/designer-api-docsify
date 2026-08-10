# SwipeGestureHandler

快滑手势处理器对象类型。

**Inheritance/Implementation:** SwipeGestureHandler extends [GestureHandler](arkts-arkui-gesturehandler-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class SwipeGestureHandler extends GestureHandler--><!--Device-unnamed-export declare class SwipeGestureHandler extends GestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: SwipeGestureHandlerOptions)
```

快滑手势处理器的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeGestureHandler-constructor(options?: SwipeGestureHandlerOptions)--><!--Device-SwipeGestureHandler-constructor(options?: SwipeGestureHandlerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [SwipeGestureHandlerOptions](arkts-arkui-gesture-swipegesturehandleroptions-i.md) | No | 快滑手势处理器配置参数。 |

## onAction

```TypeScript
onAction(event: Callback<GestureEvent>): this
```

设置快滑手势处理器识别成功回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeGestureHandler-onAction(event: Callback<GestureEvent>): this--><!--Device-SwipeGestureHandler-onAction(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 快滑手势处理器识别成功回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回当前快滑手势处理器对象。 |

