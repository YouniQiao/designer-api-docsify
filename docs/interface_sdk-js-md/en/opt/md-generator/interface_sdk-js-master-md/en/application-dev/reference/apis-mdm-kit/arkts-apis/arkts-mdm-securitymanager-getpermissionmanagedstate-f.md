# getPermissionManagedState

## Modules to Import

```TypeScript
import { securityManager } from '@kit.MDMKit';
```

## getPermissionManagedState

```TypeScript
function getPermissionManagedState(
    admin: Want,
    applicationInstance: ApplicationInstance,
    permission: string
  ): PermissionManagedState
```

Obtains the management policy for the [user_grant permission](../../apis-ability-kit/arkts-apis/arkts-ability-permissions-t.md#Permissions) of a specified application.

**Since:** 20

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_USER_GRANT_PERMISSION

**Model restriction:** This API can be used only in the stage model.

<!--Device-securityManager-function getPermissionManagedState(    admin: Want,    applicationInstance: ApplicationInstance,    permission: string  ): PermissionManagedState--><!--Device-securityManager-function getPermissionManagedState(    admin: Want,    applicationInstance: ApplicationInstance,    permission: string  ): PermissionManagedState-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| applicationInstance | [ApplicationInstance](arkts-mdm-securitymanager-applicationinstance-i.md) | Yes |
| permission | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PermissionManagedState](arkts-mdm-securitymanager-permissionmanagedstate-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { Want } from '@kit.AbilityKit';
import { securityManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let appInstanceTemp: securityManager.ApplicationInstance = {
  // Replace with actual values.
  appIdentifier: '736498586',
  appIndex: 0,
  accountId: 100
};
let permissionTemp: string = 'ohos.permission.ENTERPRISE_MANAGE_USER_GRANT_PERMISSION';
try {
  let result: securityManager.PermissionManagedState = securityManager.getPermissionManagedState(wantTemp, appInstanceTemp, permissionTemp);
  console.info(`Succeeded in getting permission managed state, result : ${result}`);
} catch(err) {
  console.error(`Failed to get permission managed state. Code: ${err.code}, message: ${err.message}`);
}
```
