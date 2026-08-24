# CellInformation

Defines the cell information.

**Since:** 23

<!--Device-radio-export interface CellInformation--><!--Device-radio-export interface CellInformation-End-->

**System capability:** SystemCapability.Telephony.CoreService

## Modules to Import

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## data

```TypeScript
data: CdmaCellInformation | GsmCellInformation | LteCellInformation | NrCellInformation | TdscdmaCellInformation
      | WcdmaCellInformation
```

Obtains signal strength under different network formats.

**Type:** [CdmaCellInformation](arkts-telephony-radio-cdmacellinformation-i-sys.md) \| [GsmCellInformation](arkts-telephony-radio-gsmcellinformation-i-sys.md) \| [LteCellInformation](arkts-telephony-radio-ltecellinformation-i-sys.md) \| [NrCellInformation](arkts-telephony-radio-nrcellinformation-i-sys.md) \| [TdscdmaCellInformation](arkts-telephony-radio-tdscdmacellinformation-i-sys.md) \| [WcdmaCellInformation](arkts-telephony-radio-wcdmacellinformation-i-sys.md)

**Since:** 23

<!--Device-CellInformation-data: CdmaCellInformation | GsmCellInformation | LteCellInformation | NrCellInformation | TdscdmaCellInformation      | WcdmaCellInformation--><!--Device-CellInformation-data: CdmaCellInformation | GsmCellInformation | LteCellInformation | NrCellInformation | TdscdmaCellInformation      | WcdmaCellInformation-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

## isCamped

```TypeScript
isCamped: boolean
```

Obtains the camp-on status of the serving cell.Returns {@code true} if the user equipment (UE) is camped on the cell; returns {@code false} otherwise.

**Type:** boolean

**Since:** 23

<!--Device-CellInformation-isCamped: boolean--><!--Device-CellInformation-isCamped: boolean-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

## timeStamp

```TypeScript
timeStamp: int
```

Obtains the timestamp when the cell information is obtained.Returns a timestamp since boot, in nanoseconds.

**Type:** int

**Since:** 23

<!--Device-CellInformation-timeStamp: int--><!--Device-CellInformation-timeStamp: int-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

