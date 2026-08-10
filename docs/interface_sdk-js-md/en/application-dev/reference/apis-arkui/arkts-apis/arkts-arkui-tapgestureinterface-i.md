# TapGestureInterface

支持单击、双击和多次点击事件的识别。

> **说明：**
> 
> 当组件同时绑定双击和单击手势且双击手势先绑定时，单击手势会有300ms的延时。

**Inheritance/Implementation:** TapGestureInterface extends [GestureInterface<TapGestureInterface>](GestureInterface<TapGestureInterface>)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-interface TapGestureInterface extends GestureInterface<TapGestureInterface>--><!--Device-unnamed-interface TapGestureInterface extends GestureInterface<TapGestureInterface>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## [[Call]]

```TypeScript
(value?: TapGestureParameters): TapGestureInterface
```

创建点击手势对象。继承自[GestureInterface&lt;T&gt;](arkts-arkui-gestureinterface-i.md)。

触发点击手势事件的设备类型为键盘或手柄时，事件的[SourceTool](arkts-arkui-common-sourcetool-e.md)值为Unknown，事件的[SourceType](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-touchevent-sourcetype-e.md/arkts-input-multimodalinput-touchevent-sourcetype-e.md)值为KEY或JOYSTICK。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TapGestureInterface-(value?: TapGestureParameters): TapGestureInterface--><!--Device-TapGestureInterface-(value?: TapGestureParameters): TapGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [TapGestureParameters](arkts-arkui-gesture-tapgestureparameters-i.md) | No | 点击手势的相关参数。<br>**Since:** 12 |

**Return value:**

| Type | Description |
| --- | --- |
| [TapGestureInterface](arkts-arkui-tapgestureinterface-i.md) |  |

## onAction

```TypeScript
onAction(event: (event: GestureEvent) => void): TapGestureInterface
```

点击手势识别成功回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TapGestureInterface-onAction(event: (event: GestureEvent) => void): TapGestureInterface--><!--Device-TapGestureInterface-onAction(event: (event: GestureEvent) => void): TapGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (event: GestureEvent) =&gt; void | Yes | 手势事件回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [TapGestureInterface](arkts-arkui-tapgestureinterface-i.md) |  |

