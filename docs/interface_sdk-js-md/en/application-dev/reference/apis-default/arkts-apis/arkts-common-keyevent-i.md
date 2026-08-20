# KeyEvent

KeyEvent object description:

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface KeyEvent--><!--Device-unnamed-export declare interface KeyEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stopPropagation

```TypeScript
stopPropagation(): void
```

Block event bubbling.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyEvent-stopPropagation(): void--><!--Device-KeyEvent-stopPropagation(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## deviceId

```TypeScript
deviceId: int
```

Indicates the ID of the input device that triggers the current key.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyEvent-deviceId: int--><!--Device-KeyEvent-deviceId: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getModifierKeyState

```TypeScript
getModifierKeyState?: ModifierKeyStateGetter
```

Query the modifier key press state, support 'ctrl'|'alt'|'shift'

**Type:** [ModifierKeyStateGetter](arkts-modifierkeystategetter-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyEvent-getModifierKeyState?: ModifierKeyStateGetter--><!--Device-KeyEvent-getModifierKeyState?: ModifierKeyStateGetter-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## intentionCode

```TypeScript
intentionCode: IntentionCode
```

Intention code of a key or modifier keys.

**Type:** [IntentionCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-intentioncode-intentioncode-e.md)

**Default:** IntentionCode.INTENTION_UNKNOWN

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyEvent-intentionCode: IntentionCode--><!--Device-KeyEvent-intentionCode: IntentionCode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isCapsLockOn

```TypeScript
isCapsLockOn?: boolean
```

Whether Caps Lock is on

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyEvent-isCapsLockOn?: boolean--><!--Device-KeyEvent-isCapsLockOn?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isNumLockOn

```TypeScript
isNumLockOn?: boolean
```

Whether Num Lock is on

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyEvent-isNumLockOn?: boolean--><!--Device-KeyEvent-isNumLockOn?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isScrollLockOn

```TypeScript
isScrollLockOn?: boolean
```

Whether Scroll Lock is on

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyEvent-isScrollLockOn?: boolean--><!--Device-KeyEvent-isScrollLockOn?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## keyCode

```TypeScript
keyCode: int
```

Key code of a key

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyEvent-keyCode: int--><!--Device-KeyEvent-keyCode: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## keySource

```TypeScript
keySource: KeySource
```

Type of the input device that triggers the current key, such as the keyboard or handle.

**Type:** [KeySource](../../apis-arkui/arkts-apis/arkts-arkui-keysource-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyEvent-keySource: KeySource--><!--Device-KeyEvent-keySource: KeySource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## keyText

```TypeScript
keyText: string
```

Key value of a key.

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyEvent-keyText: string--><!--Device-KeyEvent-keyText: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## metaKey

```TypeScript
metaKey: int
```

Indicates the status of the key when the key is pressed. The value 1 indicates the pressed state, and the value 0 indicates the unpressed state.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyEvent-metaKey: int--><!--Device-KeyEvent-metaKey: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## timestamp

```TypeScript
timestamp: long
```

Timestamp when the key was pressed.

**Type:** long

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyEvent-timestamp: long--><!--Device-KeyEvent-timestamp: long-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: KeyType
```

Type of a key.

**Type:** [KeyType](../../apis-arkui/arkts-apis/arkts-arkui-keytype-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyEvent-type: KeyType--><!--Device-KeyEvent-type: KeyType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## unicode

```TypeScript
unicode?: long
```

Unicode of a key

**Type:** long

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyEvent-unicode?: long--><!--Device-KeyEvent-unicode?: long-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

