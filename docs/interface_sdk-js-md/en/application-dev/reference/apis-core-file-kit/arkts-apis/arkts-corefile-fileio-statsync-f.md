# statSync

## statSync

```TypeScript
declare function statSync(path: string): Stat
```

Obtains file information. This API returns the result synchronously.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [fs:statSync](arkts-corefile-fileio-statsync-f.md#statsync)

<!--Device-unnamed-declare function statSync(path: string): Stat--><!--Device-unnamed-declare function statSync(path: string): Stat-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file. |

**Return value:**

| Type | Description |
| --- | --- |
| [Stat](arkts-corefile-file-fs-stat-i.md) | File information obtained. |

