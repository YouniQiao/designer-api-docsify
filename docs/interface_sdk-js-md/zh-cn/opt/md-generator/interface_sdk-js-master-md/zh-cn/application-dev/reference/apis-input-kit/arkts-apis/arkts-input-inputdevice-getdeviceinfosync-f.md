# getDeviceInfoSync

## 导入模块

```TypeScript
```

## getDeviceInfoSync

```TypeScript
function getDeviceInfoSync(deviceId: number): InputDeviceData
```

获取指定输入设备的信息。

**起始版本：** 23

<!--Device-inputDevice-function getDeviceInfoSync(deviceId: int): InputDeviceData--><!--Device-inputDevice-function getDeviceInfoSync(deviceId: int): InputDeviceData-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | number | 是 |

**返回值：**

| 类型 |
| --- |
| [InputDeviceData](arkts-input-inputdevice-inputdevicedata-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

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
