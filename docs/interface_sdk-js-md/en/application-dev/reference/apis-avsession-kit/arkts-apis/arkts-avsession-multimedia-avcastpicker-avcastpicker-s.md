# AVCastPicker

A picker view to show availale streaming device list.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Component

<!--Device-unnamed-declare struct AVCastPicker--><!--Device-unnamed-declare struct AVCastPicker-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## build

```TypeScript
build(): void
```

The method to build component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

<!--Device-AVCastPicker-build(): void--><!--Device-AVCastPicker-build(): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## onStateChange

```TypeScript
onStateChange?: OnPickerStateCallback
```

Picker state change callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastPicker-onStateChange?: OnPickerStateCallback--><!--Device-AVCastPicker-onStateChange?: OnPickerStateCallback-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## activeColor

```TypeScript
activeColor?: Color | int | string
```

Assigns the color of picker component at active state.

**Type:** Color \| int \| string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastPicker-activeColor?: Color | int | string--><!--Device-AVCastPicker-activeColor?: Color | int | string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## colorMode

```TypeScript
colorMode?: AVCastPickerColorMode
```

Set the picker color mode.

**Type:** AVCastPickerColorMode

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastPicker-colorMode?: AVCastPickerColorMode--><!--Device-AVCastPicker-colorMode?: AVCastPickerColorMode-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## customPicker

```TypeScript
customPicker?: CustomBuilder
```

Set the custom builder for the picker appearance.If not set, system will show the default appearance for different device type.

**Type:** CustomBuilder

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @BuilderParam

<!--Device-AVCastPicker-customPicker?: CustomBuilder--><!--Device-AVCastPicker-customPicker?: CustomBuilder-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## normalColor

```TypeScript
normalColor?: Color | int | string
```

Assigns the color of picker component at normal state .

**Type:** Color \| int \| string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastPicker-normalColor?: Color | int | string--><!--Device-AVCastPicker-normalColor?: Color | int | string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## pickerStyle

```TypeScript
pickerStyle?: AVCastPickerStyle
```

Set the picker style.

**Type:** AVCastPickerStyle

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastPicker-pickerStyle?: AVCastPickerStyle--><!--Device-AVCastPicker-pickerStyle?: AVCastPickerStyle-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## sessionType

```TypeScript
sessionType?: string
```

Set the session type used by current picker component which can refer to AVSessionType in avSession.If not set, default value is 'audio'.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastPicker-sessionType?: string--><!--Device-AVCastPicker-sessionType?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

