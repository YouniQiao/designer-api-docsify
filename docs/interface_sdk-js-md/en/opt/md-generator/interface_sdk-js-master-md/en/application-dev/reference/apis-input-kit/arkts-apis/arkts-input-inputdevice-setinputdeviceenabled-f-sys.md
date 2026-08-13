# setInputDeviceEnabled (System API)

## Modules to Import

```TypeScript
import { inputDevice } from '@kit.InputKit';
```

## setInputDeviceEnabled

```TypeScript
function setInputDeviceEnabled(deviceId: number, enabled: boolean): Promise<void>
```

Sets the input switch status of an input device. Take the touchscreen as an example. If the input switch is off, the touchscreen does not respond when being touched. If the input switch is on, the touchscreen wakes up when being touched. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.INPUT_DEVICE_CONTROLLER

<!--Device-inputDevice-function setInputDeviceEnabled(deviceId: int, enabled: boolean): Promise<void>--><!--Device-inputDevice-function setInputDeviceEnabled(deviceId: int, enabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | number | Yes |
| enabled | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [3900001](../errorcode-inputdevice.md#3900001-device-not-exist) |

## Examples

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
          try {
            // Set the device ID to 0
            inputDevice.setInputDeviceEnabled(0, true).then(() => {
              console.info(`Succeeded in setting input device enabled.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to set device enabled, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to set device enabled, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
