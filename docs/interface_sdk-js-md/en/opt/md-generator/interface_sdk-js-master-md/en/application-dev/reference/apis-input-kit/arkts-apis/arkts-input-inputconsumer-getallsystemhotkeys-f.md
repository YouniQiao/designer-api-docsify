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

**Since:** 14

<!--Device-inputConsumer-function getAllSystemHotkeys(): Promise<Array<HotkeyOptions>>--><!--Device-inputConsumer-function getAllSystemHotkeys(): Promise<Array<HotkeyOptions>>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputConsumer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[HotkeyOptions](arkts-input-inputconsumer-hotkeyoptions-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |

## Examples

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
          // Obtains all system shortcut keys.
          inputConsumer.getAllSystemHotkeys().then((data: Array<inputConsumer.HotkeyOptions>) => {
            console.info(`Succeeded in getting list of system hotkeys: ${JSON.stringify(data)}.`);
          }).catch((error: BusinessError) => {
            console.error(`Failed to get all system hotkeys, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          })
        })
    }
  }
}
```
