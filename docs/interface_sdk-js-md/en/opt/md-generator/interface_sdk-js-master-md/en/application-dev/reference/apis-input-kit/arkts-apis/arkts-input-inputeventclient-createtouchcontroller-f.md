# createTouchController

## Modules to Import

```TypeScript
import { inputEventClient } from '@kit.InputKit';
```

## createTouchController

```TypeScript
function createTouchController(): Promise<TouchController>
```

Creates a touch controller for simulating touch operations. This API uses a promise to return the result.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputEventClient-function createTouchController(): Promise<TouchController>--><!--Device-inputEventClient-function createTouchController(): Promise<TouchController>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[TouchController](arkts-input-inputeventclient-touchcontroller-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3800001](../errorcode-infraredemitter.md#3800001-multimodal-input-service-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

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
