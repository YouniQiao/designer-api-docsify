# on (System API)

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## on('uninstallDLPSandbox')

```TypeScript
function on(type: 'uninstallDLPSandbox', listener: Callback<DLPSandboxState>): void
```

Registers a listener for the DLP sandbox uninstall event, which is used to detect changes in the sandbox environment. After the registration, the system notifies the application using a callback when the DLP sandbox is uninstalled.

After a listener is registered by calling **on**, you are advised to call   
**[off](dlpPermission.off(type: 'uninstallDLPSandbox', listener?: Callback&lt;DLPSandboxState&gt;))** to unregister the listener and release resources when the listener is no longer needed.

The DLP management application needs to track the creation and destruction status of the sandbox to maintain the sandbox list or release resources.

**Since:** 10

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

<!--Device-dlpPermission-function on(type: 'uninstallDLPSandbox', listener: Callback<DLPSandboxState>): void--><!--Device-dlpPermission-function on(type: 'uninstallDLPSandbox', listener: Callback<DLPSandboxState>): void-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'uninstallDLPSandbox' | Yes |
| listener | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DLPSandboxState&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.on('uninstallDLPSandbox', (info: dlpPermission.DLPSandboxState) => {
  console.info('uninstallDLPSandbox event', info.appIndex, info.bundleName)
}); // Subscribe to the DLP sandbox application uninstall event.
```
