# @ohos.enterprise.networkManager(网络管理)

本模块提供设备网络管理能力，包括查询设备IP地址、MAC地址信息、管理网络接口状态、配置网络全局代理、管理防火墙规则和域名过滤规则、控制移动数据网络、管理APN配置、配置以太网网络等。适用于企业IT管理员对设备网络进行集中管理和安全管控，帮助企业实现网络访问策略统一管理、防止网络攻击和数据泄露、降低网络管理成本。

> **说明：**
> 
> 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace networkManager--><!--Device-unnamed-declare namespace networkManager-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 汇总

### 函数

| 名称 |
| --- |
| [addApn](arkts-mdm-networkmanager-addapn-f.md#addapn) |
| [addDomainFilterRule](arkts-mdm-networkmanager-adddomainfilterrule-f.md#adddomainfilterrule) |
| [addFirewallRule](arkts-mdm-networkmanager-addfirewallrule-f.md#addfirewallrule) |
| [addIptablesFilterRule](arkts-mdm-networkmanager-addiptablesfilterrule-f.md#addiptablesfilterrule) |
| [addIptablesFilterRule](arkts-mdm-networkmanager-addiptablesfilterrule-f.md#addiptablesfilterrule-1) |
| [deleteApn](arkts-mdm-networkmanager-deleteapn-f.md#deleteapn) |
| [getAllNetworkInterfaces](arkts-mdm-networkmanager-getallnetworkinterfaces-f.md#getallnetworkinterfaces) |
| [getAllNetworkInterfaces](arkts-mdm-networkmanager-getallnetworkinterfaces-f.md#getallnetworkinterfaces-1) |
| [getAllNetworkInterfacesSync](arkts-mdm-networkmanager-getallnetworkinterfacessync-f.md#getallnetworkinterfacessync) |
| [getDomainFilterRules](arkts-mdm-networkmanager-getdomainfilterrules-f.md#getdomainfilterrules) |
| [getFirewallRules](arkts-mdm-networkmanager-getfirewallrules-f.md#getfirewallrules) |
| [getGlobalProxy](arkts-mdm-networkmanager-getglobalproxy-f.md#getglobalproxy) |
| [getGlobalProxy](arkts-mdm-networkmanager-getglobalproxy-f.md#getglobalproxy-1) |
| [getGlobalProxyForAccount](arkts-mdm-networkmanager-getglobalproxyforaccount-f.md#getglobalproxyforaccount) |
| [getGlobalProxySync](arkts-mdm-networkmanager-getglobalproxysync-f.md#getglobalproxysync) |
| [getIpAddress](arkts-mdm-networkmanager-getipaddress-f.md#getipaddress) |
| [getIpAddress](arkts-mdm-networkmanager-getipaddress-f.md#getipaddress-1) |
| [getIpAddressSync](arkts-mdm-networkmanager-getipaddresssync-f.md#getipaddresssync) |
| [getMac](arkts-mdm-networkmanager-getmac-f.md#getmac) |
| [getMac](arkts-mdm-networkmanager-getmac-f.md#getmac-1) |
| [getMacSync](arkts-mdm-networkmanager-getmacsync-f.md#getmacsync) |
| [isNetworkInterfaceDisabled](arkts-mdm-networkmanager-isnetworkinterfacedisabled-f.md#isnetworkinterfacedisabled) |
| [isNetworkInterfaceDisabled](arkts-mdm-networkmanager-isnetworkinterfacedisabled-f.md#isnetworkinterfacedisabled-1) |
| [isNetworkInterfaceDisabledSync](arkts-mdm-networkmanager-isnetworkinterfacedisabledsync-f.md#isnetworkinterfacedisabledsync) |
| [isNetworkInterfaceDisabledSync](arkts-mdm-networkmanager-isnetworkinterfacedisabledsync-f.md#isnetworkinterfacedisabledsync-1) |
| [listIptablesFilterRules](arkts-mdm-networkmanager-listiptablesfilterrules-f.md#listiptablesfilterrules) |
| [listIptablesFilterRules](arkts-mdm-networkmanager-listiptablesfilterrules-f.md#listiptablesfilterrules-1) |
| [queryApn](arkts-mdm-networkmanager-queryapn-f.md#queryapn) |
| [queryApn](arkts-mdm-networkmanager-queryapn-f.md#queryapn-1) |
| [removeDomainFilterRule](arkts-mdm-networkmanager-removedomainfilterrule-f.md#removedomainfilterrule) |
| [removeFirewallRule](arkts-mdm-networkmanager-removefirewallrule-f.md#removefirewallrule) |
| [removeIptablesFilterRule](arkts-mdm-networkmanager-removeiptablesfilterrule-f.md#removeiptablesfilterrule) |
| [removeIptablesFilterRule](arkts-mdm-networkmanager-removeiptablesfilterrule-f.md#removeiptablesfilterrule-1) |
| [setEthernetConfig](arkts-mdm-networkmanager-setethernetconfig-f.md#setethernetconfig) |
| [setGlobalProxy](arkts-mdm-networkmanager-setglobalproxy-f.md#setglobalproxy) |
| [setGlobalProxy](arkts-mdm-networkmanager-setglobalproxy-f.md#setglobalproxy-1) |
| [setGlobalProxyForAccount](arkts-mdm-networkmanager-setglobalproxyforaccount-f.md#setglobalproxyforaccount) |
| [setGlobalProxySync](arkts-mdm-networkmanager-setglobalproxysync-f.md#setglobalproxysync) |
| [setNetworkInterfaceDisabled](arkts-mdm-networkmanager-setnetworkinterfacedisabled-f.md#setnetworkinterfacedisabled) |
| [setNetworkInterfaceDisabled](arkts-mdm-networkmanager-setnetworkinterfacedisabled-f.md#setnetworkinterfacedisabled-1) |
| [setNetworkInterfaceDisabledSync](arkts-mdm-networkmanager-setnetworkinterfacedisabledsync-f.md#setnetworkinterfacedisabledsync) |
| [setPreferredApn](arkts-mdm-networkmanager-setpreferredapn-f.md#setpreferredapn) |
| [turnOffMobileData](arkts-mdm-networkmanager-turnoffmobiledata-f.md#turnoffmobiledata) |
| [turnOnMobileData](arkts-mdm-networkmanager-turnonmobiledata-f.md#turnonmobiledata) |
| [updateApn](arkts-mdm-networkmanager-updateapn-f.md#updateapn) |

### 接口

| 名称 |
| --- |
| [AddFilterRule](arkts-mdm-networkmanager-addfilterrule-i.md) |
| [DomainFilterRule](arkts-mdm-networkmanager-domainfilterrule-i.md) |
| [FirewallRule](arkts-mdm-networkmanager-firewallrule-i.md) |
| [InterfaceConfig](arkts-mdm-networkmanager-interfaceconfig-i.md) |
| [RemoveFilterRule](arkts-mdm-networkmanager-removefilterrule-i.md) |

### 枚举

| 名称 |
| --- |
| [Action](arkts-mdm-networkmanager-action-e.md) |
| [AddMethod](arkts-mdm-networkmanager-addmethod-e.md) |
| [Direction](arkts-mdm-networkmanager-direction-e.md) |
| [IpSetMode](arkts-mdm-networkmanager-ipsetmode-e.md) |
| [LogType](arkts-mdm-networkmanager-logtype-e.md) |
| [Protocol](arkts-mdm-networkmanager-protocol-e.md) |
