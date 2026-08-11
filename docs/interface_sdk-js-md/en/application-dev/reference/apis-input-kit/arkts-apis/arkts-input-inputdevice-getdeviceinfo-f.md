# getDeviceInfo

## Modules to Import

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## getDeviceInfo

```TypeScript
function getDeviceInfo(deviceId: int, callback: AsyncCallback<InputDeviceData>): void
```

Obtains information about the specified input device. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-inputDevice-function getDeviceInfo(deviceId: int, callback: AsyncCallback<InputDeviceData>): void--><!--Device-inputDevice-function getDeviceInfo(deviceId: int, callback: AsyncCallback<InputDeviceData>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;InputDeviceData&gt; | Yes | Callback function. If the retrieval is successful, **err** is **undefined**, and **data** is the input device information (including the device ID, name, supported input capabilities). Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

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
          // Obtain the name of the device whose ID is 1.
          try {
            inputDevice.getDeviceInfo(1, (error: BusinessError, deviceData: inputDevice.InputDeviceData) => {
              if (error) {
                console.error(`Failed to get device info, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`Device info: ${JSON.stringify(deviceData)}`);
            });
          } catch (error) {
            console.error(`Failed to get device info, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## getDeviceInfo

```TypeScript
function getDeviceInfo(deviceId: int): Promise<InputDeviceData>
```

Obtains the information about the input device with the specified ID. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-inputDevice-function getDeviceInfo(deviceId: int): Promise<InputDeviceData>--><!--Device-inputDevice-function getDeviceInfo(deviceId: int): Promise<InputDeviceData>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;InputDeviceData&gt; | Promise used to return information about the input device, including device ID, name, supported source, physical address, version information, and product information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

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
          // Obtain the name of the device whose ID is 1.
          try {
            inputDevice.getDeviceInfo(1).then((deviceData: inputDevice.InputDeviceData) => {
              console.info(`Device info: ${JSON.stringify(deviceData)}`);
            }).catch((error: BusinessError) => {
              console.error(`Get device info failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            });
          } catch (error) {
            console.error(`Failed to get device info, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

