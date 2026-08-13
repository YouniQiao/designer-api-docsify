# on_loopObserver

## on_loopObserver

```TypeScript
function on(type: 'loopObserver', timeout: number, observer: LoopObserver): void
```

注册主线程消息处理耗时监听器。注册后可以捕获到应用主线程处理消息的具体执行时间。 仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-errorManager-function on(type: 'loopObserver', timeout: number, observer: LoopObserver): void--><!--Device-errorManager-function on(type: 'loopObserver', timeout: number, observer: LoopObserver): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'loopObserver' | 是 |
| timeout | number | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [LoopObserver](arkts-ability-errormanager-loopobserver-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let observer: errorManager.LoopObserver = {
  onLoopTimeOut(timeout: number) {
    console.info('Duration timeout: ' + timeout);
  }
};

try {
  errorManager.on('loopObserver', 1, observer);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`error: ${code}, ${message}`);
}
```
