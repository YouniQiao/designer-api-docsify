# getSimLabelSync

## Modules to Import

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## getSimLabelSync

```TypeScript
function getSimLabelSync(slotId: number): SimLabel
```

Obtains the SIM card label based on the specified SIM card slot ID.

**Since:** 20

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SimLabel](arkts-telephony-sim-simlabel-i.md) |
