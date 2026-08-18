# restartSelfAtomicService

## 导入模块

```TypeScript
```

## restartSelfAtomicService

```TypeScript
function restartSelfAtomicService(context: Context): void
```

重启当前原子化服务。 > **说明：** > > - 当前仅支持以独立窗口方式拉起原子化服务。 > > - 在调用本接口成功后的3秒内，再次调用本接口、 > [ApplicationContext.restartApp()](arkts-ability-applicationcontext-c.md#restartapp)或 > [UIAbilityContext.restartApp()](arkts-ability-uiabilitycontext-c.md#restartapp)接口中的任一接口，系统将返回错误码1 > 6000064。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-abilityManager-function restartSelfAtomicService(context: Context): void--><!--Device-abilityManager-function restartSelfAtomicService(context: Context): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000086](../errorcode-ability.md#16000086-传入的context不是uiabilitycontext) |
| [16000064](../errorcode-ability.md#16000064-重启应用频繁) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000090](../errorcode-ability.md#16000090-调用方不是原子化服务) |

**示例**

```TypeScript
import { AbilityConstant, EmbeddableUIAbility, Want, abilityManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends EmbeddableUIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      // 重启当前原子化服务
      abilityManager.restartSelfAtomicService(this.context);
    } catch (e) {
      console.error(`restartSelfAtomicService error: ${JSON.stringify(e as BusinessError)}`);
    }
  }
}
```
