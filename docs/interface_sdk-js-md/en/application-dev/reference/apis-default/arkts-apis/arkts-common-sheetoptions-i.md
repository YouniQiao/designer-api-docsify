# SheetOptions

Component sheet options

@extends BindOptions

**Inheritance/Implementation:** SheetOptions extends [BindOptions](arkts-common-bindoptions-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface SheetOptions--><!--Device-unnamed-export declare interface SheetOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## blurStyle

```TypeScript
blurStyle?: BlurStyle
```

Background blur of the sheet. By default, there is no background blur.

**Type:** [BlurStyle](arkts-common-blurstyle-e.md)

**Default:** BlurStyle.NONE

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-blurStyle?: BlurStyle--><!--Device-SheetOptions-blurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderColor

```TypeScript
borderColor?: ResourceColor | EdgeColors | LocalizedEdgeColors
```

Border color of the sheet. **borderColor** must be used with **borderWidth** in pairs. &lt;p&gt;**NOTE：**: <br>For bottom sheets, the bottom border color setting is ineffective. &lt;/p&gt;

**Type:** [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| [EdgeColors](../../apis-arkui/arkts-apis/arkts-arkui-edgecolors-t.md) \| [LocalizedEdgeColors](../../apis-arkui/arkts-apis/arkts-arkui-localizededgecolors-i.md)

**Default:** Color.Black

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-borderColor?: ResourceColor | EdgeColors | LocalizedEdgeColors--><!--Device-SheetOptions-borderColor?: ResourceColor | EdgeColors | LocalizedEdgeColors-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderStyle

```TypeScript
borderStyle?: BorderStyle | EdgeStyles
```

Defines the sheet's border style.

**Type:** [BorderStyle](../../apis-arkui/arkts-apis/arkts-arkui-borderstyle-e.md) \| [EdgeStyles](../../apis-arkui/arkts-apis/arkts-arkui-edgestyles-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-borderStyle?: BorderStyle | EdgeStyles--><!--Device-SheetOptions-borderStyle?: BorderStyle | EdgeStyles-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderWidth

```TypeScript
borderWidth?: Dimension | EdgeWidths | LocalizedEdgeWidths
```

Border width of the sheet. You can set the width for all four sides or set separate widths for individual sides. Default value: **0**. Percentage parameter method: Set the border width of the sheet as a percentage of the width of the parent element. If the left and right border widths of the sheet are greater than the width of the sheet, and the top and bottom border widths are greater than the height of the sheet, the display may not appear as expected. &lt;p&gt;**Note：**: <br>For bottom sheets, the bottom border width setting is ineffective. &lt;/p&gt;

**Type:** [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md) \| [EdgeWidths](../../apis-arkui/arkts-apis/arkts-arkui-edgewidths-t.md) \| [LocalizedEdgeWidths](../../apis-arkui/arkts-apis/arkts-arkui-localizededgewidths-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-borderWidth?: Dimension | EdgeWidths | LocalizedEdgeWidths--><!--Device-SheetOptions-borderWidth?: Dimension | EdgeWidths | LocalizedEdgeWidths-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## detentSelection

```TypeScript
detentSelection?: SheetSize | Length
```

Select a detent from detents property

**Type:** [SheetSize](arkts-common-sheetsize-e.md) \| [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md)

**Default:** detents[0]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-detentSelection?: SheetSize | Length--><!--Device-SheetOptions-detentSelection?: SheetSize | Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## detents

```TypeScript
detents?: SingleLengthDetent | DoubleLengthDetents | TripleLengthDetents
```

Defines sheet detents

**Type:** [SingleLengthDetent](arkts-singlelengthdetent-t.md) \| [DoubleLengthDetents](arkts-doublelengthdetents-t.md) \| [TripleLengthDetents](arkts-triplelengthdetents-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-detents?: SingleLengthDetent | DoubleLengthDetents | TripleLengthDetents--><!--Device-SheetOptions-detents?: SingleLengthDetent | DoubleLengthDetents | TripleLengthDetents-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dragBar

```TypeScript
dragBar?: boolean
```

Whether to display the drag bar. <br>**NOTE：**<br>By default, the drag bar is displayed only when the sheet's **detents** attribute is set to multiple heights and the settings take effect.

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-dragBar?: boolean--><!--Device-SheetOptions-dragBar?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## effectEdge

```TypeScript
effectEdge?: int
```

Sets whether the sheet edge has spring effect.

**Type:** int

**Default:** 3

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-effectEdge?: int--><!--Device-SheetOptions-effectEdge?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableFloatingDragBar

```TypeScript
enableFloatingDragBar?: boolean
```

Defines whether the sheet dragbar is floating, when it's displayed.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-enableFloatingDragBar?: boolean--><!--Device-SheetOptions-enableFloatingDragBar?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHoverMode

```TypeScript
enableHoverMode?: boolean
```

Defines whether to respond to the hover mode.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-enableHoverMode?: boolean--><!--Device-SheetOptions-enableHoverMode?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableOutsideInteractive

```TypeScript
enableOutsideInteractive?: boolean
```

Whether to allow users to interact with the page pertaining to the sheet. <br>**NOTE：**<br>The value **true** means that interactions are allowed, in which case no mask is not displayed. The value **false** means that interactions are not allowed, in which case a mask is displayed. If this parameter is not set, interactions are allowed for the popup sheet, but not for bottom and center sheets. If this parameter is set to **true**, the setting of **maskColor** does not take effect.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-enableOutsideInteractive?: boolean--><!--Device-SheetOptions-enableOutsideInteractive?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
height?: SheetSize | Length
```

Defines sheet height

**Type:** [SheetSize](arkts-common-sheetsize-e.md) \| [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md)

**Default:** Sheet.LARGE

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-height?: SheetSize | Length--><!--Device-SheetOptions-height?: SheetSize | Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hoverModeArea

```TypeScript
hoverModeArea?: HoverModeAreaType
```

Defines the sheet's display area in hover mode.

**Type:** [HoverModeAreaType](arkts-common-hovermodeareatype-e.md)

**Default:** HoverModeAreaType.BOTTOM_SCREEN

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-hoverModeArea?: HoverModeAreaType--><!--Device-SheetOptions-hoverModeArea?: HoverModeAreaType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## keyboardAvoidMode

```TypeScript
keyboardAvoidMode?: SheetKeyboardAvoidMode
```

Determine the mode of sheet how to avoid keyboard.

**Type:** [SheetKeyboardAvoidMode](arkts-common-sheetkeyboardavoidmode-e.md)

**Default:** SheetKeyboardAvoidMode.TRANSLATE_AND_SCROLL

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-keyboardAvoidMode?: SheetKeyboardAvoidMode--><!--Device-SheetOptions-keyboardAvoidMode?: SheetKeyboardAvoidMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maskColor

```TypeScript
maskColor?: ResourceColor
```

Mask color of the sheet.

**Type:** [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-maskColor?: ResourceColor--><!--Device-SheetOptions-maskColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## modalTransition

```TypeScript
modalTransition?: ModalTransition
```

Defines transition type when preferType is SheetType.CONTENT_COVER.

**Type:** [ModalTransition](arkts-common-modaltransition-e.md)

**Default:** ModalTransition.DEFAULT

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-modalTransition?: ModalTransition--><!--Device-SheetOptions-modalTransition?: ModalTransition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mode

```TypeScript
mode?: SheetMode
```

Determine the level sheet shows, whether sheet should be displayed within the page.

**Type:** [SheetMode](arkts-common-sheetmode-e.md)

**Default:** SheetMode.OVERLAY

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-mode?: SheetMode--><!--Device-SheetOptions-mode?: SheetMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDetentsDidChange

```TypeScript
onDetentsDidChange?: Callback<int>
```

Callback for changes in the detents of the sheet. &lt;p&gt;**NOTE：**: <br>For a bottom sheet, the final height is returned when there are changes in detents. <br>The return value is in px. &lt;/p&gt;

**Type:** [Callback](arkts-callback-t.md)&lt;int&gt;

**Default:** false

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-onDetentsDidChange?: Callback<int>--><!--Device-SheetOptions-onDetentsDidChange?: Callback<int>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onHeightDidChange

```TypeScript
onHeightDidChange?: Callback<int>
```

Callback for changes in the height of the sheet. &lt;p&gt;**Note：**: <br>For a bottom sheet, the height of each frame is only returned when there are changes in detents or during drag actions. <br>When the sheet is pulled up or making space for the soft keyboard, only the final height is returned. <br>For other types of sheets, the final height is only returned when the sheet is pulled up. <br>The return value is in px. &lt;p&gt;

**Type:** [Callback](arkts-callback-t.md)&lt;int&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-onHeightDidChange?: Callback<int>--><!--Device-SheetOptions-onHeightDidChange?: Callback<int>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onTypeDidChange

```TypeScript
onTypeDidChange?: Callback<SheetType>
```

Called when the sheet type changed

**Type:** [Callback](arkts-callback-t.md)&lt;[SheetType](arkts-common-sheettype-e.md)&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-onTypeDidChange?: Callback<SheetType>--><!--Device-SheetOptions-onTypeDidChange?: Callback<SheetType>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWidthDidChange

```TypeScript
onWidthDidChange?: Callback<int>
```

Called when width of the sheet changed

**Type:** [Callback](arkts-callback-t.md)&lt;int&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-onWidthDidChange?: Callback<int>--><!--Device-SheetOptions-onWidthDidChange?: Callback<int>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDismiss

```TypeScript
onWillDismiss?: Callback<DismissSheetAction>
```

Callback invoked when the user performs an interactive dismiss operation: pulling down or clicking the back button, the mask, or the close icon, to obtain the type of dismiss operation and decide whether to dismiss the sheet. &lt;p&gt;**NOTE：**: <br>If this callback is registered, the sheet is not dismissed immediately when the user performs the above operations. <br>Instead, you can use the DismissSheetAction parameter in the callback to determine the type of dismiss operation and decide whether to dismiss the sheet. <br>If this callback is not registered, the sheet is dismissed immediately when the user performs the above operations, without any additional behavior. <br>No further interception with onWillDismiss is allowed in an onWillDismiss callback. &lt;/p&gt;

**Type:** [Callback](arkts-callback-t.md)&lt;[DismissSheetAction](arkts-common-dismisssheetaction-i.md)&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-onWillDismiss?: Callback<DismissSheetAction>--><!--Device-SheetOptions-onWillDismiss?: Callback<DismissSheetAction>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillSpringBackWhenDismiss

```TypeScript
onWillSpringBackWhenDismiss?: Callback<SpringBackAction>
```

Callback invoked when the user performs a pull-down-to-dismiss gesture, to control the bounce effect. &lt;p&gt;**NOTE：**: <br>If this callback is registered along with **shouldDismiss** or **onWillDismiss** you can control whether the sheet bounces back during the pull-down-to-dismiss operation by calling **springBack** in the callback. <br>If this callback is not registered but **shouldDismiss** or **onWillDismiss** is registered, the sheet will bounce back before remaining open or being dismissed based on the callback behavior. <br>If neither this callback nor **shouldDismiss** or **onWillDismiss** is registered, the sheet is dismissed by default during the pull-down-to-dismiss operation. &lt;/p&gt;

**Type:** [Callback](arkts-callback-t.md)&lt;[SpringBackAction](arkts-common-springbackaction-i.md)&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-onWillSpringBackWhenDismiss?: Callback<SpringBackAction>--><!--Device-SheetOptions-onWillSpringBackWhenDismiss?: Callback<SpringBackAction>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## placement

```TypeScript
placement?: Placement
```

The placement of popup sheet type. Supports all positions defined in Placement.

**Type:** [Placement](../../apis-arkui/arkts-apis/arkts-arkui-placement-e.md)

**Default:** Placement.Bottom

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-placement?: Placement--><!--Device-SheetOptions-placement?: Placement-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## placementOnTarget

```TypeScript
placementOnTarget?: boolean
```

placement On target node

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-placementOnTarget?: boolean--><!--Device-SheetOptions-placementOnTarget?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## preferType

```TypeScript
preferType?: SheetType
```

Type of the sheet. <br>**NOTE：**<br>The types supported by the sheet vary by window. <br>1. Width &lt; 600 vp: bottom. <br>2. 600 vp &lt;= Width: bottom, center, and popup (default). <br>3. Width &gt;= 840 vp: bottom, center, and popup (default).

**Type:** [SheetType](arkts-common-sheettype-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-preferType?: SheetType--><!--Device-SheetOptions-preferType?: SheetType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## radius

```TypeScript
radius?: LengthMetrics | BorderRadiuses | LocalizedBorderRadiuses
```

Defines sheet radius

**Type:** [LengthMetrics](arkts-graphics-lengthmetrics-c.md) \| [BorderRadiuses](../../apis-arkui/arkts-apis/arkts-arkui-borderradiuses-t.md) \| [LocalizedBorderRadiuses](../../apis-arkui/arkts-apis/arkts-arkui-localizedborderradiuses-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-radius?: LengthMetrics | BorderRadiuses | LocalizedBorderRadiuses--><!--Device-SheetOptions-radius?: LengthMetrics | BorderRadiuses | LocalizedBorderRadiuses-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## radiusRenderStrategy

```TypeScript
radiusRenderStrategy?: RenderStrategy
```

Define strategy for drawing rounded corners. NOTE 1. **RenderStrategy.FAST**: The current component and its child components will be drawn directly onto the canvas with rounded corners applied. 2. **RenderStrategy.OFFSCREEN**: The current component and its child components will first be rendered onto an off-screen canvas, then undergo a rounded corner clipping, and finally be drawn onto the main canvas.

**Type:** [RenderStrategy](../../apis-arkui/arkts-apis/arkts-arkui-renderstrategy-e.md)

**Default:** RenderStrategy.FAST

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-radiusRenderStrategy?: RenderStrategy--><!--Device-SheetOptions-radiusRenderStrategy?: RenderStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scrollSizeMode

```TypeScript
scrollSizeMode?: ScrollSizeMode
```

Content update mode of the sheet when it is scrolled.

**Type:** [ScrollSizeMode](arkts-common-scrollsizemode-e.md)

**Default:** ScrollSizeMode.FELLOW_DETEND

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-scrollSizeMode?: ScrollSizeMode--><!--Device-SheetOptions-scrollSizeMode?: ScrollSizeMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: ShadowOptions | ShadowStyle
```

Shadow of the sheet. Default value for 2-in-1 devices: **ShadowStyle.OUTER_FLOATING_SM**.

**Type:** [ShadowOptions](arkts-common-shadowoptions-i.md) \| [ShadowStyle](arkts-common-shadowstyle-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-shadow?: ShadowOptions | ShadowStyle--><!--Device-SheetOptions-shadow?: ShadowOptions | ShadowStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shouldDismiss

```TypeScript
shouldDismiss?: (sheetDismiss: SheetDismiss) => void
```

Callback invoked when the user performs an interactive dismiss operation: pulling down or clicking the back button, the mask, or the close icon.<br>**NOTE：**<br>If this callback is registered, the sheet is not dismissed immediately when the user performs the above operations. To dismiss the sheet, you must call **shouldDismiss.dismiss()** in the callback.<br>If this callback is not registered, the sheet is dismissed immediately when the user performs the above operations, without any additional behavior.<br>It is recommended that this API be used in scenarios where a secondary confirmation is required.

**Type:** (sheetDismiss: SheetDismiss) =&gt; void

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-shouldDismiss?: (sheetDismiss: SheetDismiss) => void--><!--Device-SheetOptions-shouldDismiss?: (sheetDismiss: SheetDismiss) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showClose

```TypeScript
showClose?: boolean | Resource
```

Defines whether the close icon is displayed

**Type:** boolean \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md)

**Default:** true

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-showClose?: boolean | Resource--><!--Device-SheetOptions-showClose?: boolean | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showInSubWindow

```TypeScript
showInSubWindow?: boolean
```

Whether to display in the sub window

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-showInSubWindow?: boolean--><!--Device-SheetOptions-showInSubWindow?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: SystemUiMaterial
```

Set system-styled materials for sheet. Different materials have different effects, which can influence the backgroundColor, border, shadow, and other visual attributes of sheet.

**Type:** [SystemUiMaterial](arkts-systemuimaterial-t.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-systemMaterial?: SystemUiMaterial--><!--Device-SheetOptions-systemMaterial?: SystemUiMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title?: SheetTitleOptions | CustomBuilder
```

Title of the sheet.

**Type:** [SheetTitleOptions](arkts-common-sheettitleoptions-i.md) \| [CustomBuilder](arkts-custombuilder-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-title?: SheetTitleOptions | CustomBuilder--><!--Device-SheetOptions-title?: SheetTitleOptions | CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## uiContext

```TypeScript
uiContext?: UIContext
```

The UIContext that the sheet belongs to

**Type:** [UIContext](arkts-uicontext-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-uiContext?: UIContext--><!--Device-SheetOptions-uiContext?: UIContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: Dimension
```

Width of the sheet. Percentage parameter method: Set the width of the sheet as a percentage of the width of the parent element.

**Type:** [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-width?: Dimension--><!--Device-SheetOptions-width?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

