# getRemoteGrantStatus (System API)

## Modules to Import

```TypeScript
```

## getRemoteGrantStatus

```TypeScript
export function getRemoteGrantStatus(): Promise<RemoteGrantStatus>
```

Gets the remote grant status. This function queries whether the remote authorization feature is enabled or disabled. When enabled, the device can grant permissions to remote devices; when disabled, remote authorization is not allowed.

**Since:** 26.1.0

**Required permissions:** ohos.permission.QUERY_TOOL_PERMISSIONS

<!--Device-abilityToolAccessCtrl-export function getRemoteGrantStatus(): Promise<RemoteGrantStatus>--><!--Device-abilityToolAccessCtrl-export function getRemoteGrantStatus(): Promise<RemoteGrantStatus>-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[RemoteGrantStatus](arkts-ability-abilitytoolaccessctrl-remotegrantstatus-e-sys.md)&gt; | Promise used to return \\${RemoteGrantStatus}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denial. The interface caller does not have permission "ohos.permission.QUERY_TOOL_PERMISSIONS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| 24010002 | Common internal error. possible cause: dependent service unavailable, resource access failure, etc. |
| 24010001 | Service is abnormal. possible cause: IPC failed. |

