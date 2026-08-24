# AVInputCastPicker

Picker used to show available input devices. @struct { AVInputCastPicker }

**Since:** 20

**Decorator:** @Component

<!--Device-unnamed-export declare struct AVInputCastPicker--><!--Device-unnamed-export declare struct AVInputCastPicker-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVInputCast

## Modules to Import

```TypeScript
import { AVInputCastPicker } from '@kit.AVSessionKit';
```

## customPicker

```TypeScript
customPicker?: CustomBuilder
```

Custom picker.

**Type:** [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md)

**Since:** 20

**Decorator:** @Prop

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

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AVInputCastPicker-onStateChange?: OnPickerStateCallback--><!--Device-AVInputCastPicker-onStateChange?: OnPickerStateCallback-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVInputCast

