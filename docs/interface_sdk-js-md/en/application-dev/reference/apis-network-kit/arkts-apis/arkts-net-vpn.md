# @ohos.net.vpn(VPN Management)

This module is the built-in VPN function provided by the OS. It allows users to set up VPN connections through the network settings of the OS. Generally, this module provides only limited functions and is subject to strict restrictions.

**Since:** 10

**System capability:** SystemCapability.Communication.NetManager.Vpn

## Modules to Import

```TypeScript
import vpn from '@kit.NetworkKit';
import vpnExtension from '@kit.NetworkKitExtension';
```

## Summary

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [addSysVpnConfig(VPN Management)](arkts-network-vpn-addsysvpnconfig-f-sys.md) | Add a system VPN network configuration. |
| [createVpnConnection(VPN Management)](arkts-network-vpn-createvpnconnection-f-sys.md) | Creates a VPN connection. |
| [deleteSysVpnConfig(VPN Management)](arkts-network-vpn-deletesysvpnconfig-f-sys.md) | Delete the configuration of system VPN network by the specified vpnId. |
| [getConnectedSysVpnConfig(VPN Management)](arkts-network-vpn-getconnectedsysvpnconfig-f-sys.md) | Get the connected VPN network configuration. |
| [getConnectedVpnAppInfo(VPN Management)](arkts-network-vpn-getconnectedvpnappinfo-f-sys.md) | Get the connected VPN App Info. |
| [getSysVpnConfig(VPN Management)](arkts-network-vpn-getsysvpnconfig-f-sys.md) | Get the configuration of system VPN network by the specified vpnId. |
| [getSysVpnConfigList(VPN Management)](arkts-network-vpn-getsysvpnconfiglist-f-sys.md) | Get all system VPN network configuration. |
| off(VPN Management) | Unsubscribes from vpn connect state changes. |
| off(VPN Management) | Unsubscribes from vpn connect state changes. |
| on(VPN Management) | Subscribes to vpn connect state changes. |
| on(VPN Management) | Subscribes to vpn connect state changes. |
<!--DelEnd-->

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [IpsecVpnConfig(VPN Management)](arkts-network-vpn-ipsecvpnconfig-i-sys.md) | Define configuration of the ipsec VPN network. |
| [L2tpVpnConfig(VPN Management)](arkts-network-vpn-l2tpvpnconfig-i-sys.md) | Define configuration of the l2tp VPN network. |
| [OpenVpnConfig(VPN Management)](arkts-network-vpn-openvpnconfig-i-sys.md) | Define configuration of the open VPN network. |
| [SysVpnConfig(VPN Management)](arkts-network-vpn-sysvpnconfig-i-sys.md) | Define configuration of the system VPN network. |
| [VpnConfig(VPN Management)](arkts-network-vpn-vpnconfig-i-sys.md) | Defines the VPN configuration. |
| [VpnConnection(VPN Management)](arkts-network-vpn-vpnconnection-i-sys.md) | Defines a VPN connection object. Before calling **VpnConnection** APIs, you need to create a VPN connection object by calling [vpn.createVpnConnection](arkts-network-vpn-createvpnconnection-f-sys.md). |
<!--DelEnd-->

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [SysVpnType(VPN Management)](arkts-network-vpn-sysvpntype-e-sys.md) | Defines the type for the VPN network. |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [AbilityContext(VPN Management)](arkts-network-vpn-abilitycontext-t.md) | The context of an ability. It allows access to ability-specific resources. |
| [LinkAddress(VPN Management)](arkts-network-vpn-linkaddress-t.md) | Defines the network link address information. |
| [RouteInfo(VPN Management)](arkts-network-vpn-routeinfo-t.md) | Defines the network route information. |
