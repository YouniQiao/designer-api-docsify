# getSimOperatorNumericSync

## Modules to Import

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## getSimOperatorNumericSync

```TypeScript
function getSimOperatorNumericSync(slotId: number): string
```

Obtains the home PLMN ID of the SIM card in the specified slot. This API returns the result synchronously.

**Since:** 10

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |
