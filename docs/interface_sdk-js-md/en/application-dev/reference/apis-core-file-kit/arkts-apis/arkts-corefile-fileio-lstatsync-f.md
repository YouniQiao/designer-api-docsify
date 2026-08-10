# lstatSync

## lstatSync

```TypeScript
declare function lstatSync(path: string): Stat
```

以同步方法获取链接信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:lstatSync](arkts-corefile-fileio-lstatsync-f.md#lstatsync)

<!--Device-unnamed-declare function lstatSync(path: string): Stat--><!--Device-unnamed-declare function lstatSync(path: string): Stat-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 目标文件的应用沙箱路径。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Stat](arkts-corefile-fileio-stat-i.md) | 表示文件的具体信息。 |

