# updateRemoteGrantStatus (System API)

## updateRemoteGrantStatus

```TypeScript
export function updateRemoteGrantStatus(remoteGrantStatus: RemoteGrantStatus): Promise<void>
```

Updates the remote grant status. This function enables or disables the remote authorization feature. When enabled, the device can grant permissions to remote devices; when disabled, remote authorization is not allowed.

**Since:** 26.1.0

**Required permissions:** ohos.permission.MANAGE_TOOL_RUNTIME_PERMISSIONS

<!--Device-abilityToolAccessCtrl-export function updateRemoteGrantStatus(remoteGrantStatus: RemoteGrantStatus): Promise<void>--><!--Device-abilityToolAccessCtrl-export function updateRemoteGrantStatus(remoteGrantStatus: RemoteGrantStatus): Promise<void>-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| remoteGrantStatus | [RemoteGrantStatus](arkts-ability-abilitytoolaccessctrl-remotegrantstatus-e-sys.md) | Yes | Remote grant status to be set. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denial. The interface caller does not have permission "ohos.permission.MANAGE_TOOL_RUNTIME_PERMISSIONS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| 24010002 | Common internal error. possible cause: dependent service unavailable, resource access failure, etc. |
| 24010000 | Invalid parameter. RemoteGrantStatus is invalid. |
| 24010001 | Service is abnormal. possible cause: IPC failed. |

