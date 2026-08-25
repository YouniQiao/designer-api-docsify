# DownloadInfo

Defines the download task information, which is the callback parameter of the [getTaskInfo](arkts-basicservices-request-downloadtask-i.md#gettaskinfo) API.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

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

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.Download

## downloadedBytes

```TypeScript
downloadedBytes: long
```

Real-time download size, in bytes.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.Download

## downloadId

```TypeScript
downloadId: long
```

Download task ID.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.Download

## downloadTitle

```TypeScript
downloadTitle: string
```

Name of the download task.

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.Download

## downloadTotalBytes

```TypeScript
downloadTotalBytes: long
```

Total size of the files to download, in bytes.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.Download

## failedReason

```TypeScript
failedReason: int
```

Cause of the download failure. The value can be any constant in [Download Error Codes](../../../reference/apis-basic-services-kit/js-apis-request.md#constants).

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.Download

## fileName

```TypeScript
fileName: string
```

Name of the downloaded file.

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.Download

## filePath

```TypeScript
filePath: string
```

URI of the saved file.

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.Download

## pausedReason

```TypeScript
pausedReason: int
```

Cause of download pause. The value can be any constant in [Causes of Download Pause](../../../reference/apis-basic-services-kit/js-apis-request.md#constants).

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.Download

## status

```TypeScript
status: int
```

Download task status code. The value can be any constant in [Download Task Status Codes](../../../reference/apis-basic-services-kit/js-apis-request.md#constants).

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.Download

## targetURI

```TypeScript
targetURI: string
```

URI of the downloaded file.

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.Download
