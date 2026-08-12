# ContextMenuOptions

Defines the context menu options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ContextMenuOptions--><!--Device-unnamed-export declare interface ContextMenuOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToAppear

```TypeScript
aboutToAppear?: () => void
```

Callback triggered when the menu is about to appear.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-aboutToAppear?: () => void--><!--Device-ContextMenuOptions-aboutToAppear?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToDisappear

```TypeScript
aboutToDisappear?: () => void
```

Callback triggered when the menu is about to disappear.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-aboutToDisappear?: () => void--><!--Device-ContextMenuOptions-aboutToDisappear?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onAppear

```TypeScript
onAppear?: () => void
```

Callback triggered when the menu is displayed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-onAppear?: () => void--><!--Device-ContextMenuOptions-onAppear?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDisappear

```TypeScript
onDisappear?: () => void
```

Callback function when the context menu disappear.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-onDisappear?: () => void--><!--Device-ContextMenuOptions-onDisappear?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## anchorPosition

```TypeScript
anchorPosition?: Position
```

Defines the menu position.

**Type:** [Position](arkts-arkui-position-i.md)

**Default:** { x: 0, y: 0 }

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-anchorPosition?: Position--><!--Device-ContextMenuOptions-anchorPosition?: Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arrowOffset

```TypeScript
arrowOffset?: Length
```

Offset of the arrow relative to the context menu. The offset settings take effect only when the value is valid,can be converted to a number greater than 0, and does not cause the arrow to extend beyond the safe area of the context menu.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;The safe distance of the arrow from the four sides of the menu is the sum of the menu's corner radius and half the width of the arrow. The value of placement determines whether the offset is horizontal or vertical.When the arrow is in the horizontal direction of the menu, the offset is the distance from the arrow to the leftmost arrow's safe distance. When the arrow is in the vertical direction of the menu, the offset is the distance from the arrow to the topmost arrow's safe distance. The default position where the arrow is displayed varies with the value of placement: Without any avoidance by the menu, when placement is set to Placement.Top or Placement.Bottom, the arrow is displayed horizontally and is centered by default; when placement is set to Placement.Left or Placement.Right, the arrow is displayed vertically and is centered by default; when placement is set to Placement.TopLeft or Placement.BottomLeft, the arrow is displayed horizontally by default, and the distance from the arrow to the left edge of the menu is the arrow's safe distance; when placement is set to Placement.TopRight or Placement.BottomRight, the arrow is displayed horizontally by default, and the distance from the arrow to the right edge of the menu is the arrow's safe distance; when placement is set to Placement.LeftTop or Placement.RightTop, the arrow is displayed vertically by default, and the distance from the arrow to the top edge of the menu is the arrow's safe distance; when placement is set to Placement.LeftBottom or Placement.RightBottom, the arrow is displayed vertically by default, and the distance from the arrow to the bottom edge of the menu is the arrow's safe distance.&lt;br&gt;This API is supported in bindContextMenu since API version 10 and bindMenu since API version 12.&lt;/p&gt;

**Type:** [Length](arkts-arkui-length-t.md)

**Default:** 0vp

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-arrowOffset?: Length--><!--Device-ContextMenuOptions-arrowOffset?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## availableLayoutArea

```TypeScript
availableLayoutArea?: AvailableLayoutArea
```

Defines the available layout area of preview.

