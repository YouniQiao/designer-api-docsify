# WebDownloadItem

Represents a download task, You can use this object to operate the corresponding download task. Currently, the maximum length of the download file name supported by **WebDownloadItem** is 255 bytes.

**Since:** 11

**Deprecated since:** -1

<!--Device-webview-class WebDownloadItem--><!--Device-webview-class WebDownloadItem-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## cancel

```TypeScript
cancel(): void
```

Cancel the web download.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadItem-cancel(): void--><!--Device-WebDownloadItem-cancel(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## deserialize

```TypeScript
static deserialize(serializedData: Uint8Array): WebDownloadItem
```

Deserialize web download from typed array.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadItem-static deserialize(serializedData: Uint8Array): WebDownloadItem--><!--Device-WebDownloadItem-static deserialize(serializedData: Uint8Array): WebDownloadItem-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| serializedData | Uint8Array | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WebDownloadItem](arkts-arkweb-webview-webdownloaditem-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getCurrentSpeed

```TypeScript
getCurrentSpeed(): number
```

Get current speed, in bytes per second.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadItem-getCurrentSpeed(): number--><!--Device-WebDownloadItem-getCurrentSpeed(): number-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getFullPath

```TypeScript
getFullPath(): string
```

Get full path of the web download.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadItem-getFullPath(): string--><!--Device-WebDownloadItem-getFullPath(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getGuid

```TypeScript
getGuid(): string
```

Get guid.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadItem-getGuid(): string--><!--Device-WebDownloadItem-getGuid(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getLastErrorCode

```TypeScript
getLastErrorCode(): WebDownloadErrorCode
```

Get last error code of the web download.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadItem-getLastErrorCode(): WebDownloadErrorCode--><!--Device-WebDownloadItem-getLastErrorCode(): WebDownloadErrorCode-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WebDownloadErrorCode](arkts-arkweb-webview-webdownloaderrorcode-e.md) |

## getMethod

```TypeScript
getMethod(): string
```

Get http method of the web download request.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadItem-getMethod(): string--><!--Device-WebDownloadItem-getMethod(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getMimeType

```TypeScript
getMimeType(): string
```

Get mime type of the web download.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadItem-getMimeType(): string--><!--Device-WebDownloadItem-getMimeType(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getOriginalUrl

```TypeScript
getOriginalUrl(): string
```

Get the original url of the web download.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebDownloadItem-getOriginalUrl(): string--><!--Device-WebDownloadItem-getOriginalUrl(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getPercentComplete

```TypeScript
getPercentComplete(): number
```

Get percent complete.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadItem-getPercentComplete(): number--><!--Device-WebDownloadItem-getPercentComplete(): number-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getReceivedBytes

```TypeScript
getReceivedBytes(): number
```

Get received bytes.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadItem-getReceivedBytes(): number--><!--Device-WebDownloadItem-getReceivedBytes(): number-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getReferrerUrl

```TypeScript
getReferrerUrl(): string
```

Get the referrer url of the web download.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebDownloadItem-getReferrerUrl(): string--><!--Device-WebDownloadItem-getReferrerUrl(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getState

```TypeScript
getState(): WebDownloadState
```

Get state of the web download.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadItem-getState(): WebDownloadState--><!--Device-WebDownloadItem-getState(): WebDownloadState-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WebDownloadState](arkts-arkweb-webview-webdownloadstate-e.md) |

## getSuggestedFileName

```TypeScript
getSuggestedFileName(): string
```

Get suggested file name of the web download request.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadItem-getSuggestedFileName(): string--><!--Device-WebDownloadItem-getSuggestedFileName(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getTotalBytes

```TypeScript
getTotalBytes(): number
```

Get total bytes.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadItem-getTotalBytes(): number--><!--Device-WebDownloadItem-getTotalBytes(): number-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getUrl

```TypeScript
getUrl(): string
```

Get url of the web download request.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadItem-getUrl(): string--><!--Device-WebDownloadItem-getUrl(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## pause

```TypeScript
pause(): void
```

Pause the web download.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadItem-pause(): void--><!--Device-WebDownloadItem-pause(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100019](../errorcode-webview.md#17100019-download-not-started-yet) |

## resume

```TypeScript
resume(): void
```

Resume the web download. Use WebDownloadManager.resumeDownload to resume deserialized downloads. WebDownloadItem.resume is only used to resume the currently paused download.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadItem-resume(): void--><!--Device-WebDownloadItem-resume(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100016](../errorcode-webview.md#17100016-download-task-not-paused) |

## serialize

```TypeScript
serialize(): Uint8Array
```

Serialize web download to typed array.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadItem-serialize(): Uint8Array--><!--Device-WebDownloadItem-serialize(): Uint8Array-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

## start

```TypeScript
start(downloadPath: string): void
```

Start the web download. &lt;p&gt;&lt;strong&gt;API Note&lt;/strong&gt;:&lt;br&gt; This API must be used in the **onBeforeDownload** callback of **WebDownloadDelegate**. If it is not called in the callback, the download task remains in the PENDING state and is downloaded to a temporary directory. After the target path is specified by **WebDownloadItem.start**, the temporary files are renamed to the target path and the unfinished files are directly downloaded to the target path. If you do not want to download the file to the temporary directory before invoking **WebDownloadItem.start**, you can call **WebDownloadItem.cancel** to cancel the current download task and then call **WebDownloadManager.resumeDownload** to resume the task. &lt;/p&gt;

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebDownloadItem-start(downloadPath: string): void--><!--Device-WebDownloadItem-start(downloadPath: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| downloadPath | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
