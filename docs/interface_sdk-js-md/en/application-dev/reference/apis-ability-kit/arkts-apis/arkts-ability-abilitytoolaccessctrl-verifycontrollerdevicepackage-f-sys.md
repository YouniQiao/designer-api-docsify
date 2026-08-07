# verifyControllerDevicePackage (System API)

## verifyControllerDevicePackage

```TypeScript
export function verifyControllerDevicePackage(ticketInfo: RemoteAuthPackage[], remoteInfo: RemoteInfo):
    Promise<boolean[]>
```

Verifies the authorization package from the controller device.This function verifies the remote authorization package sent by the controller device.It validates the ticket and remote device information to ensure the authorization is legitimate.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Required permissions:** ohos.permission.QUERY_TOOL_PERMISSIONS

<!--Device-abilityToolAccessCtrl-export function verifyControllerDevicePackage(ticketInfo: RemoteAuthPackage[], remoteInfo: RemoteInfo):    Promise<boolean[]>--><!--Device-abilityToolAccessCtrl-export function verifyControllerDevicePackage(ticketInfo: RemoteAuthPackage[], remoteInfo: RemoteInfo):    Promise<boolean[]>-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ticketInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_[] | Yes | Remote authorization package list. |
| remoteInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Remote device information. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean[]&gt; | Promise used to return \_\_\_ESCAPED\_DOLLAR\_\_\_{boolean[]}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denial. The interface caller does not have permission "ohos.permission.QUERY\_\_\_ESCAPED\_UNDERSCORE\_\_\_TOOL\_\_\_ESCAPED\_UNDERSCORE\_\_\_PERMISSIONS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| 24010000 | Invalid parameter. Format of ticketInfo or remoteInfo is invalid. |
| 24010001 | Service is abnormal. possible cause: IPC failed. |
| 24010002 | Common internal error. possible cause: dependent service unavailable, resource access failure, etc. |
| 24010003 | The account is not logged in, network is unavailable, timeout, etc. |

