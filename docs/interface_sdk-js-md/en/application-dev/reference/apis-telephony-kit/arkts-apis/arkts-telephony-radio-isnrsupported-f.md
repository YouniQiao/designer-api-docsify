# isNRSupported

## Modules to Import

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## isNRSupported

```TypeScript
function isNRSupported(): boolean
```

Checks whether the current device supports NR.

**Since:** 9

**System capability:** SystemCapability.Telephony.CoreService

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |


## isNRSupported

```TypeScript
function isNRSupported(slotId: number): boolean
```

Checks whether the SIM card in the specified slot supports NR.

**Since:** 9

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
