# TimePickerDialogOptions

Defines the TimePickerDialogOptions for Data Picker Dialog.

**Inheritance/Implementation:** TimePickerDialogOptions extends [TimePickerOptions](arkts-arkui-timepicker-timepickeroptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface TimePickerDialogOptions extends TimePickerOptions--><!--Device-unnamed-export declare interface TimePickerDialogOptions extends TimePickerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onAccept

```TypeScript
onAccept?: (value: TimePickerResult) => void
```

Called when the OK button in the dialog is clicked.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-onAccept?: (value: TimePickerResult) => void--><!--Device-TimePickerDialogOptions-onAccept?: (value: TimePickerResult) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [TimePickerResult](arkts-arkui-timepicker-timepickerresult-i.md) | Yes |  |

## onChange

```TypeScript
onChange?: (value: TimePickerResult) => void
```

This event is triggered when a TimePicker Time or time is selected in dialog.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-onChange?: (value: TimePickerResult) => void--><!--Device-TimePickerDialogOptions-onChange?: (value: TimePickerResult) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [TimePickerResult](arkts-arkui-timepicker-timepickerresult-i.md) | Yes |  |

## acceptButtonStyle

```TypeScript
acceptButtonStyle?: PickerDialogButtonStyle
```

Style of accept button.

**Type:** [PickerDialogButtonStyle](../arkts-components/arkts-arkui-pickerdialogbuttonstyle-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-acceptButtonStyle?: PickerDialogButtonStyle--><!--Device-TimePickerDialogOptions-acceptButtonStyle?: PickerDialogButtonStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alignment

```TypeScript
alignment?: DialogAlignment
```

Defines the dialog alignment of the screen.

**Type:** [DialogAlignment](arkts-arkui-dialogalignment-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-alignment?: DialogAlignment--><!--Device-TimePickerDialogOptions-alignment?: DialogAlignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

Defines the timePickerDialog's background blur Style

**Type:** [BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md)

**Default:** BlurStyle.COMPONENT_ULTRA_THICK

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-backgroundBlurStyle?: BlurStyle--><!--Device-TimePickerDialogOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyleOptions

```TypeScript
backgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

Defines the timePickerDialog's background blur style with options

**Type:** [BackgroundBlurStyleOptions](../arkts-components/arkts-arkui-backgroundblurstyleoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-TimePickerDialogOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

Defines the timePickerDialog's background color

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Default:** Color.Transparent

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-backgroundColor?: ResourceColor--><!--Device-TimePickerDialogOptions-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundEffect

```TypeScript
backgroundEffect?: BackgroundEffectOptions
```

Defines the timePickerDialog's background effect with options

**Type:** [BackgroundEffectOptions](../arkts-components/arkts-arkui-backgroundeffectoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-backgroundEffect?: BackgroundEffectOptions--><!--Device-TimePickerDialogOptions-backgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cancelButtonStyle

```TypeScript
cancelButtonStyle?: PickerDialogButtonStyle
```

Style of cancel button.

**Type:** [PickerDialogButtonStyle](../arkts-components/arkts-arkui-pickerdialogbuttonstyle-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-cancelButtonStyle?: PickerDialogButtonStyle--><!--Device-TimePickerDialogOptions-cancelButtonStyle?: PickerDialogButtonStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dateTimeOptions

```TypeScript
dateTimeOptions?: DateTimeOptions
```

Set time format

**Type:** [DateTimeOptions](../arkts-components/arkts-arkui-datetimeoptions-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-dateTimeOptions?: DateTimeOptions--><!--Device-TimePickerDialogOptions-dateTimeOptions?: DateTimeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disappearTextStyle

```TypeScript
disappearTextStyle?: PickerTextStyle
```

Text style of disappearing items

**Type:** [PickerTextStyle](../arkts-components/arkts-arkui-pickertextstyle-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-disappearTextStyle?: PickerTextStyle--><!--Device-TimePickerDialogOptions-disappearTextStyle?: PickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableCascade

```TypeScript
enableCascade?: boolean
```

Defines whether the AM/PM option is cascaded with the time in 12-hour mode.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-enableCascade?: boolean--><!--Device-TimePickerDialogOptions-enableCascade?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHapticFeedback

```TypeScript
enableHapticFeedback?: boolean
```

Enable or disable haptic feedback.

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-enableHapticFeedback?: boolean--><!--Device-TimePickerDialogOptions-enableHapticFeedback?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHoverMode

```TypeScript
enableHoverMode?: boolean
```

Defines whether to respond to the hover mode.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-enableHoverMode?: boolean--><!--Device-TimePickerDialogOptions-enableHoverMode?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hoverModeArea

```TypeScript
hoverModeArea?: HoverModeAreaType
```

Defines the dialog's display area in hover mode.

**Type:** [HoverModeAreaType](../arkts-components/arkts-arkui-hovermodeareatype-e.md)

**Default:** HoverModeAreaType.BOTTOM_SCREEN

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-hoverModeArea?: HoverModeAreaType--><!--Device-TimePickerDialogOptions-hoverModeArea?: HoverModeAreaType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maskRect

```TypeScript
maskRect?: Rectangle
```

Mask Region of dialog. The size cannot exceed the main window.

**Type:** [Rectangle](../arkts-components/arkts-arkui-rectangle-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-maskRect?: Rectangle--><!--Device-TimePickerDialogOptions-maskRect?: Rectangle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: Offset
```

Defines the dialog offset.

**Type:** [Offset](arkts-arkui-componentutils-offset-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-offset?: Offset--><!--Device-TimePickerDialogOptions-offset?: Offset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onCancel

```TypeScript
onCancel?: VoidCallback
```

Called when the Cancel button in the dialog is clicked.

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-onCancel?: VoidCallback--><!--Device-TimePickerDialogOptions-onCancel?: VoidCallback-End-->

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

<!--Device-TimePickerDialogOptions-onDidAppear?: VoidCallback--><!--Device-TimePickerDialogOptions-onDidAppear?: VoidCallback-End-->

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

<!--Device-TimePickerDialogOptions-onDidDisappear?: VoidCallback--><!--Device-TimePickerDialogOptions-onDidDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onEnterSelectedArea

```TypeScript
onEnterSelectedArea?: Callback<TimePickerResult>
```

This event is triggered when an item enters the selected area in dialog.

**Type:** [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;TimePickerResult&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-onEnterSelectedArea?: Callback<TimePickerResult>--><!--Device-TimePickerDialogOptions-onEnterSelectedArea?: Callback<TimePickerResult>-End-->

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

<!--Device-TimePickerDialogOptions-onWillAppear?: VoidCallback--><!--Device-TimePickerDialogOptions-onWillAppear?: VoidCallback-End-->

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

<!--Device-TimePickerDialogOptions-onWillDisappear?: VoidCallback--><!--Device-TimePickerDialogOptions-onWillDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedTextStyle

```TypeScript
selectedTextStyle?: PickerTextStyle
```

Text style of selected items

**Type:** [PickerTextStyle](../arkts-components/arkts-arkui-pickertextstyle-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-selectedTextStyle?: PickerTextStyle--><!--Device-TimePickerDialogOptions-selectedTextStyle?: PickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: ShadowOptions | ShadowStyle
```

Defines the dialog's shadow.

**Type:** [ShadowOptions](../arkts-components/arkts-arkui-shadowoptions-i.md) \| ShadowStyle

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-shadow?: ShadowOptions | ShadowStyle--><!--Device-TimePickerDialogOptions-shadow?: ShadowOptions | ShadowStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: SystemUiMaterial
```

Set system-styled materials for dialog. Different materials have different effects,which can influence backgroundColor, border, shadow, and other visual attributes of dialog.

**Type:** [SystemUiMaterial](../arkts-components/arkts-arkui-systemuimaterial-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-systemMaterial?: SystemUiMaterial--><!--Device-TimePickerDialogOptions-systemMaterial?: SystemUiMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textStyle

```TypeScript
textStyle?: PickerTextStyle
```

Text style of normal items

**Type:** [PickerTextStyle](../arkts-components/arkts-arkui-pickertextstyle-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-textStyle?: PickerTextStyle--><!--Device-TimePickerDialogOptions-textStyle?: PickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## useMilitaryTime

```TypeScript
useMilitaryTime?: boolean
```

Time Selector: indicates whether to display the 24-hour clock.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-useMilitaryTime?: boolean--><!--Device-TimePickerDialogOptions-useMilitaryTime?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

