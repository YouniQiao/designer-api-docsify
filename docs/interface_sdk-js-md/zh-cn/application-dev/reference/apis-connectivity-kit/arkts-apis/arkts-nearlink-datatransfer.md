# @ohos.nearlink.dataTransfer(星闪数传能力)

本模块提供了星闪数据传输功能，包括端口通道管理、连接管理、数据收发、连接状态查询与订阅等。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Base

## 导入模块

```TypeScript
import { dataTransfer } from '@kit.ConnectivityKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [connect(星闪数传能力)](arkts-connectivity-datatransfer-connect-f.md) |
| [createPort(星闪数传能力)](arkts-connectivity-datatransfer-createport-f.md) |
| [destroyPort(星闪数传能力)](arkts-connectivity-datatransfer-destroyport-f.md) |
| [disconnect(星闪数传能力)](arkts-connectivity-datatransfer-disconnect-f.md) |
| [getConnectionState(星闪数传能力)](arkts-connectivity-datatransfer-getconnectionstate-f.md) |
| [offConnectionStateChanged(星闪数传能力)](arkts-connectivity-datatransfer-offconnectionstatechanged-f.md) |
| [offReadData(星闪数传能力)](arkts-connectivity-datatransfer-offreaddata-f.md) |
| [onConnectionStateChanged(星闪数传能力)](arkts-connectivity-datatransfer-onconnectionstatechanged-f.md) |
| [onReadData(星闪数传能力)](arkts-connectivity-datatransfer-onreaddata-f.md) |
| [writeData(星闪数传能力)](arkts-connectivity-datatransfer-writedata-f.md) |

### 接口

| 名称 |
| --- |
| [ConnectionParams(星闪数传能力)](arkts-connectivity-datatransfer-connectionparams-i.md) |
| [ConnectionResult(星闪数传能力)](arkts-connectivity-datatransfer-connectionresult-i.md) |
| [ConnectionStateParams(星闪数传能力)](arkts-connectivity-datatransfer-connectionstateparams-i.md) |
| [DataParams(星闪数传能力)](arkts-connectivity-datatransfer-dataparams-i.md) |

### 枚举

| 名称 |
| --- |
| [TransferMode(星闪数传能力)](arkts-connectivity-datatransfer-transfermode-e.md) |

### 类型

| 名称 |
| --- |
| [ConnectionState(星闪数传能力)](arkts-connectivity-datatransfer-connectionstate-t.md) |
