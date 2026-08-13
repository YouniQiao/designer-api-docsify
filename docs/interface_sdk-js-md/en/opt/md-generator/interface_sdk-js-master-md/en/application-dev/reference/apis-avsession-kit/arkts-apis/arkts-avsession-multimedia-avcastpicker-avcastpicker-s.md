# AVCastPicker

A picker view to show available streaming device list.

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare struct AVCastPicker--><!--Device-unnamed-declare struct AVCastPicker-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## Modules to Import

```TypeScript
import { AVCastPicker } from '@kit.AVSessionKit';
```

## activeColor

```TypeScript
@Prop
  activeColor?: Color | number | string
```

Assigns the color of picker component at active state.

**Type:** Color \| number \| string

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastPicker-@Prop  activeColor?: Color | number | string--><!--Device-AVCastPicker-@Prop  activeColor?: Color | number | string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## colorMode

```TypeScript
@Prop
  colorMode?: AVCastPickerColorMode
```

Set the picker color mode.

**Type:** [AVCastPickerColorMode](arkts-avsession-multimedia-avcastpickerparam-avcastpickercolormode-e.md)

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastPicker-@Prop  colorMode?: AVCastPickerColorMode--><!--Device-AVCastPicker-@Prop  colorMode?: AVCastPickerColorMode-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## customPicker

```TypeScript
@Prop
  customPicker?: CustomBuilder
```

Set the custom builder for the picker appearance. If not set, system will show the default appearance for different device type.

**Type:** [CustomBuilder](../../apis-arkui/arkts-components/arkts-arkui-custombuilder-t.md)

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastPicker-@Prop  customPicker?: CustomBuilder--><!--Device-AVCastPicker-@Prop  customPicker?: CustomBuilder-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## normalColor

```TypeScript
@Prop
  normalColor?: Color | number | string
```

Assigns the color of picker component at normal state .

**Type:** Color \| number \| string

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastPicker-@Prop  normalColor?: Color | number | string--><!--Device-AVCastPicker-@Prop  normalColor?: Color | number | string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## onStateChange

```TypeScript
onStateChange?: (state: AVCastPickerState) => void
```

Picker state change callback.

**Type:** (state: AVCastPickerState) =&gt; void

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastPicker-onStateChange?: (state: AVCastPickerState) => void--><!--Device-AVCastPicker-onStateChange?: (state: AVCastPickerState) => void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## pickerStyle

```TypeScript
@Prop
  pickerStyle?: AVCastPickerStyle
```

Set the picker style.

**Type:** [AVCastPickerStyle](arkts-avsession-multimedia-avcastpickerparam-avcastpickerstyle-e.md)

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastPicker-@Prop  pickerStyle?: AVCastPickerStyle--><!--Device-AVCastPicker-@Prop  pickerStyle?: AVCastPickerStyle-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## sessionType

```TypeScript
@Prop
  sessionType?: string
```

Set the session type used by current picker component which can refer to AVSessionType in avSession. If not set, default value is 'audio'.

**Type:** string

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastPicker-@Prop  sessionType?: string--><!--Device-AVCastPicker-@Prop  sessionType?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast
