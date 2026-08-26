# getDefaultCellularDataSlotIdSync

## Modules to Import

```TypeScript
```

## getDefaultCellularDataSlotIdSync

```TypeScript
function getDefaultCellularDataSlotIdSync(): number
```

Obtains the default SIM card used for mobile data synchronously.

**Since:** 9

**System capability:** SystemCapability.Telephony.CellularData

**Return value:**

| Type | Description |
| --- | --- |
| number | Card slot ID. |

**Examples**

```TypeScript
import { data } from '@kit.TelephonyKit';

console.info("Result: "+ data.getDefaultCellularDataSlotIdSync())
```
