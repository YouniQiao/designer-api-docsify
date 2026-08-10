# NrCellInformation（系统接口）

Obtains NR cell information.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-radio-export interface NrCellInformation--><!--Device-radio-export interface NrCellInformation-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## mcc

```TypeScript
mcc: string
```

Indicates the mobile country code.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-NrCellInformation-mcc: string--><!--Device-NrCellInformation-mcc: string-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

## mnc

```TypeScript
mnc: string
```

Indicates the mobile network code.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-NrCellInformation-mnc: string--><!--Device-NrCellInformation-mnc: string-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

## nci

```TypeScript
nci: int
```

Indicates the 5G network cell ID.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-NrCellInformation-nci: int--><!--Device-NrCellInformation-nci: int-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

## nrArfcn

```TypeScript
nrArfcn: int
```

Indicates the NR-ARFCN(NR Absolute Radio Frequency Channel Number).

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-NrCellInformation-nrArfcn: int--><!--Device-NrCellInformation-nrArfcn: int-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

## pci

```TypeScript
pci: int
```

Indicates the physical cell identification.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-NrCellInformation-pci: int--><!--Device-NrCellInformation-pci: int-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

## tac

```TypeScript
tac: int
```

Indicates the tracking area code.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-NrCellInformation-tac: int--><!--Device-NrCellInformation-tac: int-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

