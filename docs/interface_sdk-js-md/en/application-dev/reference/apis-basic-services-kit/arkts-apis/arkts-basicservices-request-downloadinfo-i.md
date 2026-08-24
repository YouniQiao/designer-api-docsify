# DownloadInfo

Defines the download task information, which is the callback parameter of the [getTaskInfo](arkts-basicservices-request-downloadtask-i.md#gettaskinfo) API.

**Since:** 23

<!--Device-request-interface DownloadInfo--><!--Device-request-interface DownloadInfo-End-->

**System capability:** SystemCapability.MiscServices.Download

## Modules to Import

```TypeScript
import { request } from '@kit.BasicServicesKit';
```

## description

```TypeScript
description: string
```

Description of the download task.

**Type:** string

**Since:** 23

<!--Device-DownloadInfo-description: string--><!--Device-DownloadInfo-description: string-End-->

**System capability:** SystemCapability.MiscServices.Download

## downloadedBytes

```TypeScript
downloadedBytes: long
```

Real-time download size, in bytes.

**Type:** long

**Since:** 23

<!--Device-DownloadInfo-downloadedBytes: long--><!--Device-DownloadInfo-downloadedBytes: long-End-->

**System capability:** SystemCapability.MiscServices.Download

## downloadId

```TypeScript
downloadId: long
```

Download task ID.

**Type:** long

**Since:** 23

<!--Device-DownloadInfo-downloadId: long--><!--Device-DownloadInfo-downloadId: long-End-->

**System capability:** SystemCapability.MiscServices.Download

## downloadTitle

```TypeScript
downloadTitle: string
```

Name of the download task.

**Type:** string

**Since:** 23

<!--Device-DownloadInfo-downloadTitle: string--><!--Device-DownloadInfo-downloadTitle: string-End-->

**System capability:** SystemCapability.MiscServices.Download

## downloadTotalBytes

```TypeScript
downloadTotalBytes: long
```

Total size of the files to download, in bytes.

**Type:** long

**Since:** 23

<!--Device-DownloadInfo-downloadTotalBytes: long--><!--Device-DownloadInfo-downloadTotalBytes: long-End-->

**System capability:** SystemCapability.MiscServices.Download

## failedReason

```TypeScript
failedReason: int
```

Cause of the download failure. The value can be any constant in [Download Error Codes](arkts-basicservices-request-n.md#constants).

**Type:** int

**Since:** 23

<!--Device-DownloadInfo-failedReason: int--><!--Device-DownloadInfo-failedReason: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## fileName

```TypeScript
fileName: string
```

Name of the downloaded file.

**Type:** string

**Since:** 23

<!--Device-DownloadInfo-fileName: string--><!--Device-DownloadInfo-fileName: string-End-->

**System capability:** SystemCapability.MiscServices.Download

## filePath

```TypeScript
filePath: string
```

URI of the saved file.

**Type:** string

**Since:** 23

<!--Device-DownloadInfo-filePath: string--><!--Device-DownloadInfo-filePath: string-End-->

**System capability:** SystemCapability.MiscServices.Download

## pausedReason

```TypeScript
pausedReason: int
```

Cause of download pause. The value can be any constant in [Causes of Download Pause](arkts-basicservices-request-n.md#constants).

**Type:** int

**Since:** 23

<!--Device-DownloadInfo-pausedReason: int--><!--Device-DownloadInfo-pausedReason: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## status

```TypeScript
status: int
```

Download task status code. The value can be any constant in [Download Task Status Codes](arkts-basicservices-request-n.md#constants).

**Type:** int

**Since:** 23

<!--Device-DownloadInfo-status: int--><!--Device-DownloadInfo-status: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## targetURI

```TypeScript
targetURI: string
```

URI of the downloaded file.

**Type:** string

**Since:** 23

<!--Device-DownloadInfo-targetURI: string--><!--Device-DownloadInfo-targetURI: string-End-->

**System capability:** SystemCapability.MiscServices.Download

