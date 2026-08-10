# PanGestureOptions

定义PanGesture配置参数选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class PanGestureOptions--><!--Device-unnamed-export declare class PanGestureOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value?: PanGestureHandlerOptions)
```

创建滑动手势配置参数对象。通过PanGestureOptions对象接口可以动态修改滑动手势的属性，从而避免通过状态变量修改属性（状态变量修改会导致UI刷新）。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureOptions-constructor(value?: PanGestureHandlerOptions)--><!--Device-PanGestureOptions-constructor(value?: PanGestureHandlerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PanGestureHandlerOptions](arkts-arkui-pangesturehandleroptions-i.md) | No | 滑动手势配置参数对象。&lt;br/&gt;fingers用于指定触发滑动的最少手指数，最小为1指， 最大取值为10指。&lt;br/&gt;默认值：1 &lt;br/&gt;direction用于指定触发滑动的手势方向，此枚举值支持逻辑与(&)和逻辑或（\|）运算。&lt;br/&gt;默认值：PanDirection.All&lt;br/&gt;distance用于指定触发滑动手势事件的最小滑动距离，单位 为vp。&lt;br/&gt;手写笔默认值：8，其余输入源默认值：5&lt;br/&gt;**说明：**&lt;br/&gt;[Tabs](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)组件滑动与该滑动手势事件同时存在时，可将distance值设为1，使滑动更灵敏，避免 造成事件错乱。&lt;br/&gt;当设定的值小于0时，按默认值处理。&lt;br/&gt;建议设置合理的滑动距离，滑动距离设置过大时会导致滑动不跟手（响应时延慢）的问题。&lt;br/&gt;当组件应用了 [scale](arkts-arkui-common-commonmethod-i.md#scale)缩放变换时，distance的实际识别距离会按照scale比例进行缩放。 |

## getDirection

```TypeScript
getDirection(): PanDirection
```

获取滑动方向。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureOptions-getDirection(): PanDirection--><!--Device-PanGestureOptions-getDirection(): PanDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [PanDirection](arkts-arkui-gesture-pandirection-e.md) | 滑动方向。 |

## getDistance

```TypeScript
getDistance(): double
```

获取触发滑动手势事件的最小滑动距离，单位为vp。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureOptions-getDistance(): double--><!--Device-PanGestureOptions-getDistance(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double | 滑动手势事件的最小滑动距离。 |

## setDirection

```TypeScript
setDirection(value: PanDirection): void
```

设置滑动方向。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureOptions-setDirection(value: PanDirection): void--><!--Device-PanGestureOptions-setDirection(value: PanDirection): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PanDirection](arkts-arkui-gesture-pandirection-e.md) | Yes | 用于指定触发滑动的手势方向，此枚举值支持逻辑与(&)和逻辑或（\|）运算。&lt;br/&gt;默认值：PanDirection.All |

## setDistance

```TypeScript
setDistance(value: double): void
```

设置触发滑动手势事件的最小滑动距离，单位为vp。距离值不宜设置过大，避免因滑动脱手、响应时延过大等问题导致性能劣化，最佳实践请参考：  
[减小拖动识别距离](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-latency-optimization-cases#section1116134115286)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureOptions-setDistance(value: double): void--><!--Device-PanGestureOptions-setDistance(value: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | 触发滑动手势事件的最小滑动距离，单位为vp。&lt;br/&gt;手写笔默认值：8，其余输入源默认值：5&lt;br/&gt;**说明：**&lt;br/&gt;[Tabs组件](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md) 滑动与该滑动手势事件同时存在时，可将distance值设为1，使滑动更灵敏，避免造成事件错乱。&lt;br/&gt;当设定的值小于0时，按默认值处理。&lt;br/&gt;建议设置合理的滑动距离，滑动距离设置过大时会导致滑动不跟手 （响应时延慢）的问题。&lt;br/&gt;当组件应用了[scale](arkts-arkui-common-commonmethod-i.md#scale)缩放变换时，distance的实际识别距离会按照scale比例进行缩放。 |

## setFingers

```TypeScript
setFingers(value: int): void
```

设置触发滑动的最少手指数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureOptions-setFingers(value: int): void--><!--Device-PanGestureOptions-setFingers(value: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | 触发滑动的最少手指数，最小为1指， 最大取值为10指。&lt;br/&gt;默认值：1 |

