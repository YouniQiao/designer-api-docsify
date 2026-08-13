# @ohos.enterprise.networkManager

本模块提供设备网络管理能力，包括查询设备IP地址、MAC地址信息、管理网络接口状态、配置网络全局代理、管理防火墙规则和域名过滤规则、控制移动数据网络、管理APN配置、配置以太网网络等。适用于企业IT管理员对设备网络进行集中管理和安全管 控，帮助企业实现网络访问策略统一管理、防止网络攻击和数据泄露、降低网络管理成本。 > **说明：** > > 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 10

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace networkManager--><!--Device-unnamed-declare namespace networkManager-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

## 汇总

### 函数

| 名称 |
| --- |
| [addApn](arkts-mdm-networkmanager-addapn-f.md#addApn) |
| [addDomainFilterRule](arkts-mdm-networkmanager-adddomainfilterrule-f.md#addDomainFilterRule) |
| [addFirewallRule](arkts-mdm-networkmanager-addfirewallrule-f.md#addFirewallRule) |
| [deleteApn](arkts-mdm-networkmanager-deleteapn-f.md#deleteApn) |
| [getAllNetworkInterfacesSync](arkts-mdm-networkmanager-getallnetworkinterfacessync-f.md#getAllNetworkInterfacesSync) |
| [getDomainFilterRules](arkts-mdm-networkmanager-getdomainfilterrules-f.md#getDomainFilterRules) |
| [getFirewallRules](arkts-mdm-networkmanager-getfirewallrules-f.md#getFirewallRules) |
| [getGlobalProxyForAccount](arkts-mdm-networkmanager-getglobalproxyforaccount-f.md#getGlobalProxyForAccount) |
| [getGlobalProxySync](arkts-mdm-networkmanager-getglobalproxysync-f.md#getGlobalProxySync) |
| [getIpAddressSync](arkts-mdm-networkmanager-getipaddresssync-f.md#getIpAddressSync) |
| [getMacSync](arkts-mdm-networkmanager-getmacsync-f.md#getMacSync) |
| [isNetworkInterfaceDisabledSync](arkts-mdm-networkmanager-isnetworkinterfacedisabledsync-f.md#isNetworkInterfaceDisabledSync) |
| [isNetworkInterfaceDisabledSync](arkts-mdm-networkmanager-isnetworkinterfacedisabledsync-f.md#isNetworkInterfaceDisabledSync) |
| [queryApn](arkts-mdm-networkmanager-queryapn-f.md#queryApn) |
| [queryApn](arkts-mdm-networkmanager-queryapn-f.md#queryApn) |
| [removeDomainFilterRule](arkts-mdm-networkmanager-removedomainfilterrule-f.md#removeDomainFilterRule) |
| [removeFirewallRule](arkts-mdm-networkmanager-removefirewallrule-f.md#removeFirewallRule) |
| [setEthernetConfig](arkts-mdm-networkmanager-setethernetconfig-f.md#setEthernetConfig) |
| [setGlobalProxyForAccount](arkts-mdm-networkmanager-setglobalproxyforaccount-f.md#setGlobalProxyForAccount) |
| [setGlobalProxySync](arkts-mdm-networkmanager-setglobalproxysync-f.md#setGlobalProxySync) |
| [setNetworkInterfaceDisabledSync](arkts-mdm-networkmanager-setnetworkinterfacedisabledsync-f.md#setNetworkInterfaceDisabledSync) |
| [setPreferredApn](arkts-mdm-networkmanager-setpreferredapn-f.md#setPreferredApn) |
| [turnOffMobileData](arkts-mdm-networkmanager-turnoffmobiledata-f.md#turnOffMobileData) |
| [turnOnMobileData](arkts-mdm-networkmanager-turnonmobiledata-f.md#turnOnMobileData) |
| [updateApn](arkts-mdm-networkmanager-updateapn-f.md#updateApn) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addIptablesFilterRule](arkts-mdm-networkmanager-addiptablesfilterrule-f-sys.md#addIptablesFilterRule（系统接口）) |
| [addIptablesFilterRule](arkts-mdm-networkmanager-addiptablesfilterrule-f-sys.md#addIptablesFilterRule（系统接口）) |
| [getAllNetworkInterfaces](arkts-mdm-networkmanager-getallnetworkinterfaces-f-sys.md#getAllNetworkInterfaces（系统接口）) |
| [getAllNetworkInterfaces](arkts-mdm-networkmanager-getallnetworkinterfaces-f-sys.md#getAllNetworkInterfaces（系统接口）) |
| [getGlobalProxy](arkts-mdm-networkmanager-getglobalproxy-f-sys.md#getGlobalProxy（系统接口）) |
| [getGlobalProxy](arkts-mdm-networkmanager-getglobalproxy-f-sys.md#getGlobalProxy（系统接口）) |
| [getIpAddress](arkts-mdm-networkmanager-getipaddress-f-sys.md#getIpAddress（系统接口）) |
| [getIpAddress](arkts-mdm-networkmanager-getipaddress-f-sys.md#getIpAddress（系统接口）) |
| [getMac](arkts-mdm-networkmanager-getmac-f-sys.md#getMac（系统接口）) |
| [getMac](arkts-mdm-networkmanager-getmac-f-sys.md#getMac（系统接口）) |
| [isNetworkInterfaceDisabled](arkts-mdm-networkmanager-isnetworkinterfacedisabled-f-sys.md#isNetworkInterfaceDisabled（系统接口）) |
| [isNetworkInterfaceDisabled](arkts-mdm-networkmanager-isnetworkinterfacedisabled-f-sys.md#isNetworkInterfaceDisabled（系统接口）) |
| [listIptablesFilterRules](arkts-mdm-networkmanager-listiptablesfilterrules-f-sys.md#listIptablesFilterRules（系统接口）) |
| [listIptablesFilterRules](arkts-mdm-networkmanager-listiptablesfilterrules-f-sys.md#listIptablesFilterRules（系统接口）) |
| [removeIptablesFilterRule](arkts-mdm-networkmanager-removeiptablesfilterrule-f-sys.md#removeIptablesFilterRule（系统接口）) |
| [removeIptablesFilterRule](arkts-mdm-networkmanager-removeiptablesfilterrule-f-sys.md#removeIptablesFilterRule（系统接口）) |
| [setGlobalProxy](arkts-mdm-networkmanager-setglobalproxy-f-sys.md#setGlobalProxy（系统接口）) |
| [setGlobalProxy](arkts-mdm-networkmanager-setglobalproxy-f-sys.md#setGlobalProxy（系统接口）) |
| [setNetworkInterfaceDisabled](arkts-mdm-networkmanager-setnetworkinterfacedisabled-f-sys.md#setNetworkInterfaceDisabled（系统接口）) |
| [setNetworkInterfaceDisabled](arkts-mdm-networkmanager-setnetworkinterfacedisabled-f-sys.md#setNetworkInterfaceDisabled（系统接口）) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [DomainFilterRule](arkts-mdm-networkmanager-domainfilterrule-i.md) |
| [FirewallRule](arkts-mdm-networkmanager-firewallrule-i.md) |
| [InterfaceConfig](arkts-mdm-networkmanager-interfaceconfig-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [AddFilterRule](arkts-mdm-networkmanager-addfilterrule-i-sys.md) |
| [RemoveFilterRule](arkts-mdm-networkmanager-removefilterrule-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [Action](arkts-mdm-networkmanager-action-e.md) |
| [Direction](arkts-mdm-networkmanager-direction-e.md) |
| [IpSetMode](arkts-mdm-networkmanager-ipsetmode-e.md) |
| [LogType](arkts-mdm-networkmanager-logtype-e.md) |
| [Protocol](arkts-mdm-networkmanager-protocol-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [AddMethod](arkts-mdm-networkmanager-addmethod-e-sys.md) |
<!--DelEnd-->
