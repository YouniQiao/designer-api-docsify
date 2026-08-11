# AVInputCastPicker

Picker used to show available input devices.

**Since:** 20

**Decorator:** @Component

<!--Device-unnamed-export declare struct AVInputCastPicker--><!--Device-unnamed-export declare struct AVInputCastPicker-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVInputCast

## Modules to Import

```TypeScript
import { AVInputCastPicker } from 'kits/@kit.AVSessionKit';
```

## onStateChange

```TypeScript
onStateChange?: OnPickerStateCallback
```

Called when the component state changes.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AVInputCastPicker-onStateChange?: OnPickerStateCallback--><!--Device-AVInputCastPicker-onStateChange?: OnPickerStateCallback-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVInputCast

## customPicker

```TypeScript
customPicker?: CustomBuilder
```

Custom picker.

**Type:** [CustomBuilder](../../apis-arkui/arkts-components/arkts-arkui-custombuilder-t.md)

**Since:** 20

**Decorator:** @Prop

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AVInputCastPicker-customPicker?: CustomBuilder--><!--Device-AVInputCastPicker-customPicker?: CustomBuilder-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVInputCast
