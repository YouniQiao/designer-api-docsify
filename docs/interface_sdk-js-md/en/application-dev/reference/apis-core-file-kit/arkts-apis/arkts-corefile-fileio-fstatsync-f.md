# fstatSync

## fstatSync

```TypeScript
declare function fstatSync(fd: number): Stat
```

以同步方法基于文件描述符获取文件状态信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:statSync](arkts-corefile-fileio-statsync-f.md#statsync)

<!--Device-unnamed-declare function fstatSync(fd: number): Stat--><!--Device-unnamed-declare function fstatSync(fd: number): Stat-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | 待获取文件状态的文件描述符。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Stat](arkts-corefile-fileio-stat-i.md) | 表示文件状态的具体信息。 |

