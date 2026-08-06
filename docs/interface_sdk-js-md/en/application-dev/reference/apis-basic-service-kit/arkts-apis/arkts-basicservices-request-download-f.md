# download

## download

```TypeScript
function download(config: DownloadConfig, callback: AsyncCallback<DownloadTask>): void
```

Downloads a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [request.downloadFile](arkts-basicservices-request-downloadfile-f.md#downloadfile)(context:

**Required permissions:** ohos.permission.INTERNET

**Model restriction:** This API can be used only in the FA model.

<!--Device-request-function download(config: DownloadConfig, callback: AsyncCallback<DownloadTask>): void--><!--Device-request-function download(config: DownloadConfig, callback: AsyncCallback<DownloadTask>): void-End-->

**System capability:** SystemCapability.MiscServices.Download

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Download configuration. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;DownloadTask&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the **DownloadTask** object obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | The permissions check fails. |

**Example**

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

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [request.downloadFile](arkts-basicservices-request-downloadfile-f.md#downloadfile)(context:

**Required permissions:** ohos.permission.INTERNET

**Model restriction:** This API can be used only in the FA model.

<!--Device-request-function download(config: DownloadConfig): Promise<DownloadTask>--><!--Device-request-function download(config: DownloadConfig): Promise<DownloadTask>-End-->

**System capability:** SystemCapability.MiscServices.Download

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Download configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DownloadTask&gt; | Promise used to return the **DownloadTask** object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | The permissions check fails. |

**Example**

```TypeScript
let downloadTask: request.DownloadTask;
// Replace the URL with the HTTP address of the real server.
request.download({ url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
  downloadTask = data;
}).catch((err: BusinessError) => {
  console.error(`Failed to request the download. Code: ${err.code}, message: ${err.message}`);
})
```

