# TapGesture

支持单击、双击和多次点击事件的识别。

> **说明：**
> 
> 当组件同时绑定双击和单击手势且双击手势先绑定时，单击手势会有300ms的延时。

**Inheritance/Implementation:** TapGesture extends [Gesture](arkts-arkui-gesture-gesture-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class TapGesture extends Gesture--><!--Device-unnamed-export declare class TapGesture extends Gesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate(factory: () => TapGesture, value?: TapGestureParameters): TapGesture
```

创建点击手势对象。继承自[Gesture](arkts-arkui-gesture-gesture-c.md)。

触发点击手势事件的设备类型为键盘或手柄时，事件的[SourceTool](arkts-arkui-common-sourcetool-e.md)值为Unknown，事件的[SourceType](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-touchevent-sourcetype-e.md/arkts-input-multimodalinput-touchevent-sourcetype-e.md)值为KEY或JOYSTICK。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TapGesture-static $_instantiate(factory: () => TapGesture, value?: TapGestureParameters): TapGesture--><!--Device-TapGesture-static $_instantiate(factory: () => TapGesture, value?: TapGestureParameters): TapGesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | () =&gt; TapGesture | Yes |  |
| value | [TapGestureParameters](arkts-arkui-gesture-tapgestureparameters-i.md) | No | 点击手势的相关参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [TapGesture](arkts-arkui-gesture-tapgesture-c.md) |  |

## onAction

```TypeScript
onAction(event: Callback<GestureEvent>): this
```

点击手势识别成功回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TapGesture-onAction(event: Callback<GestureEvent>): this--><!--Device-TapGesture-onAction(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 手势事件回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

