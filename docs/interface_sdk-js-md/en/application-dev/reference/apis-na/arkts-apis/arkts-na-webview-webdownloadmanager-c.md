# WebDownloadManager

You can trigger download manually through this interface, or resume failed or canceled downloads.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-webview-class WebDownloadManager--><!--Device-webview-class WebDownloadManager-End-->

**System capability:** SystemCapability.Web.Webview.Core

## resumeDownload

```TypeScript
static resumeDownload(webDownloadItem: WebDownloadItem): void
```

Resume the canceled or failed download.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebDownloadManager-static resumeDownload(webDownloadItem: WebDownloadItem): void--><!--Device-WebDownloadManager-static resumeDownload(webDownloadItem: WebDownloadItem): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| webDownloadItem | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Download that need to be resume. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100018](../../apis-arkweb/errorcode-webview.md#17100018-no-webdownloaddelegate-available) | No WebDownloadDelegate has been set yet. |

## setDownloadDelegate

```TypeScript
static setDownloadDelegate(delegate: WebDownloadDelegate): void
```

Set a delegate used to receive the progress of the download triggered from WebDownloadManager.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebDownloadManager-static setDownloadDelegate(delegate: WebDownloadDelegate): void--><!--Device-WebDownloadManager-static setDownloadDelegate(delegate: WebDownloadDelegate): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| delegate | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Delegate used for download triggered from WebDownloadManager. |

