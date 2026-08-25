# startNativeChildProcess

## 导入模块

```TypeScript
import { childProcessManager } from 'kits/@kit.AbilityKit';
```

## startNativeChildProcess

```TypeScript
function startNativeChildProcess(entryPoint: string, args: ChildProcessArgs, options?: ChildProcessOptions): Promise<number>
```

启动[Native子进程](../../../application-models/ability-terminology.md#native子进程)。使用Promise异步回调。

> **说明：**&gt;
> 调用该接口创建的子进程不会继承父进程资源，子进程创建成功会返回子进程pid，然后加载参数中指定的动态链接库文件并执行子进程的入口函数，入口函数执行完后子进程会自动销毁。调用该接口的进程销毁后，所创建的子进程也会一并销毁。
**设备行为差异**：从API version 13开始，该接口在PC/2in1中可正常调用，在其他设备类型中返回801错误码。 从API version 14开始，该接口在PC/2in1、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [entryPoint](../../apis-arkui/arkts-components/arkts-arkui-dynamicoptions-i-sys.md) | string | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | [ChildProcessArgs](arkts-ability-app-ability-childprocessargs-childprocessargs-i.md) | 是 |
| options | [ChildProcessOptions](arkts-ability-app-ability-childprocessoptions-childprocessoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000061](../errorcode-ability.md#16000061-不支持的操作) |
| [16000062](../errorcode-ability.md#16000062-子进程数量超出上限) |
