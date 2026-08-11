# DownloadFailCallback

```TypeScript
export type DownloadFailCallback = (err: int) => void
```

The callback function for the download fail event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-request-export type DownloadFailCallback = (err: int) => void--><!--Device-request-export type DownloadFailCallback = (err: int) => void-End-->

**System capability:** SystemCapability.MiscServices.Download

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| err | int | Yes | the error code for download task. <br>The value should be an integer. |

