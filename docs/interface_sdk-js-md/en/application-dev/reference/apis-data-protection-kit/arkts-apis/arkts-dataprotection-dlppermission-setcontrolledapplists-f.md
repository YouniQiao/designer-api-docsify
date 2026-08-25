# setControlledAppLists

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## setControlledAppLists

```TypeScript
function setControlledAppLists(appLists: Array<string>, userId?: number): Promise<void>
```

Sets the list of applications controlled by enterprise DLP. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.DLP_POLICY_MANAGER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| appLists | Array & lt;string & gt; | Yes |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |
| [19100023](../errorcode-dlp.md#19100023-specified-user-id-inconsistent-with-the-current-user-id) |
| [19100024](../errorcode-dlp.md#19100024-personal-space-users-cannot-set-controlled-apps) |
