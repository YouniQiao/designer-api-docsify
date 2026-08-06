# HotkeyOptions

Defines shortcut key options.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-inputConsumer-interface HotkeyOptions--><!--Device-inputConsumer-interface HotkeyOptions-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

## finalKey

```TypeScript
finalKey: int
```

Modified key, which can be any key except the modifier keys and Meta key. For details about the keys, see  
[@ohos.multimodalInput.keyCode (Keycode)]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

For example, in **Ctrl+Shift+Esc**, **Esc** is the modifier key.

**Type:** int

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-HotkeyOptions-finalKey: int--><!--Device-HotkeyOptions-finalKey: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

## isRepeat

```TypeScript
isRepeat?: boolean
```

Whether to report repeated key events. The value **true** means to report repeated key events, and the value  
**false** means the opposite. The default value is **true**.

**Type:** boolean

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-HotkeyOptions-isRepeat?: boolean--><!--Device-HotkeyOptions-isRepeat?: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

## preKeys

```TypeScript
preKeys: Array<int>
```

Modifier key set (including Ctrl, Shift, and Alt). One to four modifier keys are supported. There is no requirement on the sequence of modifier keys.

For example, in **Ctrl+Shift+Esc**, **Ctrl** and **Shift** are modifier keys.

**Type:** Array&lt;int&gt;

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-HotkeyOptions-preKeys: Array<int>--><!--Device-HotkeyOptions-preKeys: Array<int>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

