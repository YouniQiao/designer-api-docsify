# fstatSync

## fstatSync

```TypeScript
declare function fstatSync(fd: number): Stat
```

Obtains file status based on the file descriptor. This API returns the result synchronously.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:statSync](arkts-corefile-fileio-statsync-f.md#statsync)

<!--Device-unnamed-declare function fstatSync(fd: number): Stat--><!--Device-unnamed-declare function fstatSync(fd: number): Stat-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | File descriptor of the file whose status is to be obtained. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Detailed file status obtained. |

