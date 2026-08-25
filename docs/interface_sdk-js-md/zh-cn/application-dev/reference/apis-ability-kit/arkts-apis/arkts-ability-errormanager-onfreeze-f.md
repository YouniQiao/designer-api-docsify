# onFreeze

## 导入模块

```TypeScript
import { errorManager } from '@kit.AbilityKit';
```

## onFreeze

```TypeScript
function onFreeze(observer: FreezeObserver): void
```

注册冻屏事件观测器。 此函数只能在主线程中调用。 请注意，每个进程只支持注册一个观测器。 如果多次注册，后注册的将覆盖之前的。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [FreezeObserver](arkts-ability-errormanager-freezeobserver-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |

**示例**

```TypeScript
import { errorManager } from '@kit.AbilityKit';

export const FreezeRegister = () => {
  try {
    let observer: errorManager.FreezeObserver = () => {
      console.info('onFreezecallback');
    };
    errorManager.onFreeze(observer);
    console.info('Registered onfreeze Handler.');
  } catch (paramError) {
      console.error('onFreeze error: ', paramError);
  }
};
```
