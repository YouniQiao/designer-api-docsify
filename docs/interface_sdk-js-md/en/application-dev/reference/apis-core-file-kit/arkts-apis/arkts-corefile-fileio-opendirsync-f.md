# opendirSync

## opendirSync

```TypeScript
declare function opendirSync(path: string): Dir
```

以同步方法打开文件目录。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:listFileSync](arkts-corefile-file-fs-listfilesync-f.md#listfilesync)

<!--Device-unnamed-declare function opendirSync(path: string): Dir--><!--Device-unnamed-declare function opendirSync(path: string): Dir-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 待打开文件目录的应用沙箱路径。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Dir](arkts-corefile-fileio-dir-depr-i.md) | 返回Dir对象。 |

