# @ohos.net.netFirewall

Provides interfaces to manage net firewall.

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为14。

<!--Device-unnamed-declare namespace netFirewall--><!--Device-unnamed-declare namespace netFirewall-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## 导入模块

```TypeScript
import { netFirewall } from 'kits/@kit.NetworkKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [addNetFirewallRule](arkts-network-netfirewall-addnetfirewallrule-f.md#addnetfirewallrule) | Add a firewall rule. |
| [getNetFirewallPolicy](arkts-network-netfirewall-getnetfirewallpolicy-f.md#getnetfirewallpolicy) | Get firewall policy by userId. |
| [getNetFirewallRule](arkts-network-netfirewall-getnetfirewallrule-f.md#getnetfirewallrule) | Get a specified firewall rule by userId and ruleId. |
| [getNetFirewallRules](arkts-network-netfirewall-getnetfirewallrules-f.md#getnetfirewallrules) | Get firewall rules by userId, and it is necessary to specify the pagination query parameters. |
| [removeNetFirewallRule](arkts-network-netfirewall-removenetfirewallrule-f.md#removenetfirewallrule) | Delete a firewall rule by userId and ruleId. |
| [setNetFirewallPolicy](arkts-network-netfirewall-setnetfirewallpolicy-f.md#setnetfirewallpolicy) | Set firewall policy by userId.&lt;p&gt;Enables or disables the firewall function, and specifies the default actions for inbound connections and outbound connections.&lt;/p&gt; |
| [updateNetFirewallRule](arkts-network-netfirewall-updatenetfirewallrule-f.md#updatenetfirewallrule) | Update a firewall rule. |

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [getInterceptedRecords](arkts-network-netfirewall-getinterceptedrecords-f-sys.md#getinterceptedrecords) | Get intercepted records by userId, and it is necessary to specify the pagination query parameters. |
<!--DelEnd-->

### 接口

| 名称 | 说明 |
| --- | --- |
| [FirewallRulePage](arkts-network-netfirewall-firewallrulepage-i.md) | Rule page information. |
| [NetFirewallDnsParams](arkts-network-netfirewall-netfirewalldnsparams-i.md) | Firewall DNS parameters. |
| [NetFirewallDomainParams](arkts-network-netfirewall-netfirewalldomainparams-i.md) | Firewall domain name parameters. |
| [NetFirewallIpParams](arkts-network-netfirewall-netfirewallipparams-i.md) | Firewall IP parameters. |
| [NetFirewallPolicy](arkts-network-netfirewall-netfirewallpolicy-i.md) | Firewall policy. |
| [NetFirewallPortParams](arkts-network-netfirewall-netfirewallportparams-i.md) | Firewall port parameters. |
| [NetFirewallRule](arkts-network-netfirewall-netfirewallrule-i.md) | Firewall rules. |
| [RequestParam](arkts-network-netfirewall-requestparam-i.md) | Pagination query input parameters. |

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [InterceptedRecord](arkts-network-netfirewall-interceptedrecord-i-sys.md) | Intercepted record. |
| [InterceptedRecordPage](arkts-network-netfirewall-interceptedrecordpage-i-sys.md) | Intercepted record page information. |
<!--DelEnd-->

### 枚举

| 名称 | 说明 |
| --- | --- |
| [FirewallRuleAction](arkts-network-netfirewall-firewallruleaction-e.md) | Firewall rule behavior enumeration. |
| [NetFirewallOrderField](arkts-network-netfirewall-netfirewallorderfield-e.md) | Pagination query sorting field. |
| [NetFirewallOrderType](arkts-network-netfirewall-netfirewallordertype-e.md) | Pagination query sorting type. |
| [NetFirewallRuleDirection](arkts-network-netfirewall-netfirewallruledirection-e.md) | Firewall rule direction enumeration. |
| [NetFirewallRuleType](arkts-network-netfirewall-netfirewallruletype-e.md) | Indicates the firewall rule type. |

