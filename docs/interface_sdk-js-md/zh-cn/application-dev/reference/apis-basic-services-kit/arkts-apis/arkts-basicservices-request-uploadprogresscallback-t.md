# UploadProgressCallback

```TypeScript
export type UploadProgressCallback = (uploadedSize: long, totalSize: long) => void
```

The callback function for the download progress event.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.Upload

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uploadedSize | long | 是 |
| totalSize | long | 是 |
