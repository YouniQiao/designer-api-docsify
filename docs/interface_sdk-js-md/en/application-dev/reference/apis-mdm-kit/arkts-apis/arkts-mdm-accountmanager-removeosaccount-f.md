# removeOsAccount

## Modules to Import

```TypeScript
import { accountManager } from '@kit.MDMKit';
```

## removeOsAccount

```TypeScript
function removeOsAccount(admin: Want, accountId: number): Promise<void>
```

Removes a system account. Currently, this API is supported only on phones and tablets. It can remove normal system accounts (of the normal type) created via [createNormalOsAccount](arkts-mdm-accountmanager-createnormalosaccount-f.md) and system accounts (of the admin, normal, and guest types) created via [addOsAccountAsync](arkts-mdm-accountmanager-addosaccountasync-f.md). The default system account (ID: 100) cannot be removed.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| accountId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-service-timeout) |
| [9201041](../errorcode-enterpriseDeviceManager.md#9201041-system-account-type-restricted) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [204](../../errorcode-universal.md#204-access-denied-by-user-access-control-policy) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
