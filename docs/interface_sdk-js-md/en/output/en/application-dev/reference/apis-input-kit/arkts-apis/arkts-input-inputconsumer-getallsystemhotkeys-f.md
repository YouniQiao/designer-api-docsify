# getAllSystemHotkeys

## getAllSystemHotkeys

```TypeScript
function getAllSystemHotkeys(): Promise<Array<HotkeyOptions>>
```

Obtains all system shortcut keys. This API uses a promise to return the result.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-inputConsumer-function getAllSystemHotkeys(): Promise<Array<HotkeyOptions>>--><!--Device-inputConsumer-function getAllSystemHotkeys(): Promise<Array<HotkeyOptions>>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;HotkeyOptions&gt;&gt; | Promise used to return the list of all system shortcut keys. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |

**Example**

```TypeScript
import { inputConsumer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          inputConsumer.getAllSystemHotkeys().then((data: Array<inputConsumer.HotkeyOptions>) => {
            console.info(`List of system hotkeys : ${JSON.stringify(data)}`);
          }).catch((error: BusinessError) => {
            console.error(`Get all system hotkeys failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          })
        })
    }
  }
}
```

