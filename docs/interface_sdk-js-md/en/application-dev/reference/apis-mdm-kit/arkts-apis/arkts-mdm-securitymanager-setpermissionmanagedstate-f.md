# setPermissionManagedState

## Modules to Import

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## setPermissionManagedState

```TypeScript
function setPermissionManagedState(
    admin: Want,
    applicationInstance: ApplicationInstance,
    permissions: Array<string>,
    managedState: PermissionManagedState
  ): void
```

Sets the management policy for the [user_grant permission](../../apis-ability-kit/arkts-apis/arkts-ability-permissions-t.md) of a specified application. This is applicable to enterprise application batch deployment scenarios, such as granting permissions silently to reduce permission prompt interruptions, and unifying permission management policies for enterprise applications, thereby improving employee user experience and management efficiency.

**Since:** 20

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_USER_GRANT_PERMISSION

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| applicationInstance | [ApplicationInstance](arkts-mdm-securitymanager-applicationinstance-i.md) | Yes |
| permissions | Array & lt;string & gt; | Yes |
| managedState | [PermissionManagedState](arkts-mdm-securitymanager-permissionmanagedstate-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-policy-conflict) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
