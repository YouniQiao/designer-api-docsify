# DataReceiveProgressInfo

This interface is used to obtain the progress information of file upload or download.

**Since:** 15

<!--Device-http-export interface DataReceiveProgressInfo--><!--Device-http-export interface DataReceiveProgressInfo-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { http } from '@kit.NetworkKit';
```

## receiveSize

```TypeScript
receiveSize: number
```

Number of data bytes received.

**Type:** number

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-DataReceiveProgressInfo-receiveSize: int--><!--Device-DataReceiveProgressInfo-receiveSize: int-End-->

**System capability:** SystemCapability.Communication.NetStack

## totalSize

```TypeScript
totalSize: number
```

Total number of bytes to receive.

**Type:** number

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-DataReceiveProgressInfo-totalSize: int--><!--Device-DataReceiveProgressInfo-totalSize: int-End-->

**System capability:** SystemCapability.Communication.NetStack

