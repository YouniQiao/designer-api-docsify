# File

Represents a **File** object opened by **open()**.

**Since:** 9

<!--Device-unnamed-declare interface File--><!--Device-unnamed-declare interface File-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
```

## getParent

```TypeScript
getParent(): string
```

Obtains the parent directory of this file object.

**Since:** 11

<!--Device-File-getParent(): string--><!--Device-File-getParent(): string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| 13900005 |
| 14300002 |
| 13900042 |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
console.info(`Succeeded in getting parent path, the parent path is: ${file.getParent()}`);
fileIo.closeSync(file);
```

## lock

```TypeScript
lock(exclusive?: boolean): Promise<void>
```

Applies an exclusive lock or a shared lock on this file in blocking mode. This API uses a promise to return the result.

**Since:** 9

<!--Device-File-lock(exclusive?: boolean): Promise<void>--><!--Device-File-lock(exclusive?: boolean): Promise<void>-End-->

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
| 13900020 |
| 13900034 |
| 13900008 |
| 13900042 |
| 13900043 |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
file.lock(true).then(() => {
  console.info(`Succeeded in locking file.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to lock file. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  fileIo.closeSync(file);
});
```

## lock

```TypeScript
lock(callback: AsyncCallback<void>): void
```

Applies an exclusive lock or a shared lock on this file in blocking mode. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-File-lock(callback: AsyncCallback<void>): void--><!--Device-File-lock(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900020 |
| 13900034 |
| 13900008 |
| 13900042 |
| 13900043 |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
file.lock((err: BusinessError) => {
  if (err) {
    console.error(`Failed to lock file. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in locking file.`);
  }
  fileIo.closeSync(file);
});
```

## lock

```TypeScript
lock(exclusive: boolean, callback: AsyncCallback<void>): void
```

Applies an exclusive lock or a shared lock on this file in blocking mode. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-File-lock(exclusive: boolean, callback: AsyncCallback<void>): void--><!--Device-File-lock(exclusive: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| exclusive | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900020 |
| 13900034 |
| 13900008 |
| 13900042 |
| 13900043 |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
file.lock(true, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to lock file. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in locking file.`);
  }
  fileIo.closeSync(file);
});
```

## tryLock

```TypeScript
tryLock(exclusive?: boolean): void
```

Applies an exclusive lock or a shared lock on this file in non-blocking mode.

**Since:** 9

<!--Device-File-tryLock(exclusive?: boolean): void--><!--Device-File-tryLock(exclusive?: boolean): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| exclusive | boolean | No |

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900020 |
| 13900034 |
| 13900008 |
| 13900042 |
| 13900043 |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
file.tryLock(true);
console.info(`Succeeded in locking file.`);
fileIo.closeSync(file);
```

## unlock

```TypeScript
unlock(): void
```

Unlocks a file. This API returns the result synchronously.

**Since:** 9

<!--Device-File-unlock(): void--><!--Device-File-unlock(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900020 |
| 13900034 |
| 13900008 |
| 13900042 |
| 13900043 |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
file.tryLock(true);
file.unlock();
console.info(`Succeeded in unlocking file.`);
fileIo.closeSync(file);
```

## fd

```TypeScript
readonly fd: number
```

FD of the file.

**Type:** number

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-File-readonly fd: number--><!--Device-File-readonly fd: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## name

```TypeScript
readonly name: string
```

Name of the file.

**Type:** string

**Since:** 10

<!--Device-File-readonly name: string--><!--Device-File-readonly name: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## path

```TypeScript
readonly path: string
```

Path of the file.

**Type:** string

**Since:** 10

<!--Device-File-readonly path: string--><!--Device-File-readonly path: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO
