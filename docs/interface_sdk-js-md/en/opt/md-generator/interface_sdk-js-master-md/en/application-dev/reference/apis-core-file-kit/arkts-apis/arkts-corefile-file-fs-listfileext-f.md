# listFileExt

## Modules to Import

```TypeScript
```

## listFileExt

```TypeScript
declare function listFileExt(
  path: string,
  options?: ListFileExtOptions
): Promise<string[]>
```

Lists all file names in a directory. This API uses a promise to return the result. This API supports recursive listing of all file names and custom file name filtering. The returned result starts with a slash (/) and contains the subdirectory.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare function listFileExt(  path: string,  options?: ListFileExtOptions): Promise<string[]>--><!--Device-unnamed-declare function listFileExt(  path: string,  options?: ListFileExtOptions): Promise<string[]>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| options | [ListFileExtOptions](arkts-corefile-file-fs-listfileextoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900002 |
| 13900018 |
| 13900011 |
