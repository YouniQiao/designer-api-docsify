# getKeyboardTypeSync

## Modules to Import

```TypeScript
import { inputDevice } from '@kit.InputKit';
```

## getKeyboardTypeSync

```TypeScript
function getKeyboardTypeSync(deviceId: number): KeyboardType
```

Obtains the keyboard type of the input device.

**Since:** 23

**Deprecated since:** -1

<!--Device-inputDevice-function getKeyboardTypeSync(deviceId: int): KeyboardType--><!--Device-inputDevice-function getKeyboardTypeSync(deviceId: int): KeyboardType-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [KeyboardType](arkts-input-inputdevice-keyboardtype-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

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
          // Query the keyboard type of the input device whose ID is 1.
          try {
            let type: inputDevice.KeyboardType = inputDevice.getKeyboardTypeSync(1)
            console.info(`Succeeded in getting keyboard type: ${JSON.stringify(type)}.`)
          } catch (error) {
            console.error(`Failed to get keyboard type, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`)
          }
        })
    }
  }
}
```
