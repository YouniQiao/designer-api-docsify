# opendirSync

## opendirSync

```TypeScript
declare function opendirSync(path: string): Dir
```

Opens a directory. This API returns the result synchronously.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:listFileSync](arkts-corefile-file-fs-listfilesync-f.md#listfilesync)

<!--Device-unnamed-declare function opendirSync(path: string): Dir--><!--Device-unnamed-declare function opendirSync(path: string): Dir-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the directory to open. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | **Dir** object opened. |

