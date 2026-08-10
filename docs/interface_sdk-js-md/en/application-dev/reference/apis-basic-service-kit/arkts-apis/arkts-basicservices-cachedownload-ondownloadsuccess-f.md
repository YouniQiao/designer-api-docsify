# onDownloadSuccess

## Modules to Import

```TypeScript
import { cacheDownload } from 'kits/@kit.BasicServicesKit';
```

## onDownloadSuccess

```TypeScript
function onDownloadSuccess(url: string, callback: Callback<void>): void
```

订阅预下载的完成事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-cacheDownload-function onDownloadSuccess(url: string, callback: Callback<void>): void--><!--Device-cacheDownload-function onDownloadSuccess(url: string, callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | 待注册回调的url，url字符串的最大长度为8192字节。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | 回调函数。 |

## Examples

```TypeScript
import { cacheDownload } from '@kit.BasicServicesKit';

try {
  const successCallback = () => {
    console.info("Succeeded in getting callback from cacheDownload");
  };
  // Subscribe to the pre-download completion events. Callback is invoked when the download is complete.
  cacheDownload.onDownloadSuccess("https://www.example.com", successCallback)
  // Download the resource. If the download is successful, the resource will be cached to the specified file in the application memory or sandbox directory. 
  cacheDownload.download("https://www.example.com", {});
} catch (err) {
  console.error(`Failed to download the resource. err code: ${err.code}, err message: ${err.message}`);
}
```

