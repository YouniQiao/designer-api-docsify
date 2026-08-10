# @ohos.net.vpnExtension

Provides VPN related interfaces.

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-unnamed-declare namespace vpnExtension--><!--Device-unnamed-declare namespace vpnExtension-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

## 导入模块

```TypeScript
import { vpnExtension } from 'kits/@kit.NetworkKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [createVpnConnection](arkts-network-vpnextension-createvpnconnection-f.md#createvpnconnection) | Create a VPN connection using the VpnExtensionContext. |
| [createVpnObserver](arkts-network-vpnextension-createvpnobserver-f.md#createvpnobserver) | Create a VPN observer. |
| [startVpnExtensionAbility](arkts-network-vpnextension-startvpnextensionability-f.md#startvpnextensionability) | Starts a new vpn extension ability. |
| [stopVpnExtensionAbility](arkts-network-vpnextension-stopvpnextensionability-f.md#stopvpnextensionability) | Stops a service within the same application. |

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [isAlwaysOnVpnEnabled](arkts-network-vpnextension-isalwaysonvpnenabled-f-sys.md#isalwaysonvpnenabled) | Get the Always on VPN mode status for a device. |
| [setAlwaysOnVpnEnabled](arkts-network-vpnextension-setalwaysonvpnenabled-f-sys.md#setalwaysonvpnenabled) | Set the Enable/Disable Always on VPN mode for a device. |
| [updateVpnAuthorizedState](arkts-network-vpnextension-updatevpnauthorizedstate-f-sys.md#updatevpnauthorizedstate) | Update a VPN dialog authorize information |
<!--DelEnd-->

### 接口

| 名称 | 说明 |
| --- | --- |
| [VpnConfig](arkts-network-vpnextension-vpnconfig-i.md) | Define configuration of the VPN network. |
| [VpnConnection](arkts-network-vpnextension-vpnconnection-i.md) | Defines a VPN connection. |
| [VpnObserver](arkts-network-vpnextension-vpnobserver-i.md) | Defines a VPN observer. |

### 类型

| 名称 | 说明 |
| --- | --- |
| [LinkAddress](arkts-network-vpnextension-linkaddress-t.md) | Get network link information. |
| [RouteInfo](arkts-network-vpnextension-routeinfo-t.md) | Get network route information. |
| [VpnExtensionContext](arkts-network-vpnextension-vpnextensioncontext-t.md) | The context of vpn extension. It allows access to serviceExtension-specific resources. |

