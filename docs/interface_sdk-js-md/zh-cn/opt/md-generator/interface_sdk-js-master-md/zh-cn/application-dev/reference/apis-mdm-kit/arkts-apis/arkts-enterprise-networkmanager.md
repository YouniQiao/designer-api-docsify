# @ohos.enterprise.networkManager

本模块提供设备网络管理能力，包括查询设备IP地址、MAC地址信息、管理网络接口状态、配置网络全局代理、管理防火墙规则和域名过滤规则、控制移动数据网络、管理APN配置、配置以太网网络等。适用于企业IT管理员对设备网络进行集中管理和安全管 控，帮助企业实现网络访问策略统一管理、防止网络攻击和数据泄露、降低网络管理成本。 > **说明：** > > 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace networkManager--><!--Device-unnamed-declare namespace networkManager-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [addApn](arkts-mdm-networkmanager-addapn-f.md#addapn) |
| [addDomainFilterRule](arkts-mdm-networkmanager-adddomainfilterrule-f.md#adddomainfilterrule) |
| [addFirewallRule](arkts-mdm-networkmanager-addfirewallrule-f.md#addfirewallrule) |
| [deleteApn](arkts-mdm-networkmanager-deleteapn-f.md#deleteapn) |
| [getAllNetworkInterfacesSync](arkts-mdm-networkmanager-getallnetworkinterfacessync-f.md#getallnetworkinterfacessync) |
| [getDomainFilterRules](arkts-mdm-networkmanager-getdomainfilterrules-f.md#getdomainfilterrules) |
| [getFirewallRules](arkts-mdm-networkmanager-getfirewallrules-f.md#getfirewallrules) |
| [getGlobalProxyForAccount](arkts-mdm-networkmanager-getglobalproxyforaccount-f.md#getglobalproxyforaccount) |
| [getGlobalProxySync](arkts-mdm-networkmanager-getglobalproxysync-f.md#getglobalproxysync) |
| [getIpAddressSync](arkts-mdm-networkmanager-getipaddresssync-f.md#getipaddresssync) |
| [getMacSync](arkts-mdm-networkmanager-getmacsync-f.md#getmacsync) |
| [isNetworkInterfaceDisabledSync](arkts-mdm-networkmanager-isnetworkinterfacedisabledsync-f.md#isnetworkinterfacedisabledsync) |
| [isNetworkInterfaceDisabledSync](arkts-mdm-networkmanager-isnetworkinterfacedisabledsync-f.md#isnetworkinterfacedisabledsync) |
| [queryApn](arkts-mdm-networkmanager-queryapn-f.md#queryapn) |
| [queryApn](arkts-mdm-networkmanager-queryapn-f.md#queryapn) |
| [removeDomainFilterRule](arkts-mdm-networkmanager-removedomainfilterrule-f.md#removedomainfilterrule) |
| [removeFirewallRule](arkts-mdm-networkmanager-removefirewallrule-f.md#removefirewallrule) |
| [setEthernetConfig](arkts-mdm-networkmanager-setethernetconfig-f.md#setethernetconfig) |
| [setGlobalProxyForAccount](arkts-mdm-networkmanager-setglobalproxyforaccount-f.md#setglobalproxyforaccount) |
| [setGlobalProxySync](arkts-mdm-networkmanager-setglobalproxysync-f.md#setglobalproxysync) |
| [setNetworkInterfaceDisabledSync](arkts-mdm-networkmanager-setnetworkinterfacedisabledsync-f.md#setnetworkinterfacedisabledsync) |
| [setPreferredApn](arkts-mdm-networkmanager-setpreferredapn-f.md#setpreferredapn) |
| [turnOffMobileData](arkts-mdm-networkmanager-turnoffmobiledata-f.md#turnoffmobiledata) |
| [turnOnMobileData](arkts-mdm-networkmanager-turnonmobiledata-f.md#turnonmobiledata) |
| [updateApn](arkts-mdm-networkmanager-updateapn-f.md#updateapn) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addIptablesFilterRule](arkts-mdm-networkmanager-addiptablesfilterrule-f-sys.md#addiptablesfilterrule系统接口) |
| [addIptablesFilterRule](arkts-mdm-networkmanager-addiptablesfilterrule-f-sys.md#addiptablesfilterrule系统接口) |
| [getAllNetworkInterfaces](arkts-mdm-networkmanager-getallnetworkinterfaces-f-sys.md#getallnetworkinterfaces系统接口) |
| [getAllNetworkInterfaces](arkts-mdm-networkmanager-getallnetworkinterfaces-f-sys.md#getallnetworkinterfaces系统接口) |
| [getGlobalProxy](arkts-mdm-networkmanager-getglobalproxy-f-sys.md#getglobalproxy系统接口) |
| [getGlobalProxy](arkts-mdm-networkmanager-getglobalproxy-f-sys.md#getglobalproxy系统接口) |
| [getIpAddress](arkts-mdm-networkmanager-getipaddress-f-sys.md#getipaddress系统接口) |
| [getIpAddress](arkts-mdm-networkmanager-getipaddress-f-sys.md#getipaddress系统接口) |
| [getMac](arkts-mdm-networkmanager-getmac-f-sys.md#getmac系统接口) |
| [getMac](arkts-mdm-networkmanager-getmac-f-sys.md#getmac系统接口) |
| [isNetworkInterfaceDisabled](arkts-mdm-networkmanager-isnetworkinterfacedisabled-f-sys.md#isnetworkinterfacedisabled系统接口) |
| [isNetworkInterfaceDisabled](arkts-mdm-networkmanager-isnetworkinterfacedisabled-f-sys.md#isnetworkinterfacedisabled系统接口) |
| [listIptablesFilterRules](arkts-mdm-networkmanager-listiptablesfilterrules-f-sys.md#listiptablesfilterrules系统接口) |
| [listIptablesFilterRules](arkts-mdm-networkmanager-listiptablesfilterrules-f-sys.md#listiptablesfilterrules系统接口) |
| [removeIptablesFilterRule](arkts-mdm-networkmanager-removeiptablesfilterrule-f-sys.md#removeiptablesfilterrule系统接口) |
| [removeIptablesFilterRule](arkts-mdm-networkmanager-removeiptablesfilterrule-f-sys.md#removeiptablesfilterrule系统接口) |
| [setGlobalProxy](arkts-mdm-networkmanager-setglobalproxy-f-sys.md#setglobalproxy系统接口) |
| [setGlobalProxy](arkts-mdm-networkmanager-setglobalproxy-f-sys.md#setglobalproxy系统接口) |
| [setNetworkInterfaceDisabled](arkts-mdm-networkmanager-setnetworkinterfacedisabled-f-sys.md#setnetworkinterfacedisabled系统接口) |
| [setNetworkInterfaceDisabled](arkts-mdm-networkmanager-setnetworkinterfacedisabled-f-sys.md#setnetworkinterfacedisabled系统接口) |
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
