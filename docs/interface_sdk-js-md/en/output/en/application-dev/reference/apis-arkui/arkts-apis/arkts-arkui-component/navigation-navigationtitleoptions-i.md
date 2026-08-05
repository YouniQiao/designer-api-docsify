# NavigationTitleOptions

Indicates the options of Navigation's Titlebar.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface NavigationTitleOptions--><!--Device-unnamed-export declare interface NavigationTitleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

Background blur style.

**Type:** BlurStyle

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTitleOptions-backgroundBlurStyle?: BlurStyle--><!--Device-NavigationTitleOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyleOptions

```TypeScript
backgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

Background blur style options.

**Type:** BackgroundBlurStyleOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTitleOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-NavigationTitleOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

Background color.

**Type:** ResourceColor

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTitleOptions-backgroundColor?: ResourceColor--><!--Device-NavigationTitleOptions-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundEffect

```TypeScript
backgroundEffect?: BackgroundEffectOptions
```

Background effect options.

**Type:** BackgroundEffectOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTitleOptions-backgroundEffect?: BackgroundEffectOptions--><!--Device-NavigationTitleOptions-backgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## barStyle

```TypeScript
barStyle?: BarStyle
```

Set title bar style. Default value: BarStyle.STANDARD.

**Type:** BarStyle

**Default:** BarStyle.STANDARD

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTitleOptions-barStyle?: BarStyle--><!--Device-NavigationTitleOptions-barStyle?: BarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHoverMode

```TypeScript
enableHoverMode?: boolean
```

Defines whether to respond to the hover mode. Default value: false.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTitleOptions-enableHoverMode?: boolean--><!--Device-NavigationTitleOptions-enableHoverMode?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mainTitleModifier

```TypeScript
mainTitleModifier?: TextModifier
```

Text modifier for main title.

**Type:** TextModifier

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTitleOptions-mainTitleModifier?: TextModifier--><!--Device-NavigationTitleOptions-mainTitleModifier?: TextModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## paddingEnd

```TypeScript
paddingEnd?: LengthMetrics
```

Set title bar end padding. Default value: LengthMetrics.resource(\_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_).

**Type:** LengthMetrics

**Default:** LengthMetrics.resource($r('sys.float.margin_right'))

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTitleOptions-paddingEnd?: LengthMetrics--><!--Device-NavigationTitleOptions-paddingEnd?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## paddingStart

```TypeScript
paddingStart?: LengthMetrics
```

Set title bar start padding. Default value: LengthMetrics.resource(\$r('sys.float.margin\_left')).

**Type:** LengthMetrics

**Default:** LengthMetrics.resource($r('sys.float.margin_left'))

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTitleOptions-paddingStart?: LengthMetrics--><!--Device-NavigationTitleOptions-paddingStart?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scrollEffectOptions

```TypeScript
scrollEffectOptions?: ScrollEffectOptions
```

Title scroll blur style.

**Type:** ScrollEffectOptions

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTitleOptions-scrollEffectOptions?: ScrollEffectOptions--><!--Device-NavigationTitleOptions-scrollEffectOptions?: ScrollEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## subTitleModifier

```TypeScript
subTitleModifier?: TextModifier
```

Text modifier for sub title.

**Type:** TextModifier

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTitleOptions-subTitleModifier?: TextModifier--><!--Device-NavigationTitleOptions-subTitleModifier?: TextModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: uiMaterial.Material
```

Set system-styled materials for the TitleBar. Different materials have different effects, which can influence the backgroundColor, border, shadow, and other visual attributes of the titleBar. Device Behavior Differences:The effect of the same material may vary across different devices depending on their computing power.

**Type:** uiMaterial.Material

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTitleOptions-systemMaterial?: uiMaterial.Material--><!--Device-NavigationTitleOptions-systemMaterial?: uiMaterial.Material-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

