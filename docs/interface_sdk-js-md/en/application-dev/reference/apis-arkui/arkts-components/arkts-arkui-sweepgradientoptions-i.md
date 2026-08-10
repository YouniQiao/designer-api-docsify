# SweepGradientOptions

角度渐变参数。

> **说明：**
> 
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

> **说明：**
> 
> metricsColors参数的约束：
> 
> [ColorMetrics](../arkts-apis/arkts-arkui-graphics-colormetrics-c.md/arkts-arkui-graphics-colormetrics-c.md)表示填充的颜色，可以使用[colorWithSpace](../arkts-apis/arkts-arkui-graphics-colormetrics-c.md/arkts-arkui-graphics-colormetrics-c.md#colorwithspace)
> 方法构造指定色域属性的颜色。number表示指定颜色所处的位置，取值范围为[0, 1.0]，0表示需要设置渐变色的容器开始处，1.0表示容器的结束处。为了实现多个颜色渐变效果，多个数组中的number类型参数应递增设置。如果后一个
> 数组中的number类型参数小于前一个数组的number类型参数，将按照等于前一个数组number值处理。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-declare interface SweepGradientOptions--><!--Device-unnamed-declare interface SweepGradientOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## center

```TypeScript
center: [Length, Length]
```

Defines center point for angle gradient.

Anonymous Object Rectification.

**Type:** [Length, Length]

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-SweepGradientOptions-center: [Length, Length]--><!--Device-SweepGradientOptions-center: [Length, Length]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## colors

```TypeScript
colors: Array<[ResourceColor, number]>
```

Defines color description for gradients.

Anonymous Object Rectification.

**Type:** Array&lt;[ResourceColor, number]&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-SweepGradientOptions-colors: Array<[ResourceColor, number]>--><!--Device-SweepGradientOptions-colors: Array<[ResourceColor, number]>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## end

```TypeScript
end?: number | string
```

Defines end point of angle gradient.

Anonymous Object Rectification.

**Type:** number \| string

**Default:** 0

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-SweepGradientOptions-end?: number | string--><!--Device-SweepGradientOptions-end?: number | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## metricsColors

```TypeScript
metricsColors?: Array<[ColorMetrics, number]>
```

Defines color description in ColorMetrics format for gradients.This parameter takes precedence over colors parameter.

**Type:** Array&lt;[ColorMetrics, number]&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SweepGradientOptions-metricsColors?: Array<[ColorMetrics, number]>--><!--Device-SweepGradientOptions-metricsColors?: Array<[ColorMetrics, number]>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## repeating

```TypeScript
repeating?: boolean
```

Defines gradient colors with repeated coloring.

Anonymous Object Rectification.

**Type:** boolean

**Default:** false

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-SweepGradientOptions-repeating?: boolean--><!--Device-SweepGradientOptions-repeating?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rotation

```TypeScript
rotation?: number | string
```

Defines the rotation angle of the gradient.

Anonymous Object Rectification.

**Type:** number \| string

**Default:** 0

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-SweepGradientOptions-rotation?: number | string--><!--Device-SweepGradientOptions-rotation?: number | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## start

```TypeScript
start?: number | string
```

Defines the starting point of angle gradient.

Anonymous Object Rectification.

**Type:** number \| string

**Default:** 0

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-SweepGradientOptions-start?: number | string--><!--Device-SweepGradientOptions-start?: number | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

