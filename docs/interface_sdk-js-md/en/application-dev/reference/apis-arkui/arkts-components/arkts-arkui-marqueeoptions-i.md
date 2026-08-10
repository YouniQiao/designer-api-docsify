# MarqueeOptions

Marquee初始化参数。

> **说明：**
> 
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-interface MarqueeOptions--><!--Device-unnamed-interface MarqueeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## delay

```TypeScript
delay?: number
```

设置两轮滚动之间的延迟时间。

默认值：0 

取值范围：[0, +∞)，设置的值小于0时等价于设置0。

单位：毫秒

**Type:** number

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-MarqueeOptions-delay?: number--><!--Device-MarqueeOptions-delay?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fromStart

```TypeScript
fromStart?: boolean
```

设置文本的滚动方向。

true：表示文本从头部位置开始正向滚动；false：表示文本反向滚动。

默认值：true

**Type:** boolean

**Default:** true [since 18]

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-MarqueeOptions-fromStart?: boolean--><!--Device-MarqueeOptions-fromStart?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## loop

```TypeScript
loop?: number
```

设置重复滚动的次数，小于等于零时无限循环。

默认值：-1

**说明：**

ArkTS卡片上该参数设置任意值都仅在可见时滚动一次。当设置为大于0的有限次数且播放完毕后，不可以通过改变start参数重置滚动次数重新开始播放。

**Type:** number

**Default:** -1 [since 18]

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-MarqueeOptions-loop?: number--><!--Device-MarqueeOptions-loop?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## spacing

```TypeScript
spacing?: LengthMetrics
```

两轮跑马灯之间的间距。如果LengthMetrics的unit值是PERCENT，当前设置不生效，按默认值处理。

默认值：跑马灯组件宽度。

**Type:** [LengthMetrics](../arkts-apis/arkts-arkui-lengthmetrics-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-MarqueeOptions-spacing?: LengthMetrics--><!--Device-MarqueeOptions-spacing?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## src

```TypeScript
src: string
```

需要滚动的文本。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-MarqueeOptions-src: string--><!--Device-MarqueeOptions-src: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## start

```TypeScript
start: boolean
```

控制跑马灯是否进入播放状态。

true：播放；false：不播放。

**说明：**

当loop参数设置为大于0的有限次数且播放完毕后，不可以通过改变start参数重置滚动次数重新开始播放。

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-MarqueeOptions-start: boolean--><!--Device-MarqueeOptions-start: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## step

```TypeScript
step?: number
```

滚动动画的文本步长。

取值范围：[0, 文本宽度]，当step大于Marquee的文本宽度时，取默认值。

默认值：6 

单位：[vp](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#基本像素单位)

**Type:** number

**Default:** 6 [since 18]

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-MarqueeOptions-step?: number--><!--Device-MarqueeOptions-step?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

