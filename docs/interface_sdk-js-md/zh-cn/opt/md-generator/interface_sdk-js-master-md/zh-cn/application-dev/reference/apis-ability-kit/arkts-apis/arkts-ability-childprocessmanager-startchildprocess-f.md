# startChildProcess

## 导入模块

```TypeScript
```

## startChildProcess

```TypeScript
function startChildProcess(srcEntry: string, startMode: StartMode): Promise<number>
```

启动[ArkTS子进程](../../../application-models/ability-terminology.md#arkts子进程)。使用Promise异步回调。 > **说明：** > > 调用该接口创建子进程成功会返回子进程pid，然后执行子进程的[ChildProcess.onStart](arkts-ability-app-ability-childprocess-childprocess-c.md#onstart)函数 > ，[ChildProcess.onStart](arkts-ability-app-ability-childprocess-childprocess-c.md#onstart)函数执行完后子进程会自动销毁。 > > 调用该接口创建的子进程不支持异步ArkTS API调用，仅支持同步ArkTS API调用。 **设备行为差异**：该接口在Tablet、PC/2in1中可正常调用，在其他设备类型中返回16000061错误码。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-childProcessManager-function startChildProcess(srcEntry: string, startMode: StartMode): Promise<int>--><!--Device-childProcessManager-function startChildProcess(srcEntry: string, startMode: StartMode): Promise<int>-End-->

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

**示例**

```TypeScript
// 在entry模块的src/main/ets/process下创建DemoProcess.ets子进程类:
// entry/src/main/ets/process/DemoProcess.ets
import { ChildProcess } from '@kit.AbilityKit';

export default class DemoProcess extends ChildProcess {
  onStart() {
    console.info('DemoProcess OnStart() called');
  }
}
```

```TypeScript
// 使用childProcessManager.startChildProcess方法启动子进程:
// entry/src/main/ets/tool/Tool.ets
import { childProcessManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import DemoProcess from '../process/DemoProcess';

try {
  DemoProcess.toString(); // 这里要调用下DemoProcess类的任意方法，防止没有引用到而被构建工具优化掉
  childProcessManager.startChildProcess("./ets/process/DemoProcess.ets", childProcessManager.StartMode.SELF_FORK)
    .then((data) => {
      console.info(`startChildProcess success, pid: ${data}`);
    }, (err: BusinessError) => {
      console.error(`startChildProcess error, errorCode: ${err.code}`);
    })
} catch (err: BusinessError) {
  console.error(`startChildProcess error, errorCode: ${(err as BusinessError).code}, errorMsg: ${(err as BusinessError).message}.`);
}
```


## startChildProcess

```TypeScript
function startChildProcess(srcEntry: string, startMode: StartMode, callback: AsyncCallback<number>): void
```

启动[ArkTS子进程](../../../application-models/ability-terminology.md#arkts子进程)。使用callback异步回调。 > **说明：** > > 调用该接口创建子进程成功会返回子进程pid，然后执行子进程的[ChildProcess.onStart](arkts-ability-app-ability-childprocess-childprocess-c.md#onstart)函数 > ，[ChildProcess.onStart](arkts-ability-app-ability-childprocess-childprocess-c.md#onstart)函数执行完后子进程会自动销毁。 > > 调用该接口创建的子进程不支持异步ArkTS API调用，仅支持同步ArkTS API调用。 **设备行为差异**：该接口在Tablet、PC/2in1中可正常调用，在其他设备类型中返回16000061错误码。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-childProcessManager-function startChildProcess(srcEntry: string, startMode: StartMode, callback: AsyncCallback<int>): void--><!--Device-childProcessManager-function startChildProcess(srcEntry: string, startMode: StartMode, callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [srcEntry](arkts-ability-insightintentdriver-subintentinfoforconfiguration-i-sys.md) | string | 是 |
| startMode | [StartMode](arkts-ability-childprocessmanager-startmode-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000061](../errorcode-ability.md#16000061-不支持的操作) |
| [16000062](../errorcode-ability.md#16000062-子进程数量超出上限) |

**示例**

```TypeScript
// 在entry模块的src/main/ets/process下创建DemoProcess.ets子进程类:
// entry/src/main/ets/process/DemoProcess.ets
import { ChildProcess } from '@kit.AbilityKit';

export default class DemoProcess extends ChildProcess {
  onStart() {
    console.info('DemoProcess OnStart() called');
  }
}
```

```TypeScript
// 使用childProcessManager.startChildProcess方法启动子进程:
// entry/src/main/ets/tool/Tool.ets
import { childProcessManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import DemoProcess from '../process/DemoProcess';

try {
  DemoProcess.toString(); // 这里要调用下DemoProcess类的任意方法，防止没有引用到而被构建工具优化掉
  childProcessManager.startChildProcess("./ets/process/DemoProcess.ets", childProcessManager.StartMode.SELF_FORK, (err, data) => {
    if (err) {
      console.error(`startChildProcess error. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info(`startChildProcess success, pid: ${data}`);
    }
  });
} catch (err: BusinessError) {
  console.error(`startChildProcess error, errorCode: ${(err as BusinessError).code}, errorMsg: ${(err as BusinessError).message}.`);
}
```
