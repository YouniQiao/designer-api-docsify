# AVCastPicker

A picker view to show availale streaming device list. @struct { AVCastPicker }

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-declare struct AVCastPicker--><!--Device-unnamed-declare struct AVCastPicker-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## Modules to Import

```TypeScript
```

## build

```TypeScript
@Builder
  build(): void
```

The method to build component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-AVCastPicker-@Builder  build(): void--><!--Device-AVCastPicker-@Builder  build(): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## activeColor

```TypeScript
@PropRef
  activeColor?: Color | int | string
```

Assigns the color of picker component at active state.

**Type:** Color \| int \| string

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-AVCastPicker-@PropRef  activeColor?: Color | int | string--><!--Device-AVCastPicker-@PropRef  activeColor?: Color | int | string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## colorMode

```TypeScript
@PropRef
  colorMode?: AVCastPickerColorMode
```

Set the picker color mode.

**Type:** [AVCastPickerColorMode](../../apis-avsession-kit/arkts-apis/arkts-avsession-multimedia-avcastpickerparam-avcastpickercolormode-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-AVCastPicker-@PropRef  colorMode?: AVCastPickerColorMode--><!--Device-AVCastPicker-@PropRef  colorMode?: AVCastPickerColorMode-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## customPicker

```TypeScript
@BuilderParam
  customPicker?: CustomBuilder
```

Set the custom builder for the picker appearance. If not set, system will show the default appearance for different device type.

**Type:** CustomBuilder

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-AVCastPicker-@BuilderParam  customPicker?: CustomBuilder--><!--Device-AVCastPicker-@BuilderParam  customPicker?: CustomBuilder-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## normalColor

```TypeScript
@PropRef
  normalColor?: Color | int | string
```

Assigns the color of picker component at normal state .

**Type:** Color \| int \| string

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-AVCastPicker-@PropRef  normalColor?: Color | int | string--><!--Device-AVCastPicker-@PropRef  normalColor?: Color | int | string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## onStateChange

```TypeScript
onStateChange?: OnPickerStateCallback
```

Picker state change callback.

**Type:** [OnPickerStateCallback](arkts-onpickerstatecallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-AVCastPicker-onStateChange?: OnPickerStateCallback--><!--Device-AVCastPicker-onStateChange?: OnPickerStateCallback-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## pickerStyle

```TypeScript
@PropRef
  pickerStyle?: AVCastPickerStyle
```

Set the picker style.

**Type:** [AVCastPickerStyle](../../apis-avsession-kit/arkts-apis/arkts-avsession-multimedia-avcastpickerparam-avcastpickerstyle-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-AVCastPicker-@PropRef  pickerStyle?: AVCastPickerStyle--><!--Device-AVCastPicker-@PropRef  pickerStyle?: AVCastPickerStyle-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## sessionType

```TypeScript
@PropRef
  sessionType?: string
```

Set the session type used by current picker component which can refer to AVSessionType in avSession. If not set, default value is 'audio'.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-AVCastPicker-@PropRef  sessionType?: string--><!--Device-AVCastPicker-@PropRef  sessionType?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

