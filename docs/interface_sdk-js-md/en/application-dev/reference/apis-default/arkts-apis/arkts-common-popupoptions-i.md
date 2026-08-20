# PopupOptions

Defines the popup options.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface PopupOptions--><!--Device-unnamed-export declare interface PopupOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arrowHeight

```TypeScript
arrowHeight?: Dimension
```

The height of the arrow.

**Type:** [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md)

**Default:** 8.0_vp.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-arrowHeight?: Dimension--><!--Device-PopupOptions-arrowHeight?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arrowOffset

```TypeScript
arrowOffset?: Length
```

The offset of the sharp corner of popup.

**Type:** [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-arrowOffset?: Length--><!--Device-PopupOptions-arrowOffset?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arrowPointPosition

```TypeScript
arrowPointPosition?: ArrowPointPosition
```

The position of the sharp corner of popup.

**Type:** [ArrowPointPosition](../../apis-arkui/arkts-apis/arkts-arkui-arrowpointposition-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-arrowPointPosition?: ArrowPointPosition--><!--Device-PopupOptions-arrowPointPosition?: ArrowPointPosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arrowWidth

```TypeScript
arrowWidth?: Dimension
```

The width of the arrow.

**Type:** [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md)

**Default:** 16.0_vp.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-arrowWidth?: Dimension--><!--Device-PopupOptions-arrowWidth?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## autoCancel

```TypeScript
autoCancel?: boolean
```

Whether hide popup when click mask

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-autoCancel?: boolean--><!--Device-PopupOptions-autoCancel?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## avoidTarget

```TypeScript
avoidTarget?: AvoidanceMode
```

Determine if popup can avoid the target when the display space is insufficient.

**Type:** [AvoidanceMode](../../apis-arkui/arkts-components/arkts-arkui-avoidancemode-e.md)

**Default:** AvoidanceMode.COVER_TARGET

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-avoidTarget?: AvoidanceMode--><!--Device-PopupOptions-avoidTarget?: AvoidanceMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

Defines popup background blur Style

**Type:** [BlurStyle](arkts-common-blurstyle-e.md)

**Default:** BlurStyle.COMPONENT_ULTRA_THICK

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-backgroundBlurStyle?: BlurStyle--><!--Device-PopupOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyleOptions

```TypeScript
backgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

Defines the popup's background blur style with options

**Type:** [BackgroundBlurStyleOptions](arkts-common-backgroundblurstyleoptions-i.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-PopupOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundEffect

```TypeScript
backgroundEffect?: BackgroundEffectOptions
```

Defines the popup's background effect with options

**Type:** [BackgroundEffectOptions](arkts-common-backgroundeffectoptions-i.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-backgroundEffect?: BackgroundEffectOptions--><!--Device-PopupOptions-backgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderLinearGradient

```TypeScript
borderLinearGradient?: PopupBorderLinearGradient
```

The LinearGradient of popup's innerline.

**Type:** [PopupBorderLinearGradient](arkts-common-popupborderlineargradient-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-borderLinearGradient?: PopupBorderLinearGradient--><!--Device-PopupOptions-borderLinearGradient?: PopupBorderLinearGradient-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderWidth

```TypeScript
borderWidth?: Dimension
```

The width of popup's border.

**Type:** [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-borderWidth?: Dimension--><!--Device-PopupOptions-borderWidth?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## colorMode

```TypeScript
colorMode?: AnchoredColorMode
```

Define the popup theme color mode.

**Type:** [AnchoredColorMode](arkts-common-anchoredcolormode-e.md)

**Default:** AnchoredColorMode.FOLLOW_TARGET

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-colorMode?: AnchoredColorMode--><!--Device-PopupOptions-colorMode?: AnchoredColorMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableArrow

```TypeScript
enableArrow?: boolean
```

whether show arrow

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-enableArrow?: boolean--><!--Device-PopupOptions-enableArrow?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHoverMode

```TypeScript
enableHoverMode?: boolean
```

Determine if it is compatible popup's half folded.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-enableHoverMode?: boolean--><!--Device-PopupOptions-enableHoverMode?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## followTransformOfTarget

```TypeScript
followTransformOfTarget?: boolean
```

Determine if popup can follow the target node when it has rotation or scale.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-followTransformOfTarget?: boolean--><!--Device-PopupOptions-followTransformOfTarget?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## keyboardAvoidMode

```TypeScript
keyboardAvoidMode?: KeyboardAvoidMode
```

Define the popup avoid keyboard mode.

**Type:** [KeyboardAvoidMode](arkts-common-keyboardavoidmode-e.md)

**Default:** KeyboardAvoidMode.NONE

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-keyboardAvoidMode?: KeyboardAvoidMode--><!--Device-PopupOptions-keyboardAvoidMode?: KeyboardAvoidMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelMode

```TypeScript
levelMode?: LevelMode
```

Defines the display level of the popup.

**Type:** [LevelMode](../../apis-arkui/arkts-apis/arkts-arkui-promptaction-levelmode-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-levelMode?: LevelMode--><!--Device-PopupOptions-levelMode?: LevelMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mask

```TypeScript
mask?: boolean | PopupMaskType
```

The mask to block gesture events of popup. When mask is set false, gesture events are not blocked. When mask is set true, gesture events are blocked and mask color is transparent.

**Type:** boolean \| [PopupMaskType](arkts-common-popupmasktype-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-mask?: boolean | PopupMaskType--><!--Device-PopupOptions-mask?: boolean | PopupMaskType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## message

```TypeScript
message: string
```

Content of the popup message.

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-message: string--><!--Device-PopupOptions-message: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## messageOptions

```TypeScript
messageOptions?: PopupMessageOptions
```

Parameters of the popup message.

**Type:** [PopupMessageOptions](arkts-common-popupmessageoptions-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-messageOptions?: PopupMessageOptions--><!--Device-PopupOptions-messageOptions?: PopupMessageOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: Position
```

Sets the position offset of the popup.

**Type:** [Position](../../apis-arkui/arkts-apis/arkts-arkui-position-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-offset?: Position--><!--Device-PopupOptions-offset?: Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidAppear

```TypeScript
onDidAppear?: VoidCallback
```

Callback function when the popup appears.

**Type:** [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-onDidAppear?: VoidCallback--><!--Device-PopupOptions-onDidAppear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidDisappear

```TypeScript
onDidDisappear?: VoidCallback
```

Callback function when the popup disappears.

**Type:** [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-onDidDisappear?: VoidCallback--><!--Device-PopupOptions-onDidDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onStateChange

```TypeScript
onStateChange?: PopupStateChangeCallback
```

on State Change

**Type:** [PopupStateChangeCallback](arkts-popupstatechangecallback-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-onStateChange?: PopupStateChangeCallback--><!--Device-PopupOptions-onStateChange?: PopupStateChangeCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillAppear

```TypeScript
onWillAppear?: VoidCallback
```

Callback function before the popup openAnimation starts.

**Type:** [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-onWillAppear?: VoidCallback--><!--Device-PopupOptions-onWillAppear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDisappear

```TypeScript
onWillDisappear?: VoidCallback
```

Callback function before the popup closeAnimation starts.

**Type:** [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-onWillDisappear?: VoidCallback--><!--Device-PopupOptions-onWillDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDismiss

```TypeScript
onWillDismiss?: boolean | Callback<DismissPopupAction>
```

Callback function when the popup interactive dismiss

**Type:** boolean \| [Callback](arkts-callback-t.md)&lt;[DismissPopupAction](arkts-common-dismisspopupaction-i.md)&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-onWillDismiss?: boolean | Callback<DismissPopupAction>--><!--Device-PopupOptions-onWillDismiss?: boolean | Callback<DismissPopupAction>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## outlineLinearGradient

```TypeScript
outlineLinearGradient?: PopupBorderLinearGradient
```

The LinearGradient of popup's outline.

**Type:** [PopupBorderLinearGradient](arkts-common-popupborderlineargradient-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-outlineLinearGradient?: PopupBorderLinearGradient--><!--Device-PopupOptions-outlineLinearGradient?: PopupBorderLinearGradient-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## outlineWidth

```TypeScript
outlineWidth?: Dimension
```

The width of popup's outline.

**Type:** [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-outlineWidth?: Dimension--><!--Device-PopupOptions-outlineWidth?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## placement

```TypeScript
placement?: Placement
```

The placement of popup. Supports all positions defined in Placement.

**Type:** [Placement](../../apis-arkui/arkts-apis/arkts-arkui-placement-e.md)

**Default:** Placement.Bottom

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-placement?: Placement--><!--Device-PopupOptions-placement?: Placement-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## popupColor

```TypeScript
popupColor?: Color | string | Resource | long
```

Set the background color of the popup.

**Type:** [Color](../../apis-arkui/arkts-apis/arkts-arkui-color-e.md) \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| long

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-popupColor?: Color | string | Resource | long--><!--Device-PopupOptions-popupColor?: Color | string | Resource | long-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primaryButton

```TypeScript
primaryButton?: PopupButton
```

The first button.

**Type:** [PopupButton](arkts-common-popupbutton-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-primaryButton?: PopupButton--><!--Device-PopupOptions-primaryButton?: PopupButton-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## radius

```TypeScript
radius?: Dimension
```

The round corners of the popup.

**Type:** [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md)

**Default:** 20.0_vp.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-radius?: Dimension--><!--Device-PopupOptions-radius?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## secondaryButton

```TypeScript
secondaryButton?: PopupButton
```

The second button.

**Type:** [PopupButton](arkts-common-popupbutton-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-secondaryButton?: PopupButton--><!--Device-PopupOptions-secondaryButton?: PopupButton-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: ShadowOptions | ShadowStyle
```

The style of popup Shadow.

**Type:** [ShadowOptions](arkts-common-shadowoptions-i.md) \| [ShadowStyle](arkts-common-shadowstyle-e.md)

**Default:** ShadowStyle.OUTER_DEFAULT_MD.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-shadow?: ShadowOptions | ShadowStyle--><!--Device-PopupOptions-shadow?: ShadowOptions | ShadowStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showInSubWindow

```TypeScript
showInSubWindow?: boolean
```

Whether to display in the sub window.

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-showInSubWindow?: boolean--><!--Device-PopupOptions-showInSubWindow?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: SystemUiMaterial
```

Set system-styled materials for popup. Different materials have different effects, which can influence the backgroundColor, border, shadow, and other visual attributes of popup.

**Type:** [SystemUiMaterial](arkts-systemuimaterial-t.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-systemMaterial?: SystemUiMaterial--><!--Device-PopupOptions-systemMaterial?: SystemUiMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## targetSpace

```TypeScript
targetSpace?: Length
```

Sets the space of between the popup and target.

**Type:** [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-targetSpace?: Length--><!--Device-PopupOptions-targetSpace?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## transition

```TypeScript
transition?: TransitionEffect
```

Defines the transition effect of popup opening and closing

**Type:** [TransitionEffect](arkts-common-transitioneffect-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-transition?: TransitionEffect--><!--Device-PopupOptions-transition?: TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: Dimension
```

Set the width of the popup.

**Type:** [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PopupOptions-width?: Dimension--><!--Device-PopupOptions-width?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

