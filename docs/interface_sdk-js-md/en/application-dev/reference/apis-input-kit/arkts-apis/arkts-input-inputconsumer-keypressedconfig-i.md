# KeyPressedConfig

Sets the key event consumption configuration.

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

<!--Device-inputConsumer-interface KeyPressedConfig--><!--Device-inputConsumer-interface KeyPressedConfig-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

## Modules to Import

```TypeScript
import { inputConsumer } from '@kit.InputKit';
```

## action

```TypeScript
action: int
```

Subscription type.

**Note：**: Since API version 21, the value of this parameter can be **1** or **2**. The value **1** indicates subscription to only key press events, and the value **2** indicates subscription to both key press and release events.

In API version 20 or earlier versions, the value of this parameter can only be set to **1**, indicating subscription to only key press events.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

<!--Device-KeyPressedConfig-action: int--><!--Device-KeyPressedConfig-action: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

## isRepeat

```TypeScript
isRepeat: boolean
```

Whether to report repeated key events. The value **true** means to report repeated key events, and the value  
**false** means the opposite. The default value is **true**.

**Type:** boolean

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

<!--Device-KeyPressedConfig-isRepeat: boolean--><!--Device-KeyPressedConfig-isRepeat: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

## key

```TypeScript
key: int
```

Key value.

**Note:** Since API version 26.0.0, the
[KEYCODE_FINGERPRINT_SLIDE_UP](arkts-input-multimodalinput-keycode-keycode-e.md#KeyCode) and  
[KEYCODE_FINGERPRINT_SLIDE_DOWN](arkts-input-multimodalinput-keycode-keycode-e.md#KeyCode) keys are supported. The keys are not universal device keys. Before using them, check whether the current device supports the reporting of related key events. For details, see  
[Preferential Response of System Function Keys](../../../device/input/keypressed-guidelines.md).

Since API version 21, the [KEYCODE_MEDIA_PLAY_PAUSE](arkts-input-multimodalinput-keycode-keycode-e.md#KeyCode),  
[KEYCODE_MEDIA_NEXT](arkts-input-multimodalinput-keycode-keycode-e.md#KeyCode), and  
[KEYCODE_MEDIA_PREVIOUS](arkts-input-multimodalinput-keycode-keycode-e.md#KeyCode) keys are supported.

In API version 20 or earlier versions, only the [KEYCODE_VOLUME_UP](arkts-input-multimodalinput-keycode-keycode-e.md#KeyCode)and [KEYCODE_VOLUME_DOWN](arkts-input-multimodalinput-keycode-keycode-e.md#KeyCode) keys are supported.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

<!--Device-KeyPressedConfig-key: int--><!--Device-KeyPressedConfig-key: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

