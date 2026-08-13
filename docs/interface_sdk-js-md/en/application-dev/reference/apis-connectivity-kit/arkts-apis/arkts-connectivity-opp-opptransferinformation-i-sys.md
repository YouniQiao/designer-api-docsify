# OppTransferInformation (System API)

Describes the transferred file information.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-opp-interface OppTransferInformation--><!--Device-opp-interface OppTransferInformation-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { opp } from '@kit.ConnectivityKit';
```

## currentBytes

```TypeScript
currentBytes: long
```

Number of bytes of the file that have been transferred currently

**Type:** long

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppTransferInformation-currentBytes: long--><!--Device-OppTransferInformation-currentBytes: long-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

## currentCount

```TypeScript
currentCount: int
```

Number of files currently transferred

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppTransferInformation-currentCount: int--><!--Device-OppTransferInformation-currentCount: int-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

## direction

```TypeScript
direction: DirectionType
```

File Transfer Direction

**Type:** [DirectionType](arkts-connectivity-opp-directiontype-e-sys.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppTransferInformation-direction: DirectionType--><!--Device-OppTransferInformation-direction: DirectionType-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

## filePath

```TypeScript
filePath: string
```

Path of the file to be transferred.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppTransferInformation-filePath: string--><!--Device-OppTransferInformation-filePath: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

## remoteDeviceId

```TypeScript
remoteDeviceId: string
```

Device Address of the peer transmission object

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppTransferInformation-remoteDeviceId: string--><!--Device-OppTransferInformation-remoteDeviceId: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

## remoteDeviceName

```TypeScript
remoteDeviceName: string
```

Device name of the peer transmission object

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppTransferInformation-remoteDeviceName: string--><!--Device-OppTransferInformation-remoteDeviceName: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

## result

```TypeScript
result: TransferResult
```

File transfer result

**Type:** [TransferResult](arkts-connectivity-opp-transferresult-e-sys.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppTransferInformation-result: TransferResult--><!--Device-OppTransferInformation-result: TransferResult-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

## status

```TypeScript
status: TransferStatus
```

File transfer status

**Type:** TransferStatus

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppTransferInformation-status: TransferStatus--><!--Device-OppTransferInformation-status: TransferStatus-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

## totalBytes

```TypeScript
totalBytes: long
```

Total number of file bytes to transfer

**Type:** long

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppTransferInformation-totalBytes: long--><!--Device-OppTransferInformation-totalBytes: long-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

## totalCount

```TypeScript
totalCount: int
```

Total number of transferred files

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppTransferInformation-totalCount: int--><!--Device-OppTransferInformation-totalCount: int-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

