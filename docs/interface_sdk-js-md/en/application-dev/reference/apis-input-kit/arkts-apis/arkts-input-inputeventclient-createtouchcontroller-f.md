# createTouchController

## Modules to Import

```TypeScript
import { inputEventClient } from 'kits/@kit.InputKit';
```

## createTouchController

```TypeScript
function createTouchController(): Promise<TouchController>
```

创建触控控制器，用于模拟触控操作。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputEventClient-function createTouchController(): Promise<TouchController>--><!--Device-inputEventClient-function createTouchController(): Promise<TouchController>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;TouchController&gt; | Promise对象，返回触控控制器实例。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 3800001 | Input service exception. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

## Examples

```TypeScript
import { inputEventClient } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          inputEventClient.createTouchController()
            .then(touchController => {
              console.info('Succeeded in creating touch controller');
            })
            .catch((error: BusinessError) => {
              console.error(`Failed to create touch controller. Code: ${error.code}, message: ${error.message}.`);
            });
        })
    }
  }
}
```

