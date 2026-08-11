# on

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## on('openDLPFile')

```TypeScript
function on(type: 'openDLPFile', listener: Callback<AccessedDLPFileInfo>): void
```

Subscribes to a DLP file open event. After this API is successfully called, a callback notification is sent to the current application when the DLP file is opened. This API can be called only in non-DLP sandbox applications.

You can subscribe to this event when your application needs to perform specific operations (such as logging and updating the UI) after a DLP file is opened.

**Since:** 10

<!--Device-dlpPermission-function on(type: 'openDLPFile', listener: Callback<AccessedDLPFileInfo>): void--><!--Device-dlpPermission-function on(type: 'openDLPFile', listener: Callback<AccessedDLPFileInfo>): void-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'openDLPFile' | Yes |
| listener | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AccessedDLPFileInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100007](../errorcode-dlp.md#19100007-access-denied-for-a-dlp-sandbox-application) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.on('openDLPFile', (info: dlpPermission.AccessedDLPFileInfo) => {
  console.info('openDlpFile event', info.uri, info.lastOpenTime);
}); // Subscribe to the DLP file open event.
```
