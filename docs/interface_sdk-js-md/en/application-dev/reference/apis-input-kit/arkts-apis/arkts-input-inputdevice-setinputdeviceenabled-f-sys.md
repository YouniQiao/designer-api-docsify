# setInputDeviceEnabled (System API)

## Modules to Import

```TypeScript
import { inputDevice } from '@kit.InputKit';
```

## setInputDeviceEnabled

```TypeScript
function setInputDeviceEnabled(deviceId: int, enabled: boolean): Promise<void>
```

Sets the input switch status of an input device. Take the touchscreen as an example. If the input switch is off,the touchscreen does not respond when being touched. If the input switch is on, the touchscreen wakes up when being touched. This API uses a promise to return the result.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INPUT_DEVICE_CONTROLLER

<!--Device-inputDevice-function setInputDeviceEnabled(deviceId: int, enabled: boolean): Promise<void>--><!--Device-inputDevice-function setInputDeviceEnabled(deviceId: int, enabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |
| enabled | boolean | Yes | Switch status of the input device. The value **true** indicates that the input device is enabled, and the value **false** indicates the opposite. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Input parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [3900001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-input-kit/errorcode-inputdevice.md#3900001-device-not-exist) | The specified device does not exist. |

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
            inputDevice.setInputDeviceEnabled(0, true).then(() => {
              console.info(`Set input device enable success`);
            }).catch((error: BusinessError) => {
              console.error(`Set device enable failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`Set input device enable error`);
          }
        })
    }
  }
}
```

