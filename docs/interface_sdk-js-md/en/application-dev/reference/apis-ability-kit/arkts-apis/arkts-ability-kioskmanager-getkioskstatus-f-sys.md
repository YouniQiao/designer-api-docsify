# getKioskStatus (System API)

## Modules to Import

```TypeScript
import { kioskManager } from '@kit.AbilityKit';
```

## getKioskStatus

```TypeScript
function getKioskStatus(): Promise<KioskStatus>
```

Obtains the Kiosk mode status information, including whether the system is in kiosk mode, and the name and UID of the application that has entered Kiosk mode. This API uses a promise to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-kioskManager-function getKioskStatus(): Promise<KioskStatus>--><!--Device-kioskManager-function getKioskStatus(): Promise<KioskStatus>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;KioskStatus&gt; | Promise used to return the kiosk mode status information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Failed to connect to the system service. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |

**Examples**

```TypeScript
import { kioskManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('getKioskInfo').margin({ top: 10 })
        .onClick(() => {
          kioskManager.getKioskStatus()
            .then((data: kioskManager.KioskStatus) => {
              hilog.info(0x0000, 'testTag', '%{public}s', `getKioskinfo success: ${JSON.stringify(data)}`);
            })
            .catch((error: BusinessError) => {
              hilog.error(0x0000, 'testTag', '%{public}s', `getKioskinfo failed:${JSON.stringify(error)}`);
            });
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

