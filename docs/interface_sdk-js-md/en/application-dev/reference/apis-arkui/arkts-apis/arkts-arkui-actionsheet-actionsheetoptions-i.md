# ActionSheetOptions

The options of ActionSheet.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface ActionSheetOptions--><!--Device-unnamed-export interface ActionSheetOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alignment

```TypeScript
alignment?: DialogAlignment
```

Alignment mode of the dialog box in the vertical direction.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;If showInSubWindow is set to true in UIExtension, the dialog box is aligned with the host window based on UIExtension.&lt;/p&gt;

**Type:** [DialogAlignment](arkts-arkui-alertdialog-dialogalignment-e.md)

**Default:** DialogAlignment.Bottom

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-alignment?: DialogAlignment--><!--Device-ActionSheetOptions-alignment?: DialogAlignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## autoCancel

```TypeScript
autoCancel?: boolean
```

Whether to close the dialog box when the overlay is clicked.

**Type:** boolean

**Default:** true - The value true means to close the dialog box when the overlay is clicked, and false means the opposite.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-autoCancel?: boolean--><!--Device-ActionSheetOptions-autoCancel?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

Background blur style of the dialog box.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;Setting this parameter to BlurStyle.NONE disables the background blur. When backgroundBlurStyle is set to a value other than NONE, do not set backgroundColor. If you do, the color display may not produce the expected visual effect.&lt;/p&gt;

**Type:** [BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md)

**Default:** BlurStyle.COMPONENT_ULTRA_THICK

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-backgroundBlurStyle?: BlurStyle--><!--Device-ActionSheetOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyleOptions

```TypeScript
backgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

Defines the actionSheet's background blur style with options

**Type:** [BackgroundBlurStyleOptions](../arkts-components/arkts-arkui-backgroundblurstyleoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-ActionSheetOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

Background color of the dialog box.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;When backgroundColor is set to a non-transparent color, backgroundBlurStyle must be set to BlurStyle.NONE;otherwise, the color display may not meet the expected effect.&lt;/p&gt;

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Default:** Color.Transparent

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-backgroundColor?: ResourceColor--><!--Device-ActionSheetOptions-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundEffect

```TypeScript
backgroundEffect?: BackgroundEffectOptions
```

Defines the actionSheet's background effect with options

**Type:** [BackgroundEffectOptions](../arkts-components/arkts-arkui-backgroundeffectoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-backgroundEffect?: BackgroundEffectOptions--><!--Device-ActionSheetOptions-backgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderColor

```TypeScript
borderColor?: ResourceColor | EdgeColors | LocalizedEdgeColors
```

Border color of the dialog box.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;When borderColor is of type LocalizedEdgeColors, the layout order can be dynamically adjusted based on the user's language settings.&lt;/p&gt;

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md) \| [EdgeColors](arkts-arkui-units-edgecolors-i.md) \| [LocalizedEdgeColors](arkts-arkui-localizededgecolors-i.md)

**Default:** Color.Black - borderColor must be used with borderWidth in pairs.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-borderColor?: ResourceColor | EdgeColors | LocalizedEdgeColors--><!--Device-ActionSheetOptions-borderColor?: ResourceColor | EdgeColors | LocalizedEdgeColors-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderStyle

```TypeScript
borderStyle?: BorderStyle | EdgeStyles
```

Border style of the dialog box.

**Type:** [BorderStyle](arkts-arkui-borderstyle-e.md) \| [EdgeStyles](arkts-arkui-units-edgestyles-i.md)

**Default:** BorderStyle.Solid - borderStyle must be used with borderWidth in pairs.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-borderStyle?: BorderStyle | EdgeStyles--><!--Device-ActionSheetOptions-borderStyle?: BorderStyle | EdgeStyles-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderWidth

```TypeScript
borderWidth?: Dimension | EdgeWidths | LocalizedEdgeWidths
```

Border width of the dialog box.You can set the width for all four sides or set separate widths for individual sides.

**Type:** [Dimension](arkts-arkui-dimension-t.md) \| [EdgeWidths](arkts-arkui-units-edgewidths-i.md) \| [LocalizedEdgeWidths](arkts-arkui-localizededgewidths-i.md)

**Default:** 0 - When set to a percentage, the value defines the border width as a percentage of the parent dialog box's width. If the left and right borders are greater than its width, or the top and bottom borders are greater than its height, the dialog box may not display as expected.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-borderWidth?: Dimension | EdgeWidths | LocalizedEdgeWidths--><!--Device-ActionSheetOptions-borderWidth?: Dimension | EdgeWidths | LocalizedEdgeWidths-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cancel

```TypeScript
cancel?: VoidCallback
```

Callback invoked when the dialog box is closed after the overlay is clicked.Anonymous Object Rectification.

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-cancel?: VoidCallback--><!--Device-ActionSheetOptions-cancel?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## confirm

```TypeScript
confirm?: ActionSheetButtonOptions
```

Information about the confirm button. When the dialog box has focus and focus has not been shifted using the Tab key, the button responds to the Enter key by default, and multiple dialog boxes can gain focus consecutively to respond automatically. The default response to the Enter key does not work when defaultFocus is set to true.

**Type:** [ActionSheetButtonOptions](arkts-arkui-actionsheet-actionsheetbuttonoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-confirm?: ActionSheetButtonOptions--><!--Device-ActionSheetOptions-confirm?: ActionSheetButtonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cornerRadius

```TypeScript
cornerRadius?: Dimension | BorderRadiuses | LocalizedBorderRadiuses
```

Corner radius of the background. You can set the radius for each of the four corners individually.

**Type:** [Dimension](arkts-arkui-dimension-t.md) \| BorderRadiuses \| [LocalizedBorderRadiuses](arkts-arkui-localizedborderradiuses-i.md)

**Default:** - {topLeft:'32vp', topRight:'32vp', bottomLeft:'32vp', bottomRight:'32vp'}, The corner radius is subject to the component size, with the maximum value being half of the component width or height. If the value is negative, the default value is used. When set to a percentage, the value defines the radius as a percentage of the parent component's width or height.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-cornerRadius?: Dimension | BorderRadiuses | LocalizedBorderRadiuses--><!--Device-ActionSheetOptions-cornerRadius?: Dimension | BorderRadiuses | LocalizedBorderRadiuses-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHoverMode

```TypeScript
enableHoverMode?: boolean
```

Whether to enable the hover mode.

**Type:** boolean

**Default:** false - meaning not to enable the hover mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-enableHoverMode?: boolean--><!--Device-ActionSheetOptions-enableHoverMode?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
height?: Dimension
```

