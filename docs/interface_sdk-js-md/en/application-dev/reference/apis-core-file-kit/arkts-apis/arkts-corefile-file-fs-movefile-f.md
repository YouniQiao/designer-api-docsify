# moveFile

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## moveFile

```TypeScript
declare function moveFile(src: string, dest: string, mode?: number): Promise<void>
```

Moves a file. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is not supported in a distributed directory.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | string | Yes |
| dest | string | Yes |
| mode | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900002 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900016 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900025 |
| 13900027 |
| 13900028 |
| 13900032 |
| 13900033 |
| 13900041 |
| 13900042 |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fs.moveFile(srcPath, destPath, 0).then(() => {
  console.info("move file succeed");
}).catch((err: BusinessError) => {
  console.error("move file failed with error message: " + err.message + ", error code: " + err.code);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fs.moveFile(srcPath, destPath, 0, (err: BusinessError) => {
  if (err) {
    console.error("move file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("move file succeed");
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fs.moveFile(srcPath, destPath, (err: BusinessError) => {
  if (err) {
    console.error("move file failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("move file succeed");
  }
});
```


## moveFile

```TypeScript
declare function moveFile(src: string, dest: string, callback: AsyncCallback<void>): void
```

Moves a file and forcibly overwrites the file with the same name in the destination directory. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is not supported in a distributed directory.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | string | Yes |
| dest | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900002 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900016 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900025 |
| 13900027 |
| 13900028 |
| 13900032 |
| 13900033 |
| 13900041 |
| 13900042 |

**Examples**

See [moveFile](#movefile)


## moveFile

```TypeScript
declare function moveFile(src: string, dest: string, mode: number, callback: AsyncCallback<void>): void
```

Moves a file with the specified mode. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is not supported in a distributed directory.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | string | Yes |
| dest | string | Yes |
| mode | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900002 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900016 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900025 |
| 13900027 |
| 13900028 |
| 13900032 |
| 13900033 |
| 13900041 |
| 13900042 |

**Examples**

See [moveFile](#movefile)
