# GestureGroup

手势识别组合，即两种及以上手势组合为复合手势，支持顺序识别、并发识别和互斥识别。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate(factory: () => GestureGroup, mode: GestureMode, ...gesture: GestureType[]): GestureGroup
```

设置组合手势事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| factory | () = & gt; GestureGroup | 是 |
| mode | [GestureMode](arkts-arkui-gesture-gesturemode-e.md) | 是 |
| gesture | [GestureType](arkts-arkui-gesturetype-t.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| [GestureGroup](arkts-arkui-gesture-gesturegroup-c.md) |

## onCancel

```TypeScript
onCancel(event: VoidCallback): GestureGroup
```

手势识别成功，接收到触摸取消事件，触发回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [GestureGroup](arkts-arkui-gesture-gesturegroup-c.md) |
