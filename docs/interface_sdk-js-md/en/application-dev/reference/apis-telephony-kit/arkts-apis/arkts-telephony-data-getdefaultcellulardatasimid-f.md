# getDefaultCellularDataSimId

## Modules to Import

```TypeScript
import { data } from 'data';
```

## getDefaultCellularDataSimId

```TypeScript
function getDefaultCellularDataSimId(): int
```

Obtains the default cellular data SIM ID.

**Since:** 23

<!--Device-data-function getDefaultCellularDataSimId(): int--><!--Device-data-function getDefaultCellularDataSimId(): int-End-->

**System capability:** SystemCapability.Telephony.CellularData

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the SIM ID of the default cellular data sim and SIM ID will increase from 1. |

**Examples**

```TypeScript
import { data } from '@kit.TelephonyKit';

console.info("Result: "+ data.getDefaultCellularDataSimId());
```

