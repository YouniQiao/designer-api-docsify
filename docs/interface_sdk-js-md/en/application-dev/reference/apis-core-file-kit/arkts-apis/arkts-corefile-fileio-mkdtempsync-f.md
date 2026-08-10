# mkdtempSync

## mkdtempSync

```TypeScript
declare function mkdtempSync(prefix: string): string
```

以同步的方法创建临时目录。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:mkdtempSync](arkts-corefile-fileio-mkdtempsync-f.md#mkdtempsync)

<!--Device-unnamed-declare function mkdtempSync(prefix: string): string--><!--Device-unnamed-declare function mkdtempSync(prefix: string): string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| prefix | string | Yes | 用随机产生的字符串替换以“XXXXXX”结尾目录路径。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 产生的唯一目录路径。 |

