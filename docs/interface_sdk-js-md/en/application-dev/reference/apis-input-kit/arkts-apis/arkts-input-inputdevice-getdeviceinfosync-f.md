# getDeviceInfoSync

## Modules to Import

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## getDeviceInfoSync

```TypeScript
function getDeviceInfoSync(deviceId: int): InputDeviceData
```

Obtains information about the specified input device.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-inputDevice-function getDeviceInfoSync(deviceId: int): InputDeviceData--><!--Device-inputDevice-function getDeviceInfoSync(deviceId: int): InputDeviceData-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |

**Return value:**

| Type | Description |
| --- | --- |
| [InputDeviceData](arkts-input-inputdevice-inputdevicedata-i.md) | Information about the input device, including the device ID, name, supported source, physical address, version information, and product information. |

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
          // Obtain the name of the device whose ID is 1.
          try {
            let deviceData: inputDevice.InputDeviceData = inputDevice.getDeviceInfoSync(1);
            console.info(`Device info: ${JSON.stringify(deviceData)}`);
          } catch (error) {
            console.error(`Failed to get device info, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

