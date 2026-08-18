# generateControllerDevicePackage (System API)

## Modules to Import

```TypeScript
```

## generateControllerDevicePackage

```TypeScript
export function generateControllerDevicePackage(remoteUserAuthResult: RemoteUserAuthResults[]):
    Promise<RemoteAuthPackage[]>
```

Generates an authorization package for the controller device. This function generates a remote authorization package based on the remote user authorization results. The generated package can be sent to the controlled device for permission verification.

**Since:** 26.1.0

**Required permissions:** ohos.permission.QUERY_TOOL_PERMISSIONS

<!--Device-abilityToolAccessCtrl-export function generateControllerDevicePackage(remoteUserAuthResult: RemoteUserAuthResults[]):    Promise<RemoteAuthPackage[]>--><!--Device-abilityToolAccessCtrl-export function generateControllerDevicePackage(remoteUserAuthResult: RemoteUserAuthResults[]):    Promise<RemoteAuthPackage[]>-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| remoteUserAuthResult | [RemoteUserAuthResults](arkts-ability-abilitytoolaccessctrl-remoteuserauthresults-i-sys.md)[] | Yes | Remote user authorization result list. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[RemoteAuthPackage](arkts-ability-abilitytoolaccessctrl-remoteauthpackage-i-sys.md)[]&gt; | Promise used to return \\${RemoteAuthPackage[]}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denial. The interface caller does not have permission "ohos.permission.QUERY_TOOL_PERMISSIONS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| 24010002 | Common internal error. possible cause: dependent service unavailable, resource access failure, etc. |
| 24010003 | The account is not logged in, network is unavailable, timeout, etc. |
| 24010000 | Invalid parameter. OperationType and operationInfo do not match, specified callerTokenId does not exist, etc. |
| 24010001 | Service is abnormal. possible cause: IPC failed. |

