# updateRemoteGrantStatus (System API)

## updateRemoteGrantStatus

```TypeScript
export function updateRemoteGrantStatus(remoteGrantStatus: RemoteGrantStatus): Promise<void>
```

更新远程授权状态。该功能用于开启或关闭远程授权特性。启用时，设备可以向远程设备授予权限；禁用时，不允许远程授权。

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Required permissions:** ohos.permission.MANAGE_TOOL_RUNTIME_PERMISSIONS

<!--Device-abilityToolAccessCtrl-export function updateRemoteGrantStatus(remoteGrantStatus: RemoteGrantStatus): Promise<void>--><!--Device-abilityToolAccessCtrl-export function updateRemoteGrantStatus(remoteGrantStatus: RemoteGrantStatus): Promise<void>-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| remoteGrantStatus | [RemoteGrantStatus](arkts-ability-abilitytoolaccessctrl-remotegrantstatus-e-sys.md) | Yes | 要设置的远程授权状态 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 不会返回任何值的Promise。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denial. The interface caller does not have permission "ohos.permission.MANAGE_TOOL_RUNTIME_PERMISSIONS". |
| 202 | The caller is not a system application. |
| 24010002 | Common internal error. possible cause: dependent service unavailable, resource access failure, etc. |
| 24010000 | Invalid parameter. RemoteGrantStatus is invalid. |
| 24010001 | Service is abnormal. possible cause: IPC failed. |

