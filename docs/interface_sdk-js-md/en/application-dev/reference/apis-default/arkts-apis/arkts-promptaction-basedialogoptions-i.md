# BaseDialogOptions

Dialog base options

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-promptAction-export interface BaseDialogOptions--><!--Device-promptAction-export interface BaseDialogOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## alignment

```TypeScript
alignment?: DialogAlignment
```

Defines the dialog alignment of the screen.

**Type:** DialogAlignment

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-alignment?: DialogAlignment--><!--Device-BaseDialogOptions-alignment?: DialogAlignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## autoCancel

```TypeScript
autoCancel?: boolean
```

Allows users to click the mask layer to exit.

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-autoCancel?: boolean--><!--Device-BaseDialogOptions-autoCancel?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyleOptions

```TypeScript
backgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

Defines the customDialog's background blur style with options

**Type:** BackgroundBlurStyleOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-BaseDialogOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundEffect

```TypeScript
backgroundEffect?: BackgroundEffectOptions
```

Defines the customDialog's background effect with options

**Type:** BackgroundEffectOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-backgroundEffect?: BackgroundEffectOptions--><!--Device-BaseDialogOptions-backgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dialogTransition

```TypeScript
dialogTransition?: TransitionEffect
```

Dialog transition parameters of opening/closing custom dialog.

**Type:** TransitionEffect

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-dialogTransition?: TransitionEffect--><!--Device-BaseDialogOptions-dialogTransition?: TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayModeInSubWindow

```TypeScript
displayModeInSubWindow?: DialogDisplayMode
```

Defines the dialog display mode when show in subwindow.

**Type:** DialogDisplayMode

**Default:** DialogDisplayMode.SCREEN_BASED

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-displayModeInSubWindow?: DialogDisplayMode--><!--Device-BaseDialogOptions-displayModeInSubWindow?: DialogDisplayMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHoverMode

```TypeScript
enableHoverMode?: boolean
```

Defines whether to respond to the hover mode.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-enableHoverMode?: boolean--><!--Device-BaseDialogOptions-enableHoverMode?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## focusable

```TypeScript
focusable?: boolean
```

Specifies whether to get focus when the custom dialog is displayed.

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-focusable?: boolean--><!--Device-BaseDialogOptions-focusable?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hoverModeArea

```TypeScript
hoverModeArea?: HoverModeAreaType
```

Defines the dialog's display area in hover mode.

**Type:** HoverModeAreaType

**Default:** HoverModeAreaType.BOTTOM_SCREEN

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-hoverModeArea?: HoverModeAreaType--><!--Device-BaseDialogOptions-hoverModeArea?: HoverModeAreaType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## immersiveMode

```TypeScript
immersiveMode?: ImmersiveMode
```

Determine the immersive mode of the dialog.

**Type:** [ImmersiveMode](../../apis-arkui/arkts-apis/arkts-arkui-promptaction-immersivemode-e.md)

**Default:** ImmersiveMode.DEFAULT

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-immersiveMode?: ImmersiveMode--><!--Device-BaseDialogOptions-immersiveMode?: ImmersiveMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isModal

```TypeScript
isModal?: boolean
```

Whether it is a modal dialog

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-isModal?: boolean--><!--Device-BaseDialogOptions-isModal?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## keyboardAvoidDistance

```TypeScript
keyboardAvoidDistance?: LengthMetrics
```

Defines the distance between the customDialog and system keyboard.

**Type:** LengthMetrics

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-keyboardAvoidDistance?: LengthMetrics--><!--Device-BaseDialogOptions-keyboardAvoidDistance?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## keyboardAvoidMode

```TypeScript
keyboardAvoidMode?: KeyboardAvoidMode
```

Defines the customDialog's keyboard avoid mode

**Type:** KeyboardAvoidMode

**Default:** KeyboardAvoidMode.DEFAULT

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-keyboardAvoidMode?: KeyboardAvoidMode--><!--Device-BaseDialogOptions-keyboardAvoidMode?: KeyboardAvoidMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelMode

```TypeScript
levelMode?: LevelMode
```

Determine the display level of the dialog.

**Type:** [LevelMode](../../apis-arkui/arkts-apis/arkts-arkui-promptaction-levelmode-e.md)

**Default:** LevelMode.OVERLAY

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-levelMode?: LevelMode--><!--Device-BaseDialogOptions-levelMode?: LevelMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelOrder

```TypeScript
levelOrder?: LevelOrder
```

Determine the display order of the dialog.

**Type:** [LevelOrder](../../apis-arkui/arkts-apis/arkts-arkui-promptaction-levelorder-c.md)

**Default:** The value returned by LevelOrder.clamp(0)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-levelOrder?: LevelOrder--><!--Device-BaseDialogOptions-levelOrder?: LevelOrder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## levelUniqueId

```TypeScript
levelUniqueId?: int
```

The uniqueId of any node in the router or navigation page.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-levelUniqueId?: int--><!--Device-BaseDialogOptions-levelUniqueId?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maskColor

```TypeScript
maskColor?: ResourceColor
```

Defines custom dialog maskColor

**Type:** ResourceColor

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-maskColor?: ResourceColor--><!--Device-BaseDialogOptions-maskColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maskRect

```TypeScript
maskRect?: Rectangle
```

Mask Region of dialog. The size can't exceed the main window.

**Type:** Rectangle

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-maskRect?: Rectangle--><!--Device-BaseDialogOptions-maskRect?: Rectangle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maskTransition

```TypeScript
maskTransition?: TransitionEffect
```

Mask transition parameters of opening/closing custom dialog.

**Type:** TransitionEffect

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-maskTransition?: TransitionEffect--><!--Device-BaseDialogOptions-maskTransition?: TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: Offset
```

