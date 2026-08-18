# WebDownloadDelegate

WebDownloadDelegate is a delegate class in the ArkWeb framework used to listen for and handle download task events of the Web component. When a web page in the Web component triggers a file download (for example, when the user taps a download link or the **startDownload** method is called), the download task state changes are notified to the app through the callback APIs of this class. Developers register a **WebDownloadDelegate** instance with the Web component through **setDownloadDelegate** to take over the complete lifecycle management of the download process. WebDownloadDelegate defines four download lifecycle callbacks: [onBeforeDownload](../../apis-na/arkts-apis/arkts-na-webview-webdownloaddelegate-c.md#onbeforedownload) is invoked before the download starts, and the app must call [WebDownloadItem.start](../../apis-na/arkts-apis/arkts-na-webview-webdownloaditem-c.md#start) in this callback and specify a download path; otherwise, the download remains in the PENDING state. [onDownloadUpdated](../../apis-na/arkts-apis/arkts-na-webview-webdownloaddelegate-c.md#ondownloadupdated) is invoked during the download process, providing updated information such as the download progress (percentage) and the number of bytes received. [onDownloadFinish](../../apis-na/arkts-apis/arkts-na-webview-webdownloaddelegate-c.md#ondownloadfinish) is invoked when the download is complete. [onDownloadFailed](../../apis-na/arkts-apis/arkts-na-webview-webdownloaddelegate-c.md#ondownloadfailed) is invoked when the download fails, and the failed task can be saved through [WebDownloadItem.serialize](../../apis-na/arkts-apis/arkts-na-webview-webdownloaditem-c.md#serialize) for later recovery.

**Since:** 11

<!--Device-webview-class WebDownloadDelegate--><!--Device-webview-class WebDownloadDelegate-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## onBeforeDownload

```TypeScript
onBeforeDownload(callback: Callback<WebDownloadItem>): void
```

Invoked to notify the app before the download starts. The app must call **WebDownloadItem.start("xxx")** in this API and provide a download path. Otherwise, the download remains in the PENDING state. > **NOTE：**> > For a download task in the PENDING state, the file is first saved to a temporary directory. After > [WebDownloadItem.start](../../apis-na/arkts-apis/arkts-na-webview-webdownloaditem-c.md#start) is called and the target path is specified, the > temporary file is renamed to the target file name, and the remaining part of the download is saved directly to > the target path. To avoid generating a temporary file before **WebDownloadItem.start** is called, you can first > cancel the current download task through [WebDownloadItem.cancel](../../apis-na/arkts-apis/arkts-na-webview-webdownloaditem-c.md#cancel), and > then use [WebDownloadManager.resumeDownload](../../apis-na/arkts-apis/arkts-na-webview-webdownloadmanager-c.md#resumedownload) to resume the > canceled download task.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadDelegate-onBeforeDownload(callback: Callback<WebDownloadItem>): void--><!--Device-WebDownloadDelegate-onBeforeDownload(callback: Callback<WebDownloadItem>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WebDownloadItem](../../apis-na/arkts-apis/arkts-na-webview-webdownloaditem-c.md)&gt; | Yes | Callback invoked before the download starts. |

## onDownloadFailed

```TypeScript
onDownloadFailed(callback: Callback<WebDownloadItem>): void
```

Callback invoked when the download fails. The app can obtain detailed information about the download failure through this callback for error handling, retry, or logging.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadDelegate-onDownloadFailed(callback: Callback<WebDownloadItem>): void--><!--Device-WebDownloadDelegate-onDownloadFailed(callback: Callback<WebDownloadItem>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WebDownloadItem](../../apis-na/arkts-apis/arkts-na-webview-webdownloaditem-c.md)&gt; | Yes | Callback for the download failure. |

## onDownloadFinish

```TypeScript
onDownloadFinish(callback: Callback<WebDownloadItem>): void
```

Callback invoked when the download is complete. The app can obtain the information of the completed download task through this callback for subsequent processing (such as updating the UI or notifying the user).

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadDelegate-onDownloadFinish(callback: Callback<WebDownloadItem>): void--><!--Device-WebDownloadDelegate-onDownloadFinish(callback: Callback<WebDownloadItem>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WebDownloadItem](../../apis-na/arkts-apis/arkts-na-webview-webdownloaditem-c.md)&gt; | Yes | Callback invoked when the download is complete. |

## onDownloadUpdated

```TypeScript
onDownloadUpdated(callback: Callback<WebDownloadItem>): void
```

Callback invoked during the download process. The app can obtain information such as the download progress ( percentage) and the number of bytes received through this callback to monitor or update the download status.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadDelegate-onDownloadUpdated(callback: Callback<WebDownloadItem>): void--><!--Device-WebDownloadDelegate-onDownloadUpdated(callback: Callback<WebDownloadItem>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[WebDownloadItem](../../apis-na/arkts-apis/arkts-na-webview-webdownloaditem-c.md)&gt; | Yes | Callback used to return the download update. |

