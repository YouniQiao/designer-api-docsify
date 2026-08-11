# supportKeysSync

## Modules to Import

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## supportKeysSync

```TypeScript
function supportKeysSync(deviceId: number, keys: Array<KeyCode>): Array<boolean>
```

Checks whether the input device supports the specified keys.

**Since:** 10

<!--Device-inputDevice-function supportKeysSync(deviceId: int, keys: Array<KeyCode>): Array<boolean>--><!--Device-inputDevice-function supportKeysSync(deviceId: int, keys: Array<KeyCode>): Array<boolean>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | number | Yes |
| keys | Array&lt;[KeyCode](arkts-input-multimodalinput-keycode-keycode-e.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;boolean&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { inputDevice } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // Check whether the input device whose ID is 1 supports keys 17, 22, and 2055.
          try {
            let supportResult: Array<Boolean> = inputDevice.supportKeysSync(1, [17, 22, 2055])
            console.info(`Succeeded in querying support keys, result: ${JSON.stringify(supportResult)}.`)
          } catch (error) {
            console.error(`Failed to query support key, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`)
          }
        })
    }
  }
}
```
