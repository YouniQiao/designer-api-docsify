# DataSendProgressInfo

This interface is used to monitor the progress of sending data.

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为26.0.0。

<!--Device-http-export interface DataSendProgressInfo--><!--Device-http-export interface DataSendProgressInfo-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { http } from 'kits/@kit.NetworkKit';
```

## sendSize

```TypeScript
sendSize: int
```

Used to specify the data size to be sent.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-DataSendProgressInfo-sendSize: int--><!--Device-DataSendProgressInfo-sendSize: int-End-->

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

<!--Device-DataSendProgressInfo-totalSize: int--><!--Device-DataSendProgressInfo-totalSize: int-End-->

**系统能力：** SystemCapability.Communication.NetStack

