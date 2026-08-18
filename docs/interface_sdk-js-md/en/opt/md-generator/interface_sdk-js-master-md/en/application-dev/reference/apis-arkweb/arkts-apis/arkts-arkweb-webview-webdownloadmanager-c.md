# WebDownloadManager

WebDownloadManager is a static management class for download tasks of the Web component in the ArkWeb framework. It manages all file download processes triggered by the Web component. Developers can use this class to set a download delegate to receive download progress callbacks and resume failed download tasks. All methods of this class are static methods and take effect globally within the entire app. WebDownloadManager works together with [WebDownloadDelegate](arkts-arkweb-webview-webdownloaddelegate-c.md#webdownloaddelegate) and [WebDownloadItem](arkts-arkweb-webview-webdownloaditem-c.md#webdownloaditem): WebDownloadManager is responsible for lifecycle management and delegate setting of download tasks, WebDownloadDelegate reports download progress and status change events to the app layer, and WebDownloadItem represents a single download task entity, supporting operations such as pause, resume, and cancel.

**Since:** 11

<!--Device-webview-class WebDownloadManager--><!--Device-webview-class WebDownloadManager-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## resumeDownload

```TypeScript
static resumeDownload(webDownloadItem: WebDownloadItem): void
```

Resumes a failed download task. You need to obtain the deserialized object through the [WebDownloadItem.deserialize](arkts-arkweb-webview-webdownloaditem-c.md#deserialize) method. This applies only to previously failed download tasks. > **NOTE：**> > - Before calling this API, if the Web component has not been created and the initializeWebEngine method has not > been executed to complete web kernel initialization, you must call the initializeWebEngine method for > initialization first. Otherwise, calling this API is invalid. > > - You must call [setDownloadDelegate](#setdownloaddelegate) to set the download > delegate first. Otherwise, error code 17100018 will be thrown.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadManager-static resumeDownload(webDownloadItem: WebDownloadItem): void--><!--Device-WebDownloadManager-static resumeDownload(webDownloadItem: WebDownloadItem): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| webDownloadItem | [WebDownloadItem](arkts-arkweb-webview-webdownloaditem-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17100018](../errorcode-webview.md#17100018-no-webdownloaddelegate-available) |

## setDownloadDelegate

```TypeScript
static setDownloadDelegate(delegate: WebDownloadDelegate): void
```

Sets the delegate used to receive download progress triggered by WebDownloadManager. > **NOTE：**> > - Before calling this API, if the Web component has not been created and the > [initializeWebEngine](arkts-arkweb-webview-webviewcontroller-c.md#initializewebengine) method has not been executed, you > must call this method to initialize the web kernel first. Otherwise, calling this API is invalid.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadManager-static setDownloadDelegate(delegate: WebDownloadDelegate): void--><!--Device-WebDownloadManager-static setDownloadDelegate(delegate: WebDownloadDelegate): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| delegate | [WebDownloadDelegate](arkts-arkweb-webview-webdownloaddelegate-c.md) | Yes |
