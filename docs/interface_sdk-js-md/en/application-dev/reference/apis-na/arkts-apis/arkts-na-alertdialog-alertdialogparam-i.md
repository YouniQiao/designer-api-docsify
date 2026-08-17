# AlertDialogParam

Base param used for AlertDialog.show method.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface AlertDialogParam--><!--Device-unnamed-export declare interface AlertDialogParam-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alignment

```TypeScript
alignment?: DialogAlignment
```

Alignment in the vertical direction.

**Type:** [DialogAlignment](arkts-na-alertdialog-dialogalignment-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-alignment?: DialogAlignment--><!--Device-AlertDialogParam-alignment?: DialogAlignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## autoCancel

```TypeScript
autoCancel?: boolean
```

Allows users to click the mask layer to exit.

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-autoCancel?: boolean--><!--Device-AlertDialogParam-autoCancel?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

Defines the alertDialog's background blur Style

**Type:** [BlurStyle](../../apis-arkui/arkts-components/arkts-arkui-blurstyle-e.md)

**Default:** BlurStyle.COMPONENT_ULTRA_THICK

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-backgroundBlurStyle?: BlurStyle--><!--Device-AlertDialogParam-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyleOptions

```TypeScript
backgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

Defines the alertDialog's background blur style with options

**Type:** [BackgroundBlurStyleOptions](../../apis-arkui/arkts-components/arkts-arkui-backgroundblurstyleoptions-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-AlertDialogParam-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

Defines the alertDialog's background color

**Type:** [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md)

**Default:** Color.Transparent

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-backgroundColor?: ResourceColor--><!--Device-AlertDialogParam-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundEffect

```TypeScript
backgroundEffect?: BackgroundEffectOptions
```

Defines the alertDialog's background effect with options

**Type:** [BackgroundEffectOptions](../../apis-arkui/arkts-components/arkts-arkui-backgroundeffectoptions-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-backgroundEffect?: BackgroundEffectOptions--><!--Device-AlertDialogParam-backgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderColor

```TypeScript
borderColor?: ResourceColor | EdgeColors | LocalizedEdgeColors
```

Defines the alertDialog's border color.

**Type:** [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| [EdgeColors](../../apis-arkui/arkts-apis/arkts-arkui-edgecolors-t.md) \| [LocalizedEdgeColors](../../apis-arkui/arkts-apis/arkts-arkui-localizededgecolors-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-borderColor?: ResourceColor | EdgeColors | LocalizedEdgeColors--><!--Device-AlertDialogParam-borderColor?: ResourceColor | EdgeColors | LocalizedEdgeColors-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderStyle

```TypeScript
borderStyle?: BorderStyle | EdgeStyles
```

Defines the alertDialog's border style.

**Type:** [BorderStyle](../../apis-arkui/arkts-apis/arkts-arkui-borderstyle-e.md) \| [EdgeStyles](../../apis-arkui/arkts-apis/arkts-arkui-edgestyles-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-borderStyle?: BorderStyle | EdgeStyles--><!--Device-AlertDialogParam-borderStyle?: BorderStyle | EdgeStyles-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderWidth

```TypeScript
borderWidth?: Dimension | EdgeWidths | LocalizedEdgeWidths
```

Defines the alertDialog's border width.

**Type:** [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md) \| [EdgeWidths](../../apis-arkui/arkts-apis/arkts-arkui-edgewidths-t.md) \| [LocalizedEdgeWidths](../../apis-arkui/arkts-apis/arkts-arkui-localizededgewidths-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-borderWidth?: Dimension | EdgeWidths | LocalizedEdgeWidths--><!--Device-AlertDialogParam-borderWidth?: Dimension | EdgeWidths | LocalizedEdgeWidths-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cancel

```TypeScript
cancel?: VoidCallback
```

Execute Cancel Function. Anonymous Object Rectification.

**Type:** [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-cancel?: VoidCallback--><!--Device-AlertDialogParam-cancel?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cornerRadius

```TypeScript
cornerRadius?: Dimension | BorderRadiuses | LocalizedBorderRadiuses
```

Defines the alertDialog's corner radius.

**Type:** [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md) \| [BorderRadiuses](../../apis-arkui/arkts-apis/arkts-arkui-borderradiuses-t.md) \| [LocalizedBorderRadiuses](../../apis-arkui/arkts-apis/arkts-arkui-localizedborderradiuses-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-cornerRadius?: Dimension | BorderRadiuses | LocalizedBorderRadiuses--><!--Device-AlertDialogParam-cornerRadius?: Dimension | BorderRadiuses | LocalizedBorderRadiuses-End-->

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

<!--Device-AlertDialogParam-enableHoverMode?: boolean--><!--Device-AlertDialogParam-enableHoverMode?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## gridCount

```TypeScript
gridCount?: int
```

Grid count of dialog.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-gridCount?: int--><!--Device-AlertDialogParam-gridCount?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
height?: Dimension
```

Defines the alertDialog's height.

**Type:** [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-height?: Dimension--><!--Device-AlertDialogParam-height?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hoverModeArea

```TypeScript
hoverModeArea?: HoverModeAreaType
```

Defines the alertDialog's display area in hover mode.

**Type:** [HoverModeAreaType](../../apis-arkui/arkts-components/arkts-arkui-hovermodeareatype-e.md)

**Default:** HoverModeAreaType.BOTTOM_SCREEN

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-hoverModeArea?: HoverModeAreaType--><!--Device-AlertDialogParam-hoverModeArea?: HoverModeAreaType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## immersiveMode

```TypeScript
immersiveMode?: ImmersiveMode
```

Determine the immersive mode of the dialog.

**Type:** [ImmersiveMode](../../apis-arkui/arkts-apis/arkts-arkui-promptaction-immersivemode-e.md)

**Default:** ImmersiveMode.DEFAULT

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-immersiveMode?: ImmersiveMode--><!--Device-AlertDialogParam-immersiveMode?: ImmersiveMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isModal

```TypeScript
isModal?: boolean
```

Whether it is a modal dialog

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-isModal?: boolean--><!--Device-AlertDialogParam-isModal?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelMode

```TypeScript
levelMode?: LevelMode
```

Determine the display level of the dialog.

**Type:** [LevelMode](../../apis-arkui/arkts-apis/arkts-arkui-promptaction-levelmode-e.md)

**Default:** LevelMode.OVERLAY

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-levelMode?: LevelMode--><!--Device-AlertDialogParam-levelMode?: LevelMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelOrder

```TypeScript
levelOrder?: LevelOrder
```

Determine the display order of the dialog.

**Type:** [LevelOrder](../../apis-arkui/arkts-apis/arkts-arkui-promptaction-levelorder-c.md)

**Default:** The value returns by LevelOrder.clamp(0)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-levelOrder?: LevelOrder--><!--Device-AlertDialogParam-levelOrder?: LevelOrder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelUniqueId

```TypeScript
levelUniqueId?: int
```

The uniqueId of any node in the router or navigation page.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-levelUniqueId?: int--><!--Device-AlertDialogParam-levelUniqueId?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maskRect

```TypeScript
maskRect?: Rectangle
```

Mask Region of dialog. The size cannot exceed the main window.

**Type:** [Rectangle](../../apis-arkui/arkts-components/arkts-arkui-rectangle-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-maskRect?: Rectangle--><!--Device-AlertDialogParam-maskRect?: Rectangle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## message

```TypeScript
message: ResourceStr
```

message Properties

**Type:** [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-message: ResourceStr--><!--Device-AlertDialogParam-message: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: Offset
```

Offset of the pop-up window relative to the alignment position.

**Type:** [Offset](../../apis-arkui/arkts-apis/arkts-arkui-offset-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-offset?: Offset--><!--Device-AlertDialogParam-offset?: Offset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidAppear

```TypeScript
onDidAppear?: VoidCallback
```

Callback function when the dialog appears.

**Type:** [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-onDidAppear?: VoidCallback--><!--Device-AlertDialogParam-onDidAppear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidDisappear

```TypeScript
onDidDisappear?: VoidCallback
```

Callback function when the dialog disappears.

**Type:** [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-onDidDisappear?: VoidCallback--><!--Device-AlertDialogParam-onDidDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillAppear

```TypeScript
onWillAppear?: VoidCallback
```

Callback function before the dialog openAnimation starts.

**Type:** [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-onWillAppear?: VoidCallback--><!--Device-AlertDialogParam-onWillAppear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDisappear

```TypeScript
onWillDisappear?: VoidCallback
```

Callback function before the dialog closeAnimation starts.

**Type:** [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-onWillDisappear?: VoidCallback--><!--Device-AlertDialogParam-onWillDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDismiss

```TypeScript
onWillDismiss?: Callback<DismissDialogAction>
```

Callback function when the dialog interactive dismiss

**Type:** [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[DismissDialogAction](arkts-na-actionsheet-dismissdialogaction-i.md)&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-onWillDismiss?: Callback<DismissDialogAction>--><!--Device-AlertDialogParam-onWillDismiss?: Callback<DismissDialogAction>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: ShadowOptions | ShadowStyle
```

Defines the alertDialog's shadow.

**Type:** [ShadowOptions](../../apis-arkui/arkts-components/arkts-arkui-shadowoptions-i.md) \| [ShadowStyle](../../apis-arkui/arkts-components/arkts-arkui-shadowstyle-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-shadow?: ShadowOptions | ShadowStyle--><!--Device-AlertDialogParam-shadow?: ShadowOptions | ShadowStyle-End-->

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

<!--Device-AlertDialogParam-showInSubWindow?: boolean--><!--Device-AlertDialogParam-showInSubWindow?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## subtitle

```TypeScript
subtitle?: ResourceStr
```

Subtitle Properties

**Type:** [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-subtitle?: ResourceStr--><!--Device-AlertDialogParam-subtitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: SystemUiMaterial
```

Set system-styled materials for dialog. Different materials have different effects, which can influence backgroundColor, border, shadow, and other visual attributes of dialog. Device Behavior Differences:The effect of same material may vary across different devices depending on their computing power.

**Type:** [SystemUiMaterial](../../apis-arkui/arkts-components/arkts-arkui-systemuimaterial-t-sys.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-systemMaterial?: SystemUiMaterial--><!--Device-AlertDialogParam-systemMaterial?: SystemUiMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textStyle

```TypeScript
textStyle?: AlertDialogTextStyleOptions
```

Set the alertDialog's textStyle.

**Type:** [AlertDialogTextStyleOptions](arkts-na-alertdialog-alertdialogtextstyleoptions-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-textStyle?: AlertDialogTextStyleOptions--><!--Device-AlertDialogParam-textStyle?: AlertDialogTextStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title?: ResourceStr
```

Title Properties

**Type:** [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-title?: ResourceStr--><!--Device-AlertDialogParam-title?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## transition

```TypeScript
transition?: TransitionEffect
```

Transition parameters of opening/closing AlertDialog.

**Type:** [TransitionEffect](../../apis-arkui/arkts-components/arkts-arkui-transitioneffect-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-transition?: TransitionEffect--><!--Device-AlertDialogParam-transition?: TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: Dimension
```

Defines the alertDialog's width.

**Type:** [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParam-width?: Dimension--><!--Device-AlertDialogParam-width?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

