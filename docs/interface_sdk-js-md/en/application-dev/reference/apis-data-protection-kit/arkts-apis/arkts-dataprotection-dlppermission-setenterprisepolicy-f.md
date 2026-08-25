# setEnterprisePolicy

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## setEnterprisePolicy

```TypeScript
function setEnterprisePolicy(policy: EnterprisePolicy): void
```

Sets the protection policy for enterprise applications. After the API is successfully called, the DLP protection for enterprise applications is implemented based on the configured policy.This API is used by the enterprise administrator to configure DLP security policies for unified management of data security protection rules.

> **NOTE：**&gt;
> This API can be called only by enterprise accounts.

**Since:** 21

**Required permissions:** ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| policy | [EnterprisePolicy](arkts-dataprotection-dlppermission-enterprisepolicy-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |
| [19100021](../errorcode-dlp.md#19100021-failed-to-set-enterprise-application-policy) |
