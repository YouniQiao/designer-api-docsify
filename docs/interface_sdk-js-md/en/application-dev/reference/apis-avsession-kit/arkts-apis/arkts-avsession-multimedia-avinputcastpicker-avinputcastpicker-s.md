# AVInputCastPicker

A picker view to show availale input device list.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Component

<!--Device-unnamed-export declare struct AVInputCastPicker--><!--Device-unnamed-export declare struct AVInputCastPicker-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVInputCast

## Modules to Import

```TypeScript
import { AVInputCastPicker } from '@kit.AVSessionKit';
```

## build

```TypeScript
build(): void
```

The method to build component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

<!--Device-AVInputCastPicker-build(): void--><!--Device-AVInputCastPicker-build(): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVInputCast

## customPicker

```TypeScript
customPicker?: CustomBuilder
```

Set the custom builder for the picker appearance.If not set, system will show the default appearance for different device type.

**Type:** [CustomBuilder](../../apis-arkui/arkts-apis/arkts-arkui-custombuilder-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @BuilderParam

<!--Device-AVInputCastPicker-customPicker?: CustomBuilder--><!--Device-AVInputCastPicker-customPicker?: CustomBuilder-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVInputCast

## onStateChange

```TypeScript
onStateChange?: OnPickerStateCallback
```

Picker state change callback.

**Type:** [OnPickerStateCallback](arkts-avsession-onpickerstatecallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVInputCastPicker-onStateChange?: OnPickerStateCallback--><!--Device-AVInputCastPicker-onStateChange?: OnPickerStateCallback-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVInputCast

