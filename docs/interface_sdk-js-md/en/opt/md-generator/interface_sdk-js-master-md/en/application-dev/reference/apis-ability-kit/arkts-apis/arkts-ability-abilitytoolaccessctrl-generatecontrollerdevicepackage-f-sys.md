# generateControllerDevicePackage (System API)

## generateControllerDevicePackage

```TypeScript
export function generateControllerDevicePackage(remoteUserAuthResult: RemoteUserAuthResults[]):
    Promise<RemoteAuthPackage[]>
```

Generates an authorization package for the controller device.This function generates a remote authorization package based on the remote user authorization results.The generated package can be sent to the controlled device for permission verification.

**Since:** 26.1.0

**Required permissions:** ohos.permission.QUERY_TOOL_PERMISSIONS

<!--Device-abilityToolAccessCtrl-export function generateControllerDevicePackage(remoteUserAuthResult: RemoteUserAuthResults[]):    Promise<RemoteAuthPackage[]>--><!--Device-abilityToolAccessCtrl-export function generateControllerDevicePackage(remoteUserAuthResult: RemoteUserAuthResults[]):    Promise<RemoteAuthPackage[]>-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| remoteUserAuthResult | [RemoteUserAuthResults](arkts-ability-abilitytoolaccessctrl-remoteuserauthresults-i-sys.md)[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;RemoteAuthPackage[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 24010002 |
| 24010003 |
| 24010000 |
| 24010001 |
