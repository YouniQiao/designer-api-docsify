# getxattrSync

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from 'kits/@kit.CoreFileKit';
```

## getxattrSync

```TypeScript
declare function getxattrSync(path: string, key: string): string
```

Obtains an extended attribute of a file or directory. This API returns the result synchronously.

**Since:** 12

<!--Device-unnamed-declare function getxattrSync(path: string, key: string): string--><!--Device-unnamed-declare function getxattrSync(path: string, key: string): string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| key | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900037 |
| 13900038 |
| 13900007 |
| 13900002 |
| 13900012 |
| 13900031 |
| 13900042 |
