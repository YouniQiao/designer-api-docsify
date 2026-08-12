# DataReceiveProgressInfo

This interface is used to obtain the progress information of file upload or download.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 26.0.0.

<!--Device-http-export interface DataReceiveProgressInfo--><!--Device-http-export interface DataReceiveProgressInfo-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { http } from '@kit.NetworkKit';
```

## receiveSize

```TypeScript
receiveSize: int
```

Number of data bytes received.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-DataReceiveProgressInfo-receiveSize: int--><!--Device-DataReceiveProgressInfo-receiveSize: int-End-->

**System capability:** SystemCapability.Communication.NetStack

## totalSize

```TypeScript
totalSize: int
```

Total number of bytes to receive.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-DataReceiveProgressInfo-totalSize: int--><!--Device-DataReceiveProgressInfo-totalSize: int-End-->

**System capability:** SystemCapability.Communication.NetStack

