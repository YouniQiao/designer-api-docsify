# DownloadProgressCallback

```TypeScript
export type DownloadProgressCallback = (receivedSize: long, totalSize: long) => void
```

The callback function for the download progress event.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.Download

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| receivedSize | long | 是 |
| totalSize | long | 是 |
