# addFirewallRule

## Modules to Import

```TypeScript
import { networkManager } from 'kits/@kit.MDMKit';
```

## addFirewallRule

```TypeScript
function addFirewallRule(admin: Want, firewallRule: FirewallRule): void
```

为设备添加防火墙过滤规则。适用于企业网络安全管控场景，例如限制特定IP地址的网络访问、防止恶意网络攻击、控制应用程序的网络通信、实现网络访问的允许名单或禁用名单管理，帮助企业精细化控制网络访问，防止网络攻击和数据泄露。

API version 21及之前版本，仅支持IPv4。从API version 22开始，支持IPv4和IPv6。

从API version 23开始，支持[LogType](arkts-mdm-networkmanager-logtype-e.md)。

> **说明：**
> 
> - 添加了[Action](arkts-mdm-networkmanager-action-e.md)为ALLOW规则后，将会默认添加DENY规则，不在ALLOW规则之内的网络数据包将会被丢弃或拦截。
> 
> - 设备重启，将会清空防火墙过滤规则。
> 
> - 规则匹配顺序：先匹配域名过滤规则（由[addDomainFilterRule](arkts-mdm-networkmanager-adddomainfilterrule-f.md#adddomainfilterrule)添加），再匹配本接口添加的IP防火墙规则；在域名规则或IP规
> 则中，均按[Action](arkts-mdm-networkmanager-action-e.md)为ALLOW、DENY、REJECT的顺序进行匹配。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**Model restriction:** This API can be used only in the stage model.

<!--Device-networkManager-function addFirewallRule(admin: Want, firewallRule: FirewallRule): void--><!--Device-networkManager-function addFirewallRule(admin: Want, firewallRule: FirewallRule): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| firewallRule | [FirewallRule](arkts-mdm-networkmanager-firewallrule-i.md) | Yes | 添加防火墙过滤规则。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let firewallRule: networkManager.FirewallRule = {
  // Replace with actual values.
  "srcAddr": "192.168.1.1-192.168.22.66",
  "destAddr": "10.1.1.1",
  "srcPort": "8080",
  "destPort": "8080",
  "appUid": "9696",
  "direction": networkManager.Direction.OUTPUT,
  "action": networkManager.Action.DENY,
  "protocol": networkManager.Protocol.UDP,
  "family": 1,
  "logType": networkManager.LogType.NFLOG
};

try {
  networkManager.addFirewallRule(wantTemp, firewallRule);
  console.info('Succeeded in adding firewall rule.');
} catch (err) {
  console.error(`Failed to add firewall rule. Code: ${err.code}, message: ${err.message}`);
}
```

