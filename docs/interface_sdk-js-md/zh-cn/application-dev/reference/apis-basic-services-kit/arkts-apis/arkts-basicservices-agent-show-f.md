# show

## 导入模块

```TypeScript
import { request } from '@kit.BasicServicesKit';
```

## show

```TypeScript
function show(id: string, callback: AsyncCallback<TaskInfo>): void
```

根据任务id查询任务的详细信息。使用callback异步回调。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;TaskInfo&gt; | 是 |

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

request.agent.show("123456", (err: BusinessError<void> | null, taskInfo: request.agent.TaskInfo | undefined) => {
  if (err) {
    console.error(`Failed to show a upload task, Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in showing a upload task.`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

request.agent.show("123456").then((taskInfo: request.agent.TaskInfo) => {
  console.info(`Succeeded in showing a upload task.`);
}).catch((err: Error) => {
  console.error(`Failed to show a upload task, Code: ${err.code}, message: ${err.message}`);
});
```


## show

```TypeScript
function show(id: string): Promise<TaskInfo>
```

根据任务id查询任务的详细信息。使用Promise异步回调。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;TaskInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [13400003](../errorcode-request.md#13400003-服务异常) |
| [21900006](../errorcode-request.md#21900006-操作不存在的任务错误) |

**示例**

参见 [show](#show)
