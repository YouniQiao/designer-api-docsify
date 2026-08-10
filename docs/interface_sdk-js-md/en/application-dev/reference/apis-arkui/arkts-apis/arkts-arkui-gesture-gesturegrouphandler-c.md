# GestureGroupHandler

手势组处理器对象类型。

**Inheritance/Implementation:** GestureGroupHandler extends [GestureHandler](arkts-arkui-gesturehandler-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class GestureGroupHandler extends GestureHandler--><!--Device-unnamed-export declare class GestureGroupHandler extends GestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: GestureGroupGestureHandlerOptions)
```

手势组处理器的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureGroupHandler-constructor(options?: GestureGroupGestureHandlerOptions)--><!--Device-GestureGroupHandler-constructor(options?: GestureGroupGestureHandlerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [GestureGroupGestureHandlerOptions](arkts-arkui-gesturegroupgesturehandleroptions-i.md) | No | 手势组处理器配置参数。 |

## onCancel

```TypeScript
onCancel(event: VoidCallback): this
```

设置手势组处理器取消回调。顺序组合手势（[GestureMode](arkts-arkui-gesturemode-e.md).Sequence）取消后触发回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureGroupHandler-onCancel(event: VoidCallback): this--><!--Device-GestureGroupHandler-onCancel(event: VoidCallback): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) | Yes | 手势组处理器取消回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回当前手势组处理器对象。 |

