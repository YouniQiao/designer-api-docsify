# TextPickerDialogOptions

Defines the TextPickerDialogOptions for Text Picker Dialog.

**Inheritance/Implementation:** TextPickerDialogOptions extends [TextPickerOptions](arkts-arkui-textpickeroptions-i.md#TextPickerOptions)

**Since:** 8

<!--Device-unnamed-declare interface TextPickerDialogOptions extends TextPickerOptions--><!--Device-unnamed-declare interface TextPickerDialogOptions extends TextPickerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onAccept

```TypeScript
onAccept?: (value: TextPickerResult) => void
```

Callback invoked when the OK button in the dialog box is clicked.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextPickerDialogOptions-onAccept?: (value: TextPickerResult) => void--><!--Device-TextPickerDialogOptions-onAccept?: (value: TextPickerResult) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [TextPickerResult](arkts-arkui-textpickerresult-i.md) | Yes |

## onCancel

```TypeScript
onCancel?: () => void
```

Callback invoked when the Cancel button in the dialog box is clicked.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextPickerDialogOptions-onCancel?: () => void--><!--Device-TextPickerDialogOptions-onCancel?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onChange

```TypeScript
onChange?: (value: TextPickerResult) => void
```

Callback invoked when the text picker in the dialog box snaps to the selected item.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextPickerDialogOptions-onChange?: (value: TextPickerResult) => void--><!--Device-TextPickerDialogOptions-onChange?: (value: TextPickerResult) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [TextPickerResult](arkts-arkui-textpickerresult-i.md) | Yes |

## onDidAppear

```TypeScript
onDidAppear?: () => void
```

Event callback when the dialog box appears.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;1. The normal timing sequence is as follows:onWillAppear > onDidAppear > (onAccept/onCancel/onChange/onScrollStop) > onWillDisappear > onDidDisappear.&lt;br&gt;2. You can set the callback event for changing the dialog box display effect in onDidAppear.The settings take effect next time the dialog box appears.&lt;br&gt;3. If the user closes the dialog box immediately after it appears,onWillDisappearis invoked before onDidAppear.&lt;br&gt;4. If the dialog box is closed before its entrance animation is finished, this callback is not invoked.&lt;/p&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextPickerDialogOptions-onDidAppear?: () => void--><!--Device-TextPickerDialogOptions-onDidAppear?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidDisappear

```TypeScript
onDidDisappear?: () => void
```

Event callback when the dialog box disappears.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;The normal timing sequence is as follows:&lt;br&gt;onWillAppear > onDidAppear > (onAccept/onCancel/onChange/onScrollStop) > onWillDisappear > onDidDisappear.&lt;/p&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextPickerDialogOptions-onDidDisappear?: () => void--><!--Device-TextPickerDialogOptions-onDidDisappear?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillAppear

```TypeScript
onWillAppear?: () => void
```

Event callback when the dialog box is about to appear.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;1. The normal timing sequence is as follows:&lt;br&gt;onWillAppear > onDidAppear > (onAccept/onCancel/onChange/onScrollStop) > onWillDisappear > onDidDisappear.&lt;br&gt;2. You can set the callback event for changing the dialog box display effect in onWillAppear.&lt;br&gt;the settings take effect next time the dialog box appears.&lt;/p&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextPickerDialogOptions-onWillAppear?: () => void--><!--Device-TextPickerDialogOptions-onWillAppear?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDisappear

```TypeScript
onWillDisappear?: () => void
```

Event callback when the dialog box is about to disappear.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;1. The normal timing sequence is as follows:onWillAppear > onDidAppear > (onAccept/onCancel/onChange/onScrollStop) > onWillDisappear > onDidDisappear.&lt;br&gt;2. If the user closes the dialog box immediately after it appears,onWillDisappear is invoked before onDidAppear.&lt;/p&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextPickerDialogOptions-onWillDisappear?: () => void--><!--Device-TextPickerDialogOptions-onWillDisappear?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## acceptButtonStyle

```TypeScript
acceptButtonStyle?: PickerDialogButtonStyle
```

Style of accept button.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;In the acceptButtonStyle and cancelButtonStyle configurations,&lt;br&gt;only one primary field can be set to true at most.&lt;br&gt;If both the primary fields are set to true, neither will take effect.&lt;/p&gt;

**Type:** [PickerDialogButtonStyle](arkts-arkui-pickerdialogbuttonstyle-i.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextPickerDialogOptions-acceptButtonStyle?: PickerDialogButtonStyle--><!--Device-TextPickerDialogOptions-acceptButtonStyle?: PickerDialogButtonStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alignment

```TypeScript
alignment?: DialogAlignment
```

Alignment mode of the dialog box in the vertical direction.

**Type:** [DialogAlignment](../arkts-apis/arkts-arkui-dialogalignment-e.md)

**Default:** DialogAlignment.Default [since 11]

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextPickerDialogOptions-alignment?: DialogAlignment--><!--Device-TextPickerDialogOptions-alignment?: DialogAlignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

Background blur style of the dialog box.

**Type:** BlurStyle

**Default:** BlurStyle.COMPONENT_ULTRA_THICK

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextPickerDialogOptions-backgroundBlurStyle?: BlurStyle--><!--Device-TextPickerDialogOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyleOptions

```TypeScript
backgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

Options for customizing the background blur style.

**Type:** [BackgroundBlurStyleOptions](arkts-arkui-backgroundblurstyleoptions-i.md)

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-TextPickerDialogOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-TextPickerDialogOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

Backplane color of the dialog box.

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Default:** Color.Transparent

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextPickerDialogOptions-backgroundColor?: ResourceColor--><!--Device-TextPickerDialogOptions-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundEffect

```TypeScript
backgroundEffect?: BackgroundEffectOptions
```

Options for customizing the background effect.

**Type:** [BackgroundEffectOptions](arkts-arkui-backgroundeffectoptions-i.md)

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-TextPickerDialogOptions-backgroundEffect?: BackgroundEffectOptions--><!--Device-TextPickerDialogOptions-backgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## canLoop

```TypeScript
canLoop?: boolean
```

Whether to support scroll looping.The value true means to support scroll looping, and false means the opposite.

Default Value: true

**Type:** boolean

**Default:** true

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextPickerDialogOptions-canLoop?: boolean--><!--Device-TextPickerDialogOptions-canLoop?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cancelButtonStyle

```TypeScript
cancelButtonStyle?: PickerDialogButtonStyle
```

Style of cancel button.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;In the acceptButtonStyle and cancelButtonStyle configurations,&lt;br&gt;only one primary field can be set to true at most.&lt;br&gt;If both the primary fields are set to true, neither will take effect.&lt;/p&gt;

**Type:** [PickerDialogButtonStyle](arkts-arkui-pickerdialogbuttonstyle-i.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextPickerDialogOptions-cancelButtonStyle?: PickerDialogButtonStyle--><!--Device-TextPickerDialogOptions-cancelButtonStyle?: PickerDialogButtonStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultPickerItemHeight

```TypeScript
defaultPickerItemHeight?: number | string
```

Height of the picker item.

**Type:** number \| string

**Default:** 56 vp (selected) and 36 vp (unselected) [since 11]

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextPickerDialogOptions-defaultPickerItemHeight?: number | string--><!--Device-TextPickerDialogOptions-defaultPickerItemHeight?: number | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultTextStyle

```TypeScript
defaultTextStyle?: TextPickerTextStyle
```

Style of the text items when the text style change animation during the scrolling process is disabled.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;It is effective only when disableTextStyleAnimation is true.&lt;/p&gt;

**Type:** [TextPickerTextStyle](arkts-arkui-textpickertextstyle-i.md)

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-TextPickerDialogOptions-defaultTextStyle?: TextPickerTextStyle--><!--Device-TextPickerDialogOptions-defaultTextStyle?: TextPickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disableTextStyleAnimation

```TypeScript
disableTextStyleAnimation?: boolean
```

Sets whether to enable the text style change animation during the scrolling process.true: Disable the text style change animation.false: Enable the text style change animation.

**Type:** boolean

**Default:** false

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-TextPickerDialogOptions-disableTextStyleAnimation?: boolean--><!--Device-TextPickerDialogOptions-disableTextStyleAnimation?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disappearTextStyle

```TypeScript
disappearTextStyle?: PickerTextStyle
```

Font color, font size, and font weight of the top and bottom items.

Default Value：{ color: '#ff182431', font: { size: '14fp', weight: FontWeight.Regular } }

**Type:** [PickerTextStyle](arkts-arkui-pickertextstyle-i.md)

**Default:** { color: '#ff182431', font: { size: '14fp', weight: FontWeight.Regular } }

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextPickerDialogOptions-disappearTextStyle?: PickerTextStyle--><!--Device-TextPickerDialogOptions-disappearTextStyle?: PickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHapticFeedback

```TypeScript
enableHapticFeedback?: boolean
```

Whether to enable haptic feedback.true (default): Haptic feedback is enabled.false: Haptic feedback is disabled.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;To enable haptic feedback, you must declare the ohos.permission.VIBRATE permission&lt;br&gt;under requestPermissions in the module.json5 file of the project.&lt;br&gt;"requestPermissions": [{"name": "ohos.permission.VIBRATE"}].&lt;/p&gt;

**Type:** boolean

**Default:** true

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TextPickerDialogOptions-enableHapticFeedback?: boolean--><!--Device-TextPickerDialogOptions-enableHapticFeedback?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHoverMode

```TypeScript
enableHoverMode?: boolean
```

Whether to enable the hover mode.

Default Value: false

**Type:** boolean

**Default:** false - meaning not to enable the hover mode.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-TextPickerDialogOptions-enableHoverMode?: boolean--><!--Device-TextPickerDialogOptions-enableHoverMode?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hoverModeArea

```TypeScript
hoverModeArea?: HoverModeAreaType
```

Display area of the dialog box in hover mode.

Default Value: HoverModeAreaType.BOTTOM_SCREEN

**Type:** [HoverModeAreaType](arkts-arkui-hovermodeareatype-e.md)

**Default:** HoverModeAreaType.BOTTOM_SCREEN

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-TextPickerDialogOptions-hoverModeArea?: HoverModeAreaType--><!--Device-TextPickerDialogOptions-hoverModeArea?: HoverModeAreaType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maskRect

```TypeScript
maskRect?: Rectangle
```

Mask area of the dialog box.Events outside the mask area are transparently transmitted, and events within the mask area are not.

**Type:** [Rectangle](arkts-arkui-rectangle-i.md)

**Default:** { x: 0, y: 0, width: '100%', height: '100%' } [since 11]

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextPickerDialogOptions-maskRect?: Rectangle--><!--Device-TextPickerDialogOptions-maskRect?: Rectangle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: Offset
```

Offset of the dialog box based on the alignment settings.

**Type:** Offset

**Default:** { dx: 0 , dy: 0 } [since 11]

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextPickerDialogOptions-offset?: Offset--><!--Device-TextPickerDialogOptions-offset?: Offset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onEnterSelectedArea

```TypeScript
onEnterSelectedArea?: Callback<TextPickerResult>
```

Represents the callback triggered during the scrolling of the text picker when an item enters the divider area.Compared to the onChange event, this event is triggered earlier,specifically when the scroll distance of the current column exceeds half the height of the selected item,which indicates that the item has entered the divider area.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;In scenarios where the picker contains linked columns,&lt;br&gt;the use of this callback is not recommended.&lt;br&gt;The reason is that it identifies nodes where items enter the divider area during scrolling.&lt;br&gt;However, items that change in response to the scrolling do not themselves scroll. As a result,&lt;br&gt;he callback's return values will only reflect changes for the currently scrolling column,&lt;br&gt;while other non-scrolling columns will remain unchanged.&lt;/p&gt;

**Type:** Callback&lt;[TextPickerResult](arkts-arkui-textpickerresult-i.md)&gt;

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TextPickerDialogOptions-onEnterSelectedArea?: Callback<TextPickerResult>--><!--Device-TextPickerDialogOptions-onEnterSelectedArea?: Callback<TextPickerResult>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onScrollStop

```TypeScript
onScrollStop?: Callback<TextPickerResult>
```

Callback invoked when the scrolling in the text picker of the dialog box stops.

**Type:** Callback&lt;[TextPickerResult](arkts-arkui-textpickerresult-i.md)&gt;

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-TextPickerDialogOptions-onScrollStop?: Callback<TextPickerResult>--><!--Device-TextPickerDialogOptions-onScrollStop?: Callback<TextPickerResult>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedBackgroundStyle

```TypeScript
selectedBackgroundStyle?: PickerBackgroundStyle
```

Background style of selected items.

Default Value: { color: \$r('sys.color.comp_background_tertiary'),borderRadius: \$r('sys.float.corner_radius_level12') }

**Type:** [PickerBackgroundStyle](arkts-arkui-pickerbackgroundstyle-i.md)

**Default:** { color: $r('sys.color.comp_background_tertiary'), borderRadius: $r('sys.float.corner_radius_level12') }

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextPickerDialogOptions-selectedBackgroundStyle?: PickerBackgroundStyle--><!--Device-TextPickerDialogOptions-selectedBackgroundStyle?: PickerBackgroundStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedTextStyle

```TypeScript
selectedTextStyle?: PickerTextStyle
```

Font color, font size, and font weight of the selected item.

**Type:** [PickerTextStyle](arkts-arkui-pickertextstyle-i.md)

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextPickerDialogOptions-selectedTextStyle?: PickerTextStyle--><!--Device-TextPickerDialogOptions-selectedTextStyle?: PickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: ShadowOptions | ShadowStyle
```

Shadow of the dialog box.Default value on 2-in-1 devices: ShadowStyle.OUTER_FLOATING_MD when the dialog box is focused and ShadowStyle.OUTER_FLOATING_SM otherwise.

**Type:** [ShadowOptions](arkts-arkui-shadowoptions-i.md) \| [ShadowStyle](arkts-arkui-shadowstyle-e.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextPickerDialogOptions-shadow?: ShadowOptions | ShadowStyle--><!--Device-TextPickerDialogOptions-shadow?: ShadowOptions | ShadowStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textStyle

```TypeScript
textStyle?: PickerTextStyle
```

Font color, font size, and font weight of all items except the top, bottom, and selected items.

Default Value：{ color: '#ff182431', font: { size: '16fp', weight: FontWeight.Regular } }

**Type:** [PickerTextStyle](arkts-arkui-pickertextstyle-i.md)

**Default:** { color: '#ff182431', font: { size: '16fp', weight: FontWeight.Regular } }

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextPickerDialogOptions-textStyle?: PickerTextStyle--><!--Device-TextPickerDialogOptions-textStyle?: PickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
