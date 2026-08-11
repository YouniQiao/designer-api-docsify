# createKeyboardController

## Modules to Import

```TypeScript
import { inputEventClient } from 'kits/@kit.InputKit';
```

## createKeyboardController

```TypeScript
function createKeyboardController(): Promise<KeyboardController>
```

Creates a keyboard controller for simulating key operations. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputEventClient-function createKeyboardController(): Promise<KeyboardController>--><!--Device-inputEventClient-function createKeyboardController(): Promise<KeyboardController>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputSimulator

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;KeyboardController&gt; |

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
          inputEventClient.createKeyboardController()
            .then(keyboardController => {
              console.info('Succeeded in creating keyboard controller');
            })
            .catch((error: BusinessError) => {
              console.error(`Failed to create keyboard controller. Code: ${error.code}, message: ${error.message}.`);
            });
        })
    }
  }
}
```
