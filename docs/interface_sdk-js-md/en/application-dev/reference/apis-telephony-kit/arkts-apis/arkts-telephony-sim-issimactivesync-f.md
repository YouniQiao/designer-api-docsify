# isSimActiveSync

## Modules to Import

```TypeScript
import { sim } from '@kit.TelephonyKit';
```

## isSimActiveSync

```TypeScript
function isSimActiveSync(slotId: number): boolean
```

Checks whether the SIM card in the specified slot is activated.

**Since:** 10

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | number | Yes | Card slot ID.    - **0**: card slot 1.    - **1**: card slot 2 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the SIM card in the specified slot is activated. |

**Examples**

```TypeScript
import { sim } from '@kit.TelephonyKit';

let isSimActive: boolean = sim.isSimActiveSync(0);
console.info(`the sim is active:` + isSimActive);
```
