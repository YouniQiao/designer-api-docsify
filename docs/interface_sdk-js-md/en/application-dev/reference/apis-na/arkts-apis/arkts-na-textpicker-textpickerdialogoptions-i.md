# TextPickerDialogOptions

Defines the TextPickerDialogOptions for Text Picker Dialog.

**Inheritance/Implementation:** TextPickerDialogOptions extends [TextPickerOptions](arkts-na-textpicker-textpickeroptions-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface TextPickerDialogOptions--><!--Device-unnamed-export declare interface TextPickerDialogOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## acceptButtonStyle

```TypeScript
acceptButtonStyle?: PickerDialogButtonStyle
```

Style of accept button. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>In the acceptButtonStyle and cancelButtonStyle configurations, <br>only one primary field can be set to true at most. <br>If both the primary fields are set to true, neither will take effect. &lt;/p&gt;

**Type:** [PickerDialogButtonStyle](../../apis-arkui/arkts-components/arkts-arkui-pickerdialogbuttonstyle-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-acceptButtonStyle?: PickerDialogButtonStyle--><!--Device-TextPickerDialogOptions-acceptButtonStyle?: PickerDialogButtonStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alignment

```TypeScript
alignment?: DialogAlignment
```

Alignment mode of the dialog box in the vertical direction.

**Type:** [DialogAlignment](arkts-na-alertdialog-dialogalignment-e.md)

**Default:** DialogAlignment.Default

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-alignment?: DialogAlignment--><!--Device-TextPickerDialogOptions-alignment?: DialogAlignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

Background blur style of the dialog box.

**Type:** [BlurStyle](../../apis-arkui/arkts-components/arkts-arkui-blurstyle-e.md)

**Default:** BlurStyle.COMPONENT_ULTRA_THICK

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-backgroundBlurStyle?: BlurStyle--><!--Device-TextPickerDialogOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyleOptions

```TypeScript
backgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

Options for customizing the background blur style.

**Type:** [BackgroundBlurStyleOptions](../../apis-arkui/arkts-components/arkts-arkui-backgroundblurstyleoptions-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-TextPickerDialogOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

Backplane color of the dialog box.

**Type:** [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md)

**Default:** Color.Transparent

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-backgroundColor?: ResourceColor--><!--Device-TextPickerDialogOptions-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundEffect

```TypeScript
backgroundEffect?: BackgroundEffectOptions
```

Options for customizing the background effect.

**Type:** [BackgroundEffectOptions](../../apis-arkui/arkts-components/arkts-arkui-backgroundeffectoptions-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-backgroundEffect?: BackgroundEffectOptions--><!--Device-TextPickerDialogOptions-backgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## canLoop

```TypeScript
canLoop?: boolean
```

Whether to support scroll looping. The value true means to support scroll looping, and false means the opposite.

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-canLoop?: boolean--><!--Device-TextPickerDialogOptions-canLoop?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cancelButtonStyle

```TypeScript
cancelButtonStyle?: PickerDialogButtonStyle
```

Style of cancel button. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>In the acceptButtonStyle and cancelButtonStyle configurations, <br>only one primary field can be set to true at most. <br>If both the primary fields are set to true, neither will take effect. &lt;/p&gt;

**Type:** [PickerDialogButtonStyle](../../apis-arkui/arkts-components/arkts-arkui-pickerdialogbuttonstyle-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-cancelButtonStyle?: PickerDialogButtonStyle--><!--Device-TextPickerDialogOptions-cancelButtonStyle?: PickerDialogButtonStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultPickerItemHeight

```TypeScript
defaultPickerItemHeight?: double | string
```

Height of the picker item.

**Type:** double \| string

**Default:** 56 vp (selected) and 36 vp (unselected)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-defaultPickerItemHeight?: double | string--><!--Device-TextPickerDialogOptions-defaultPickerItemHeight?: double | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultTextStyle

```TypeScript
defaultTextStyle?: TextPickerTextStyle
```

Style of the text items when the text style change animation during the scrolling process is disabled. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>It is effective only when disableTextStyleAnimation is true. &lt;/p&gt;

**Type:** [TextPickerTextStyle](arkts-na-textpicker-textpickertextstyle-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-defaultTextStyle?: TextPickerTextStyle--><!--Device-TextPickerDialogOptions-defaultTextStyle?: TextPickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disableTextStyleAnimation

```TypeScript
disableTextStyleAnimation?: boolean
```

Sets whether to enable the text style change animation during the scrolling process. true: Disable the text style change animation. false: Enable the text style change animation.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-disableTextStyleAnimation?: boolean--><!--Device-TextPickerDialogOptions-disableTextStyleAnimation?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disappearTextStyle

```TypeScript
disappearTextStyle?: PickerTextStyle
```

Font color, font size, and font weight of the top and bottom items.

**Type:** [PickerTextStyle](../../apis-arkui/arkts-components/arkts-arkui-pickertextstyle-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-disappearTextStyle?: PickerTextStyle--><!--Device-TextPickerDialogOptions-disappearTextStyle?: PickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHapticFeedback

```TypeScript
enableHapticFeedback?: boolean
```

Whether to enable haptic feedback. true (default): Haptic feedback is enabled. false: Haptic feedback is disabled. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>To enable haptic feedback, you must declare the ohos.permission.VIBRATE permission <br>under requestPermissions in the module.json5 file of the project. <br>"requestPermissions": [{"name": "ohos.permission.VIBRATE"}]. &lt;/p&gt;

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-enableHapticFeedback?: boolean--><!--Device-TextPickerDialogOptions-enableHapticFeedback?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHoverMode

```TypeScript
enableHoverMode?: boolean
```

Whether to enable the hover mode.

**Type:** boolean

**Default:** false - meaning not to enable the hover mode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-enableHoverMode?: boolean--><!--Device-TextPickerDialogOptions-enableHoverMode?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hoverModeArea

```TypeScript
hoverModeArea?: HoverModeAreaType
```

Display area of the dialog box in hover mode.

**Type:** [HoverModeAreaType](../../apis-arkui/arkts-components/arkts-arkui-hovermodeareatype-e.md)

**Default:** HoverModeAreaType.BOTTOM_SCREEN

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-hoverModeArea?: HoverModeAreaType--><!--Device-TextPickerDialogOptions-hoverModeArea?: HoverModeAreaType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maskRect

```TypeScript
maskRect?: Rectangle
```

Mask area of the dialog box. Events outside the mask area are transparently transmitted, and events within the mask area are not.

**Type:** [Rectangle](../../apis-arkui/arkts-components/arkts-arkui-rectangle-i.md)

**Default:** { x: 0, y: 0, width: '100%', height: '100%' }

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-maskRect?: Rectangle--><!--Device-TextPickerDialogOptions-maskRect?: Rectangle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: Offset
```

Offset of the dialog box based on the alignment settings.

**Type:** [Offset](../../apis-arkui/arkts-apis/arkts-arkui-offset-t.md)

**Default:** { dx: 0 , dy: 0 }

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-offset?: Offset--><!--Device-TextPickerDialogOptions-offset?: Offset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onAccept

```TypeScript
onAccept?: (value: TextPickerResult) => void
```

Callback invoked when the OK button in the dialog box is clicked.

**Type:** (value: TextPickerResult) =&gt; void

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-onAccept?: (value: TextPickerResult) => void--><!--Device-TextPickerDialogOptions-onAccept?: (value: TextPickerResult) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onCancel

```TypeScript
onCancel?: () => void
```

Callback invoked when the Cancel button in the dialog box is clicked.

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-onCancel?: () => void--><!--Device-TextPickerDialogOptions-onCancel?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onChange

```TypeScript
onChange?: (value: TextPickerResult) => void
```

Callback invoked when the text picker in the dialog box snaps to the selected item.

**Type:** (value: TextPickerResult) =&gt; void

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-onChange?: (value: TextPickerResult) => void--><!--Device-TextPickerDialogOptions-onChange?: (value: TextPickerResult) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidAppear

```TypeScript
onDidAppear?: () => void
```

Event callback when the dialog box appears. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>1. The normal timing sequence is as follows: onWillAppear &gt; onDidAppear &gt; (onAccept/onCancel/onChange/onScrollStop) &gt; onWillDisappear &gt; onDidDisappear. <br>2. You can set the callback event for changing the dialog box display effect in onDidAppear. The settings take effect next time the dialog box appears. <br>3. If the user closes the dialog box immediately after it appears, onWillDisappearis invoked before onDidAppear. <br>4. If the dialog box is closed before its entrance animation is finished, this callback is not invoked. &lt;/p&gt;

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-onDidAppear?: () => void--><!--Device-TextPickerDialogOptions-onDidAppear?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidDisappear

```TypeScript
onDidDisappear?: () => void
```

Event callback when the dialog box disappears. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The normal timing sequence is as follows: <br>onWillAppear &gt; onDidAppear &gt; (onAccept/onCancel/onChange/onScrollStop) &gt; onWillDisappear &gt; onDidDisappear. &lt;/p&gt;

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-onDidDisappear?: () => void--><!--Device-TextPickerDialogOptions-onDidDisappear?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onEnterSelectedArea

```TypeScript
onEnterSelectedArea?: Callback<TextPickerResult>
```

Represents the callback triggered during the scrolling of the text picker when an item enters the divider area. Compared to the onChange event, this event is triggered earlier, specifically when the scroll distance of the current column exceeds half the height of the selected item, which indicates that the item has entered the divider area. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>In scenarios where the picker contains linked columns, <br>the use of this callback is not recommended. <br>The reason is that it identifies nodes where items enter the divider area during scrolling. <br>However, items that change in response to the scrolling do not themselves scroll. As a result, <br>he callback's return values will only reflect changes for the currently scrolling column, <br>while other non-scrolling columns will remain unchanged. &lt;/p&gt;

**Type:** [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[TextPickerResult](arkts-na-textpicker-textpickerresult-i.md)&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-onEnterSelectedArea?: Callback<TextPickerResult>--><!--Device-TextPickerDialogOptions-onEnterSelectedArea?: Callback<TextPickerResult>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onScrollStop

```TypeScript
onScrollStop?: Callback<TextPickerResult>
```

Callback invoked when the scrolling in the text picker of the dialog box stops.

**Type:** [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[TextPickerResult](arkts-na-textpicker-textpickerresult-i.md)&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-onScrollStop?: Callback<TextPickerResult>--><!--Device-TextPickerDialogOptions-onScrollStop?: Callback<TextPickerResult>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillAppear

```TypeScript
onWillAppear?: () => void
```

Event callback when the dialog box is about to appear. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>1. The normal timing sequence is as follows: <br>onWillAppear &gt; onDidAppear &gt; (onAccept/onCancel/onChange/onScrollStop) &gt; onWillDisappear &gt; onDidDisappear. <br>2. You can set the callback event for changing the dialog box display effect in onWillAppear. <br>the settings take effect next time the dialog box appears. &lt;/p&gt;

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-onWillAppear?: () => void--><!--Device-TextPickerDialogOptions-onWillAppear?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDisappear

```TypeScript
onWillDisappear?: () => void
```

Event callback when the dialog box is about to disappear. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>1. The normal timing sequence is as follows: onWillAppear &gt; onDidAppear &gt; (onAccept/onCancel/onChange/onScrollStop) &gt; onWillDisappear &gt; onDidDisappear. <br>2. If the user closes the dialog box immediately after it appears, onWillDisappear is invoked before onDidAppear. &lt;/p&gt;

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-onWillDisappear?: () => void--><!--Device-TextPickerDialogOptions-onWillDisappear?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedTextStyle

```TypeScript
selectedTextStyle?: PickerTextStyle
```

Font color, font size, and font weight of the selected item.

**Type:** [PickerTextStyle](../../apis-arkui/arkts-components/arkts-arkui-pickertextstyle-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-selectedTextStyle?: PickerTextStyle--><!--Device-TextPickerDialogOptions-selectedTextStyle?: PickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: ShadowOptions | ShadowStyle
```

Shadow of the dialog box. Default value on 2-in-1 devices: ShadowStyle.OUTER_FLOATING_MD when the dialog box is focused and ShadowStyle.OUTER_FLOATING_SM otherwise.

**Type:** [ShadowOptions](../../apis-arkui/arkts-components/arkts-arkui-shadowoptions-i.md) \| [ShadowStyle](../../apis-arkui/arkts-components/arkts-arkui-shadowstyle-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-shadow?: ShadowOptions | ShadowStyle--><!--Device-TextPickerDialogOptions-shadow?: ShadowOptions | ShadowStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textStyle

```TypeScript
textStyle?: PickerTextStyle
```

Font color, font size, and font weight of all items except the top, bottom, and selected items.

**Type:** [PickerTextStyle](../../apis-arkui/arkts-components/arkts-arkui-pickertextstyle-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerDialogOptions-textStyle?: PickerTextStyle--><!--Device-TextPickerDialogOptions-textStyle?: PickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

