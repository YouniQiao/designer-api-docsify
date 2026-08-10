# KeyEvent

按键事件。

**Inheritance/Implementation:** KeyEvent extends [InputEvent](arkts-input-multimodalinput-inputevent-inputevent-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface KeyEvent extends InputEvent--><!--Device-unnamed-export declare interface KeyEvent extends InputEvent-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## Modules to Import

```TypeScript
import { KeyEvent, Action, Key } from 'kits/@kit.InputKit';
```

## action

```TypeScript
action: Action
```

按键事件类型。

**Type:** [Action](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-action-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-KeyEvent-action: Action--><!--Device-KeyEvent-action: Action-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## altKey

```TypeScript
altKey: boolean
```

当前altKey是否处于按下状态。 

true表示处于按下状态，false表示处于抬起状态。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-KeyEvent-altKey: boolean--><!--Device-KeyEvent-altKey: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## capsLock

```TypeScript
capsLock: boolean
```

当前capsLock是否处于使能状态。 

true表示处于使能状态，false表示处于未使能状态。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-KeyEvent-capsLock: boolean--><!--Device-KeyEvent-capsLock: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## ctrlKey

```TypeScript
ctrlKey: boolean
```

当前ctrlKey是否处于按下状态。 

true表示处于按下状态，false表示处于抬起状态。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-KeyEvent-ctrlKey: boolean--><!--Device-KeyEvent-ctrlKey: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## fnKey

```TypeScript
fnKey: boolean
```

当前fnKey是否处于按下状态。 

true表示处于按下状态，false表示处于抬起状态。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-KeyEvent-fnKey: boolean--><!--Device-KeyEvent-fnKey: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## key

```TypeScript
key: Key
```

按键。

**Type:** [Key](arkts-input-multimodalinput-keyevent-key-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-KeyEvent-key: Key--><!--Device-KeyEvent-key: Key-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## keys

```TypeScript
keys: Key[]
```

当前处于按下状态的按键列表。

**Type:** [Key](arkts-input-multimodalinput-keyevent-key-i.md)[]

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-KeyEvent-keys: Key[]--><!--Device-KeyEvent-keys: Key[]-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## logoKey

```TypeScript
logoKey: boolean
```

当前logoKey是否处于按下状态。 

true表示处于按下状态，false表示处于抬起状态。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-KeyEvent-logoKey: boolean--><!--Device-KeyEvent-logoKey: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## numLock

```TypeScript
numLock: boolean
```

当前numLock是否处于使能状态。 

true表示处于使能状态，false表示处于未使能状态。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-KeyEvent-numLock: boolean--><!--Device-KeyEvent-numLock: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## scrollLock

```TypeScript
scrollLock: boolean
```

当前scrollLock是否处于使能状态。 

true表示处于使能状态，false表示处于未使能状态。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-KeyEvent-scrollLock: boolean--><!--Device-KeyEvent-scrollLock: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## shiftKey

```TypeScript
shiftKey: boolean
```

当前shiftKey是否处于按下状态。 

true表示处于按下状态，false表示处于抬起状态。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-KeyEvent-shiftKey: boolean--><!--Device-KeyEvent-shiftKey: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## unicodeChar

```TypeScript
unicodeChar: int
```

按键对应的unicode字符。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-KeyEvent-unicodeChar: int--><!--Device-KeyEvent-unicodeChar: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

