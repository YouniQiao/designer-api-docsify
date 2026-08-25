# @ohos.nearlink.remoteDevice(星闪远端设备连接能力)

本模块提供了星闪远端设备的连接与管理能力，包括连接与断开远端设备、可信配对与确认、调整连接间隔、订阅配对请求等。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Base

## 导入模块

```TypeScript
import { remoteDevice } from 'kits/@kit.ConnectivityKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [createRemoteDevice(星闪远端设备连接能力)](arkts-connectivity-remotedevice-createremotedevice-f.md) |
| [offAcbStateChange(星闪远端设备连接能力)](arkts-connectivity-remotedevice-offacbstatechange-f.md) |
| [offConnectionStateChange(星闪远端设备连接能力)](arkts-connectivity-remotedevice-offconnectionstatechange-f.md) |
| [offPairingStateChange(星闪远端设备连接能力)](arkts-connectivity-remotedevice-offpairingstatechange-f.md) |
| [onAcbStateChange(星闪远端设备连接能力)](arkts-connectivity-remotedevice-onacbstatechange-f.md) |
| [onConnectionStateChange(星闪远端设备连接能力)](arkts-connectivity-remotedevice-onconnectionstatechange-f.md) |
| [onPairingStateChange(星闪远端设备连接能力)](arkts-connectivity-remotedevice-onpairingstatechange-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [offPairingRequest(星闪远端设备连接能力)](arkts-connectivity-remotedevice-offpairingrequest-f-sys.md) |
| [onPairingRequest(星闪远端设备连接能力)](arkts-connectivity-remotedevice-onpairingrequest-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [AcbStateParam(星闪远端设备连接能力)](arkts-connectivity-remotedevice-acbstateparam-i.md) |
| [ConnectionStateParam(星闪远端设备连接能力)](arkts-connectivity-remotedevice-connectionstateparam-i.md) |
| [DeviceInformation(星闪远端设备连接能力)](arkts-connectivity-remotedevice-deviceinformation-i.md) |
| [PairingRequestParam(星闪远端设备连接能力)](arkts-connectivity-remotedevice-pairingrequestparam-i.md) |
| [PairingStateParam(星闪远端设备连接能力)](arkts-connectivity-remotedevice-pairingstateparam-i.md) |
| [RemoteDevice(星闪远端设备连接能力)](arkts-connectivity-remotedevice-remotedevice-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [DeviceModel(星闪远端设备连接能力)](arkts-connectivity-remotedevice-devicemodel-i-sys.md) |
| [RemoteDevice(星闪远端设备连接能力)](arkts-connectivity-remotedevice-remotedevice-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [ConnectionReason(星闪远端设备连接能力)](arkts-connectivity-remotedevice-connectionreason-e.md) |
| [PairingReason(星闪远端设备连接能力)](arkts-connectivity-remotedevice-pairingreason-e.md) |
| [PairingType(星闪远端设备连接能力)](arkts-connectivity-remotedevice-pairingtype-e.md) |

### 类型

| 名称 |
| --- |
| [AcbState(星闪远端设备连接能力)](arkts-connectivity-remotedevice-acbstate-t.md) |
| [ConnectionState(星闪远端设备连接能力)](arkts-connectivity-remotedevice-connectionstate-t.md) |
| [DeviceClass(星闪远端设备连接能力)](arkts-connectivity-remotedevice-deviceclass-t.md) |
| [PairingState(星闪远端设备连接能力)](arkts-connectivity-remotedevice-pairingstate-t.md) |

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [ConnectionInterval(星闪远端设备连接能力)](arkts-connectivity-remotedevice-connectioninterval-t-sys.md) |
<!--DelEnd-->
