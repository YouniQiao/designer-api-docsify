# CellInformation

小区信息。

**起始版本：** 23

<!--Device-radio-export interface CellInformation--><!--Device-radio-export interface CellInformation-End-->

**系统能力：** SystemCapability.Telephony.CoreService

## 导入模块

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## data

```TypeScript
data: CdmaCellInformation | GsmCellInformation | LteCellInformation | NrCellInformation | TdscdmaCellInformation
      | WcdmaCellInformation
```

Obtains signal strength under different network formats.

**类型：** [CdmaCellInformation](arkts-telephony-radio-cdmacellinformation-i-sys.md) \| [GsmCellInformation](arkts-telephony-radio-gsmcellinformation-i-sys.md) \| [LteCellInformation](arkts-telephony-radio-ltecellinformation-i-sys.md) \| [NrCellInformation](arkts-telephony-radio-nrcellinformation-i-sys.md) \| [TdscdmaCellInformation](arkts-telephony-radio-tdscdmacellinformation-i-sys.md) \| [WcdmaCellInformation](arkts-telephony-radio-wcdmacellinformation-i-sys.md)

**起始版本：** 23

<!--Device-CellInformation-data: CdmaCellInformation | GsmCellInformation | LteCellInformation | NrCellInformation | TdscdmaCellInformation      | WcdmaCellInformation--><!--Device-CellInformation-data: CdmaCellInformation | GsmCellInformation | LteCellInformation | NrCellInformation | TdscdmaCellInformation      | WcdmaCellInformation-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

## isCamped

```TypeScript
isCamped: boolean
```

Obtains the camp-on status of the serving cell.Returns {@code true} if the user equipment (UE) is camped on the cell; returns {@code false} otherwise.

**类型：** boolean

**起始版本：** 23

<!--Device-CellInformation-isCamped: boolean--><!--Device-CellInformation-isCamped: boolean-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

## timeStamp

```TypeScript
timeStamp: int
```

Obtains the timestamp when the cell information is obtained.Returns a timestamp since boot, in nanoseconds.

**类型：** int

**起始版本：** 23

<!--Device-CellInformation-timeStamp: int--><!--Device-CellInformation-timeStamp: int-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

