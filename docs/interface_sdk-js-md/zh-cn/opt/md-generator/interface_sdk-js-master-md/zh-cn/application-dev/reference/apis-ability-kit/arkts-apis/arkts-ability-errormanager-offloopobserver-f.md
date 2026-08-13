# off_loopObserver

## off_loopObserver

```TypeScript
function off(type: 'loopObserver', observer?: LoopObserver): void
```

注销主线程消息处理监听器。 仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-errorManager-function off(type: 'loopObserver', observer?: LoopObserver): void--><!--Device-errorManager-function off(type: 'loopObserver', observer?: LoopObserver): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'loopObserver' | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [LoopObserver](arkts-ability-errormanager-loopobserver-t.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16300004](../errorcode-ability.md#16300004-指定的observer不存在) |

## 示例

```TypeScript
import { errorManager } from '@kit.AbilityKit';

try {
  errorManager.off('loopObserver');
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`error: ${code}, ${message}`);
}
```
