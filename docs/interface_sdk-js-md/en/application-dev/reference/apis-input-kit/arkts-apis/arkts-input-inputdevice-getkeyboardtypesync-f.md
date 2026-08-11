# getKeyboardTypeSync

## Modules to Import

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## getKeyboardTypeSync

```TypeScript
function getKeyboardTypeSync(deviceId: int): KeyboardType
```

Obtains the keyboard type of the input device.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-inputDevice-function getKeyboardTypeSync(deviceId: int): KeyboardType--><!--Device-inputDevice-function getKeyboardTypeSync(deviceId: int): KeyboardType-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |

**Return value:**

| Type | Description |
| --- | --- |
| [KeyboardType](arkts-input-inputdevice-keyboardtype-e.md) | Keyboard type. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

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
            let type: number = inputDevice.getKeyboardTypeSync(1)
            console.info(`Keyboard type: ${JSON.stringify(type)}`)
          } catch (error) {
            console.error(`Failed to get keyboard type, error: ${JSON.stringify(error, [`code`, `message`])}`)
          }
        })
    }
  }
}
```

