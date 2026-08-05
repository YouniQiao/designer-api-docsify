# DatePickerDialogOptions

Parameters of the date picker dialog box.

**Inheritance/Implementation:** DatePickerDialogOptions extends [DatePickerOptions](datepicker-datepickeroptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface DatePickerDialogOptions extends DatePickerOptions--><!--Device-unnamed-export declare interface DatePickerDialogOptions extends DatePickerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## acceptButtonStyle

```TypeScript
acceptButtonStyle?: PickerDialogButtonStyle
```

Style of accept button. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_: \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_In the acceptButtonStyle and cancelButtonStyle configurations, \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_only one primary field can be set to true at most. \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_If both the primary fields are set to true, neither will take effect. \_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_

**Type:** PickerDialogButtonStyle

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-acceptButtonStyle?: PickerDialogButtonStyle--><!--Device-DatePickerDialogOptions-acceptButtonStyle?: PickerDialogButtonStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alignment

```TypeScript
alignment?: DialogAlignment
```

Alignment mode of the dialog box in the vertical direction.

**Type:** DialogAlignment

**Default:** DialogAlignment.Default

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-alignment?: DialogAlignment--><!--Device-DatePickerDialogOptions-alignment?: DialogAlignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

Background blur style of the dialog box.

**Type:** BlurStyle

**Default:** BlurStyle.COMPONENT_ULTRA_THICK

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-backgroundBlurStyle?: BlurStyle--><!--Device-DatePickerDialogOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyleOptions

```TypeScript
backgroundBlurStyleOptions?: BackgroundBlurStyleOptions
```

Options for customizing the background blur style.

**Type:** BackgroundBlurStyleOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions--><!--Device-DatePickerDialogOptions-backgroundBlurStyleOptions?: BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

Backplane color of the dialog box.

**Type:** ResourceColor

**Default:** Color.Transparent

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-backgroundColor?: ResourceColor--><!--Device-DatePickerDialogOptions-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundEffect

```TypeScript
backgroundEffect?: BackgroundEffectOptions
```

Options for customizing the background effect.

**Type:** BackgroundEffectOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-backgroundEffect?: BackgroundEffectOptions--><!--Device-DatePickerDialogOptions-backgroundEffect?: BackgroundEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## canLoop

```TypeScript
canLoop?: boolean
```

Can scroll loop if true is set, on the contrary it can not.

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-canLoop?: boolean--><!--Device-DatePickerDialogOptions-canLoop?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cancelButtonStyle

```TypeScript
cancelButtonStyle?: PickerDialogButtonStyle
```

Style of cancel button. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_: \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_In the acceptButtonStyle and cancelButtonStyle configurations, \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_only one primary field can be set to true at most. \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_If both the primary fields are set to true, neither will take effect. \_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_

**Type:** PickerDialogButtonStyle

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-cancelButtonStyle?: PickerDialogButtonStyle--><!--Device-DatePickerDialogOptions-cancelButtonStyle?: PickerDialogButtonStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dateTimeOptions

```TypeScript
dateTimeOptions?: DateTimeOptions
```

Whether to display a leading zero for the hours and minutes. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_: \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_Currently only the configuration of the hour and minute parameters is supported. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_

**Type:** DateTimeOptions

**Default:** hour: In the 24-hour format, it defaults to 2-digit, which means a leading zero is used;
<br>In the 12-hour format, it defaults to numeric, which means no leading zero is used.
<br>minute: defaults to 2-digit, which means a leading zero is used.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-dateTimeOptions?: DateTimeOptions--><!--Device-DatePickerDialogOptions-dateTimeOptions?: DateTimeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disappearTextStyle

```TypeScript
disappearTextStyle?: PickerTextStyle
```

Font color, font size, and font width for the top and bottom items.

**Type:** PickerTextStyle

**Default:** {<br>color: '#ff182431',<br>font: {<br>size: '14fp', <br>weight: FontWeight.Regular<br>}<br>}

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-disappearTextStyle?: PickerTextStyle--><!--Device-DatePickerDialogOptions-disappearTextStyle?: PickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHapticFeedback

```TypeScript
enableHapticFeedback?: boolean
```

Whether to enable haptic feedback. The value true means to enable haptic feedback, and false means the opposite

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-enableHapticFeedback?: boolean--><!--Device-DatePickerDialogOptions-enableHapticFeedback?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHoverMode

```TypeScript
enableHoverMode?: boolean
```

Whether to enable the hover mode.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-enableHoverMode?: boolean--><!--Device-DatePickerDialogOptions-enableHoverMode?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hoverModeArea

```TypeScript
hoverModeArea?: HoverModeAreaType
```

Display area of the dialog box in hover mode.

**Type:** HoverModeAreaType

**Default:** HoverModeAreaType.BOTTOM_SCREEN

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-hoverModeArea?: HoverModeAreaType--><!--Device-DatePickerDialogOptions-hoverModeArea?: HoverModeAreaType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lunar

```TypeScript
lunar?: boolean
```

Whether to display the lunar calendar. The value true means to display the lunar calendar, and false means the opposite.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-lunar?: boolean--><!--Device-DatePickerDialogOptions-lunar?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lunarSwitch

```TypeScript
lunarSwitch?: boolean
```

Whether to display the lunar calendar switch. The value true means to display the lunar calendar switch, and false means the opposite.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-lunarSwitch?: boolean--><!--Device-DatePickerDialogOptions-lunarSwitch?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lunarSwitchStyle

```TypeScript
lunarSwitchStyle?: LunarSwitchStyle
```

Style of the lunar calendar switch.

**Type:** LunarSwitchStyle

**Default:** { selectedColor: $r('sys.color.ohos_id_color_text_primary_actived'),
<br>unselectedColor: $r('sys.color.ohos_id_color_switch_outline_off'), strokeColor: Color.White }.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-lunarSwitchStyle?: LunarSwitchStyle--><!--Device-DatePickerDialogOptions-lunarSwitchStyle?: LunarSwitchStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maskRect

```TypeScript
maskRect?: Rectangle
```

Mask area of the dialog box. Events outside the mask area are transparently transmitted, and events within the mask area are not.

**Type:** Rectangle

**Default:** { x: 0, y: 0, width: '100%', height: '100%' }

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-maskRect?: Rectangle--><!--Device-DatePickerDialogOptions-maskRect?: Rectangle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: Offset
```

Offset of the dialog box based on the alignment settings.

**Type:** Offset

**Default:** { dx: 0 , dy: 0 }

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-offset?: Offset--><!--Device-DatePickerDialogOptions-offset?: Offset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onCancel

```TypeScript
onCancel?: VoidCallback
```

Callback invoked when the Cancel button in the dialog box is clicked. Anonymous Object Rectification.

**Type:** VoidCallback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-onCancel?: VoidCallback--><!--Device-DatePickerDialogOptions-onCancel?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDateAccept

```TypeScript
onDateAccept?: Callback<Date>
```

Callback invoked when the OK button in the dialog box is clicked. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_: \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_When showTime is set to true, the hour and minute in the value returned by \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_the callback are the hour and minute selected in the picker. Otherwise, \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_the hour and minute are the hour and minute of the system time. \_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_

**Type:** Callback&lt;Date&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-onDateAccept?: Callback<Date>--><!--Device-DatePickerDialogOptions-onDateAccept?: Callback<Date>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDateChange

```TypeScript
onDateChange?: Callback<Date>
```

Callback invoked when the selected item in the picker changes. Anonymous Object Rectification. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_: \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_When showTime is set to true, the hour and minute in the value returned by \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_the callback are the hour and minute selected in the picker. Otherwise, \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_the hour and minute are the hour and minute of the system time. \_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_

**Type:** Callback&lt;Date&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-onDateChange?: Callback<Date>--><!--Device-DatePickerDialogOptions-onDateChange?: Callback<Date>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidAppear

```TypeScript
onDidAppear?: VoidCallback
```

Event callback when the dialog box appears. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_: \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_1. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onDateAccept/onCancel/onDateChange) > onWillDisappear > onDidDisappear. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_2. You can set the callback event for changing the dialog box display effect in onDidAppear. The settings take effect next time the dialog box appears. \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_3. If the user closes the dialog box immediately after it appears, onWillDisappear is invoked before onDidAppear. \_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_4. If the dialog box is closed before its entrance animation is finished, this callback is not invoked. \_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_

**Type:** VoidCallback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-onDidAppear?: VoidCallback--><!--Device-DatePickerDialogOptions-onDidAppear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidDisappear

```TypeScript
onDidDisappear?: VoidCallback
```

Event callback when the dialog box disappears. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_: \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_1. The normal timing sequence is as follows: onWillAppear > onDidAppear > \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_(onDateAccept/onCancel/onDateChange) > onWillDisappear > onDidDisappear. \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_

**Type:** VoidCallback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-onDidDisappear?: VoidCallback--><!--Device-DatePickerDialogOptions-onDidDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillAppear

```TypeScript
onWillAppear?: VoidCallback
```

Event callback when the dialog box is about to appear. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_: \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_1. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onDateAccept/onCancel/onDateChange) > onWillDisappear > onDidDisappear. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_2. You can set the callback event for changing the dialog box display effect in onWillAppear. The settings take effect next time the dialog box appears. \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_

**Type:** VoidCallback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-onWillAppear?: VoidCallback--><!--Device-DatePickerDialogOptions-onWillAppear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDisappear

```TypeScript
onWillDisappear?: VoidCallback
```

Event callback when the dialog box is about to disappear. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_: \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_1. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onDateAccept/onCancel/onDateChange) > onWillDisappear > onDidDisappear. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_2. If the user closes the dialog box immediately after it appears, onWillDisappear is invoked before onDidAppear. \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_

**Type:** VoidCallback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-onWillDisappear?: VoidCallback--><!--Device-DatePickerDialogOptions-onWillDisappear?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedTextStyle

```TypeScript
selectedTextStyle?: PickerTextStyle
```

Font color, font size, and font width of the selected item.

**Type:** PickerTextStyle

**Default:** {<br>color: '#ff007dff',<br>font: {<br>size: '20vp', <br>weight: FontWeight.Medium<br>}

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-selectedTextStyle?: PickerTextStyle--><!--Device-DatePickerDialogOptions-selectedTextStyle?: PickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: ShadowOptions | ShadowStyle
```

Shadow of the dialog box. Default value on 2-in-1 devices: ShadowStyle.OUTER\_FLOATING\_MD when the dialog box is focused and ShadowStyle.OUTER\_FLOATING\_SM

**Type:** ShadowOptions \| ShadowStyle

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-shadow?: ShadowOptions | ShadowStyle--><!--Device-DatePickerDialogOptions-shadow?: ShadowOptions | ShadowStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showTime

```TypeScript
showTime?: boolean
```

Whether to display the time item. The value true means to display the time item, and false means the opposite. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_: \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_With showTime=true, the mode parameter has no effect and the default three columns for year, \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_month, and day are displayed. \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-showTime?: boolean--><!--Device-DatePickerDialogOptions-showTime?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## systemMaterial

```TypeScript
systemMaterial?: SystemUiMaterial
```

Set system-styled materials for dialog. Different materials have different effects, which can influence backgroundColor, border, shadow, and other visual attributes of dialog.

**Type:** SystemUiMaterial

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-systemMaterial?: SystemUiMaterial--><!--Device-DatePickerDialogOptions-systemMaterial?: SystemUiMaterial-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textStyle

```TypeScript
textStyle?: PickerTextStyle
```

Font color, font size, and font width of all items except the top, bottom, and selected items.

**Type:** PickerTextStyle

**Default:** {<br>color: '#ff182431',<br>font: {<br>size: '16fp', <br>weight: FontWeight.Regular<br>}<br>}

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-textStyle?: PickerTextStyle--><!--Device-DatePickerDialogOptions-textStyle?: PickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## useMilitaryTime

```TypeScript
useMilitaryTime?: boolean
```

Whether to display time in 24-hour format. The value true means to display time in 24-hour format, and false means the opposite. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_: \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_When the display time is in 12-hour format, the AM/PM zone does not change depending on the hour portion. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-useMilitaryTime?: boolean--><!--Device-DatePickerDialogOptions-useMilitaryTime?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

