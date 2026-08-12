# removeDomainFilterRule

## Modules to Import

```TypeScript
import { networkManager } from '@kit.MDMKit';
```

## removeDomainFilterRule

```TypeScript
function removeDomainFilterRule(admin: Want, domainFilterRule?: DomainFilterRule): void
```

Removes the domain name filtering rules. This API is suitable for enterprise network security policy adjustment scenarios, such as canceling access restrictions on certain domain names, adjusting domain name filtering policies,removing outdated or invalid rules, and resolving false positive blocking issues. It helps enterprises flexibly adjust domain name access policies to ensure that network access control policies meet actual business requirements.

In API version 21 and earlier versions, only IPv4 is supported. IPv4 and IPv6 are supported since API version 22.

[LogType](arkts-mdm-networkmanager-logtype-e.md#LogType) is supported since API version 23.

If there is no rule with [Action](arkts-mdm-networkmanager-action-e.md#Action) being **ALLOW** after the rule is removed, the  
**DENY** rules that are added by default with [addDomainFilterRule](arkts-mdm-networkmanager-adddomainfilterrule-f.md#addDomainFilterRule) will be removed.

**Since:** 12

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**Model restriction:** This API can be used only in the stage model.

<!--Device-networkManager-function removeDomainFilterRule(admin: Want, domainFilterRule?: DomainFilterRule): void--><!--Device-networkManager-function removeDomainFilterRule(admin: Want, domainFilterRule?: DomainFilterRule): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| domainFilterRule | [DomainFilterRule](arkts-mdm-networkmanager-domainfilterrule-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [9200001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

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

// Remove the specified firewall rule.
try {
  networkManager.removeDomainFilterRule(wantTemp, domainFilterRule);
  console.info('Succeeded in removing domain filter rules');
} catch (err) {
  console.error(`Failed to remove domain filter rules. Code: ${err.code}, message: ${err.message}`);
}

// Clears all IPv4 rules.
try {
  networkManager.removeDomainFilterRule(wantTemp);
  console.info('Succeeded in removing all domain filter rules');
} catch (err) {
  console.error(`Failed to remove all domain filter rules. Code: ${err.code}, message: ${err.message}`);
}
```
