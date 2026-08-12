# setEnterprisePolicy

## Modules to Import

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
```

## setEnterprisePolicy

```TypeScript
function setEnterprisePolicy(policy: EnterprisePolicy): void
```

Sets the protection policy for enterprise applications. After the API is successfully called, the DLP protection for enterprise applications is implemented based on the configured policy.

This API is used by the enterprise administrator to configure DLP security policies for unified management of data security protection rules.

> **NOTE：**
> 
> This API can be called only by enterprise accounts.

**Since:** 21

**Required permissions:** ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

<!--Device-dlpPermission-function setEnterprisePolicy(policy: EnterprisePolicy): void--><!--Device-dlpPermission-function setEnterprisePolicy(policy: EnterprisePolicy): void-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| policy | [EnterprisePolicy](arkts-dataprotection-dlppermission-enterprisepolicy-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [19100001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100001-invalid-parameter) |
| [19100021](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100021-failed-to-set-enterprise-application-policy) |
| [19100011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-system-service-abnormal) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

interface Attribute {
  attributeId: string;
  attributeValues: Array<string>;
  valueType: number;
  opt: number;
}

interface Rule {
  ruleId: string;
  attributes: Array<Attribute>;
}

interface Policy {
  rules: Array<Rule>;
  policyId: string;
  ruleConflictAlg: number;
}

try {
    let attributeValues: Array<string> = [ '1' ];
    let attribute: Attribute = {
        attributeId: 'DeviceHealthyStatus',
        attributeValues: attributeValues,
        valueType: 0,
        opt: 2
    }; // Attribute information
    let rule: Rule = {
        ruleId: 'ruleId',
        attributes: [ attribute ]
    }; // Rules
    let policy: Policy = {
        rules: [ rule ],
        policyId: 'policyId',
        ruleConflictAlg: 0
    }; // Policy
    let enterprisePolicy: dlpPermission.EnterprisePolicy = {
        policyString: JSON.stringify(policy)
    };
    dlpPermission.setEnterprisePolicy(enterprisePolicy);
    console.info('set enterprise policy success'); 
} catch (err) { 
    console.error(`Failed to set enterprise policy. Code: ${err.code}, message: ${err.message}`);
}
```
