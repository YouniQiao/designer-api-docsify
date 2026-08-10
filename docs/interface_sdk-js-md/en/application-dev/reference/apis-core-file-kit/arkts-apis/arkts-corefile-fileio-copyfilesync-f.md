# copyFileSync

## copyFileSync

```TypeScript
declare function copyFileSync(src: string | number, dest: string | number, mode?: number): void
```

以同步方法复制文件。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:copyFileSync](arkts-corefile-fileio-copyfilesync-f.md#copyfilesync)

<!--Device-unnamed-declare function copyFileSync(src: string | number, dest: string | number, mode?: number): void--><!--Device-unnamed-declare function copyFileSync(src: string | number, dest: string | number, mode?: number): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | string \| number | Yes | 待复制文件的路径或待复制文件的描述符。 |
| dest | string \| number | Yes | 目标文件路径或目标文件描述符。 |
| mode | number | No | mode提供覆盖文件的选项，当前仅支持0，且默认为0。&lt;br/&gt;0：完全覆盖目标文件，未覆盖部分将被裁切掉。 |

