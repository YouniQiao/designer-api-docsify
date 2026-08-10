# RadialGradientOptions

径向渐变参数。

> **说明：**
> 
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

> **说明：**
> 
> colors参数的约束：
> 
> [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md/arkts-arkui-resourcecolor-t.md)表示填充的颜色，number表示指定颜色所处的位置，取值范围为[0,1.0]，0表示需要设置渐变色的容器的开始处，1.0表示容器的结尾处。想要实现多个颜色渐变
> 效果时，多个数组中number参数建议递增设置，如后一个数组number参数比前一个数组number小的话，按照等于前一个数组number的值处理。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-declare interface RadialGradientOptions--><!--Device-unnamed-declare interface RadialGradientOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## center

```TypeScript
center: [Length, Length]
```

Defines center point for radial gradient.

Anonymous Object Rectification.

**Type:** [Length, Length]

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-RadialGradientOptions-center: [Length, Length]--><!--Device-RadialGradientOptions-center: [Length, Length]-End-->

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

<!--Device-RadialGradientOptions-colors: Array<[ResourceColor, number]>--><!--Device-RadialGradientOptions-colors: Array<[ResourceColor, number]>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## radius

```TypeScript
radius: Length
```

Defines radius of the radial gradient.

Anonymous Object Rectification.

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-RadialGradientOptions-radius: Length--><!--Device-RadialGradientOptions-radius: Length-End-->

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

<!--Device-RadialGradientOptions-repeating?: boolean--><!--Device-RadialGradientOptions-repeating?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

