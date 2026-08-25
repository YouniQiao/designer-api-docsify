# WebDownloadItem

WebDownloadItem is a class in the ArkWeb framework used to represent and manage a single download task. Through the callback parameters of [WebDownloadDelegate](arkts-arkweb-webview-webdownloaddelegate-c.md), an app can obtain a WebDownloadItem instance and then query and control the download task, including starting the download to a specified path, querying the download progress and status, pausing/resuming/canceling the task, and serializing failed tasks for later recovery.

> **NOTE：**&gt;
> - During the download process, the download progress is notified to the user through WebDownloadDelegate, and the
> user can operate the download task through the WebDownloadItem parameter.&gt;
> - The maximum length of the download file path (including the file name) supported by WebDownloadItem is 255
> bytes<!--RP1--><!--RP1End-->.

**Since:** 11

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from 'kits/@kit.ArkWeb';
```

## cancel

```TypeScript
cancel(): void
```

Cancels the download task.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

## deserialize

```TypeScript
static deserialize(serializedData: Uint8Array): WebDownloadItem
```

Deserializes the serialized byte array into a **WebDownloadItem** object.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

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

Obtains the download speed, in bytes per second.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getFullPath

```TypeScript
getFullPath(): string
```

Obtains the full path of the downloaded file on the disk.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getGuid

```TypeScript
getGuid(): string
```

Obtains the unique ID of this download task.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getLastErrorCode

```TypeScript
getLastErrorCode(): WebDownloadErrorCode
```

Obtains the download error code.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WebDownloadErrorCode](arkts-arkweb-webview-webdownloaderrorcode-e.md) |

## getMethod

```TypeScript
getMethod(): string
```

Obtains the request mode of this download task.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getMimeType

```TypeScript
getMimeType(): string
```

Obtains the MIME type of this download task (for example, a sound file may be marked as audio/ogg, and an image file may be image/png).

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getOriginalUrl

```TypeScript
getOriginalUrl(): string
```

Obtains the original URL address of the download file.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getPercentComplete

```TypeScript
getPercentComplete(): number
```

Obtains the download progress. The value **100** indicates that the download is complete.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getReceivedBytes

```TypeScript
getReceivedBytes(): number
```

Obtains the number of received bytes.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getReferrerUrl

```TypeScript
getReferrerUrl(): string
```

Obtains the referrer address of the download file.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getState

```TypeScript
getState(): WebDownloadState
```

Obtains the download state.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WebDownloadState](arkts-arkweb-webview-webdownloadstate-e.md) |

## getSuggestedFileName

```TypeScript
getSuggestedFileName(): string
```

Obtains the suggested file name for this download task.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getTotalBytes

```TypeScript
getTotalBytes(): number
```

Obtains the total length of the file to be downloaded.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getUrl

```TypeScript
getUrl(): string
```

Obtains the download request URL.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## pause

```TypeScript
pause(): void
```

Pauses the download task.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100019](../errorcode-webview.md#17100019-download-not-started-yet) |

## resume

```TypeScript
resume(): void
```

Resumes a download task.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100016](../errorcode-webview.md#17100016-download-task-not-paused) |

## serialize

```TypeScript
serialize(): Uint8Array
```

Serializes the failed download to a byte array.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

## start

```TypeScript
start(downloadPath: string): void
```

Starts downloading to the specified directory. The parameter specifies the disk storage path (including the file name) of the download file.

> **NOTE：**&gt;
> This API must be used in the **onBeforeDownload** callback of **WebDownloadDelegate**. If it is not called in
> the callback, the download task remains in the PENDING state and is downloaded to a temporary directory. After
> the target path is specified by **WebDownloadItem.start**, the temporary files are renamed to the target path
> and the unfinished files are directly downloaded to the target path. If you do not want to download the file to
> the temporary directory before invoking **WebDownloadItem.start**, you can call **WebDownloadItem.cancel** to
> cancel the current download task and then call **WebDownloadManager.resumeDownload** to resume the task.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| downloadPath | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
