# verifyControllerDevicePackage (System API)

## verifyControllerDevicePackage

```TypeScript
export function verifyControllerDevicePackage(ticketInfo: RemoteAuthPackage[], remoteInfo: RemoteInfo):
    Promise<boolean[]>
```

验证来自控制器设备的授权包。验证控制器设备发送的远程授权包。它验证票证和远程设备信息，以确保授权是合法的。

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Required permissions:** ohos.permission.QUERY_TOOL_PERMISSIONS

<!--Device-abilityToolAccessCtrl-export function verifyControllerDevicePackage(ticketInfo: RemoteAuthPackage[], remoteInfo: RemoteInfo):    Promise<boolean[]>--><!--Device-abilityToolAccessCtrl-export function verifyControllerDevicePackage(ticketInfo: RemoteAuthPackage[], remoteInfo: RemoteInfo):    Promise<boolean[]>-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ticketInfo | [RemoteAuthPackage](arkts-ability-abilitytoolaccessctrl-remoteauthpackage-i-sys.md)[] | Yes | 远程授权包列表 |
| remoteInfo | [RemoteInfo](arkts-ability-abilitytoolaccessctrl-remoteinfo-i-sys.md) | Yes | 远端设备信息 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean[]&gt; | Promise用于返回\\${boolean[]}。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denial. The interface caller does not have permission "ohos.permission.QUERY_TOOL_PERMISSIONS". |
| 202 | The caller is not a system application. |
| 24010002 | Common internal error. possible cause: dependent service unavailable, resource access failure, etc. |
| 24010003 | The account is not logged in, network is unavailable, timeout, etc. |
| 24010000 | Invalid parameter. Format of ticketInfo or remoteInfo is invalid. |
| 24010001 | Service is abnormal. possible cause: IPC failed. |

