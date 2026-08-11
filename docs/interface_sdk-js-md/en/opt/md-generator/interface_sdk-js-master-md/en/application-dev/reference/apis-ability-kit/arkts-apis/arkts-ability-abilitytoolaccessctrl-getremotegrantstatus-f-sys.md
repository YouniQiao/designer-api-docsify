# getRemoteGrantStatus (System API)

## getRemoteGrantStatus

```TypeScript
export function getRemoteGrantStatus(): Promise<RemoteGrantStatus>
```

Gets the remote grant status.This function queries whether the remote authorization feature is enabled or disabled.When enabled, the device can grant permissions to remote devices; when disabled, remote authorization is not allowed.

**Since:** 26.1.0

**Required permissions:** ohos.permission.QUERY_TOOL_PERMISSIONS

<!--Device-abilityToolAccessCtrl-export function getRemoteGrantStatus(): Promise<RemoteGrantStatus>--><!--Device-abilityToolAccessCtrl-export function getRemoteGrantStatus(): Promise<RemoteGrantStatus>-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;RemoteGrantStatus&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 24010002 |
| 24010001 |
