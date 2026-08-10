# @ohos.nearlink.manager

提供管理星闪设备的方法。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace manager--><!--Device-unnamed-declare namespace manager-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { manager } from 'kits/@kit.ConnectivityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getLocalName](arkts-connectivity-manager-getlocalname-f.md#getlocalname) | 获取本地设备的名称。 |
| [getPairedDevices](arkts-connectivity-manager-getpaireddevices-f.md#getpaireddevices) | 获取已与当前设备配对的设备列表。如果用户有ohos.permission.GET_NEARLINK_PEER_MAC权限，则返回真实设备地址。否则，返回随机的设备地址 |
| [getState](arkts-connectivity-manager-getstate-f.md#getstate) | 获取星闪状态。 |
| [isNearLinkSupported](arkts-connectivity-manager-isnearlinksupported-f.md#isnearlinksupported) | 检查当前设备是否支持星闪。 |
| [offStateChange](arkts-connectivity-manager-offstatechange-f.md#offstatechange) | 取消订阅状态变更事件。 |
| [onStateChange](arkts-connectivity-manager-onstatechange-f.md#onstatechange) | 订阅状态变更事件。 |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [disable](arkts-connectivity-manager-disable-f-sys.md#disable) | 关闭星闪。 |
| [enable](arkts-connectivity-manager-enable-f-sys.md#enable) | 开启星闪。 |
| [factoryReset](arkts-connectivity-manager-factoryreset-f-sys.md#factoryreset) | 恢复星闪设置。 |
| [getLocalAddress](arkts-connectivity-manager-getlocaladdress-f-sys.md#getlocaladdress) | 获取本端设备的MAC地址。 |
| [setConnectionMode](arkts-connectivity-manager-setconnectionmode-f-sys.md#setconnectionmode) | 设置设备的NearLink连接模式。 |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [NearlinkState](arkts-connectivity-manager-nearlinkstate-e.md) | 星闪状态的枚举。 |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [ConnectionMode](arkts-connectivity-manager-connectionmode-e-sys.md) | 连接模式的枚举。 |
<!--DelEnd-->

