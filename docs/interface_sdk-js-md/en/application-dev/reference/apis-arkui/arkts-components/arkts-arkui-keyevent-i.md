# KeyEvent

按键事件信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare interface KeyEvent--><!--Device-unnamed-declare interface KeyEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getModifierKeyState

```TypeScript
getModifierKeyState?(keys: Array<string>): boolean
```

获取功能键按压状态。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-KeyEvent-getModifierKeyState?(keys: Array<string>): boolean--><!--Device-KeyEvent-getModifierKeyState?(keys: Array<string>): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keys | Array&lt;string&gt; | Yes | 功能键列表。支持功能键 'Ctrl'\| 'Alt' \| 'Shift'。&lt;br/&gt;**说明：**&lt;br/&gt;此接口不支持在手写笔场景下使用。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 功能键是否被按下。true表示被按下，false表示未被按下。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. 2. Parameter verification failed. |

## stopPropagation

```TypeScript
stopPropagation: () => void
```

阻塞[事件冒泡](../../../ui/arkts-interaction-basic-principles.md#事件冒泡)传递。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-KeyEvent-stopPropagation: () => void--><!--Device-KeyEvent-stopPropagation: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## deviceId

```TypeScript
deviceId: number
```

触发当前按键的输入设备ID。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-KeyEvent-deviceId: number--><!--Device-KeyEvent-deviceId: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## intentionCode

```TypeScript
intentionCode: IntentionCode
```

按键对应的意图。

默认值：IntentionCode.INTENTION_UNKNOWN。

**Type:** [IntentionCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-intentioncode-intentioncode-e.md)

**Default:** IntentionCode.INTENTION_UNKNOWN

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-KeyEvent-intentionCode: IntentionCode--><!--Device-KeyEvent-intentionCode: IntentionCode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isCapsLockOn

```TypeScript
isCapsLockOn?: boolean
```

CapsLock是否锁定（true: 锁定；false: 解锁）。

**Type:** boolean

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-KeyEvent-isCapsLockOn?: boolean--><!--Device-KeyEvent-isCapsLockOn?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isNumLockOn

```TypeScript
isNumLockOn?: boolean
```

NumLock是否锁定（true: 锁定；false: 解锁）。

**Type:** boolean

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-KeyEvent-isNumLockOn?: boolean--><!--Device-KeyEvent-isNumLockOn?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isScrollLockOn

```TypeScript
isScrollLockOn?: boolean
```

ScrollLock是否锁定（true: 锁定；false: 解锁）。

**Type:** boolean

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-KeyEvent-isScrollLockOn?: boolean--><!--Device-KeyEvent-isScrollLockOn?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## keyCode

```TypeScript
keyCode: number
```

按键的键值。按键设备提供的键值请参考[KeyCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md/arkts-input-multimodalinput-keycode-keycode-e.md)。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-KeyEvent-keyCode: number--><!--Device-KeyEvent-keyCode: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## keySource

```TypeScript
keySource: KeySource
```

触发当前按键的输入设备类型。

**Type:** [KeySource](../arkts-apis/arkts-arkui-keysource-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-KeyEvent-keySource: KeySource--><!--Device-KeyEvent-keySource: KeySource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## keyText

```TypeScript
keyText: string
```

按键的名称。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-KeyEvent-keyText: string--><!--Device-KeyEvent-keyText: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## metaKey

```TypeScript
metaKey: number
```

按键发生时元键（即键盘左下角紧挨Ctrl键或Fn标记了窗口logo的按键）的状态，1表示按压态，0表示未按压态。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-KeyEvent-metaKey: number--><!--Device-KeyEvent-metaKey: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## timestamp

```TypeScript
timestamp: number
```

事件时间戳。触发事件时距离系统启动的时间间隔，单位：ns。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-KeyEvent-timestamp: number--><!--Device-KeyEvent-timestamp: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: KeyType
```

按键的类型。

**Type:** [KeyType](../arkts-apis/arkts-arkui-keytype-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-KeyEvent-type: KeyType--><!--Device-KeyEvent-type: KeyType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## unicode

```TypeScript
unicode?: number
```

按键的Unicode码值。支持范围为非空格的基本拉丁字符：0x0021-0x007E，不支持字符为0。组合键场景下，返回当前keyEvent对应按键的Unicode码值。

**Type:** number

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-KeyEvent-unicode?: number--><!--Device-KeyEvent-unicode?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

