# getDefaultCellularDataSimId

## Modules to Import

```TypeScript
```

## getDefaultCellularDataSimId

```TypeScript
function getDefaultCellularDataSimId(): number
```

Obtains the default cellular data SIM ID.

**Since:** 23

<!--Device-data-function getDefaultCellularDataSimId(): int--><!--Device-data-function getDefaultCellularDataSimId(): int-End-->

**System capability:** SystemCapability.Telephony.CellularData

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Examples**

```TypeScript
import { data } from '@kit.TelephonyKit';

console.info("Result: "+ data.getDefaultCellularDataSimId());
```
