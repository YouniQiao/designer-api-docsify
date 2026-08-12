# cancelRetentionState

## Modules to Import

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
```

## cancelRetentionState

```TypeScript
function cancelRetentionState(docUris: Array<string>): Promise<void>
```

Cancels the sandbox retention state, that is, allows the sandbox application to be automatically uninstalled when the DLP file is closed. This API uses a promise to return the result.

This API is used to cancel the retention state for sandbox application and restore the default behavior to release system resources. It is applicable to scenarios where the DLP file is no longer frequently accessed.

**Since:** 10

<!--Device-dlpPermission-function cancelRetentionState(docUris: Array<string>): Promise<void>--><!--Device-dlpPermission-function cancelRetentionState(docUris: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [docUris](arkts-dataprotection-dlppermission-retentionsandboxinfo-i.md) | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [19100001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100001-invalid-parameter) |
| [19100011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-system-service-abnormal) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

let uri = "file://docs/storage/Users/currentUser/Desktop/test.txt.dlp";
dlpPermission.cancelRetentionState([uri]).then(() => { // Cancel the retention state for a sandbox application.
  console.info('success!');
}).catch((error: BusinessError)=> {
  console.error(JSON.stringify(error));
});
```


## cancelRetentionState

```TypeScript
function cancelRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void
```

Cancels the sandbox retention state, that is, allows the sandbox application to be automatically uninstalled when the DLP file is closed. This API uses an asynchronous callback to return the result.

This API is used to cancel the retention state for sandbox application and restore the default behavior to release system resources. It is applicable to scenarios where the DLP file is no longer frequently accessed.

**Since:** 10

<!--Device-dlpPermission-function cancelRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void--><!--Device-dlpPermission-function cancelRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [docUris](arkts-dataprotection-dlppermission-retentionsandboxinfo-i.md) | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [19100001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100001-invalid-parameter) |
| [19100011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-system-service-abnormal) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

let uri = "file://docs/storage/Users/currentUser/Desktop/test.txt.dlp";
dlpPermission.cancelRetentionState([uri], (err, res) => {
  if (err) {
    console.error(`Failed to cancel retention state. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('cancelRetentionState success');
  }
}); // Cancel the sandbox retention state.
```
