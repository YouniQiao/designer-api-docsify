# DataSendProgressInfo

This interface is used to monitor the progress of sending data.

**Since:** 15

<!--Device-http-export interface DataSendProgressInfo--><!--Device-http-export interface DataSendProgressInfo-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { http } from '@kit.NetworkKit';
```

## sendSize

```TypeScript
sendSize: number
```

Used to specify the data size to be sent.

**Type:** number

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-DataSendProgressInfo-sendSize: int--><!--Device-DataSendProgressInfo-sendSize: int-End-->

**System capability:** SystemCapability.Communication.NetStack

## totalSize

```TypeScript
totalSize: number
```

Total number of bytes to receive.

**Type:** number

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-DataSendProgressInfo-totalSize: int--><!--Device-DataSendProgressInfo-totalSize: int-End-->

**System capability:** SystemCapability.Communication.NetStack

