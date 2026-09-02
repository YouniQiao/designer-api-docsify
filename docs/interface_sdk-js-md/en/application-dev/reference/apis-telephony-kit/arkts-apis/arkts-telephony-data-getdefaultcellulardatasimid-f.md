# getDefaultCellularDataSimId

## Modules to Import

```TypeScript
import { data } from '@kit.TelephonyKit';
```

## getDefaultCellularDataSimId

```TypeScript
function getDefaultCellularDataSimId(): number
```

Obtains the default ID of the SIM card used for mobile data.

**Since:** 10

**System capability:** SystemCapability.Telephony.CellularData

**Return value:**

| Type | Description |
| --- | --- |
| number | Obtains the default ID of the SIM card used for mobile data. |

**Examples**

```TypeScript
import { data } from '@kit.TelephonyKit';

console.info("Result: "+ data.getDefaultCellularDataSimId());
```
