# SwipeGestureInterface

用于触发快滑手势，滑动速度需大于速度阈值，默认最小速度为100vp/s。

**Inheritance/Implementation:** SwipeGestureInterface extends [GestureInterface<SwipeGestureInterface>](GestureInterface<SwipeGestureInterface>)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-interface SwipeGestureInterface extends GestureInterface<SwipeGestureInterface>--><!--Device-unnamed-interface SwipeGestureInterface extends GestureInterface<SwipeGestureInterface>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## [[Call]]

```TypeScript
(value?: { fingers?: number; direction?: SwipeDirection; speed?: number }): SwipeGestureInterface
```

继承自[GestureInterface&lt;T&gt;](arkts-arkui-gestureinterface-i.md)，设置快滑手势事件。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SwipeGestureInterface-(value?: { fingers?: number; direction?: SwipeDirection; speed?: number }): SwipeGestureInterface--><!--Device-SwipeGestureInterface-(value?: { fingers?: number; direction?: SwipeDirection; speed?: number }): SwipeGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | { fingers?: number; direction?: SwipeDirection; speed?: number } | No | 设置快滑事件参数。 &lt;br&gt; - fingers：触发快滑的最少手指数。&lt;br/&gt;默认值：1 &lt;br/&gt;取值范围：[1, 10] &lt;br&gt; - direction：触发快滑手势的滑动方向。&lt;br/&gt;默认值：SwipeDirection.All &lt;br&gt; - speed：识别快滑的最小速度。&lt;br/&gt;默认值：100VP/s &lt;br/&gt;取值范围：(0, +∞) &lt;br/&gt;**说明：** &lt;br/&gt;当滑动速度的值小于等于0时，会被转化为默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SwipeGestureInterface](arkts-arkui-swipegestureinterface-i.md) |  |

## [[Call]]

```TypeScript
(options?: SwipeGestureHandlerOptions): SwipeGestureInterface
```

设置快滑手势事件。与[SwipeGesture](arkts-arkui-swipegestureinterface-i.md))}相比，options参数新增了isFingerCountLimited，表示是否检查触摸屏幕的手指数量。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-SwipeGestureInterface-(options?: SwipeGestureHandlerOptions): SwipeGestureInterface--><!--Device-SwipeGestureInterface-(options?: SwipeGestureHandlerOptions): SwipeGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [SwipeGestureHandlerOptions](arkts-arkui-gesture-swipegesturehandleroptions-i.md) | No | 快滑事件处理器配置参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SwipeGestureInterface](arkts-arkui-swipegestureinterface-i.md) |  |

## onAction

```TypeScript
onAction(event: (event: GestureEvent) => void): SwipeGestureInterface
```

Swipe手势识别成功时触发回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SwipeGestureInterface-onAction(event: (event: GestureEvent) => void): SwipeGestureInterface--><!--Device-SwipeGestureInterface-onAction(event: (event: GestureEvent) => void): SwipeGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (event: GestureEvent) =&gt; void | Yes | 手势事件回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SwipeGestureInterface](arkts-arkui-swipegestureinterface-i.md) |  |

