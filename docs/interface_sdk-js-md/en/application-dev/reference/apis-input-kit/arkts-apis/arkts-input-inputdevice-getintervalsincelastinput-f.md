# getIntervalSinceLastInput

## Modules to Import

```TypeScript
import { inputDevice } from '@kit.InputKit';
```

## getIntervalSinceLastInput

```TypeScript
function getIntervalSinceLastInput(): Promise<long>
```

Obtains the interval (including the device sleep time) elapsed since the last system input event. This API uses a promise to return the result.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| ArkTS-Dyn: Promise & lt;number & gt;<br>ArkTS-Sta：Promise & lt;long & gt; |

**Examples**

```TypeScript
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          inputDevice.getIntervalSinceLastInput().then((timeInterval: number) => {
            console.info(`Interval since last input: ${JSON.stringify(timeInterval)}`);
          }).catch((error: BusinessError) => {
            console.error(`Get interval since last input failed, error: ${JSON.stringify(error)}`);
          })
        })
    }
  }
}
```
