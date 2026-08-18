# AVInputCastPicker

A picker view to show availale input device list.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare struct AVInputCastPicker--><!--Device-unnamed-export declare struct AVInputCastPicker-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVInputCast

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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-AVInputCastPicker-@Builder   build(): void--><!--Device-AVInputCastPicker-@Builder   build(): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVInputCast

## customPicker

```TypeScript
@BuilderParam
  customPicker?: CustomBuilder
```

Set the custom builder for the picker appearance. If not set, system will show the default appearance for different device type.

**Type:** CustomBuilder

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-AVInputCastPicker-@BuilderParam  customPicker?: CustomBuilder--><!--Device-AVInputCastPicker-@BuilderParam  customPicker?: CustomBuilder-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVInputCast

## onStateChange

```TypeScript
onStateChange?: OnPickerStateCallback
```

Picker state change callback.

**Type:** [OnPickerStateCallback](../../apis-avsession-kit/arkts-apis/arkts-avsession-onpickerstatecallback-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-AVInputCastPicker-onStateChange?: OnPickerStateCallback--><!--Device-AVInputCastPicker-onStateChange?: OnPickerStateCallback-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVInputCast

