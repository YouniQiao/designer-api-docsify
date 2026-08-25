# getPermissionUsedRecordToggleStatus (System API)

## Modules to Import

```TypeScript
import { privacyManager } from 'kits/@kit.AbilityKit';
```

## getPermissionUsedRecordToggleStatus

```TypeScript
function getPermissionUsedRecordToggleStatus(): Promise<boolean>
```

A system application can call this API to obtain the current user's permission usage record toggle status, for example, to display the current toggle setting status on the permission management interface. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100004](../errorcode-access-token.md#12100004-listener-apis-not-used-in-pairs) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |


## getPermissionUsedRecordToggleStatus

```TypeScript
function getPermissionUsedRecordToggleStatus(subProfileId: number): Promise<boolean>
```

A system application can call this API to obtain the permission usage record toggle status for a specified sub-profile, for example, to display the current toggle setting status on the permission management interface. This API uses a promise to return the result.

**Since:** 26.1.0

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [subProfileId](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |
