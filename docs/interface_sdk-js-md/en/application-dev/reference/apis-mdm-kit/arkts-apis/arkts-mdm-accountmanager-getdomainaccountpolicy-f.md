# getDomainAccountPolicy

## Modules to Import

```TypeScript
import { accountManager } from 'kits/@kit.MDMKit';
```

## getDomainAccountPolicy

```TypeScript
function getDomainAccountPolicy(admin: Want, domainAccountInfo: osAccount.DomainAccountInfo): DomainAccountPolicy
```

Obtains the domain account policy. This API is applicable to enterprise management scenarios, such as querying the current domain account policy configuration and auditing policy compliance.

**Since:** 19

**Required permissions:** ohos.permission.ENTERPRISE_SET_ACCOUNT_POLICY

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| [domainAccountInfo](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | osAccount.DomainAccountInfo | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DomainAccountPolicy](arkts-mdm-accountmanager-domainaccountpolicy-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
