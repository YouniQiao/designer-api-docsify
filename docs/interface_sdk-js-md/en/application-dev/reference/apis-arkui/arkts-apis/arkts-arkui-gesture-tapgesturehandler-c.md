# TapGestureHandler

点击手势处理器对象类型。

**Inheritance/Implementation:** TapGestureHandler extends [GestureHandler](arkts-arkui-gesturehandler-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class TapGestureHandler extends GestureHandler--><!--Device-unnamed-export declare class TapGestureHandler extends GestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: TapGestureHandlerOptions)
```

点击手势处理器的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TapGestureHandler-constructor(options?: TapGestureHandlerOptions)--><!--Device-TapGestureHandler-constructor(options?: TapGestureHandlerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TapGestureHandlerOptions](arkts-arkui-tapgesturehandleroptions-i.md) | No | 点击手势处理器配置参数。 |

## onAction

```TypeScript
onAction(event: Callback<GestureEvent>): this
```

设置点击手势处理器识别成功回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TapGestureHandler-onAction(event: Callback<GestureEvent>): this--><!--Device-TapGestureHandler-onAction(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 点击手势处理器识别成功回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回当前点击手势处理器对象。 |

