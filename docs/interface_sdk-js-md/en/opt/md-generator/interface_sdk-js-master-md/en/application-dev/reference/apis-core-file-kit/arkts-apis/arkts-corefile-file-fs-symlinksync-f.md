# symlinkSync

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## symlinkSync

```TypeScript
declare function symlinkSync(target: string, srcPath: string): void
```

Creates a symbolic link based on the file path. This API returns the result synchronously. > **NOTE：**> > Since API version 11, this API cannot be used by third-party applications.

**Since:** 9

**Deprecated since:** -1

<!--Device-unnamed-declare function symlinkSync(target: string, srcPath: string): void--><!--Device-unnamed-declare function symlinkSync(target: string, srcPath: string): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | string | Yes |
| srcPath | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900018 |
| 13900030 |
| 13900025 |
| 13900027 |
| 13900005 |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900008 |
| 13900041 |
| 13900042 |
| 13900011 |
