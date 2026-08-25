# offChange

## 导入模块

```TypeScript
import { inputDevice } from '@kit.InputKit';
```

## offChange

```TypeScript
function offChange(listener?: Callback<DeviceListener>): void
```

取消监听输入设备的热插拔事件。在应用退出前调用，取消监听。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| listener | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DeviceListener](arkts-input-inputdevice-devicelistener-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { Entry, Text, RelativeContainer, Component } from '@kit.ArkUI';
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          let callback = (data: inputDevice.DeviceListener) => {
            console.info(`Succeeded in listening to device change, data: ${JSON.stringify(data, [`type`, `deviceId`])}.`);
          };
          try {
            // 监听设备热插拔事件
            inputDevice.onChange(callback);
          } catch (error) {
            console.error(`Failed to listen device event, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
          // 取消指定的监听。
          try {
            // 取消监听设备热插拔事件
            inputDevice.offChange(callback);
          } catch (error) {
            console.error(`Failed to cancel listening device event, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
          // 取消所有监听。
          try {
            // 取消监听设备热插拔事件
            inputDevice.offChange();
          } catch (error) {
            console.error(`Failed to cancel all listening device event, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
