# statSync

## statSync

```TypeScript
declare function statSync(path: string): Stat
```

以同步方法获取文件的信息。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:statSync](arkts-corefile-fileio-statsync-f.md#statsync)

<!--Device-unnamed-declare function statSync(path: string): Stat--><!--Device-unnamed-declare function statSync(path: string): Stat-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 待获取文件的应用沙箱路径。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Stat](arkts-corefile-fileio-stat-i.md) | 表示文件的具体信息。 |

