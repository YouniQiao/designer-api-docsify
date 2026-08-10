# AVInputCastPicker

录音设备选择组件，可用于切换音频输入设备。

该组件为自定义组件，开发者在使用前需要先了解[@Component](../../../ui/state-management/arkts-create-custom-components.md#component)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Component

<!--Device-unnamed-export declare struct AVInputCastPicker--><!--Device-unnamed-export declare struct AVInputCastPicker-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVInputCast

## Modules to Import

```TypeScript
import { AVInputCastPicker } from 'kits/@kit.AVSessionKit';
```

## build

```TypeScript
build(): void
```

构造组件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

<!--Device-AVInputCastPicker-build(): void--><!--Device-AVInputCastPicker-build(): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVInputCast

## customPicker

```TypeScript
customPicker?: CustomBuilder
```

自定义样式。建议开发者自定义组件样式，可有效提升组件渲染性能。

If not set, system will show the default appearance for different device type.

**Type:** [CustomBuilder](../../apis-arkui/arkts-components/arkts-arkui-custombuilder-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @BuilderParam

<!--Device-AVInputCastPicker-customPicker?: CustomBuilder--><!--Device-AVInputCastPicker-customPicker?: CustomBuilder-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVInputCast

## onStateChange

```TypeScript
onStateChange?: OnPickerStateCallback
```

设备列表状态变更回调。

**Type:** [OnPickerStateCallback](arkts-avsession-onpickerstatecallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVInputCastPicker-onStateChange?: OnPickerStateCallback--><!--Device-AVInputCastPicker-onStateChange?: OnPickerStateCallback-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVInputCast

