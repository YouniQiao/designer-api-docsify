# deleteGroup

## 导入模块

```TypeScript
import { request } from '@kit.BasicServicesKit';
```

## deleteGroup

```TypeScript
function deleteGroup(gid: string): Promise<void>
```

移除指定分组，后续不能再往该分组中添加任务id。使用Promise异步回调。当分组中的所有任务处于完成、失败或移除状态，并且分组被移除时，显示该分组的完成或失败通知。

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| gid | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [13400003](../errorcode-request.md#13400003-服务异常) |
| [21900008](../errorcode-request.md#21900008-任务分组不存在或已移除) |

**示例**

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 准备分组id。
let groupId: string = "123456789";

// 调用 deleteGroup 接口移除分组。
request.agent.deleteGroup(groupId).then(() => {
  console.info(`Succeeded in deleting the download task group.`);
}).catch((err: Error) => {
  console.error(`Failed to delete the download group, Code: ${err.code}, message: ${err.message}`);
});
```
