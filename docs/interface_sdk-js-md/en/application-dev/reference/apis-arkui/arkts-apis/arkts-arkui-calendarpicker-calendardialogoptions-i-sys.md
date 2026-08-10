# CalendarDialogOptions

日历选择器弹窗选项。

继承自[CalendarOptions](arkts-arkui-calendarpicker-calendaroptions-i.md)。

> **说明：**
> 
> 在应用窗口缩小过程中，弹窗的宽度会被不断压缩，当缩小到一定程度时会导致其内容无法完整显示，保证CalendarPickerDialog内容能够
> 完整显示的最小窗口宽度为386vp。

**Inheritance/Implementation:** CalendarDialogOptions extends [CalendarOptions](arkts-arkui-calendarpicker-calendaroptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface CalendarDialogOptions extends CalendarOptions--><!--Device-unnamed-export declare interface CalendarDialogOptions extends CalendarOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## distortionMode

```TypeScript
distortionMode?: DistortionMode
```

设置对话框的形变动画模式。

**Type:** [DistortionMode](../arkts-components/arkts-arkui-distortionmode-e-sys.md)

**Default:** DistortionMode.DISTORTION_AUTO

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CalendarDialogOptions-distortionMode?: DistortionMode--><!--Device-CalendarDialogOptions-distortionMode?: DistortionMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## edgeLightMode

```TypeScript
edgeLightMode?: EdgeLightMode
```

设置对话框的边缘光动画模式。

**Type:** [EdgeLightMode](../arkts-components/arkts-arkui-edgelightmode-e-sys.md)

**Default:** EdgeLightMode.EDGELIGHT_AUTO

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CalendarDialogOptions-edgeLightMode?: EdgeLightMode--><!--Device-CalendarDialogOptions-edgeLightMode?: EdgeLightMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

