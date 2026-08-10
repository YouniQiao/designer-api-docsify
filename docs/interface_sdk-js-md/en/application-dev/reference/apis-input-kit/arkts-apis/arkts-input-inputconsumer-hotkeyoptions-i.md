# HotkeyOptions

快捷键选项。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-inputConsumer-interface HotkeyOptions--><!--Device-inputConsumer-interface HotkeyOptions-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

## Modules to Import

```TypeScript
import { inputConsumer } from 'kits/@kit.InputKit';
```

## finalKey

```TypeScript
finalKey: int
```

被修饰键，除修饰键和Meta键以外的按键，详细按键介绍请参见[@ohos.multimodalInput.keyCode (键值)](arkts-input-multimodalinput-keycode-keycode-e.md)。

例如，Ctrl+Shift+Esc中，Esc称为被修饰键。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-HotkeyOptions-finalKey: int--><!--Device-HotkeyOptions-finalKey: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

## isRepeat

```TypeScript
isRepeat?: boolean
```

是否上报重复的按键事件。true表示上报，false表示不上报，默认值为true。

**Type:** boolean

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-HotkeyOptions-isRepeat?: boolean--><!--Device-HotkeyOptions-isRepeat?: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

## preKeys

```TypeScript
preKeys: Array<int>
```

修饰键（包括 Ctrl、Shift 和 Alt）集合，数量范围[1, 4]，无顺序要求。

例如，Ctrl+Shift+Esc中，Ctrl+Shift称为修饰键。

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-HotkeyOptions-preKeys: Array<int>--><!--Device-HotkeyOptions-preKeys: Array<int>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

