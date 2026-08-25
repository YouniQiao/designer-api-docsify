# getxattr

## 导入模块

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from '@kit.CoreFileKit';
```

## getxattr

```TypeScript
declare function getxattr(path: string, key: string): Promise<string>
```

获取文件或目录的扩展属性。使用promise异步回调。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900002 |
| 13900007 |
| 13900012 |
| 13900031 |
| 13900037 |
| 13900038 |
| 13900042 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let attrKey = "user.comment";

fileIo.getxattr(filePath, attrKey).then((attrValue: string) => {
  console.info(`Succeeded in getting extended attribute, the value is: ${attrValue}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get extended attribute. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let attrKey = "user.comment";

fileIo.getxattr(filePath, attrKey).then((attrValue: string) => {
  console.info(`Succeeded in getting extended attribute, the value is: ${attrValue}`);
}).catch((error: Error) => {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to get extended attribute. Code: ${err.code}, message: ${err.message}`);
});
```
