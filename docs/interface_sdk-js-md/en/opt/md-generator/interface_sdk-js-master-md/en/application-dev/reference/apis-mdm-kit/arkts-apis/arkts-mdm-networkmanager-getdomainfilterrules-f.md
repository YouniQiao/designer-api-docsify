# getDomainFilterRules

## Modules to Import

```TypeScript
import { networkManager } from '@kit.MDMKit';
```

## getDomainFilterRules

```TypeScript
function getDomainFilterRules(admin: Want): Array<DomainFilterRule>
```

Obtains domain name filtering rules. This API is suitable for enterprise network security audit scenarios, such as checking current domain name filtering policy configurations, auditing domain name access control rules, verifying whether domain name filtering rules are correctly executed, and troubleshooting domain name access issues. It helps enterprises review and validate domain name access control policies to ensure network access control complies with security requirements.

In API version 21 and earlier versions, only IPv4 is supported. IPv4 and IPv6 are supported since API version 22.

[LogType](arkts-mdm-networkmanager-logtype-e.md#LogType) is supported since API version 23.

**Since:** 12

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**Model restriction:** This API can be used only in the stage model.

<!--Device-networkManager-function getDomainFilterRules(admin: Want): Array<DomainFilterRule>--><!--Device-networkManager-function getDomainFilterRules(admin: Want): Array<DomainFilterRule>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[DomainFilterRule](arkts-mdm-networkmanager-domainfilterrule-i.md)&gt; |

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
let domainFilterRule: Array<networkManager.DomainFilterRule>;
try {
  domainFilterRule = networkManager.getDomainFilterRules(wantTemp);
  console.info('Succeeded in getting domain filter rules');
} catch (err) {
  console.error(`Failed to get domain filter rules. Code: ${err.code}, message: ${err.message}`);
}
```