Height of the dialog box.

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Default:** - Default maximum height of the dialog box: 0.9 x (Window height – Safe area) <br>When this parameter is set to a percentage, the reference height of the dialog box is the height of the window where the dialog box is located minus the safe area. You can decrease or increase the height as needed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-height?: Dimension--><!--Device-ActionSheetOptions-height?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hoverModeArea

```TypeScript
hoverModeArea?: HoverModeAreaType
```

Display area of the dialog box in hover mode.

**Type:** [HoverModeAreaType](../arkts-components/arkts-arkui-hovermodeareatype-e.md)

**Default:** HoverModeAreaType.BOTTOM_SCREEN

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-hoverModeArea?: HoverModeAreaType--><!--Device-ActionSheetOptions-hoverModeArea?: HoverModeAreaType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## immersiveMode

```TypeScript
immersiveMode?: ImmersiveMode
```

Overlay effect for the page-level dialog box.

**Type:** [ImmersiveMode](arkts-arkui-promptaction-immersivemode-e.md)

**Default:** ImmersiveMode.DEFAULT - This parameter takes effect only when levelMode is set to LevelMode.EMBEDDED.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-immersiveMode?: ImmersiveMode--><!--Device-ActionSheetOptions-immersiveMode?: ImmersiveMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isModal

```TypeScript
isModal?: boolean
```

Whether the dialog box is a modal. A modal dialog box has a mask applied, while a non-modal dialog box does not.

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-isModal?: boolean--><!--Device-ActionSheetOptions-isModal?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelMode

```TypeScript
levelMode?: LevelMode
```

Display level of the dialog box.

**Type:** [LevelMode](arkts-arkui-promptaction-levelmode-e.md)

**Default:** LevelMode.OVERLAY - This parameter takes effect only when showInSubWindow is set to false.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-levelMode?: LevelMode--><!--Device-ActionSheetOptions-levelMode?: LevelMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelOrder

```TypeScript
levelOrder?: LevelOrder
```

Determine the display order of the dialog.

**Type:** [LevelOrder](arkts-arkui-promptaction-levelorder-c.md)

**Default:** The value returns by LevelOrder.clamp(0)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-levelOrder?: LevelOrder--><!--Device-ActionSheetOptions-levelOrder?: LevelOrder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelUniqueId

```TypeScript
levelUniqueId?: int
```

Unique ID of the node under the display level for the page-level dialog box.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;This parameter takes effect only when levelMode is set to LevelMode.EMBEDDED.&lt;/p&gt;

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-levelUniqueId?: int--><!--Device-ActionSheetOptions-levelUniqueId?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maskRect

```TypeScript
maskRect?: Rectangle
```

Mask area of the dialog box. Events outside the mask area are transparently transmitted,and events within the mask area are not.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;maskRect does not take effect when showInSubWindow is set to true.&lt;/p&gt;

**Type:** [Rectangle](../arkts-components/arkts-arkui-rectangle-i.md)

**Default:** - {x:0,y:0, width:'100%', height:'100%'}

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-maskRect?: Rectangle--><!--Device-ActionSheetOptions-maskRect?: Rectangle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## message

```TypeScript
message: string | Resource
```

Content of the dialog box.

