# exitKioskMode

## 导入模块

```TypeScript
```

## exitKioskMode

```TypeScript
function exitKioskMode(context: UIAbilityContext): Promise<void>
```

退出Kiosk模式。使用Promise异步回调。 该接口仅对已进入Kiosk模式的应用生效。 该接口仅在Phone、PC/2in1和Tablet设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-kioskManager-function exitKioskMode(context: UIAbilityContext): Promise<void>--><!--Device-kioskManager-function exitKioskMode(context: UIAbilityContext): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIAbilityContext](arkts-ability-uiabilitycontext-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000112](../errorcode-ability.md#16000112-当前系统没有应用进入kiosk模式) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000110](../errorcode-ability.md#16000110-当前应用不在kiosk模式的列表内) |

**示例**

```TypeScript
import { common, kioskManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private uiAbilityContext: common.UIAbilityContext | undefined =
    this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    Column() {
      Button('exitKioskMode').margin({ top: 10 })
        .onClick(() => {
          kioskManager.exitKioskMode(this.uiAbilityContext)
            .then(() => {
              hilog.info(0x0000, 'testTag', '%{public}s', 'exitKioskMode success');
            })
            .catch((error: BusinessError) => {
              hilog.error(0x0000, 'testTag', '%{public}s', `exitKioskMode failed. Code: ${error.code}, message: ${error.message}`);
            });
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