**Type:** [AvailableLayoutArea](arkts-arkui-common-availablelayoutarea-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-availableLayoutArea?: AvailableLayoutArea--><!--Device-ContextMenuOptions-availableLayoutArea?: AvailableLayoutArea-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

Background blur style of the menu.

**Type:** [BlurStyle](arkts-arkui-common-blurstyle-e.md)

**Default:** BlurStyle.COMPONENT_ULTRA_THICK

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-backgroundBlurStyle?: BlurStyle--><!--Device-ContextMenuOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyleOptions

```TypeScript
backgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

Defines the menu's background blur style with options

**Type:** [BackgroundBlurStyleOptions](arkts-arkui-common-backgroundblurstyleoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-ContextMenuOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

Background color of the menu.

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Default:** Color.Transparent

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-backgroundColor?: ResourceColor--><!--Device-ContextMenuOptions-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundEffect

```TypeScript
backgroundEffect?: BackgroundEffectOptions
```

Defines the menu's background effect with options

**Type:** [BackgroundEffectOptions](arkts-arkui-common-backgroundeffectoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-backgroundEffect?: BackgroundEffectOptions--><!--Device-ContextMenuOptions-backgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderRadius

```TypeScript
borderRadius?: Length | BorderRadiuses | LocalizedBorderRadiuses
```

Border radius of the menu.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;The value can be in percentage.&lt;br&gt;If the sum of the two maximum corner radii in the horizontal direction exceeds the menu's width, or if the sum of the two maximum corner radii in the vertical direction exceeds the menu's height, the default corner radius of the menu will be used.&lt;/p&gt;

**Type:** [Length](arkts-arkui-length-t.md) \| BorderRadiuses \| [LocalizedBorderRadiuses](arkts-arkui-localizedborderradiuses-i.md)

**Default:** 8vp for 2-in-1 devices and 20vp for other devices

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-borderRadius?: Length | BorderRadiuses | LocalizedBorderRadiuses--><!--Device-ContextMenuOptions-borderRadius?: Length | BorderRadiuses | LocalizedBorderRadiuses-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## colorMode

```TypeScript
colorMode?: AnchoredColorMode
```

Define the menu theme color mode.

**Type:** [AnchoredColorMode](arkts-arkui-common-anchoredcolormode-e.md)

**Default:** AnchoredColorMode.FOLLOW_TARGET

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-colorMode?: AnchoredColorMode--><!--Device-ContextMenuOptions-colorMode?: AnchoredColorMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableArrow

```TypeScript
enableArrow?: boolean
```

whether show arrow belong to the menu.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;When enableArrow is true, an arrow is displayed in the position specified by placement.&lt;br&gt;If placement is not set or its value is invalid, the arrow is displayed above the target.&lt;br&gt;If the position is insufficient for holding the arrow, it is automatically adjusted.&lt;br&gt;When enableArrow is undefined, no arrow is displayed.&lt;br&gt;This API is supported in bindContextMenu since API version 10 and bindMenu since API version 12.&lt;/p&gt;

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-enableArrow?: boolean--><!--Device-ContextMenuOptions-enableArrow?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHoverMode

```TypeScript
enableHoverMode?: boolean
```

Determine if it is compatible menu's half folded.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-enableHoverMode?: boolean--><!--Device-ContextMenuOptions-enableHoverMode?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## gridStyle

```TypeScript
gridStyle?: MenuGridStyleOptions
```

Define grid style of menu. Only fixed-style menus are effective.For example, using MenuElement in bindMenu/bindContextMenu or using MenuItemOptions in MenuItem.

**Type:** [MenuGridStyleOptions](arkts-arkui-common-menugridstyleoptions-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-gridStyle?: MenuGridStyleOptions--><!--Device-ContextMenuOptions-gridStyle?: MenuGridStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hapticFeedbackMode

```TypeScript
hapticFeedbackMode?: HapticFeedbackMode
```

Defines the haptic feedback mode of menu.

**Type:** [HapticFeedbackMode](arkts-arkui-common-hapticfeedbackmode-e.md)

**Default:** HapticFeedbackMode.DISABLED

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-hapticFeedbackMode?: HapticFeedbackMode--><!--Device-ContextMenuOptions-hapticFeedbackMode?: HapticFeedbackMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## keyboardAvoidMode

```TypeScript
keyboardAvoidMode?: MenuKeyboardAvoidMode
```

Determine the mode of menu how to avoid keyboard.

No avoiding by default

**Type:** [MenuKeyboardAvoidMode](arkts-arkui-common-menukeyboardavoidmode-e.md)

**Default:** MenuKeyboardAvoidMode.NONE

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-keyboardAvoidMode?: MenuKeyboardAvoidMode--><!--Device-ContextMenuOptions-keyboardAvoidMode?: MenuKeyboardAvoidMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## layoutRegionMargin

```TypeScript
layoutRegionMargin?: Margin
```

The margin of menu's layoutRegion.

**Type:** [Margin](arkts-arkui-margin-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-layoutRegionMargin?: Margin--><!--Device-ContextMenuOptions-layoutRegionMargin?: Margin-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mask

```TypeScript
mask?: boolean | MenuMaskType
```

Whether it is a menu without mask.

**Type:** boolean \| [MenuMaskType](arkts-arkui-common-menumasktype-i.md)

**Default:** true when preview is enabled, or is false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-mask?: boolean | MenuMaskType--><!--Device-ContextMenuOptions-mask?: boolean | MenuMaskType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxHeight

```TypeScript
maxHeight?: LengthMetrics
```

Defines the max height of menu.

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-maxHeight?: LengthMetrics--><!--Device-ContextMenuOptions-maxHeight?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## minKeyboardAvoidDistance

```TypeScript
minKeyboardAvoidDistance?: LengthMetrics
```

Defines the minimum distance between menu and keyboard.

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-minKeyboardAvoidDistance?: LengthMetrics--><!--Device-ContextMenuOptions-minKeyboardAvoidDistance?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## modalMode

```TypeScript
modalMode?: ModalMode
```

Defines modal mode of menu.

**Type:** [ModalMode](arkts-arkui-common-modalmode-e.md)

**Default:** ModalMode.AUTO

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-modalMode?: ModalMode--><!--Device-ContextMenuOptions-modalMode?: ModalMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: Position
```

Offset for showing the context menu, which should not cause the menu to extend beyond the screen.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;When the menu is displayed relative to the parent component area, the width or height of the area is automatically counted into the offset based on the placement attribute of the menu. When the menu is displayed above the parent component (that is, placement is set to Placement.TopLeft, Placement.Top, or Placement.TopRight), a positive value of x indicates rightward movement relative to the parent component,and a positive value of y indicates upward movement. When the menu is displayed below the parent component(that is, placement is set to Placement.BottomLeft, Placement.Bottom, or Placement.BottomRight), a positive value of x indicates rightward movement relative to the parent component, and a positive value of y indicates downward movement. When the menu is displayed on the left of the parent component (that is, placement is set to Placement.LeftTop, Placement.Left, or Placement.LeftBottom), a positive value of x indicates leftward movement relative to the parent component, and a positive value of y indicates downward movement. When the menu is displayed on the right of the parent component (that is, placement is set to Placement.RightTop,Placement.Right, or Placement.RightBottom), a positive value of x indicates rightward movement relative to the parent component, and a positive value of y indicates downward movement. If the display position of the menu is adjusted (different from the main direction of the initial placement value), the offset value is invalid.&lt;/p&gt;

**Type:** [Position](arkts-arkui-position-i.md)

**Default:** {x:0,y:0} - Percentage values are not supported.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-offset?: Position--><!--Device-ContextMenuOptions-offset?: Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidAppear

```TypeScript
onDidAppear?: VoidCallback
```

Callback function when the menu appears.

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-onDidAppear?: VoidCallback--><!--Device-ContextMenuOptions-onDidAppear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidDisappear

```TypeScript
onDidDisappear?: VoidCallback
```

Callback function when the menu disappears.

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-onDidDisappear?: VoidCallback--><!--Device-ContextMenuOptions-onDidDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillAppear

```TypeScript
onWillAppear?: VoidCallback
```

Callback function before the menu openAnimation starts.

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-onWillAppear?: VoidCallback--><!--Device-ContextMenuOptions-onWillAppear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDisappear

```TypeScript
onWillDisappear?: VoidCallback
```

Callback function before the menu closeAnimation starts.

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-onWillDisappear?: VoidCallback--><!--Device-ContextMenuOptions-onWillDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## outlineColor

```TypeScript
outlineColor?: ResourceColor | EdgeColors
```

The color of menu's outer border.

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md) \| [EdgeColors](arkts-arkui-units-edgecolors-i.md)