Defines the dialog offset.

**Type:** Offset

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-offset?: Offset--><!--Device-BaseDialogOptions-offset?: Offset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidAppear

```TypeScript
onDidAppear?: VoidCallback
```

Callback function when the dialog appears.

**Type:** VoidCallback

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-onDidAppear?: VoidCallback--><!--Device-BaseDialogOptions-onDidAppear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidDisappear

```TypeScript
onDidDisappear?: VoidCallback
```

Callback function when the dialog disappears.

**Type:** VoidCallback

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-onDidDisappear?: VoidCallback--><!--Device-BaseDialogOptions-onDidDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillAppear

```TypeScript
onWillAppear?: VoidCallback
```

Callback function before the dialog openAnimation starts.

**Type:** VoidCallback

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-onWillAppear?: VoidCallback--><!--Device-BaseDialogOptions-onWillAppear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDisappear

```TypeScript
onWillDisappear?: VoidCallback
```

Callback function before the dialog closeAnimation starts.

**Type:** VoidCallback

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-onWillDisappear?: VoidCallback--><!--Device-BaseDialogOptions-onWillDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDismiss

```TypeScript
onWillDismiss?: Callback<DismissDialogAction>
```

Callback function when the CustomDialog interactive dismiss.

**Type:** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[DismissDialogAction](../../apis-arkui/arkts-apis/arkts-arkui-promptaction-dismissdialogaction-i.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-onWillDismiss?: Callback<DismissDialogAction>--><!--Device-BaseDialogOptions-onWillDismiss?: Callback<DismissDialogAction>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showInSubWindow

```TypeScript
showInSubWindow?: boolean
```

Whether to display in the sub window.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-showInSubWindow?: boolean--><!--Device-BaseDialogOptions-showInSubWindow?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: uiMaterial.Material
```

Set system-styled materials for dialog. Different materials have different effects, which can influence backgroundColor, border, shadow, and other visual attributes of dialog.

Device Behavior Differences:The effect of same material may vary across different devices depending on their computing power.

**Type:** uiMaterial.Material

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-systemMaterial?: uiMaterial.Material--><!--Device-BaseDialogOptions-systemMaterial?: uiMaterial.Material-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## transition

```TypeScript
transition?: TransitionEffect
```

Transition parameters of opening/closing custom dialog.

**Type:** TransitionEffect

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseDialogOptions-transition?: TransitionEffect--><!--Device-BaseDialogOptions-transition?: TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

