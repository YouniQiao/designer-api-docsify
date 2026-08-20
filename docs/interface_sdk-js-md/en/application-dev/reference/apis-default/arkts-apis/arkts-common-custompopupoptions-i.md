# CustomPopupOptions

Defines the custom popup options.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface CustomPopupOptions--><!--Device-unnamed-export declare interface CustomPopupOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arrowHeight

```TypeScript
arrowHeight?: Dimension
```

The height of the arrow. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This parameter cannot be set in percentage. &lt;/p&gt;

**Type:** [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md)

**Default:** 8.0_vp.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomPopupOptions-arrowHeight?: Dimension--><!--Device-CustomPopupOptions-arrowHeight?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arrowOffset

```TypeScript
arrowOffset?: Length
```

The offset of the sharp corner of popup.

Offset of the popup arrow relative to the popup. When the arrow is at the top or bottom of the popup: <br>The value 0 indicates that the arrow is located on the leftmost, and any other value indicates the distance from the arrow to the leftmost; the arrow is centered by default. When the arrow is on the left or right side of the popup: The value indicates the distance from the arrow to the top; the arrow is centered by default. When the popup is displayed on either edge of the screen, it will automatically deviate leftward or rightward to stay within the safe area. When the value is 0, the arrow always points to the bound component.

