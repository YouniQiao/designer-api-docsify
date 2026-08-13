# UploadProgressCallback

```TypeScript
export type UploadProgressCallback = (uploadedSize: number, totalSize: number) => void
```

The callback function for the download progress event.

**起始版本：** 23

**废弃版本：** -1

<!--Device-request-export type UploadProgressCallback = (uploadedSize: long, totalSize: long) => void--><!--Device-request-export type UploadProgressCallback = (uploadedSize: long, totalSize: long) => void-End-->

**系统能力：** SystemCapability.MiscServices.Upload

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uploadedSize | number | 是 |
| totalSize | number | 是 |
