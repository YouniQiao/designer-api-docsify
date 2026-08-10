# @ohos.nearlink.remoteDevice

提供与远端设备的配对、连接等交互方式。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace remoteDevice--><!--Device-unnamed-declare namespace remoteDevice-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { remoteDevice } from 'kits/@kit.ConnectivityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createRemoteDevice](arkts-connectivity-remotedevice-createremotedevice-f.md#createremotedevice) | 创建远端设备实例。 |
| [offAcbStateChange](arkts-connectivity-remotedevice-offacbstatechange-f.md#offacbstatechange) | 取消订阅星闪 ACB连接状态更改事件。 |
| [offConnectionStateChange](arkts-connectivity-remotedevice-offconnectionstatechange-f.md#offconnectionstatechange) | 取消订阅星闪连接状态更改事件。 |
| [offPairingStateChange](arkts-connectivity-remotedevice-offpairingstatechange-f.md#offpairingstatechange) | 取消订阅星闪配对状态更改事件。 |
| [onAcbStateChange](arkts-connectivity-remotedevice-onacbstatechange-f.md#onacbstatechange) | 订阅NearLink ACB连接状态变化事件。ACB采用异步双向链路。 |
| [onConnectionStateChange](arkts-connectivity-remotedevice-onconnectionstatechange-f.md#onconnectionstatechange) | 订阅星闪连接状态更改事件。如果用户有ohos.permission.GET_NEARLINK_PEER_MAC权限，则返回真实设备地址。否则返回一个随机的设备地址。  只有授予了ohos.permission.NEARLINK_ACCESS权限的应用程序才能访问此事件。如果应用被赋予了ohos.permission.GET_NEARLINK_PEER_MAC权限。回调返回真实设备地址，否则返回随机设备地址。 |
| [onPairingStateChange](arkts-connectivity-remotedevice-onpairingstatechange-f.md#onpairingstatechange) | 订阅NearLink配对状态变更事件。  只有授予了ohos.permission.NEARLINK_ACCESS权限的应用程序才能访问此事件。如果应用被赋予了ohos.permission.GET_NEARLINK_PEER_MAC权限。回调返回真实设备地址，否则返回随机设备地址。 |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [offPairingRequest](arkts-connectivity-remotedevice-offpairingrequest-f-sys.md#offpairingrequest) | 取消订阅来自远端星闪设备的配对请求事件。 |
| [onPairingRequest](arkts-connectivity-remotedevice-onpairingrequest-f-sys.md#onpairingrequest) | 订阅来自远程NearLink设备的配对请求事件。如果用户被赋予了ohos.permission.GET_NEARLINK_PEER_MAC权限。回调返回真实设备地址，否则返回随机设备地址  只有授予了ohos.permission.NEARLINK_ACCESS权限的系统应用程序才能访问此事件。如果应用被赋予了ohos.permission.GET_NEARLINK_PEER_MAC权限。回调返回真实设备地址，否则返回随机设备地址。 |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [AcbStateParam](arkts-connectivity-remotedevice-acbstateparam-i.md) | ACB连接状态参数。 |
| [ConnectionStateParam](arkts-connectivity-remotedevice-connectionstateparam-i.md) | 连接状态参数。 |
| [DeviceInformation](arkts-connectivity-remotedevice-deviceinformation-i.md) | 描述远端设备信息。 |
| [PairingRequestParam](arkts-connectivity-remotedevice-pairingrequestparam-i.md) | 配对请求参数说明。 |
| [PairingStateParam](arkts-connectivity-remotedevice-pairingstateparam-i.md) | 配对状态参数。 |
| [RemoteDevice](arkts-connectivity-remotedevice-remotedevice-i.md) | 远程设备操作方法。 |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [DeviceModel](arkts-connectivity-remotedevice-devicemodel-i-sys.md) | 远程设备的型号信息。 |
| [RemoteDevice](arkts-connectivity-remotedevice-remotedevice-i-sys.md) | 远程设备操作方法。 |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [ConnectionReason](arkts-connectivity-remotedevice-connectionreason-e.md) | 连接原因的枚举。 |
| [PairingReason](arkts-connectivity-remotedevice-pairingreason-e.md) | 配对原因的枚举。 |
| [PairingType](arkts-connectivity-remotedevice-pairingtype-e.md) | 配对类型的枚举。 |

### Types

| Name | Description |
| --- | --- |
| [AcbState](arkts-connectivity-remotedevice-acbstate-t.md) | ACB（异步面向连接的双向）连接状态。 |
| [ConnectionState](arkts-connectivity-remotedevice-connectionstate-t.md) | 连接状态。 |
| [DeviceClass](arkts-connectivity-remotedevice-deviceclass-t.md) | 设备类型。 |
| [PairingState](arkts-connectivity-remotedevice-pairingstate-t.md) | 配对状态。 |

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [ConnectionInterval](arkts-connectivity-remotedevice-connectioninterval-t-sys.md) | 连接间隔。 |
<!--DelEnd-->

