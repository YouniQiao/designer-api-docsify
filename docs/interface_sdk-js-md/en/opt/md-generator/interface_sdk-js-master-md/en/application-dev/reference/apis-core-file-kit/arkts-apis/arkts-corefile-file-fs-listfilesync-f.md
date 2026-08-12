# listFileSync

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## listFileSync

```TypeScript
declare function listFileSync(
  path: string,
  options?: ListFileOptions
): string[]
```

Lists the names of all files and directories in the current directory. This API returns the result synchronously.Filtering is supported.

You can configure the **recursion** parameter in **options** to recursively list the relative paths of all files. The relative path starts with a slash (/).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function listFileSync(  path: string,  options?: ListFileOptions): string[]--><!--Device-unnamed-declare function listFileSync(  path: string,  options?: ListFileOptions): string[]-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| options | [ListFileOptions](arkts-corefile-file-fs-listfileoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string[] |

**Error codes:**

| Error Code ID |
| --- |
| 13900002 |
| 13900018 |
| 13900008 |
| 13900042 |
| 13900011 |
