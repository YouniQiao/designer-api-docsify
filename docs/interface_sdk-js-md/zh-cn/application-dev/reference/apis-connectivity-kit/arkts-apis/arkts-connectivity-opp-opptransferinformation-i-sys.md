# OppTransferInformation（系统接口）

Describes the transferred file information.

**起始版本：** 16

**ArkTS模式：** ArkTS-Dyn起始版本为16；ArkTS-Sta起始版本为26.0.0。

<!--Device-opp-interface OppTransferInformation--><!--Device-opp-interface OppTransferInformation-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { opp } from 'kits/@kit.ConnectivityKit';
```

## currentBytes

```TypeScript
currentBytes: long
```

Number of bytes of the file that have been transferred currently

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 16

**ArkTS模式：** ArkTS-Dyn起始版本为16；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OppTransferInformation-currentBytes: long--><!--Device-OppTransferInformation-currentBytes: long-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## currentCount

```TypeScript
currentCount: int
```

Number of files currently transferred

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 16

**ArkTS模式：** ArkTS-Dyn起始版本为16；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OppTransferInformation-currentCount: int--><!--Device-OppTransferInformation-currentCount: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## direction

```TypeScript
direction: DirectionType
```

File Transfer Direction

**类型：** [DirectionType](arkts-connectivity-opp-directiontype-e-sys.md)

**起始版本：** 16

**ArkTS模式：** ArkTS-Dyn起始版本为16；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OppTransferInformation-direction: DirectionType--><!--Device-OppTransferInformation-direction: DirectionType-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## filePath

```TypeScript
filePath: string
```

Path of the file to be transferred.

**类型：** string

**起始版本：** 16

**ArkTS模式：** ArkTS-Dyn起始版本为16；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OppTransferInformation-filePath: string--><!--Device-OppTransferInformation-filePath: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## remoteDeviceId

```TypeScript
remoteDeviceId: string
```

Device Address of the peer transmission object

**类型：** string

**起始版本：** 16

**ArkTS模式：** ArkTS-Dyn起始版本为16；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OppTransferInformation-remoteDeviceId: string--><!--Device-OppTransferInformation-remoteDeviceId: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## remoteDeviceName

```TypeScript
remoteDeviceName: string
```

Device name of the peer transmission object

**类型：** string

**起始版本：** 16

**ArkTS模式：** ArkTS-Dyn起始版本为16；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OppTransferInformation-remoteDeviceName: string--><!--Device-OppTransferInformation-remoteDeviceName: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## result

```TypeScript
result: TransferResult
```

File transfer result

**类型：** [TransferResult](arkts-connectivity-opp-transferresult-e-sys.md)

**起始版本：** 16

**ArkTS模式：** ArkTS-Dyn起始版本为16；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OppTransferInformation-result: TransferResult--><!--Device-OppTransferInformation-result: TransferResult-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## status

```TypeScript
status: TransferStatus
```

File transfer status

**类型：** [TransferStatus](../../apis-telephony-kit/arkts-apis/arkts-telephony-call-transferstatus-e.md)

**起始版本：** 16

**ArkTS模式：** ArkTS-Dyn起始版本为16；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OppTransferInformation-status: TransferStatus--><!--Device-OppTransferInformation-status: TransferStatus-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## totalBytes

```TypeScript
totalBytes: long
```

Total number of file bytes to transfer

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 16

**ArkTS模式：** ArkTS-Dyn起始版本为16；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OppTransferInformation-totalBytes: long--><!--Device-OppTransferInformation-totalBytes: long-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

## totalCount

```TypeScript
totalCount: int
```

Total number of transferred files

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 16

**ArkTS模式：** ArkTS-Dyn起始版本为16；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OppTransferInformation-totalCount: int--><!--Device-OppTransferInformation-totalCount: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**系统接口：** 此接口为系统接口。

