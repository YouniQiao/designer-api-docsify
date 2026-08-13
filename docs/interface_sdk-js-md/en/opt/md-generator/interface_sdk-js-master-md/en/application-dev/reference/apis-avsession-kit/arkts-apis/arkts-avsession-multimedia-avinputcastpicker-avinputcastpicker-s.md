# AVInputCastPicker

Picker used to show available input devices.

**Since:** 20

**Deprecated since:** -1

<!--Device-unnamed-export declare struct AVInputCastPicker--><!--Device-unnamed-export declare struct AVInputCastPicker-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVInputCast

## Modules to Import

```TypeScript
import { AVInputCastPicker } from '@kit.AVSessionKit';
```

## customPicker

```TypeScript
@Prop
  customPicker?: CustomBuilder
```

Custom picker.

**Type:** [CustomBuilder](../../apis-arkui/arkts-components/arkts-arkui-custombuilder-t.md)

**Since:** 20

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AVInputCastPicker-@Prop  customPicker?: CustomBuilder--><!--Device-AVInputCastPicker-@Prop  customPicker?: CustomBuilder-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVInputCast

## onStateChange

```TypeScript
onStateChange?: OnPickerStateCallback
```

Called when the component state changes.

**Type:** [OnPickerStateCallback](arkts-avsession-onpickerstatecallback-t.md)

**Since:** 20

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AVInputCastPicker-onStateChange?: OnPickerStateCallback--><!--Device-AVInputCastPicker-onStateChange?: OnPickerStateCallback-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVInputCast
