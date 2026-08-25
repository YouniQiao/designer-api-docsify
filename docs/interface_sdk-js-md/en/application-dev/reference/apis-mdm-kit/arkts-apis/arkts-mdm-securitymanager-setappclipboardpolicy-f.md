# setAppClipboardPolicy

## Modules to Import

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## setAppClipboardPolicy

```TypeScript
function setAppClipboardPolicy(admin: Want, tokenId: number, policy: ClipboardPolicy): void
```

Sets the device clipboard policy. After the policy is set, applications will be restricted in their clipboard usage according to the configured policy. This API is applicable to enterprise data leakage prevention scenarios, such as restricting clipboard usage for sensitive applications (such as enterprise email and financial systems) to prevent sensitive data from being copied to unauthorized applications, thereby reducing the risk of data leakage. Enterprises can use this API to control application clipboard usage permissions, preventing sensitive data from being leaked to unauthorized applications via the clipboard, and enhancing enterprise data security protection capabilities.

**Since:** 12

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| tokenId | number | Yes |
| policy | [ClipboardPolicy](arkts-mdm-securitymanager-clipboardpolicy-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## setAppClipboardPolicy

```TypeScript
function setAppClipboardPolicy(admin: Want, bundleName: string, accountId: number, policy: ClipboardPolicy): void
```

Sets the device clipboard policy of a specified application for a specified user. After the policy is set, the clipboard of the specified application will be restricted in its usage scope according to the configured policy. Enterprises can configure differentiated clipboard usage permissions for different applications across different users, enabling fine-grained data access control and meeting the security management requirements in multi-user, multi-application scenarios.

**Since:** 18

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| bundleName | string | Yes |
| accountId | number | Yes |
| policy | [ClipboardPolicy](arkts-mdm-securitymanager-clipboardpolicy-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [201](../../errorcode-universal.md#201-permission-denied) |
