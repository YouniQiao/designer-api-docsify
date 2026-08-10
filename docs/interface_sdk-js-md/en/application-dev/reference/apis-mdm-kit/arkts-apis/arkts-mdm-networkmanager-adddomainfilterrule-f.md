# addDomainFilterRule

## Modules to Import

```TypeScript
import { networkManager } from 'kits/@kit.MDMKit';
```

## addDomainFilterRule

```TypeScript
function addDomainFilterRule(admin: Want, domainFilterRule: DomainFilterRule): void
```

为设备添加域名过滤规则。

API version 21及之前版本，仅支持IPv4。从API version 22开始，支持IPv4和IPv6。

从API version 23开始，支持[LogType](arkts-mdm-networkmanager-logtype-e.md)。

> **说明：**
> 
> - 添加[Action](arkts-mdm-networkmanager-action-e.md)为ALLOW规则后会自动添加默认DENY规则，不在ALLOW规则之内的域名解析数据包将被丢弃或拦截。
> 
> - 添加的规则在设备重启后会被清空。
> 
> - 为避免DNS缓存导致拦截规则失效，建议系统启动后立即配置域名过滤规则。若已因DNS缓存导致拦截失效，重启系统可清除缓存，恢复拦截功能。
> 
> - 规则匹配顺序：先匹配本接口添加的域名过滤规则，再匹配IP防火墙规则（由[addFirewallRule](arkts-mdm-networkmanager-addfirewallrule-f.md#addfirewallrule)添加）；在域名规则或IP规则中，均按
> [Action](arkts-mdm-networkmanager-action-e.md)为ALLOW、DENY、REJECT的顺序进行匹配。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**Model restriction:** This API can be used only in the stage model.

<!--Device-networkManager-function addDomainFilterRule(admin: Want, domainFilterRule: DomainFilterRule): void--><!--Device-networkManager-function addDomainFilterRule(admin: Want, domainFilterRule: DomainFilterRule): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| domainFilterRule | [DomainFilterRule](arkts-mdm-networkmanager-domainfilterrule-i.md) | Yes | 域名过滤规则对象，包含域名、应用UID、IP协议版本等配置项。 |

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
let domainFilterRule: networkManager.DomainFilterRule = {
  // Replace with actual values.
  "domainName": "www.example.com",
  "appUid": "9696",
  "action": networkManager.Action.DENY,
  "family": 1,
  "logType": networkManager.LogType.NFLOG
};

try {
  networkManager.addDomainFilterRule(wantTemp, domainFilterRule);
  console.info('Succeeded in adding domain filter rules');
} catch (err) {
  console.error(`Failed to add domain filter rules. Code: ${err.code}, message: ${err.message}`);
}
```

