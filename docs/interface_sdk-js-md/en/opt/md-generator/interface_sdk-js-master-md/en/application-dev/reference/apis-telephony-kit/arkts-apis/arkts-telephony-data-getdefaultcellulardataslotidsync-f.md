# getDefaultCellularDataSlotIdSync

## Modules to Import

```TypeScript
import { data } from '@kit.TelephonyKit';
```

## getDefaultCellularDataSlotIdSync

```TypeScript
function getDefaultCellularDataSlotIdSync(): number
```

Get the default cellular data card.

**Since:** 23

**Deprecated since:** -1

<!--Device-data-function getDefaultCellularDataSlotIdSync(): int--><!--Device-data-function getDefaultCellularDataSlotIdSync(): int-End-->

**System capability:** SystemCapability.Telephony.CellularData

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
import { data } from '@kit.TelephonyKit';

console.info("Result: "+ data.getDefaultCellularDataSlotIdSync())
```
