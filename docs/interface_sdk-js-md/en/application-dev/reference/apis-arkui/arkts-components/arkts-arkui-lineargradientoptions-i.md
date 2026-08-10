# LinearGradientOptions

线性渐变的参数。

> **说明：**
> 
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-declare interface LinearGradientOptions--><!--Device-unnamed-declare interface LinearGradientOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## angle

```TypeScript
angle?: number | string
```

Defines starting angle of linear gradient.

Anonymous Object Rectification.

**Type:** number \| string

**Default:** 180

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-LinearGradientOptions-angle?: number | string--><!--Device-LinearGradientOptions-angle?: number | string-End-->

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

<!--Device-LinearGradientOptions-colors: Array<[ResourceColor, number]>--><!--Device-LinearGradientOptions-colors: Array<[ResourceColor, number]>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction?: GradientDirection
```

Defines the direction of linear gradient.

Anonymous Object Rectification.

**Type:** [GradientDirection](../arkts-apis/arkts-arkui-gradientdirection-e.md)

**Default:** GradientDirection.Bottom

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-LinearGradientOptions-direction?: GradientDirection--><!--Device-LinearGradientOptions-direction?: GradientDirection-End-->

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

<!--Device-LinearGradientOptions-repeating?: boolean--><!--Device-LinearGradientOptions-repeating?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

