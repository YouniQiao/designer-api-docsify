# WebDownloadManager

You can trigger download manually through this interface, or resume failed or canceled downloads.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-webview-class WebDownloadManager--><!--Device-webview-class WebDownloadManager-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## resumeDownload

```TypeScript
static resumeDownload(webDownloadItem: WebDownloadItem): void
```

Resume the canceled or failed download.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebDownloadManager-static resumeDownload(webDownloadItem: WebDownloadItem): void--><!--Device-WebDownloadManager-static resumeDownload(webDownloadItem: WebDownloadItem): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| webDownloadItem | [WebDownloadItem](arkts-webview-webdownloaditem-c.md) | Yes | Download that need to be resume. |

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

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebDownloadManager-static setDownloadDelegate(delegate: WebDownloadDelegate): void--><!--Device-WebDownloadManager-static setDownloadDelegate(delegate: WebDownloadDelegate): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| delegate | [WebDownloadDelegate](arkts-webview-webdownloaddelegate-c.md) | Yes | Delegate used for download triggered from WebDownloadManager. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();

  build() {
    Column() {
      Button('setDownloadDelegate')
        .onClick(() => {
          try {
            this.controller.setDownloadDelegate(this.delegate);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

