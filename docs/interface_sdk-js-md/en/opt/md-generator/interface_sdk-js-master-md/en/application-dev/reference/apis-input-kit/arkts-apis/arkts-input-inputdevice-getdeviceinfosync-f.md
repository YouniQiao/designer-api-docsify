# getDeviceInfoSync

## Modules to Import

```TypeScript
import { inputDevice } from '@kit.InputKit';
```

## getDeviceInfoSync

```TypeScript
function getDeviceInfoSync(deviceId: number): InputDeviceData
```

Obtains information about the specified input device.

**Since:** 10

<!--Device-inputDevice-function getDeviceInfoSync(deviceId: int): InputDeviceData--><!--Device-inputDevice-function getDeviceInfoSync(deviceId: int): InputDeviceData-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [InputDeviceData](arkts-input-inputdevice-inputdevicedata-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

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
          // Obtain the name of the device whose ID is 1.
          try {
            let deviceData: inputDevice.InputDeviceData = inputDevice.getDeviceInfoSync(1);
            console.info(`Succeeded in getting device info: ${JSON.stringify(deviceData)}.`);
          } catch (error) {
            console.error(`Failed to get device info, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