**Default:** '#19ffffff'

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-outlineColor?: ResourceColor | EdgeColors--><!--Device-ContextMenuOptions-outlineColor?: ResourceColor | EdgeColors-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## outlineWidth

```TypeScript
outlineWidth?: Dimension | EdgeOutlineWidths
```

The width of menu's outer border.If outline effects are required, outlineWidth is required.

**Type:** [Dimension](arkts-arkui-dimension-t.md) \| [EdgeOutlineWidths](arkts-arkui-units-edgeoutlinewidths-i.md)

**Default:** 0vp - Percentage values are not supported.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-outlineWidth?: Dimension | EdgeOutlineWidths--><!--Device-ContextMenuOptions-outlineWidth?: Dimension | EdgeOutlineWidths-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## placement

```TypeScript
placement?: Placement
```

Preferred position of the context menu. If the set position is insufficient for holding the component, it will be automatically adjusted.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;If a menu is displayed by pressing and holding or right-clicking, the menu is displayed at the clicked position.&lt;/p&gt;

**Type:** [Placement](arkts-arkui-placement-e.md)

**Default:** Placement.BottomLeft

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-placement?: Placement--><!--Device-ContextMenuOptions-placement?: Placement-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## preview

```TypeScript
preview?: MenuPreviewMode | CustomBuilder
```

