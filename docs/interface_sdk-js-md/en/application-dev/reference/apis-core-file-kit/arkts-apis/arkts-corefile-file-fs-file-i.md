# File

Represents a **File** object opened by **open()**.

**Since:** 9

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## getParent

```TypeScript
getParent(): string
```

Obtains the parent directory of this file object.

**Since:** 11

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| 13900005 |
| 13900042 |
| 14300002 |

## lock

```TypeScript
lock(exclusive?: boolean): Promise<void>
```

Applies an exclusive lock or a shared lock on this file in blocking mode. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| exclusive | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900008 |
| 13900020 |
| 13900034 |
| 13900042 |
| 13900043 |

## lock

```TypeScript
lock(callback: AsyncCallback<void>): void
```

Applies an exclusive lock or a shared lock on this file in blocking mode. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900008 |
| 13900020 |
| 13900034 |
| 13900042 |
| 13900043 |

## lock

```TypeScript
lock(exclusive: boolean, callback: AsyncCallback<void>): void
```

Applies an exclusive lock or a shared lock on this file in blocking mode. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| exclusive | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900008 |
| 13900020 |
| 13900034 |
| 13900042 |
| 13900043 |

## tryLock

```TypeScript
tryLock(exclusive?: boolean): void
```

Applies an exclusive lock or a shared lock on this file in non-blocking mode.

**Since:** 9

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| exclusive | boolean | No |

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900008 |
| 13900020 |
| 13900034 |
| 13900042 |
| 13900043 |

## unlock

```TypeScript
unlock(): void
```

Unlocks a file. This API returns the result synchronously.

**Since:** 9

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900008 |
| 13900020 |
| 13900034 |
| 13900042 |
| 13900043 |

## fd

```TypeScript
readonly fd: number
```

FD of the file.

**Type:** number

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.FileManagement.File.FileIO

## name

```TypeScript
readonly name: string
```

Name of the file.

**Type:** string

**Since:** 10

**System capability:** SystemCapability.FileManagement.File.FileIO

## path

```TypeScript
readonly path: string
```

Path of the file.

**Type:** string

**Since:** 10

**System capability:** SystemCapability.FileManagement.File.FileIO
