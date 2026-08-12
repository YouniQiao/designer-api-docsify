# PinchGestureInterface

用于触发捏合手势，最少需要2指，最多5指，最小识别距离为5vp。在支持鼠标和键盘输入的设备上，通过“Ctrl+鼠标滚轮”也可以触发捏合手势。

> **说明：**
> 
> 捏合手势触发成功后，抬起手指直至不再满足触发条件。再次满足条件时，可重新触发捏合手势。

**继承/实现关系：** PinchGestureInterface extends [GestureInterface<PinchGestureInterface>](GestureInterface<PinchGestureInterface>)

**起始版本：** 7

<!--Device-unnamed-interface PinchGestureInterface extends GestureInterface<PinchGestureInterface>--><!--Device-unnamed-interface PinchGestureInterface extends GestureInterface<PinchGestureInterface>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## [[Call]]

```TypeScript
(value?: { fingers?: number; distance?: number }): PinchGestureInterface
```

继承自[GestureInterface&lt;T&gt;](arkts-arkui-gestureinterface-i.md#GestureInterface)，设置捏合手势事件。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PinchGestureInterface-(value?: { fingers?: number; distance?: number }): PinchGestureInterface--><!--Device-PinchGestureInterface-(value?: { fingers?: number; distance?: number }): PinchGestureInterface-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | { fingers?: number; distance?: number } | 否 |

**返回值：**

| 类型 |
| --- |
| [PinchGestureInterface](arkts-arkui-pinchgestureinterface-i.md) |

## [[Call]]

```TypeScript
(options?: PinchGestureHandlerOptions): PinchGestureInterface
```

设置捏合手势事件。与[PinchGesture](PinchGestureInterface(value?: { fingers?: number; distance?: number))}相比，options参数新增isFingerCountLimited，表示是否检查触摸屏幕的手指数量。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-PinchGestureInterface-(options?: PinchGestureHandlerOptions): PinchGestureInterface--><!--Device-PinchGestureInterface-(options?: PinchGestureHandlerOptions): PinchGestureInterface-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [PinchGestureHandlerOptions](arkts-arkui-pinchgesturehandleroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [PinchGestureInterface](arkts-arkui-pinchgestureinterface-i.md) |

## onActionCancel

```TypeScript
onActionCancel(event: () => void): PinchGestureInterface
```

Pinch手势识别成功，接收到触摸取消事件触发的回调，不返回手势事件信息。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PinchGestureInterface-onActionCancel(event: () => void): PinchGestureInterface--><!--Device-PinchGestureInterface-onActionCancel(event: () => void): PinchGestureInterface-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | () = & gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| [PinchGestureInterface](arkts-arkui-pinchgestureinterface-i.md) |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<GestureEvent>): PinchGestureInterface
```

Pinch手势识别成功并接收到触摸取消事件的回调。与[onActionCancel](PinchGestureInterface.onActionCancel(event: () => void))相比，该回调返回手势事件信息。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-PinchGestureInterface-onActionCancel(event: Callback<GestureEvent>): PinchGestureInterface--><!--Device-PinchGestureInterface-onActionCancel(event: Callback<GestureEvent>): PinchGestureInterface-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | Callback&lt;[GestureEvent](arkts-arkui-gestureevent-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [PinchGestureInterface](arkts-arkui-pinchgestureinterface-i.md) |

## onActionEnd

```TypeScript
onActionEnd(event: (event: GestureEvent) => void): PinchGestureInterface
```

Pinch手势识别成功，当抬起最后一根满足手势触发条件的手指后，触发回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PinchGestureInterface-onActionEnd(event: (event: GestureEvent) => void): PinchGestureInterface--><!--Device-PinchGestureInterface-onActionEnd(event: (event: GestureEvent) => void): PinchGestureInterface-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (event: GestureEvent) = & gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| [PinchGestureInterface](arkts-arkui-pinchgestureinterface-i.md) |

## onActionStart

```TypeScript
onActionStart(event: (event: GestureEvent) => void): PinchGestureInterface
```

Pinch手势识别成功后触发回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PinchGestureInterface-onActionStart(event: (event: GestureEvent) => void): PinchGestureInterface--><!--Device-PinchGestureInterface-onActionStart(event: (event: GestureEvent) => void): PinchGestureInterface-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (event: GestureEvent) = & gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| [PinchGestureInterface](arkts-arkui-pinchgestureinterface-i.md) |

## onActionUpdate

```TypeScript
onActionUpdate(event: (event: GestureEvent) => void): PinchGestureInterface
```

Pinch手势移动过程中回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PinchGestureInterface-onActionUpdate(event: (event: GestureEvent) => void): PinchGestureInterface--><!--Device-PinchGestureInterface-onActionUpdate(event: (event: GestureEvent) => void): PinchGestureInterface-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (event: GestureEvent) = & gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| [PinchGestureInterface](arkts-arkui-pinchgestureinterface-i.md) |
