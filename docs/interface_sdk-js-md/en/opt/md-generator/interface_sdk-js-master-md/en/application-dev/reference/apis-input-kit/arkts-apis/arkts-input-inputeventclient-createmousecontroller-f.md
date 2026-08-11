# createMouseController

## Modules to Import

```TypeScript
import { inputEventClient } from 'kits/@kit.InputKit';
```

## createMouseController

```TypeScript
function createMouseController(): Promise<MouseController>
```

Creates a mouse controller for simulating mouse operations. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputEventClient-function createMouseController(): Promise<MouseController>--><!--Device-inputEventClient-function createMouseController(): Promise<MouseController>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;MouseController&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
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
          inputEventClient.createMouseController()
            .then(mouseController => {
              console.info('Succeeded in creating mouse controller');
            })
            .catch((error: BusinessError) => {
              console.error(`Failed to create mouse controller. Code: ${error.code}, message: ${error.message}.`);
            });
        })
    }
  }
}
```
