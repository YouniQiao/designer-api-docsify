# truncateSync

## truncateSync

```TypeScript
declare function truncateSync(path: string, len?: number): void
```

以同步方法基于文件路径截断文件。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:truncateSync](arkts-corefile-fileio-truncatesync-f.md#truncatesync)

<!--Device-unnamed-declare function truncateSync(path: string, len?: number): void--><!--Device-unnamed-declare function truncateSync(path: string, len?: number): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 待截断文件的应用沙箱路径。 |
| len | number | No | 文件截断后的长度，单位为Byte。默认为0。 |