**Type:** [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomPopupOptions-arrowOffset?: Length--><!--Device-CustomPopupOptions-arrowOffset?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arrowPointPosition

```TypeScript
arrowPointPosition?: ArrowPointPosition
```

Position of the popup arrow relative to its parent component. Available positions are Start, Center, and End, in both vertical and horizontal directions. All these positions are within the parent component area.

**Type:** [ArrowPointPosition](../../apis-arkui/arkts-apis/arkts-arkui-arrowpointposition-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomPopupOptions-arrowPointPosition?: ArrowPointPosition--><!--Device-CustomPopupOptions-arrowPointPosition?: ArrowPointPosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arrowWidth

```TypeScript
arrowWidth?: Dimension
```

Arrow thickness. If the arrow thickness exceeds the length of the edge minus twice the size of the popup rounded corner, the arrow is not drawn. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This parameter cannot be set in percentage. &lt;/p&gt;

**Type:** [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md)

**Default:** 16.0_vp.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomPopupOptions-arrowWidth?: Dimension--><!--Device-CustomPopupOptions-arrowWidth?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## autoCancel

```TypeScript
autoCancel?: boolean
```

Whether to automatically dismiss the popup when an operation is performed on the page. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>To enable the popup to disappear upon a click on it, place a layout component in the builder place the &lt;Popup&gt; component in the layout component, and modify the value of the bindPopup variable (show: boolean) in the onClick event of the layout component. &lt;/p&gt;

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomPopupOptions-autoCancel?: boolean--><!--Device-CustomPopupOptions-autoCancel?: boolean-End-->

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

<!--Device-CustomPopupOptions-avoidTarget?: AvoidanceMode--><!--Device-CustomPopupOptions-avoidTarget?: AvoidanceMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

Background blur style of the popup.

**Type:** [BlurStyle](arkts-common-blurstyle-e.md)

**Default:** BlurStyle.COMPONENT_ULTRA_THICK

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomPopupOptions-backgroundBlurStyle?: BlurStyle--><!--Device-CustomPopupOptions-backgroundBlurStyle?: BlurStyle-End-->

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

<!--Device-CustomPopupOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-CustomPopupOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

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

<!--Device-CustomPopupOptions-backgroundEffect?: BackgroundEffectOptions--><!--Device-CustomPopupOptions-backgroundEffect?: BackgroundEffectOptions-End-->

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

<!--Device-CustomPopupOptions-borderLinearGradient?: PopupBorderLinearGradient--><!--Device-CustomPopupOptions-borderLinearGradient?: PopupBorderLinearGradient-End-->

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

<!--Device-CustomPopupOptions-borderWidth?: Dimension--><!--Device-CustomPopupOptions-borderWidth?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## builder

```TypeScript
builder: CustomBuilder
```

Popup builder. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The popup attribute is a universal attribute. A custom popup does not support display of another popup. <br>The position attribute cannot be used for the first-layer container in the builder. <br>If the position attribute is used, the popup will not be displayed. <br>If a custom component is used in the builder, the aboutToAppear and aboutToDisappear lifecycle callbacks of the custom component are irrelevant to the visibility of the popup. As such, the lifecycle of the custom component cannot be used to determine whether the popup is displayed or not. &lt;/p&gt;

**Type:** [CustomBuilder](arkts-custombuilder-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomPopupOptions-builder: CustomBuilder--><!--Device-CustomPopupOptions-builder: CustomBuilder-End-->

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

<!--Device-CustomPopupOptions-colorMode?: AnchoredColorMode--><!--Device-CustomPopupOptions-colorMode?: AnchoredColorMode-End-->

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

<!--Device-CustomPopupOptions-enableArrow?: boolean--><!--Device-CustomPopupOptions-enableArrow?: boolean-End-->

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

<!--Device-CustomPopupOptions-enableHoverMode?: boolean--><!--Device-CustomPopupOptions-enableHoverMode?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## focusable

```TypeScript
focusable?: boolean
```

Set popup focusable

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomPopupOptions-focusable?: boolean--><!--Device-CustomPopupOptions-focusable?: boolean-End-->

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

<!--Device-CustomPopupOptions-followTransformOfTarget?: boolean--><!--Device-CustomPopupOptions-followTransformOfTarget?: boolean-End-->

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

<!--Device-CustomPopupOptions-keyboardAvoidMode?: KeyboardAvoidMode--><!--Device-CustomPopupOptions-keyboardAvoidMode?: KeyboardAvoidMode-End-->

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

<!--Device-CustomPopupOptions-levelMode?: LevelMode--><!--Device-CustomPopupOptions-levelMode?: LevelMode-End-->

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

<!--Device-CustomPopupOptions-mask?: boolean | PopupMaskType--><!--Device-CustomPopupOptions-mask?: boolean | PopupMaskType-End-->

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

<!--Device-CustomPopupOptions-offset?: Position--><!--Device-CustomPopupOptions-offset?: Position-End-->

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

<!--Device-CustomPopupOptions-onDidAppear?: VoidCallback--><!--Device-CustomPopupOptions-onDidAppear?: VoidCallback-End-->

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

<!--Device-CustomPopupOptions-onDidDisappear?: VoidCallback--><!--Device-CustomPopupOptions-onDidDisappear?: VoidCallback-End-->

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

<!--Device-CustomPopupOptions-onStateChange?: PopupStateChangeCallback--><!--Device-CustomPopupOptions-onStateChange?: PopupStateChangeCallback-End-->

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

<!--Device-CustomPopupOptions-onWillAppear?: VoidCallback--><!--Device-CustomPopupOptions-onWillAppear?: VoidCallback-End-->

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

<!--Device-CustomPopupOptions-onWillDisappear?: VoidCallback--><!--Device-CustomPopupOptions-onWillDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDismiss

```TypeScript
onWillDismiss?: boolean | Callback<DismissPopupAction>
```

Whether to perform dismissal event interception and interception callback. 1. If this parameter is set to false, the system does not respond to the dismissal event initiated by touching the Back button, swiping left or right on the screen, or pressing the Esc key; and the system dismisses the popup only when show is set to false. If this parameter is set to true, the system responds to the dismissal event as expected. 2. If this parameter is set to a function, the dismissal event is intercepted and the callback function is executed. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>No more onWillDismiss callback is allowed in an onWillDismiss callback. &lt;/p&gt;

**Type:** boolean \| [Callback](arkts-callback-t.md)&lt;[DismissPopupAction](arkts-common-dismisspopupaction-i.md)&gt;

**Default:** true

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomPopupOptions-onWillDismiss?: boolean | Callback<DismissPopupAction>--><!--Device-CustomPopupOptions-onWillDismiss?: boolean | Callback<DismissPopupAction>-End-->

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

<!--Device-CustomPopupOptions-outlineLinearGradient?: PopupBorderLinearGradient--><!--Device-CustomPopupOptions-outlineLinearGradient?: PopupBorderLinearGradient-End-->

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

<!--Device-CustomPopupOptions-outlineWidth?: Dimension--><!--Device-CustomPopupOptions-outlineWidth?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## placement

```TypeScript
placement?: Placement
```

Preferred position of the popup. If the set position is insufficient for holding the popup, it will be automatically adjusted.

**Type:** [Placement](../../apis-arkui/arkts-apis/arkts-arkui-placement-e.md)

**Default:** Placement.Bottom

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomPopupOptions-placement?: Placement--><!--Device-CustomPopupOptions-placement?: Placement-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## popupColor

```TypeScript
popupColor?: Color | string | Resource | long
```

Color of the popup. To remove the background blur, set backgroundBlurStyle to BlurStyle.NONE.

**Type:** [Color](../../apis-arkui/arkts-apis/arkts-arkui-color-e.md) \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| long

**Default:** TRANSPARENT plus COMPONENT_ULTRA_THICK

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomPopupOptions-popupColor?: Color | string | Resource | long--><!--Device-CustomPopupOptions-popupColor?: Color | string | Resource | long-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## radius

```TypeScript
radius?: Dimension
```

Rounded corner radius of the popup.

**Type:** [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md)

**Default:** 20.0_vp.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomPopupOptions-radius?: Dimension--><!--Device-CustomPopupOptions-radius?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: ShadowOptions | ShadowStyle
```

Popup shadow.

**Type:** [ShadowOptions](arkts-common-shadowoptions-i.md) \| [ShadowStyle](arkts-common-shadowstyle-e.md)

**Default:** ShadowStyle.OUTER_DEFAULT_MD.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomPopupOptions-shadow?: ShadowOptions | ShadowStyle--><!--Device-CustomPopupOptions-shadow?: ShadowOptions | ShadowStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showInSubWindow

```TypeScript
showInSubWindow?: boolean
```

Whether to display in the sub window.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomPopupOptions-showInSubWindow?: boolean--><!--Device-CustomPopupOptions-showInSubWindow?: boolean-End-->

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

<!--Device-CustomPopupOptions-systemMaterial?: SystemUiMaterial--><!--Device-CustomPopupOptions-systemMaterial?: SystemUiMaterial-End-->

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

<!--Device-CustomPopupOptions-targetSpace?: Length--><!--Device-CustomPopupOptions-targetSpace?: Length-End-->

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

<!--Device-CustomPopupOptions-transition?: TransitionEffect--><!--Device-CustomPopupOptions-transition?: TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: Dimension
```

Width of the popup.

**Type:** [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomPopupOptions-width?: Dimension--><!--Device-CustomPopupOptions-width?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

