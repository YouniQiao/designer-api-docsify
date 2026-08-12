# TapGestureInterface

支持单击、双击和多次点击事件的识别。

> **说明：**
> 
> 当组件同时绑定双击和单击手势且双击手势先绑定时，单击手势会有300ms的延时。

**继承/实现关系：** TapGestureInterface extends [GestureInterface<TapGestureInterface>](GestureInterface<TapGestureInterface>)

**起始版本：** 7

<!--Device-unnamed-interface TapGestureInterface extends GestureInterface<TapGestureInterface>--><!--Device-unnamed-interface TapGestureInterface extends GestureInterface<TapGestureInterface>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## [[Call]]

```TypeScript
(value?: TapGestureParameters): TapGestureInterface
```

创建点击手势对象。继承自[GestureInterface&lt;T&gt;](arkts-arkui-gestureinterface-i.md#GestureInterface)。

触发点击手势事件的设备类型为键盘或手柄时，事件的[SourceTool](../arkts-components/arkts-arkui-sourcetool-e.md#SourceTool)值为Unknown，事件的[SourceType](SourceType)值为KEY或JOYSTICK。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-TapGestureInterface-(value?: TapGestureParameters): TapGestureInterface--><!--Device-TapGestureInterface-(value?: TapGestureParameters): TapGestureInterface-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [TapGestureParameters](arkts-arkui-tapgestureparameters-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [TapGestureInterface](arkts-arkui-tapgestureinterface-i.md) |

## onAction

```TypeScript
onAction(event: (event: GestureEvent) => void): TapGestureInterface
```

点击手势识别成功回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-TapGestureInterface-onAction(event: (event: GestureEvent) => void): TapGestureInterface--><!--Device-TapGestureInterface-onAction(event: (event: GestureEvent) => void): TapGestureInterface-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (event: GestureEvent) = & gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| [TapGestureInterface](arkts-arkui-tapgestureinterface-i.md) |
