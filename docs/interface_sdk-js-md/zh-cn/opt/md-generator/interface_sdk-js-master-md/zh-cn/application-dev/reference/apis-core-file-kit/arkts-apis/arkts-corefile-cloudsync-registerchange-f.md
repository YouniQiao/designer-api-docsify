# registerChange

## 导入模块

```TypeScript
```

## registerChange

```TypeScript
function registerChange(uri: string, recursion: boolean, callback: Callback<ChangeData>): void
```

订阅监听指定文件的变化通知。callback返回更改的数据。

**起始版本：** 23

<!--Device-cloudSync-function registerChange(uri: string, recursion: boolean, callback: Callback<ChangeData>): void--><!--Device-cloudSync-function registerChange(uri: string, recursion: boolean, callback: Callback<ChangeData>): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| recursion | boolean | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChangeData&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900001 |
| 13900002 |
| 14000002 |
| 13900012 |

**示例**

```TypeScript
import { fileUri } from '@kit.CoreFileKit';

let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);
let onCallback1 = (changeData: cloudSync.ChangeData) => {
  if (changeData.type == cloudSync.NotifyType.NOTIFY_ADDED) {
    // file has been added, do something
  } else if (changeData.type== cloudSync.NotifyType.NOTIFY_DELETED) {
    // file has been removed, do something
  }
}
cloudSync.registerChange(uri, false, onCallback1);
// 取消注册监听
cloudSync.unregisterChange(uri);
```
