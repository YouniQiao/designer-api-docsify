# on_globalErrorOccurred

## on_globalErrorOccurred

```TypeScript
function on(type: 'globalErrorOccurred', observer: GlobalObserver): void
```

在进程中的任意线程中注册 `errormanager.on` 接口，监听整个进程中任意线程的异常。观测器捕获到该异常时应用不退出，建议在回调函数执行完后，增加同步退出操作。

**起始版本：** 18

**废弃版本：** -1

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-errorManager-function on(type: 'globalErrorOccurred', observer: GlobalObserver): void--><!--Device-errorManager-function on(type: 'globalErrorOccurred', observer: GlobalObserver): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'globalErrorOccurred' | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [GlobalObserver](arkts-ability-errormanager-globalobserver-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |

## 示例

```TypeScript
import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const errorFunc = (observer: errorManager.GlobalError) => {
  console.info('result name :' + observer.name);
  console.info('result message :' + observer.message);
  console.info('result stack :' + observer.stack);
  console.info('result instanceName :' + observer.instanceName);
  console.info('result instanceType :' + observer.instanceType);
};

try {
  errorManager.on('globalErrorOccurred', errorFunc);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`error: ${code}, ${message}`);
}
```
