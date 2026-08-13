# moveDirSync

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## moveDirSync

```TypeScript
declare function moveDirSync(src: string, dest: string, mode?: number): void
```

Moves the source directory to the destination directory. This API returns the result synchronously. > **NOTE：**> > This API is not supported in a distributed directory.

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare function moveDirSync(src: string, dest: string, mode?: number): void--><!--Device-unnamed-declare function moveDirSync(src: string, dest: string, mode?: number): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | string | Yes |
| dest | string | Yes |
| mode | number | No |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900016 |
| 13900018 |
| 13900019 |
| 13900028 |
| 13900025 |
| 13900027 |
| 13900032 |
| 13900001 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900008 |
| 13900041 |
| 13900042 |
| 13900011 |
