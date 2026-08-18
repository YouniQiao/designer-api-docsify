# isNRSupported

## Modules to Import

```TypeScript
```

## isNRSupported

```TypeScript
function isNRSupported(): boolean
```

Checks whether the device supports 5G New Radio (NR).

**Since:** 23

<!--Device-radio-function isNRSupported(): boolean--><!--Device-radio-function isNRSupported(): boolean-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
let result: boolean = radio.isNRSupported();
console.info("Result: "+ result);
```


## isNRSupported

```TypeScript
function isNRSupported(slotId: number): boolean
```

Checks whether the device supports 5G New Radio (NR) by according card slot.

**Since:** 23

<!--Device-radio-function isNRSupported(slotId: int): boolean--><!--Device-radio-function isNRSupported(slotId: int): boolean-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
let slotId: number = 0;
let result: boolean = radio.isNRSupported(slotId);
console.info("Result: "+ result);
```
