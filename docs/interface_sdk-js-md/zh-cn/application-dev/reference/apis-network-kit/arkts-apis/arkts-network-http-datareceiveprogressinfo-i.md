# DataReceiveProgressInfo

This interface is used to obtain the progress information of file upload or download.

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为26.0.0。

<!--Device-http-export interface DataReceiveProgressInfo--><!--Device-http-export interface DataReceiveProgressInfo-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { http } from 'kits/@kit.NetworkKit';
```

## receiveSize

```TypeScript
receiveSize: int
```

Number of data bytes received.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-DataReceiveProgressInfo-receiveSize: int--><!--Device-DataReceiveProgressInfo-receiveSize: int-End-->

**系统能力：** SystemCapability.Communication.NetStack

## totalSize

```TypeScript
totalSize: int
```

Total number of bytes to receive.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-DataReceiveProgressInfo-totalSize: int--><!--Device-DataReceiveProgressInfo-totalSize: int-End-->

**系统能力：** SystemCapability.Communication.NetStack

