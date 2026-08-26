# getMaxSimCount

## Modules to Import

```TypeScript
```

## getMaxSimCount

```TypeScript
function getMaxSimCount(): number
```

Obtains the number of card slots.

**Since:** 7

**System capability:** SystemCapability.Telephony.CoreService

**Return value:**

| Type | Description |
| --- | --- |
| number | Number of card slots. |

**Examples**

```TypeScript
import { sim } from '@kit.TelephonyKit';

console.info("Result: "+ sim.getMaxSimCount());
```
