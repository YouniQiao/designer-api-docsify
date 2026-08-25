# accessSync

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## accessSync

```TypeScript
declare function accessSync(path: string, mode?: AccessModeType): boolean
```

以同步方法检查文件或目录是否存在，或校验操作权限。校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| mode | [AccessModeType](arkts-corefile-file-fs-accessmodetype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| 13900002 |
| 13900005 |
| 13900008 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900018 |
| 13900020 |
| 13900023 |
| 13900030 |
| 13900033 |
| 13900042 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
try {
  let res = fileIo.accessSync(filePath);
  if (res) {
    console.info(`Succeeded in checking file, file exists.`);
  } else {
    console.info(`Succeeded in checking file, file does not exist.`);
  }
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to accessSync. Code: ${err.code}, message: ${err.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
try {
  let res = fileIo.accessSync(filePath, fileIo.AccessModeType.EXIST, fileIo.AccessFlagType.LOCAL);
  if (res) {
    console.info(`Succeeded in checking file, file exists.`);
  } else {
    console.info(`Succeeded in checking file, file does not exist.`);
  }
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to accessSync. Code: ${err.code}, message: ${err.message}`);
}
```


## accessSync

```TypeScript
declare function accessSync(path: string, mode: AccessModeType, flag: AccessFlagType): boolean
```

以同步方法检查文件或目录是否在本地，或校验操作权限。校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| mode | [AccessModeType](arkts-corefile-file-fs-accessmodetype-e.md) | 是 |
| flag | [AccessFlagType](arkts-corefile-file-fs-accessflagtype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900005 |
| 13900011 |
| 13900012 |
| 13900013 |
| 13900018 |
| 13900020 |
| 13900023 |
| 13900030 |
| 13900033 |

**示例**

参见 [accessSync](#accesssync)
