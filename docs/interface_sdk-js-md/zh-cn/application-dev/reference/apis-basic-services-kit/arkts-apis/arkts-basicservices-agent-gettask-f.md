# getTask

## 导入模块

```TypeScript
import { request } from '@kit.BasicServicesKit';
```

## getTask

```TypeScript
function getTask(context: BaseContext, id: string, token?: string): Promise<Task>
```

根据任务id查询任务。使用Promise异步回调。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| id | string | 是 |
| token | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Task & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [13400003](../errorcode-request.md#13400003-服务异常) |
| [21900006](../errorcode-request.md#21900006-操作不存在的任务错误) |

**示例**

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
request.agent.getTask(context, "123456").then((task: request.agent.Task) => {
  console.info(`Succeeded in querying a task. result: ${task.tid}`);
}).catch((err: Error) => {
  console.error(`Failed to query a task, Code: ${err.code}, message: ${err.message}`);
});
```
