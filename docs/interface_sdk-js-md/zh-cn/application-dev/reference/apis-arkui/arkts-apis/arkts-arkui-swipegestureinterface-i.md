# SwipeGestureInterface

用于触发快滑手势，滑动速度需大于速度阈值，默认最小速度为100vp/s。

**继承/实现关系：** SwipeGestureInterface extends GestureInterface<SwipeGestureInterface>

**起始版本：** 8

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## [[Call]]

```TypeScript
(value?: { fingers?: number; direction?: SwipeDirection; speed?: number }): SwipeGestureInterface
```

继承自[GestureInterface&lt;T&gt;](arkts-arkui-gestureinterface-i.md)，设置快滑手势事件。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | { fingers?: number; direction?: SwipeDirection; speed?: number } | 否 |

**返回值：**

| 类型 |
| --- |
| [SwipeGestureInterface](arkts-arkui-swipegestureinterface-i.md) |

## [[Call]]

```TypeScript
(options?: SwipeGestureHandlerOptions): SwipeGestureInterface
```

设置快滑手势事件。与SwipeGesture)}相比， options参数新增了isFingerCountLimited，表示是否检查触摸屏幕的手指数量。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [SwipeGestureHandlerOptions](arkts-arkui-swipegesturehandleroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [SwipeGestureInterface](arkts-arkui-swipegestureinterface-i.md) |

## onAction

```TypeScript
onAction(event: (event: GestureEvent) => void): SwipeGestureInterface
```

Swipe手势识别成功时触发回调。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (event: GestureEvent) = & gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| [SwipeGestureInterface](arkts-arkui-swipegestureinterface-i.md) |
