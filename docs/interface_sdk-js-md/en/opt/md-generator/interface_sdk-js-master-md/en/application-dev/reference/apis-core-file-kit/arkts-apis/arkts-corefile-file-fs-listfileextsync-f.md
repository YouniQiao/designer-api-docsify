# listFileExtSync

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## listFileExtSync

```TypeScript
declare function listFileExtSync(
  path: string,
  options?: ListFileExtOptions
): string[]
```

Lists all file names in a directory. This API returns the result synchronously. This API supports recursive listing of all file names and custom file name filtering. The returned result starts with a slash (/) and contains the subdirectory.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare function listFileExtSync(  path: string,  options?: ListFileExtOptions): string[]--><!--Device-unnamed-declare function listFileExtSync(  path: string,  options?: ListFileExtOptions): string[]-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| options | [ListFileExtOptions](arkts-corefile-file-fs-listfileextoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string[] |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900002 |
| 13900018 |
| 13900011 |
