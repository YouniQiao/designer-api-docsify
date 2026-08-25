# @ohos.enterprise.networkManager(网络管理)

本模块提供设备网络管理能力，包括查询设备IP地址、MAC地址信息、管理网络接口状态、配置网络全局代理、管理防火墙规则和域名过滤规则、控制移动数据网络、管理APN配置、配置以太网网络等。适用于企业IT管理员对设备网络进行集中管理和安全管 控，帮助企业实现网络访问策略统一管理、防止网络攻击和数据泄露、降低网络管理成本。

> **说明：**&gt;
> 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 导入模块

```TypeScript
import { networkManager } from '@kit.MDMKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [addApn(网络管理)](arkts-mdm-networkmanager-addapn-f.md) |
| [addDomainFilterRule(网络管理)](arkts-mdm-networkmanager-adddomainfilterrule-f.md) |
| [addFirewallRule(网络管理)](arkts-mdm-networkmanager-addfirewallrule-f.md) |
| [deleteApn(网络管理)](arkts-mdm-networkmanager-deleteapn-f.md) |
| [getAllNetworkInterfacesSync(网络管理)](arkts-mdm-networkmanager-getallnetworkinterfacessync-f.md) |
| [getDomainFilterRules(网络管理)](arkts-mdm-networkmanager-getdomainfilterrules-f.md) |
| [getFirewallRules(网络管理)](arkts-mdm-networkmanager-getfirewallrules-f.md) |
| [getGlobalProxyForAccount(网络管理)](arkts-mdm-networkmanager-getglobalproxyforaccount-f.md) |
| [getGlobalProxySync(网络管理)](arkts-mdm-networkmanager-getglobalproxysync-f.md) |
| [getIpAddressSync(网络管理)](arkts-mdm-networkmanager-getipaddresssync-f.md) |
| [getMacSync(网络管理)](arkts-mdm-networkmanager-getmacsync-f.md) |
| [isNetworkInterfaceDisabledSync(网络管理)](arkts-mdm-networkmanager-isnetworkinterfacedisabledsync-f.md) |
| [isNetworkInterfaceDisabledSync(网络管理)](arkts-mdm-networkmanager-isnetworkinterfacedisabledsync-f.md) |
| [queryApn(网络管理)](arkts-mdm-networkmanager-queryapn-f.md) |
| [queryApn(网络管理)](arkts-mdm-networkmanager-queryapn-f.md) |
| [removeDomainFilterRule(网络管理)](arkts-mdm-networkmanager-removedomainfilterrule-f.md) |
| [removeFirewallRule(网络管理)](arkts-mdm-networkmanager-removefirewallrule-f.md) |
| [setEthernetConfig(网络管理)](arkts-mdm-networkmanager-setethernetconfig-f.md) |
| [setGlobalProxyForAccount(网络管理)](arkts-mdm-networkmanager-setglobalproxyforaccount-f.md) |
| [setGlobalProxySync(网络管理)](arkts-mdm-networkmanager-setglobalproxysync-f.md) |
| [setNetworkInterfaceDisabledSync(网络管理)](arkts-mdm-networkmanager-setnetworkinterfacedisabledsync-f.md) |
| [setPreferredApn(网络管理)](arkts-mdm-networkmanager-setpreferredapn-f.md) |
| [turnOffMobileData(网络管理)](arkts-mdm-networkmanager-turnoffmobiledata-f.md) |
| [turnOnMobileData(网络管理)](arkts-mdm-networkmanager-turnonmobiledata-f.md) |
| [updateApn(网络管理)](arkts-mdm-networkmanager-updateapn-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addIptablesFilterRule(网络管理)](arkts-mdm-networkmanager-addiptablesfilterrule-f-sys.md) |
| [addIptablesFilterRule(网络管理)](arkts-mdm-networkmanager-addiptablesfilterrule-f-sys.md) |
| [getAllNetworkInterfaces(网络管理)](arkts-mdm-networkmanager-getallnetworkinterfaces-f-sys.md) |
| [getAllNetworkInterfaces(网络管理)](arkts-mdm-networkmanager-getallnetworkinterfaces-f-sys.md) |
| [getGlobalProxy(网络管理)](arkts-mdm-networkmanager-getglobalproxy-f-sys.md) |
| [getGlobalProxy(网络管理)](arkts-mdm-networkmanager-getglobalproxy-f-sys.md) |
| [getIpAddress(网络管理)](arkts-mdm-networkmanager-getipaddress-f-sys.md) |
| [getIpAddress(网络管理)](arkts-mdm-networkmanager-getipaddress-f-sys.md) |
| [getMac(网络管理)](arkts-mdm-networkmanager-getmac-f-sys.md) |
| [getMac(网络管理)](arkts-mdm-networkmanager-getmac-f-sys.md) |
| [isNetworkInterfaceDisabled(网络管理)](arkts-mdm-networkmanager-isnetworkinterfacedisabled-f-sys.md) |
| [isNetworkInterfaceDisabled(网络管理)](arkts-mdm-networkmanager-isnetworkinterfacedisabled-f-sys.md) |
| [listIptablesFilterRules(网络管理)](arkts-mdm-networkmanager-listiptablesfilterrules-f-sys.md) |
| [listIptablesFilterRules(网络管理)](arkts-mdm-networkmanager-listiptablesfilterrules-f-sys.md) |
| [removeIptablesFilterRule(网络管理)](arkts-mdm-networkmanager-removeiptablesfilterrule-f-sys.md) |
| [removeIptablesFilterRule(网络管理)](arkts-mdm-networkmanager-removeiptablesfilterrule-f-sys.md) |
| [setGlobalProxy(网络管理)](arkts-mdm-networkmanager-setglobalproxy-f-sys.md) |
| [setGlobalProxy(网络管理)](arkts-mdm-networkmanager-setglobalproxy-f-sys.md) |
| [setNetworkInterfaceDisabled(网络管理)](arkts-mdm-networkmanager-setnetworkinterfacedisabled-f-sys.md) |
| [setNetworkInterfaceDisabled(网络管理)](arkts-mdm-networkmanager-setnetworkinterfacedisabled-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [DomainFilterRule(网络管理)](arkts-mdm-networkmanager-domainfilterrule-i.md) |
| [FirewallRule(网络管理)](arkts-mdm-networkmanager-firewallrule-i.md) |
| [InterfaceConfig(网络管理)](arkts-mdm-networkmanager-interfaceconfig-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [AddFilterRule(网络管理)](arkts-mdm-networkmanager-addfilterrule-i-sys.md) |
| [RemoveFilterRule(网络管理)](arkts-mdm-networkmanager-removefilterrule-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [Action(网络管理)](arkts-mdm-networkmanager-action-e.md) |
| [Direction(网络管理)](arkts-mdm-networkmanager-direction-e.md) |
| [IpSetMode(网络管理)](arkts-mdm-networkmanager-ipsetmode-e.md) |
| [LogType(网络管理)](arkts-mdm-networkmanager-logtype-e.md) |
| [Protocol(网络管理)](arkts-mdm-networkmanager-protocol-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [AddMethod(网络管理)](arkts-mdm-networkmanager-addmethod-e-sys.md) |
<!--DelEnd-->
