# connectDfs

## Modules to Import

```TypeScript
import { Options, ReaderIteratorResult, Watcher, ReadTextOptions, WatchEventListener, TaskSignal, WriteOptions, ListFileExtOptions, DfsListeners, Filter, ReadOptions, ListFileOptions, WatchEvent, FileFilter, ConflictFiles } from '@kit.CoreFileKit';
```

## connectDfs

```TypeScript
declare function connectDfs(networkId: string, listeners: DfsListeners): Promise<void>
```

Triggers connection. If the peer device is abnormal, [onStatus](arkts-corefile-file-fs-dfslisteners-i.md#onStatus) in **DfsListeners** will be called to notify the application.

**Since:** 12

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-unnamed-declare function connectDfs(networkId: string, listeners: DfsListeners): Promise<void>--><!--Device-unnamed-declare function connectDfs(networkId: string, listeners: DfsListeners): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| networkId | string | Yes |
| listeners | [DfsListeners](arkts-corefile-file-fs-dfslisteners-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 13900045 |
| 13900046 |
