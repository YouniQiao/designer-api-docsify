# setEnterprisePolicy

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## setEnterprisePolicy

```TypeScript
function setEnterprisePolicy(policy: EnterprisePolicy): void
```

设置企业应用防护策略。调用成功后，企业应用的DLP防护将按照设置的策略执行。

该接口可用于企业管理员配置DLP安全策略，以统一管理企业数据安全防护规则。

> **说明：**
> 
> 该接口仅支持企业账号调用。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Required permissions:** ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

<!--Device-dlpPermission-function setEnterprisePolicy(policy: EnterprisePolicy): void--><!--Device-dlpPermission-function setEnterprisePolicy(policy: EnterprisePolicy): void-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| policy | [EnterprisePolicy](arkts-dataprotection-dlppermission-enterprisepolicy-i.md) | Yes | 待设置的企业应用防护策略，设置后将按策略对企业DLP文件进行访问控制和行为限制。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19100001 | Invalid parameter value. |
| 19100021 | Failed to set the enterprise policy. |
| 19100011 | The system ability works abnormally. |
| 201 | Permission denied. |

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

