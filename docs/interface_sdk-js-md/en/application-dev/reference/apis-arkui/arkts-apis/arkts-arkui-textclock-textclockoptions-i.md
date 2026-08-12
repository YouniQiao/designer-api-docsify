# TextClockOptions

Options to construct TextClock component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface TextClockOptions--><!--Device-unnamed-export declare interface TextClockOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## controller

```TypeScript
controller?: TextClockController
```

TextClock controller.Anonymous Object Rectification.

**Type:** [TextClockController](arkts-arkui-textclock-textclockcontroller-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextClockOptions-controller?: TextClockController--><!--Device-TextClockOptions-controller?: TextClockController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## timeZoneOffset

```TypeScript
timeZoneOffset?: double
```

Set the time zone offset.The value range is [-14, 12]. The value ranges from GMT-12 to GMT-12. A negative value indicates the eastern time zone, and a positive value indicates the western time zone. For example, the value of GMT-8 is -8. If this parameter is set to a floating point number within the value range, the system rounds the number and discards the decimal part.For countries or regions that cross the international date line, -13 (UTC + 13) and -14 (UTC + 14) are used to ensure that the time of the entire country or region is the same. If the value is not within the value range, the current system time zone offset is used.If the value is a floating point number in the {9.5, 3.5, -3.5, -4.5, -5.5, -5.75, -6.5, -9.5, -10.5, -12.75} set,the rounding is not performed.Default value: Time zone offset of the current system.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextClockOptions-timeZoneOffset?: double--><!--Device-TextClockOptions-timeZoneOffset?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

