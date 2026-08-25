# getPasswordPolicy (System API)

## Modules to Import

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## getPasswordPolicy

```TypeScript
function getPasswordPolicy(): PasswordPolicy
```

Obtains the device screen lock password policy.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

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
