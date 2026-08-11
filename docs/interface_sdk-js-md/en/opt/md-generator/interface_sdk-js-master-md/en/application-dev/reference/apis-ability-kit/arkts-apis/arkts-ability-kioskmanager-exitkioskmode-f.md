# exitKioskMode

## Modules to Import

```TypeScript
import { kioskManager } from 'kits/@kit.AbilityKit';
```

## exitKioskMode

```TypeScript
function exitKioskMode(context: UIAbilityContext): Promise<void>
```

Exits kiosk mode. This API uses a promise to return the result.This API takes effect only for applications that have entered kiosk mode.This API can be properly called only on phones, PC/2-in-1 devices, and tablets. On other devices, it returns the error code 801.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

<!--Device-kioskManager-function exitKioskMode(context: UIAbilityContext): Promise<void>--><!--Device-kioskManager-function exitKioskMode(context: UIAbilityContext): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIAbilityContext](arkts-ability-uiabilitycontext-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [16000112](../errorcode-ability.md#16000112-no-application-is-in-kiosk-mode) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000110](../errorcode-ability.md#16000110-application-is-not-in-the-kiosk-mode-list) |

## Examples

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
              hilog.error(0x0000, 'testTag', '%{public}s', `exitKioskMode failed:${JSON.stringify(error)}`);
            });
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
