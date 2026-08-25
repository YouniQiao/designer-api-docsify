# SwipeGesture

用于触发快滑手势，滑动速度需大于速度阈值，默认最小速度为100vp/s。

**继承/实现关系：** SwipeGesture extends [Gesture](arkts-arkui-gesture-gesture-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate(factory: () => SwipeGesture, value?: SwipeGestureHandlerOptions): SwipeGesture
```

设置快滑手势事件。继承自[Gesture](arkts-arkui-gesture-gesture-c.md)。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| factory | () = & gt; SwipeGesture | 是 |
| value | [SwipeGestureHandlerOptions](arkts-arkui-gesture-swipegesturehandleroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [SwipeGesture](arkts-arkui-gesture-swipegesture-c.md) |

## onAction

```TypeScript
onAction(event: Callback<GestureEvent>): this
```

Swipe手势识别成功时触发回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[GestureEvent](arkts-arkui-gesture-gestureevent-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| this |