Preview displayed when the context menu is triggered by a long-press or use the isShown variable of bindContextMenu to display the preview content style of the menu.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;This parameter has no effect when responseType is set to ResponseType.RightClick.&lt;br&gt;If preview is set to MenuPreviewMode.NONE or is not set, the enableArrow parameter is effective.&lt;br&gt;If preview is set to MenuPreviewMode.IMAGE or CustomBuilder, no arrow will be displayed even when enableArrow is true.&lt;/p&gt;

**Type:** [MenuPreviewMode](arkts-arkui-common-menupreviewmode-e.md) \| [CustomBuilder](arkts-arkui-custombuilder-t.md)

**Default:** MenuPreviewMode.NONE

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-preview?: MenuPreviewMode | CustomBuilder--><!--Device-ContextMenuOptions-preview?: MenuPreviewMode | CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## previewAnimationOptions

```TypeScript
previewAnimationOptions?: ContextMenuAnimationOptions
```

The preview animator options.

**Type:** [ContextMenuAnimationOptions](arkts-arkui-common-contextmenuanimationoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-previewAnimationOptions?: ContextMenuAnimationOptions--><!--Device-ContextMenuOptions-previewAnimationOptions?: ContextMenuAnimationOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## previewBorderRadius

```TypeScript
previewBorderRadius?: BorderRadiusType
```

Defines the border radius for preview of menu.

**Type:** [BorderRadiusType](arkts-arkui-borderradiustype-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-previewBorderRadius?: BorderRadiusType--><!--Device-ContextMenuOptions-previewBorderRadius?: BorderRadiusType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## previewScaleMode

```TypeScript
previewScaleMode?: PreviewScaleMode
```

Defines the scaling mode for custom preview of contextMenu.

**Type:** [PreviewScaleMode](arkts-arkui-common-previewscalemode-e.md)

**Default:** PreviewScaleMode.AUTO

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-previewScaleMode?: PreviewScaleMode--><!--Device-ContextMenuOptions-previewScaleMode?: PreviewScaleMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scrollBar

```TypeScript
scrollBar?: BarState
```

Defines the scroll bar state of menu.

**Type:** [BarState](arkts-arkui-barstate-e.md)

**Default:** BarState.Auto

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-scrollBar?: BarState--><!--Device-ContextMenuOptions-scrollBar?: BarState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: SystemUiMaterial
```

Set system-styled materials for menu. The material effect behaves differently on devices with different level of computing powers. On devices with lower computing power, it affects attributes such as the backgroundColor, borderWidth, borderColor, shadow. On devices with higher computing power, it adds a filter effect at the system material layer, which can produce an effect similar to glass.

**Type:** [SystemUiMaterial](arkts-arkui-systemuimaterial-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-systemMaterial?: SystemUiMaterial--><!--Device-ContextMenuOptions-systemMaterial?: SystemUiMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## targetSpace

```TypeScript
targetSpace?: LengthMetrics
```

Sets the space between the menu and target.When both targetSpace and offset are set, they take effect additively. It is recommended to use targetSpace to set the space between the menu and target, and use offset for additional offset.

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-targetSpace?: LengthMetrics--><!--Device-ContextMenuOptions-targetSpace?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## transition

```TypeScript
transition?: TransitionEffect
```

Defines the transition effect of menu opening and closing.

**Type:** [TransitionEffect](arkts-arkui-common-transitioneffect-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContextMenuOptions-transition?: TransitionEffect--><!--Device-ContextMenuOptions-transition?: TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

