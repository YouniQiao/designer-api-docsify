# DownloadProgressCallback

```TypeScript
export type DownloadProgressCallback = (receivedSize: number, totalSize: number) => void
```

The callback function for the download progress event.

**起始版本：** 23

<!--Device-request-export type DownloadProgressCallback = (receivedSize: long, totalSize: long) => void--><!--Device-request-export type DownloadProgressCallback = (receivedSize: long, totalSize: long) => void-End-->

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| receivedSize | number | 是 |
| totalSize | number | 是 |
