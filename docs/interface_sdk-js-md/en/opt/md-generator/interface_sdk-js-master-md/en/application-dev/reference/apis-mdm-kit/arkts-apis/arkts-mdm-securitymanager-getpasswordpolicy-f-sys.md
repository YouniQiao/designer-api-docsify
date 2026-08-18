# getPasswordPolicy (System API)

## Modules to Import

```TypeScript
```

## getPasswordPolicy

```TypeScript
function getPasswordPolicy(): PasswordPolicy
```

Obtains the device screen lock password policy.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-securityManager-function getPasswordPolicy(): PasswordPolicy--><!--Device-securityManager-function getPasswordPolicy(): PasswordPolicy-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PasswordPolicy](arkts-mdm-securitymanager-passwordpolicy-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { securityManager } from '@kit.MDMKit';

try {
  let result: securityManager.PasswordPolicy = securityManager.getPasswordPolicy();
  console.info(`Succeeded in getting password policy, result : ${JSON.stringify(result)}`);
} catch(err) {
  console.error(`Failed to get password policy. Code: ${err.code}, message: ${err.message}`);
}
```
