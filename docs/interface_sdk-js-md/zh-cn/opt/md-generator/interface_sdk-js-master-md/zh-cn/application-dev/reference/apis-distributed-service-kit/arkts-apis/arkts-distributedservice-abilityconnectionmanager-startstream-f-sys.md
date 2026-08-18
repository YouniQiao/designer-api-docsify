# startStream（系统接口）

## 导入模块

```TypeScript
```

## startStream

```TypeScript
function startStream(streamId: number): void
```

Start Streaming

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-abilityConnectionManager-function startStream(streamId: int): void--><!--Device-abilityConnectionManager-function startStream(streamId: int): void-End-->

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamId | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [32300002](../../apis-distributedservice-kit/errorcode-device-manager.md#32300002-流接收端未启动) |

**示例**

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let streamId = 100;
hilog.info(0x0000, 'testTag', 'startStream called');
abilityConnectionManager.startStream(streamId);
```
