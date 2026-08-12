# verifyControlledDevicePackage (System API)

## verifyControlledDevicePackage

```TypeScript
export function verifyControlledDevicePackage(ticketInfo: RemoteAuthPackage[]): Promise<boolean[]>
```

Verifies the authorization package from the controlled device.This function verifies the remote authorization package sent by the controlled device.It validates the ticket to ensure the authorization is legitimate.

**Since:** 26.1.0

**Required permissions:** ohos.permission.QUERY_TOOL_PERMISSIONS

<!--Device-abilityToolAccessCtrl-export function verifyControlledDevicePackage(ticketInfo: RemoteAuthPackage[]): Promise<boolean[]>--><!--Device-abilityToolAccessCtrl-export function verifyControlledDevicePackage(ticketInfo: RemoteAuthPackage[]): Promise<boolean[]>-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ticketInfo | [RemoteAuthPackage](arkts-ability-abilitytoolaccessctrl-remoteauthpackage-i-sys.md)[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 24010002 |
| 24010003 |
| 24010000 |
| 24010001 |
