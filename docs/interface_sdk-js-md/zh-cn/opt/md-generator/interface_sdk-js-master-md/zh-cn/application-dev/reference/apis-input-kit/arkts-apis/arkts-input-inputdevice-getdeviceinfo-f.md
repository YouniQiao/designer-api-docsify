# getDeviceInfo

## getDeviceInfo

```TypeScript
function getDeviceInfo(deviceId: number, callback: AsyncCallback<InputDeviceData>): void
```

获取指定输入设备的信息，使用callback异步回调。

**起始版本：** 9

<!--Device-inputDevice-function getDeviceInfo(deviceId: int, callback: AsyncCallback<InputDeviceData>): void--><!--Device-inputDevice-function getDeviceInfo(deviceId: int, callback: AsyncCallback<InputDeviceData>): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;InputDeviceData&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

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
          // 获取输入设备ID为1的设备信息。
          try {
            // 获取输入设备信息
            inputDevice.getDeviceInfo(1, (error: BusinessError, deviceData: inputDevice.InputDeviceData) => {
              if (error) {
                console.error(`Failed to get device info, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                return;
              }
              console.info(`Succeeded in getting device info: ${JSON.stringify(deviceData)}.`);
            });
          } catch (error) {
            console.error(`Failed to get device info, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## getDeviceInfo

```TypeScript
function getDeviceInfo(deviceId: number): Promise<InputDeviceData>
```

获取指定id的输入设备信息，使用Promise异步回调。

**起始版本：** 9

<!--Device-inputDevice-function getDeviceInfo(deviceId: int): Promise<InputDeviceData>--><!--Device-inputDevice-function getDeviceInfo(deviceId: int): Promise<InputDeviceData>-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;InputDeviceData&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

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
          // 获取输入设备ID为1的设备信息。
          try {
            // 获取输入设备信息
            inputDevice.getDeviceInfo(1).then((deviceData: inputDevice.InputDeviceData) => {
              console.info(`Succeeded in getting device info: ${JSON.stringify(deviceData)}.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to get device info, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            });
          } catch (error) {
            console.error(`Failed to get device info, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
