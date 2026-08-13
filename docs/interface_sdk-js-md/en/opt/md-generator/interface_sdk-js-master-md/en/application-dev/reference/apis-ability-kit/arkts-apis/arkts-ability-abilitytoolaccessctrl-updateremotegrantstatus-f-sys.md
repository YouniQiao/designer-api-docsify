# updateRemoteGrantStatus (System API)

## updateRemoteGrantStatus

```TypeScript
export function updateRemoteGrantStatus(remoteGrantStatus: RemoteGrantStatus): Promise<void>
```

Updates the remote grant status. This function enables or disables the remote authorization feature. When enabled, the device can grant permissions to remote devices; when disabled, remote authorization is not allowed.

**Since:** 26.1.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_TOOL_RUNTIME_PERMISSIONS

<!--Device-abilityToolAccessCtrl-export function updateRemoteGrantStatus(remoteGrantStatus: RemoteGrantStatus): Promise<void>--><!--Device-abilityToolAccessCtrl-export function updateRemoteGrantStatus(remoteGrantStatus: RemoteGrantStatus): Promise<void>-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| remoteGrantStatus | [RemoteGrantStatus](arkts-ability-abilitytoolaccessctrl-remotegrantstatus-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 24010002 |
| 24010000 |
| 24010001 |
