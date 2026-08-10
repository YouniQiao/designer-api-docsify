# PanGestureInterface

滑动手势事件，当滑动的最小距离达到设定的最小值时触发滑动手势事件。

**Inheritance/Implementation:** PanGestureInterface extends [GestureInterface<PanGestureInterface>](GestureInterface<PanGestureInterface>)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-interface PanGestureInterface extends GestureInterface<PanGestureInterface>--><!--Device-unnamed-interface PanGestureInterface extends GestureInterface<PanGestureInterface>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## [[Call]]

```TypeScript
(value?: { fingers?: number; direction?: PanDirection; distance?: number } | PanGestureOptions): PanGestureInterface
```

创建滑动手势对象。继承自[GestureInterface&lt;T&gt;](arkts-arkui-gestureinterface-i.md)。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanGestureInterface-(value?: { fingers?: number; direction?: PanDirection; distance?: number } | PanGestureOptions): PanGestureInterface--><!--Device-PanGestureInterface-(value?: { fingers?: number; direction?: PanDirection; distance?: number } | PanGestureOptions): PanGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | { fingers?: number; direction?: PanDirection; distance?: number } \| PanGestureOptions | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [PanGestureInterface](arkts-arkui-pangestureinterface-i.md) |  |

## [[Call]]

```TypeScript
(options?: PanGestureHandlerOptions): PanGestureInterface
```

创建滑动手势对象。与[PanGesture](arkts-arkui-pangestureinterface-i.md) | PanGestureOptions)}相比，options参数新增了对isFingerCountLimited和distanceMap参数，分别表示是否检查触摸屏幕的手指数量以及指定不同输入源触发滑动手势事件的最小滑动距离。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-PanGestureInterface-(options?: PanGestureHandlerOptions): PanGestureInterface--><!--Device-PanGestureInterface-(options?: PanGestureHandlerOptions): PanGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PanGestureHandlerOptions](arkts-arkui-pangesturehandleroptions-i.md) | No | 滑动手势处理器配置参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PanGestureInterface](arkts-arkui-pangestureinterface-i.md) |  |

## onActionCancel

```TypeScript
onActionCancel(event: () => void): PanGestureInterface
```

设置滑动手势取消回调。滑动手势识别成功后，接收到触摸取消事件时触发回调。不返回手势事件信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanGestureInterface-onActionCancel(event: () => void): PanGestureInterface--><!--Device-PanGestureInterface-onActionCancel(event: () => void): PanGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | () =&gt; void | Yes | 滑动手势取消回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PanGestureInterface](arkts-arkui-pangestureinterface-i.md) |  |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<GestureEvent>): PanGestureInterface
```

设置滑动手势取消回调。滑动手势识别成功后，接收到触摸取消事件时触发回调。返回手势事件信息。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PanGestureInterface-onActionCancel(event: Callback<GestureEvent>): PanGestureInterface--><!--Device-PanGestureInterface-onActionCancel(event: Callback<GestureEvent>): PanGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 滑动手势取消回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PanGestureInterface](arkts-arkui-pangestureinterface-i.md) |  |

## onActionEnd

```TypeScript
onActionEnd(event: (event: GestureEvent) => void): PanGestureInterface
```

设置滑动手势结束回调。滑动手势识别成功后，手指抬起时触发回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanGestureInterface-onActionEnd(event: (event: GestureEvent) => void): PanGestureInterface--><!--Device-PanGestureInterface-onActionEnd(event: (event: GestureEvent) => void): PanGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (event: GestureEvent) =&gt; void | Yes | 滑动手势结束回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PanGestureInterface](arkts-arkui-pangestureinterface-i.md) |  |

## onActionStart

```TypeScript
onActionStart(event: (event: GestureEvent) => void): PanGestureInterface
```

设置滑动手势识别成功回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanGestureInterface-onActionStart(event: (event: GestureEvent) => void): PanGestureInterface--><!--Device-PanGestureInterface-onActionStart(event: (event: GestureEvent) => void): PanGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (event: GestureEvent) =&gt; void | Yes | 滑动手势识别成功回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PanGestureInterface](arkts-arkui-pangestureinterface-i.md) |  |

## onActionUpdate

```TypeScript
onActionUpdate(event: (event: GestureEvent) => void): PanGestureInterface
```

设置滑动手势更新回调。fingerList为多根手指时，该回调监听每次只会更新一根手指的位置信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanGestureInterface-onActionUpdate(event: (event: GestureEvent) => void): PanGestureInterface--><!--Device-PanGestureInterface-onActionUpdate(event: (event: GestureEvent) => void): PanGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (event: GestureEvent) =&gt; void | Yes | 滑动手势更新回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PanGestureInterface](arkts-arkui-pangestureinterface-i.md) |  |

