# @ohos.net.vpn(VPN管理)

本模块是操作系统提供的内置VPN功能，允许用户通过系统的网络设置进行VPN连接，通常提供的功能较少，而且有比较严格的限制。

> **说明：**&gt;
> 本模块首批接口从 API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.NetManager.Vpn

## 导入模块

```TypeScript
import { vpn } from 'kits/@kit.NetworkKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addSysVpnConfig(VPN管理)](arkts-network-vpn-addsysvpnconfig-f-sys.md) |
| [createVpnConnection(VPN管理)](arkts-network-vpn-createvpnconnection-f-sys.md) |
| [deleteSysVpnConfig(VPN管理)](arkts-network-vpn-deletesysvpnconfig-f-sys.md) |
| [getConnectedSysVpnConfig(VPN管理)](arkts-network-vpn-getconnectedsysvpnconfig-f-sys.md) |
| [getConnectedVpnAppInfo(VPN管理)](arkts-network-vpn-getconnectedvpnappinfo-f-sys.md) |
| [getSysVpnConfig(VPN管理)](arkts-network-vpn-getsysvpnconfig-f-sys.md) |
| [getSysVpnConfigList(VPN管理)](arkts-network-vpn-getsysvpnconfiglist-f-sys.md) |
| off(VPN管理) |
| off(VPN管理) |
| on(VPN管理) |
| on(VPN管理) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [IpsecVpnConfig(VPN管理)](arkts-network-vpn-ipsecvpnconfig-i-sys.md) |
| [L2tpVpnConfig(VPN管理)](arkts-network-vpn-l2tpvpnconfig-i-sys.md) |
| [OpenVpnConfig(VPN管理)](arkts-network-vpn-openvpnconfig-i-sys.md) |
| [SysVpnConfig(VPN管理)](arkts-network-vpn-sysvpnconfig-i-sys.md) |
| [VpnConfig(VPN管理)](arkts-network-vpn-vpnconfig-i-sys.md) |
| [VpnConnection(VPN管理)](arkts-network-vpn-vpnconnection-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [SysVpnType(VPN管理)](arkts-network-vpn-sysvpntype-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [AbilityContext(VPN管理)](arkts-network-vpn-abilitycontext-t.md) |
| [LinkAddress(VPN管理)](arkts-network-vpn-linkaddress-t.md) |
| [RouteInfo(VPN管理)](arkts-network-vpn-routeinfo-t.md) |
