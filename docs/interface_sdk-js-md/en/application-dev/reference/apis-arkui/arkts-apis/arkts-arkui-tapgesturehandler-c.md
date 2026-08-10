# TapGestureHandler

点击手势处理器对象类型。

**Inheritance/Implementation:** TapGestureHandler extends [GestureHandler<TapGestureHandler>](GestureHandler<TapGestureHandler>)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class TapGestureHandler extends GestureHandler<TapGestureHandler>--><!--Device-unnamed-declare class TapGestureHandler extends GestureHandler<TapGestureHandler>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: TapGestureHandlerOptions)
```

点击手势处理器的构造函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TapGestureHandler-constructor(options?: TapGestureHandlerOptions)--><!--Device-TapGestureHandler-constructor(options?: TapGestureHandlerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TapGestureHandlerOptions](arkts-arkui-tapgesturehandleroptions-i.md) | No | 点击手势处理器配置参数。 |

## onAction

```TypeScript
onAction(event: Callback<GestureEvent>): TapGestureHandler
```

设置点击手势处理器识别成功回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TapGestureHandler-onAction(event: Callback<GestureEvent>): TapGestureHandler--><!--Device-TapGestureHandler-onAction(event: Callback<GestureEvent>): TapGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 点击手势处理器识别成功回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [TapGestureHandler](arkts-arkui-gesture-tapgesturehandler-c.md) | 返回当前点击手势处理器对象。 |

