# copyDirSync

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## copyDirSync

```TypeScript
declare function copyDirSync(src: string, dest: string, mode?: number): void
```

Copies the source directory to the destination path. This API returns the result synchronously.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

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
| 13900002 |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900010 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900015 |
| 13900018 |
| 13900019 |
| 13900020 |
| 13900030 |
| 13900031 |
| 13900033 |
| 13900034 |
| 13900038 |
| 13900042 |
| 13900044 |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// Copy srcPath to destPath.
let srcPath = pathDir + "/srcDir/";
let destPath = pathDir + "/destDir/";
try {
  fs.copyDirSync(srcPath, destPath, 0);
  console.info("copy directory succeed");
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error("copy directory failed with error message: " + err.message + ", error code: " + err.code);
}
```
