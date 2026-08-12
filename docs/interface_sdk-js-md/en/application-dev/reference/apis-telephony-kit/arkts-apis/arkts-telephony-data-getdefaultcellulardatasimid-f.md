# getDefaultCellularDataSimId

## Modules to Import

```TypeScript
import { data } from '@kit.TelephonyKit';
```

## getDefaultCellularDataSimId

```TypeScript
function getDefaultCellularDataSimId(): int
```

Obtains the default cellular data SIM ID.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-data-function getDefaultCellularDataSimId(): int--><!--Device-data-function getDefaultCellularDataSimId(): int-End-->

**System capability:** SystemCapability.Telephony.CellularData

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Returns the SIM ID of the default cellular data sim and SIM ID will increase from 1. |

## Examples

```TypeScript
import { data } from '@kit.TelephonyKit';

console.info("Result: "+ data.getDefaultCellularDataSimId());
```

