# CalendarDialogOptions

Defines the configuration options of the calendar picker dialog box. Inherits from [CalendarOptions](arkts-arkui-calendaroptions-i.md#CalendarOptions). > **NOTE：**> > When the application window is resized, the width of the dialog box is continuously compressed. If the window width > is reduced below a certain threshold, the content of the dialog box may not be fully visible. To ensure that the > content of the **CalendarPickerDialog** component is fully displayed, the minimum window width required is 386 vp.

**Inheritance/Implementation:** CalendarDialogOptions extends [CalendarOptions](arkts-arkui-calendaroptions-i.md#CalendarOptions)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-unnamed-declare interface CalendarDialogOptions--><!--Device-unnamed-declare interface CalendarDialogOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## distortionMode

```TypeScript
distortionMode?: DistortionMode
```

Sets the distortion animation mode for the dialog. Default Value: DistortionMode.DISTORTION_AUTO

**Type:** DistortionMode

**Default:** DistortionMode.DISTORTION_AUTO

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CalendarDialogOptions-distortionMode?: DistortionMode--><!--Device-CalendarDialogOptions-distortionMode?: DistortionMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## edgeLightMode

```TypeScript
edgeLightMode?: EdgeLightMode
```

Sets the edge light animation mode for the dialog. Default value: EdgeLightMode.EDGELIGHT_AUTO

**Type:** EdgeLightMode

**Default:** EdgeLightMode.EDGELIGHT_AUTO

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CalendarDialogOptions-edgeLightMode?: EdgeLightMode--><!--Device-CalendarDialogOptions-edgeLightMode?: EdgeLightMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

