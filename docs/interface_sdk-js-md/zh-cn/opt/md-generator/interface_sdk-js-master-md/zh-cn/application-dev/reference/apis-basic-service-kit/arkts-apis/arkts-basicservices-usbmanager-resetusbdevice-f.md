# resetUsbDevice

## resetUsbDevice

```TypeScript
function resetUsbDevice(pipe: USBDevicePipe): boolean
```

重置USB外设。 > **说明：** > > 本接口调用后会重置此前设置的配置和替换接口，请在调用之前确认相关业务已结束。

**起始版本：** 23

**废弃版本：** -1

<!--Device-usbManager-function resetUsbDevice(pipe: USBDevicePipe): boolean--><!--Device-usbManager-function resetUsbDevice(pipe: USBDevicePipe): boolean-End-->

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pipe](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md) | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14400010](../../apis-basic-services-kit/errorcode-usb.md#14400010-无法识别的错误) |
| [14400008](../../apis-basic-services-kit/errorcode-usb.md#14400008-没有设备连接已断开) |
| [14400013](../../apis-basic-services-kit/errorcode-usb.md#14400013-参数合法性检查失败) |
| [14400001](../../apis-basic-services-kit/errorcode-usb.md#14400001-usb设备访问权限被拒绝) |
| [14400004](../../apis-basic-services-kit/errorcode-usb.md#14400004-服务异常) |

## 示例

```TypeScript
import {BusinessError} from '@kit.BasicServicesKit';
async function resetUsbDevice() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.error(`device list is empty`);
    return;
  }

  let rightResult = await usbManager.requestRight(devicesList?.[0]?.name);
  if (!rightResult) {
    console.error(`request right failed`);
    return;
  }
  let devicePipe: usbManager.USBDevicePipe = usbManager.connectDevice(devicesList?.[0]);
  if (devicePipe == undefined) {
    console.error(`connect device failed`);
    return;
  }
  try {
    let ret: boolean = usbManager.resetUsbDevice(devicePipe);
    console.info(`resetUsbDevice  = ${ret}`);
  } catch (err) {
    console.error(`Failed to reset USB device. Code: ${err.code}, message: ${err.message}`);
  }
  usbManager.closePipe(devicePipe);
}
```