**Type:** string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-message: string | Resource--><!--Device-ActionSheetOptions-message: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: ActionSheetOffset
```

Offset of the dialog box relative to the alignment position.&lt;br&gt;When alignment is set to Top, TopStart, or TopEnd: {dx: 0,dy: "40vp"}&lt;br&gt;When alignment is set to any other value: {dx: 0,dy: "-40vp"}

**Type:** [ActionSheetOffset](arkts-arkui-actionsheet-actionsheetoffset-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-offset?: ActionSheetOffset--><!--Device-ActionSheetOptions-offset?: ActionSheetOffset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidAppear

```TypeScript
onDidAppear?: VoidCallback
```

Callback function when the dialog appears.

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-onDidAppear?: VoidCallback--><!--Device-ActionSheetOptions-onDidAppear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidDisappear

```TypeScript
onDidDisappear?: VoidCallback
```

Callback function when the dialog disappears.

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-onDidDisappear?: VoidCallback--><!--Device-ActionSheetOptions-onDidDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillAppear

```TypeScript
onWillAppear?: VoidCallback
```

Callback function before the dialog openAnimation starts.

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-onWillAppear?: VoidCallback--><!--Device-ActionSheetOptions-onWillAppear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDisappear

```TypeScript
onWillDisappear?: VoidCallback
```

Callback function before the dialog closeAnimation starts.

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-onWillDisappear?: VoidCallback--><!--Device-ActionSheetOptions-onWillDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDismiss

```TypeScript
onWillDismiss?: Callback<DismissDialogAction>
```

Callback for interactive closure of the dialog box.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:1. If this callback is registered, the dialog box will not be closed immediately after the user touches the mask or the Back button, presses the Esc key, or swipes left or right on the screen. The reason parameter in the callback is used to determine whether the dialog box can be closed. The reason returned by the component does not support the value CLOSE_BUTTON.2. In the onWillDismiss callback, another onWillDismiss callback is not allowed.&lt;/p&gt;

**Type:** [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[DismissDialogAction](arkts-arkui-actionsheet-dismissdialogaction-i.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-onWillDismiss?: Callback<DismissDialogAction>--><!--Device-ActionSheetOptions-onWillDismiss?: Callback<DismissDialogAction>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: ShadowOptions | ShadowStyle
```

Shadow of the dialog box.

**Type:** [ShadowOptions](../arkts-components/arkts-arkui-shadowoptions-i.md) \| [ShadowStyle](../arkts-components/arkts-arkui-shadowstyle-e.md)

**Default:** - Default value on 2-in-1 devices: ShadowStyle.OUTER_FLOATING_MD when the dialog box is focused and ShadowStyle.OUTER_FLOATING_SM otherwise.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-shadow?: ShadowOptions | ShadowStyle--><!--Device-ActionSheetOptions-shadow?: ShadowOptions | ShadowStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## sheets

```TypeScript
sheets: Array<SheetInfo>
```

Options in the dialog box. Each option supports the image, text, and callback.

**Type:** Array&lt;[SheetInfo](arkts-arkui-actionsheet-sheetinfo-i.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-sheets: Array<SheetInfo>--><!--Device-ActionSheetOptions-sheets: Array<SheetInfo>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showInSubWindow

```TypeScript
showInSubWindow?: boolean
```

Whether to show the dialog box in a subwindow when the dialog box needs to be displayed outside the main window.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;A dialog box whose showInSubWindow attribute is true cannot trigger the display of another dialog box whose showInSubWindow attribute is also true.&lt;/p&gt;

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-showInSubWindow?: boolean--><!--Device-ActionSheetOptions-showInSubWindow?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## subtitle

```TypeScript
subtitle?: ResourceStr
```

Subtitle of the dialog box.

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-subtitle?: ResourceStr--><!--Device-ActionSheetOptions-subtitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: SystemUiMaterial
```

Set system-styled materials for dialog. Different materials have different effects, which can influence backgroundColor, border, shadow, and other visual attributes of dialog.

Device Behavior Differences:The effect of same material may vary across different devices depending on their computing power.

**Type:** [SystemUiMaterial](../arkts-components/arkts-arkui-systemuimaterial-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-systemMaterial?: SystemUiMaterial--><!--Device-ActionSheetOptions-systemMaterial?: SystemUiMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title: string | Resource
```

Title of the dialog box.

**Type:** string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-title: string | Resource--><!--Device-ActionSheetOptions-title: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## transition

```TypeScript
transition?: TransitionEffect
```

Transition effect for the entrance and exit of the dialog box.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:1. If this parameter is not set, the default effect is used.2. Touching the Back button during the entrance animation pauses the entrance animation and starts the exit animation. The final effect is one obtained after the curves of the entrance and exit animations are combined.3. Touching the Back button during the exit animation does not affect the animation playback. Touching the Back button again closes the application.&lt;/p&gt;

**Type:** [TransitionEffect](../arkts-components/arkts-arkui-transitioneffect-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-transition?: TransitionEffect--><!--Device-ActionSheetOptions-transition?: TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: Dimension
```

Width of the dialog box.

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Default:** - Default maximum width of the dialog box: 400 vp, When this parameter is set to a percentage, the reference width of the dialog box is the width of the window where the dialog box is located. You can decrease or increase the width as needed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetOptions-width?: Dimension--><!--Device-ActionSheetOptions-width?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

