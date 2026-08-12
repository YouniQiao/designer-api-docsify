# statSync

## statSync

```TypeScript
declare function statSync(path: string): Stat
```

Obtains file information. This API returns the result synchronously.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [statSync](arkts-corefile-file-fs-statsync-f.md#statSync)

<!--Device-unnamed-declare function statSync(path: string): Stat--><!--Device-unnamed-declare function statSync(path: string): Stat-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file. |

**Return value:**

| Type | Description |
| --- | --- |
| [Stat](arkts-corefile-fileio-stat-depr-i.md) | File information obtained. |

