# PanGestureOptions

定义PanGesture配置参数选项。

**起始版本：** 7

**废弃版本：** -1

<!--Device-unnamed-declare class PanGestureOptions--><!--Device-unnamed-declare class PanGestureOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value?: { fingers?: number; direction?: PanDirection; distance?: number })
```

创建滑动手势配置参数对象。通过PanGestureOptions对象接口可以动态修改滑动手势的属性，从而避免通过状态变量修改属性（状态变量修改会导致UI刷新）。

**起始版本：** 7

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PanGestureOptions-constructor(value?: { fingers?: number; direction?: PanDirection; distance?: number })--><!--Device-PanGestureOptions-constructor(value?: { fingers?: number; direction?: PanDirection; distance?: number })-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | { fingers?: number; direction?: PanDirection; distance?: number } | 否 | 滑动手势配置参数对象。 & lt;br/ & gt;fingers用于指定触发滑动的最少手指数，最小为1指， 最大取值为10指。 & lt;br/ & gt;默认值：1 & lt;br/ & gt;direction用于指定触发滑动的手 势方向，此枚举值支持逻辑与( & )和逻辑或（\ |

## getDirection

```TypeScript
getDirection(): PanDirection
```

获取滑动方向。

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-PanGestureOptions-getDirection(): PanDirection--><!--Device-PanGestureOptions-getDirection(): PanDirection-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [PanDirection](arkts-arkui-pandirection-e.md) |

## getDistance

```TypeScript
getDistance(): number
```

获取触发滑动手势事件的最小滑动距离，单位为vp。

**起始版本：** 18

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-PanGestureOptions-getDistance(): number--><!--Device-PanGestureOptions-getDistance(): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## setDirection

```TypeScript
setDirection(value: PanDirection)
```

设置滑动方向。

**起始版本：** 7

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PanGestureOptions-setDirection(value: PanDirection)--><!--Device-PanGestureOptions-setDirection(value: PanDirection)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [PanDirection](arkts-arkui-pandirection-e.md) | 是 | 用于指定触发滑动的手势方向，此枚举值支持逻辑与( & )和逻辑或（\ |

## setDistance

```TypeScript
setDistance(value: number)
```

设置触发滑动手势事件的最小滑动距离，单位为vp。距离值不宜设置过大，避免因滑动脱手、响应时延过大等问题导致性能劣化，最佳实践请参考： [减小拖动识别距离](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-latency-optimization-cases#section1116134115286)。

**起始版本：** 7

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PanGestureOptions-setDistance(value: number)--><!--Device-PanGestureOptions-setDistance(value: number)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## setFingers

```TypeScript
setFingers(value: number)
```

设置触发滑动的最少手指数。

**起始版本：** 7

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PanGestureOptions-setFingers(value: number)--><!--Device-PanGestureOptions-setFingers(value: number)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
