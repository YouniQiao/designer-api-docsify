# download

## Modules to Import

```TypeScript
import { request } from '@kit.BasicServicesKit';
```

## download

```TypeScript
function download(config: DownloadConfig, callback: AsyncCallback<DownloadTask>): void
```

Downloads a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [downloadFile](request.downloadFile(context:)

**Required permissions:** ohos.permission.INTERNET

**Model restriction:** This API can be used only in the FA model.

<!--Device-request-function download(config: DownloadConfig, callback: AsyncCallback<DownloadTask>): void--><!--Device-request-function download(config: DownloadConfig, callback: AsyncCallback<DownloadTask>): void-End-->

**System capability:** SystemCapability.MiscServices.Download

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [DownloadConfig](arkts-basicservices-request-downloadconfig-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[DownloadTask](arkts-basicservices-request-downloadtask-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
let downloadTask: request.DownloadTask;
// Replace the URL with the HTTP address of the real server.
request.download({ url: 'https://xxxx/xxxxx.hap', 
filePath: 'xxx/xxxxx.hap'}, (err: BusinessError, data: request.DownloadTask) => {
  if (err) {
    console.error(`Failed to request the download. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  downloadTask = data;
});
```


## download

```TypeScript
function download(config: DownloadConfig): Promise<DownloadTask>
```

Downloads a file. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [downloadFile](request.downloadFile(context:)

**Required permissions:** ohos.permission.INTERNET

**Model restriction:** This API can be used only in the FA model.

<!--Device-request-function download(config: DownloadConfig): Promise<DownloadTask>--><!--Device-request-function download(config: DownloadConfig): Promise<DownloadTask>-End-->

**System capability:** SystemCapability.MiscServices.Download

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [DownloadConfig](arkts-basicservices-request-downloadconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DownloadTask](arkts-basicservices-request-downloadtask-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
let downloadTask: request.DownloadTask;
// Replace the URL with the HTTP address of the real server.
request.download({ url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
  downloadTask = data;
}).catch((err: BusinessError) => {
  console.error(`Failed to request the download. Code: ${err.code}, message: ${err.message}`);
})
```
