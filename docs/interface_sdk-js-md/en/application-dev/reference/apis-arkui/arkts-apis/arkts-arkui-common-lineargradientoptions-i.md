# LinearGradientOptions

Defines the options of linear gradient.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface LinearGradientOptions--><!--Device-unnamed-export declare interface LinearGradientOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## angle

```TypeScript
angle?: double | string
```

Defines starting angle of linear gradient.

Anonymous Object Rectification.

**Type:** double \| string

**Default:** 180

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LinearGradientOptions-angle?: double | string--><!--Device-LinearGradientOptions-angle?: double | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## colors

```TypeScript
colors: Array<[
        ResourceColor,
        double
    ]>
```

Defines color description for gradients.

Anonymous Object Rectification.

**Type:** Array&lt;[         ResourceColor, double     ]&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LinearGradientOptions-colors: Array<[        ResourceColor,        double    ]>--><!--Device-LinearGradientOptions-colors: Array<[        ResourceColor,        double    ]>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction?: GradientDirection
```

Defines the direction of linear gradient.

Anonymous Object Rectification.

**Type:** [GradientDirection](arkts-arkui-gradientdirection-e.md)

**Default:** GradientDirection.Bottom

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

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

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LinearGradientOptions-repeating?: boolean--><!--Device-LinearGradientOptions-repeating?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

