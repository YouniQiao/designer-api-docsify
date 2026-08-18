# getAllSystemHotkeys

## Modules to Import

```TypeScript
import { inputConsumer } from '@kit.InputKit';
```

## getAllSystemHotkeys

```TypeScript
function getAllSystemHotkeys(): Promise<Array<HotkeyOptions>>
```

Obtains all system shortcut keys. This API uses a promise to return the result.

**Since:** 23

<!--Device-inputConsumer-function getAllSystemHotkeys(): Promise<Array<HotkeyOptions>>--><!--Device-inputConsumer-function getAllSystemHotkeys(): Promise<Array<HotkeyOptions>>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[HotkeyOptions](arkts-input-inputconsumer-hotkeyoptions-i.md)&gt;&gt; | Promise used to return the list of all system shortcut keys. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

**Examples**

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

