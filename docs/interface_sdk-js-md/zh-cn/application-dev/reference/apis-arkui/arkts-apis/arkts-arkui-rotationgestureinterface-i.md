# RotationGestureInterface

用于触发旋转手势，最少需要2指，最多5指，最小改变度数为1度。该手势不支持通过触控板双指旋转操作触发。

**继承/实现关系：** RotationGestureInterface extends GestureInterface<RotationGestureInterface>

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## [[Call]]

```TypeScript
(value?: { fingers?: number; angle?: number }): RotationGestureInterface
```

继承自[GestureInterface&lt;T&gt;](arkts-arkui-gestureinterface-i.md)，设置旋转手势事件。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | { fingers?: number; angle?: number } | 否 |

**返回值：**

| 类型 |
| --- |
| [RotationGestureInterface](arkts-arkui-rotationgestureinterface-i.md) |

## [[Call]]

```TypeScript
(options?: RotationGestureHandlerOptions): RotationGestureInterface
```

设置旋转手势事件。与RotationGesture)}相比， options参数新增了isFingerCountLimited参数，表示是否检查触摸屏幕的手指数量。

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为15。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [RotationGestureHandlerOptions](arkts-arkui-rotationgesturehandleroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [RotationGestureInterface](arkts-arkui-rotationgestureinterface-i.md) |

## onActionCancel

```TypeScript
onActionCancel(event: () => void): RotationGestureInterface
```

Rotation手势识别成功，接收到触摸取消事件触发的回调。该回调不返回手势事件信息。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | () = & gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| [RotationGestureInterface](arkts-arkui-rotationgestureinterface-i.md) |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<GestureEvent>): RotationGestureInterface
```

Rotation手势识别成功，接收到触摸取消事件触发的回调。与onActionCancel相 比，该回调返回手势事件信息。

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为18。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | Callback&lt;[GestureEvent](arkts-arkui-gestureevent-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [RotationGestureInterface](arkts-arkui-rotationgestureinterface-i.md) |

## onActionEnd

```TypeScript
onActionEnd(event: (event: GestureEvent) => void): RotationGestureInterface
```

Rotation手势识别成功，当抬起最后一根满足手势触发条件的手指后触发的回调。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (event: GestureEvent) = & gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| [RotationGestureInterface](arkts-arkui-rotationgestureinterface-i.md) |

## onActionStart

```TypeScript
onActionStart(event: (event: GestureEvent) => void): RotationGestureInterface
```

Rotation手势识别成功后触发的回调。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (event: GestureEvent) = & gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| [RotationGestureInterface](arkts-arkui-rotationgestureinterface-i.md) |

## onActionUpdate

```TypeScript
onActionUpdate(event: (event: GestureEvent) => void): RotationGestureInterface
```

Rotation手势移动过程中触发的回调。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (event: GestureEvent) = & gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| [RotationGestureInterface](arkts-arkui-rotationgestureinterface-i.md) |
