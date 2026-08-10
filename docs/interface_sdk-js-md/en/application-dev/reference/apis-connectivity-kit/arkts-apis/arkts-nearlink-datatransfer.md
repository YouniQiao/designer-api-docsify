# @ohos.nearlink.dataTransfer

提供操作和管理星闪数据传输的方法。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace dataTransfer--><!--Device-unnamed-declare namespace dataTransfer-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { dataTransfer } from 'kits/@kit.ConnectivityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [connect](arkts-connectivity-datatransfer-connect-f.md#connect) | 连接服务端。如果连接成功，则可以向服务端发送数据。 |
| [createPort](arkts-connectivity-datatransfer-createport-f.md#createport) | 通过UUID创建可以接收数据的星闪端口。 |
| [destroyPort](arkts-connectivity-datatransfer-destroyport-f.md#destroyport) | 根据UUID销毁监听端口并释放相关资源。 |
| [disconnect](arkts-connectivity-datatransfer-disconnect-f.md#disconnect) | 断开或停止与服务端的连接。 |
| [getConnectionState](arkts-connectivity-datatransfer-getconnectionstate-f.md#getconnectionstate) | 获取数据传输的连接状态。 |
| [offConnectionStateChanged](arkts-connectivity-datatransfer-offconnectionstatechanged-f.md#offconnectionstatechanged) | 取消订阅连接状态变更事件。 |
| [offReadData](arkts-connectivity-datatransfer-offreaddata-f.md#offreaddata) | 取消订阅从端口读取数据的事件。 |
| [onConnectionStateChanged](arkts-connectivity-datatransfer-onconnectionstatechanged-f.md#onconnectionstatechanged) | 订阅连接状态变化事件。  只有授予了ohos.permission.NEARLINK_ACCESS权限的应用程序才能访问此事件。 |
| [onReadData](arkts-connectivity-datatransfer-onreaddata-f.md#onreaddata) | 订阅从端口读取数据事件。  只有授予了ohos.permission.NEARLINK_ACCESS权限的应用程序才能访问此事件。 |
| [writeData](arkts-connectivity-datatransfer-writedata-f.md#writedata) | 根据地址和UUID写入数据。 |

### Interfaces

| Name | Description |
| --- | --- |
| [ConnectionParams](arkts-connectivity-datatransfer-connectionparams-i.md) | 连接参数。 |
| [ConnectionResult](arkts-connectivity-datatransfer-connectionresult-i.md) | 连接结果的参数说明。 |
| [ConnectionStateParams](arkts-connectivity-datatransfer-connectionstateparams-i.md) | 获取连接状态所需的参数。 |
| [DataParams](arkts-connectivity-datatransfer-dataparams-i.md) | 数据参数说明。 |

### Enums

| Name | Description |
| --- | --- |
| [TransferMode](arkts-connectivity-datatransfer-transfermode-e.md) | 数据传输模式。 |

### Types

| Name | Description |
| --- | --- |
| [ConnectionState](arkts-connectivity-datatransfer-connectionstate-t.md) | 连接状态。 |

