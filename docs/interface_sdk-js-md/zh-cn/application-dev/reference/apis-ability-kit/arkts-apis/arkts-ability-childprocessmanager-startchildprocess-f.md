# startChildProcess

## 导入模块

```TypeScript
import { childProcessManager } from 'kits/@kit.AbilityKit';
```

## startChildProcess

```TypeScript
function startChildProcess(srcEntry: string, startMode: StartMode): Promise<number>
```

启动[ArkTS子进程](../../../application-models/ability-terminology.md#arkts子进程)。使用Promise异步回调。

> **说明：**&gt;
> 调用该接口创建子进程成功会返回子进程pid，然后执行子进程的[ChildProcess.onStart](arkts-ability-app-ability-childprocess-childprocess-c.md#onstart)函数
> ，[ChildProcess.onStart](arkts-ability-app-ability-childprocess-childprocess-c.md#onstart)函数执行完后子进程会自动销毁。&gt;
> 调用该接口创建的子进程不支持异步ArkTS API调用，仅支持同步ArkTS API调用。
**设备行为差异**：该接口在Tablet、PC/2in1中可正常调用，在其他设备类型中返回16000061错误码。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [srcEntry](arkts-ability-insightintentdriver-subintentinfoforconfiguration-i-sys.md) | string | 是 |
| startMode | [StartMode](arkts-ability-childprocessmanager-startmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000061](../errorcode-ability.md#16000061-不支持的操作) |
| [16000062](../errorcode-ability.md#16000062-子进程数量超出上限) |


## startChildProcess

```TypeScript
function startChildProcess(srcEntry: string, startMode: StartMode, callback: AsyncCallback<number>): void
```

启动[ArkTS子进程](../../../application-models/ability-terminology.md#arkts子进程)。使用callback异步回调。

> **说明：**&gt;
> 调用该接口创建子进程成功会返回子进程pid，然后执行子进程的[ChildProcess.onStart](arkts-ability-app-ability-childprocess-childprocess-c.md#onstart)函数
> ，[ChildProcess.onStart](arkts-ability-app-ability-childprocess-childprocess-c.md#onstart)函数执行完后子进程会自动销毁。&gt;
> 调用该接口创建的子进程不支持异步ArkTS API调用，仅支持同步ArkTS API调用。
**设备行为差异**：该接口在Tablet、PC/2in1中可正常调用，在其他设备类型中返回16000061错误码。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [srcEntry](arkts-ability-insightintentdriver-subintentinfoforconfiguration-i-sys.md) | string | 是 |
| startMode | [StartMode](arkts-ability-childprocessmanager-startmode-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000061](../errorcode-ability.md#16000061-不支持的操作) |
| [16000062](../errorcode-ability.md#16000062-子进程数量超出上限) |
