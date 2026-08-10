# getRemoteGrantStatus (System API)

## getRemoteGrantStatus

```TypeScript
export function getRemoteGrantStatus(): Promise<RemoteGrantStatus>
```

获取远程授权状态。该功能用于查询远程授权特性的使能状态。启用时，设备可以向远程设备授予权限；禁用时，不允许远程授权。

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Required permissions:** ohos.permission.QUERY_TOOL_PERMISSIONS

<!--Device-abilityToolAccessCtrl-export function getRemoteGrantStatus(): Promise<RemoteGrantStatus>--><!--Device-abilityToolAccessCtrl-export function getRemoteGrantStatus(): Promise<RemoteGrantStatus>-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;RemoteGrantStatus&gt; | Promise用于返回\\${RemoteGrantStatus}。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denial. The interface caller does not have permission "ohos.permission.QUERY_TOOL_PERMISSIONS". |
| 202 | The caller is not a system application. |
| 24010002 | Common internal error. possible cause: dependent service unavailable, resource access failure, etc. |
| 24010001 | Service is abnormal. possible cause: IPC failed. |

