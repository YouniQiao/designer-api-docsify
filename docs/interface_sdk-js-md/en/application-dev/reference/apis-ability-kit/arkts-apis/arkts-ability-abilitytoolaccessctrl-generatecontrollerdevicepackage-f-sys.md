# generateControllerDevicePackage (System API)

## generateControllerDevicePackage

```TypeScript
export function generateControllerDevicePackage(remoteUserAuthResult: RemoteUserAuthResults[]):
    Promise<RemoteAuthPackage[]>
```

Generates an authorization package for the controller device.This function generates a remote authorization package based on the remote user authorization results.The generated package can be sent to the controlled device for permission verification.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Required permissions:** ohos.permission.QUERY_TOOL_PERMISSIONS

<!--Device-abilityToolAccessCtrl-export function generateControllerDevicePackage(remoteUserAuthResult: RemoteUserAuthResults[]):    Promise<RemoteAuthPackage[]>--><!--Device-abilityToolAccessCtrl-export function generateControllerDevicePackage(remoteUserAuthResult: RemoteUserAuthResults[]):    Promise<RemoteAuthPackage[]>-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| remoteUserAuthResult | \_\_\_MD\_LINK\_USD\_0\_\_\_[] | Yes | Remote user authorization result list. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;RemoteAuthPackage[]&gt; | Promise used to return \_\_\_ESCAPED\_DOLLAR\_\_\_{RemoteAuthPackage[]}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denial. The interface caller does not have permission "ohos.permission.QUERY\_\_\_ESCAPED\_UNDERSCORE\_\_\_TOOL\_\_\_ESCAPED\_UNDERSCORE\_\_\_PERMISSIONS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| 24010000 | Invalid parameter. OperationType and operationInfo do not match, specified callerTokenId does not exist, etc. |
| 24010001 | Service is abnormal. possible cause: IPC failed. |
| 24010002 | Common internal error. possible cause: dependent service unavailable, resource access failure, etc. |
| 24010003 | The account is not logged in, network is unavailable, timeout, etc. |

