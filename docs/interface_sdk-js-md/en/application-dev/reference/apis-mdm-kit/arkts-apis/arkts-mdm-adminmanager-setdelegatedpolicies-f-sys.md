# setDelegatedPolicies (System API)

## Modules to Import

```TypeScript
import { adminManager } from 'kits/@kit.MDMKit';
```

## setDelegatedPolicies

```TypeScript
function setDelegatedPolicies(bundleName: string, accountId: number, policies: Array<string>): void
```

Delegates other applications to set device management policies. The applications must request the permissions required.

**Since:** 20

**Required permissions:** ohos.permission.MANAGE_ENTERPRISE_DEVICE_ADMIN

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| accountId | number | Yes |
| policies | Array & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200009](../errorcode-enterpriseDeviceManager.md#9200009-failed-to-grant-permissions-to-an-application) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
