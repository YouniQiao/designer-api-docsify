# killProcessesInBatch（系统接口）

## 导入模块

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## killProcessesInBatch

```TypeScript
function killProcessesInBatch(pids: Array<number>): Promise<void>
```

批量终止进程。使用Promise异步回调。 该接口在PC/2in1中可正常调用，在其他设备类型中返回801错误码。 **需要权限**：ohos.permission.KILL_APP_PROCESSES

**起始版本：** 14

**需要权限：** ohos.permission.KILL_APP_PROCESSES

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pids | Array & lt;number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
