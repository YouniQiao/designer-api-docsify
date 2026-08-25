# HotkeyOptions

Defines shortcut key options.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

## Modules to Import

```TypeScript
import { inputConsumer } from '@kit.InputKit';
```

## finalKey

```TypeScript
finalKey: int
```

Modified key, which can be any key except the modifier keys and Meta key. For details about the keys, see [@ohos.multimodalInput.keyCode (Keycode)](arkts-input-multimodalinput-keycode-keycode-e.md).For example, in **Ctrl+Shift+Esc**, **Esc** is the modifier key.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

## isRepeat

```TypeScript
isRepeat?: boolean
```

Whether to report repeated key events. The value **true** means to report repeated key events, and the value **false** means the opposite. The default value is **true**.

**Type:** boolean

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

## preKeys

```TypeScript
preKeys: Array<int>
```

Modifier key set (including Ctrl, Shift, and Alt). One to four modifier keys are supported. There is no requirement on the sequence of modifier keys.For example, in **Ctrl+Shift+Esc**, **Ctrl** and **Shift** are modifier keys.

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer
