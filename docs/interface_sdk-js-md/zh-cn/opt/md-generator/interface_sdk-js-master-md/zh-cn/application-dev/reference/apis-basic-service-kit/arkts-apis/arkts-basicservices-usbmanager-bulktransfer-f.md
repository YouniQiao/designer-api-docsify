# bulkTransfer

## bulkTransfer

```TypeScript
function bulkTransfer(
    pipe: USBDevicePipe,
    endpoint: USBEndpoint,
    buffer: Uint8Array,
    timeout?: number
  ): Promise<number>
```

批量传输。使用Promise异步回调。

> **说明：**
> 
> 单次批量传输的传输数据总量（包括pipe、endpoint、buffer、timeout）请控制在200KB以下，数据总量过大会导致传输失败返回-1。
> 
> 在调用接口前需要通过
> [usbManager.claimInterface](arkts-basicservices-usbmanager-claiminterface-f.md#claiminterface)
> claim通信接口。

**起始版本：** 9

<!--Device-usbManager-function bulkTransfer(    pipe: USBDevicePipe,    endpoint: USBEndpoint,    buffer: Uint8Array,    timeout?: int  ): Promise<int>--><!--Device-usbManager-function bulkTransfer(    pipe: USBDevicePipe,    endpoint: USBEndpoint,    buffer: Uint8Array,    timeout?: int  ): Promise<int>-End-->

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pipe | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | 是 |
| endpoint | [USBEndpoint](arkts-basicservices-usbmanager-usbendpoint-i.md) | 是 |
| buffer | Uint8Array | 是 |
| timeout | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;number&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## 示例

以下示例代码只是调用bulkTransfer接口的必要流程，实际调用时，设备开发者需要遵循目标USB设备的协议规范进行调用，具体协议要求请参考设备的技术文档，确保数据的正确传输和设备的兼容性。

```TypeScript
import {BusinessError} from '@kit.BasicServicesKit';
// usbManager.getDevices 接口返回数据集合，取其中一个设备对象，并获取权限。
// 把获取到的设备对象作为参数传入usbManager.connectDevice；当usbManager.connectDevice接口成功返回之后；
// 才可以调用第三个接口usbManager.claimInterface。当usbManager.claimInterface 调用成功以后，再调用该接口。
async function bulkTransfer() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }

  let device: usbManager.USBDevice = devicesList?.[0];
  await usbManager.requestRight(device.name);
  if (!usbManager.hasRight(device.name)) {
    console.error(`request right fail`);
    return;
  }
  let devicePipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
  if (devicePipe == undefined) {
    console.error(`connect device failed`);
    return;
  }
  for (let i = 0; i < device.configs?.[0]?.interfaces.length; i++) {
    if (device.configs?.[0]?.interfaces?.[i]?.endpoints?.[0]?.attributes == 2) {
      let endpoint: usbManager.USBEndpoint = device.configs?.[0]?.interfaces?.[i]?.endpoints?.[0];
      let interfaces: usbManager.USBInterface = device.configs?.[0]?.interfaces?.[i];
      let ret: number = usbManager.claimInterface(devicePipe, interfaces);
      if (ret !== 0) {
        console.error(`claim interface failed`);
        continue;
      }
      let buffer = new Uint8Array(128);
      usbManager.bulkTransfer(devicePipe, endpoint, buffer).then((ret: number) => {
        console.info(`bulkTransfer = ${ret}`);
        ret = usbManager.releaseInterface(devicePipe, interfaces);
        console.info(`releaseInterface = ${ret}`);
        if (i === device.configs?.[0]?.interfaces.length - 1) {
          usbManager.closePipe(devicePipe);
        }
      }).catch((error: BusinessError) => {
        console.error(`Failed to transfer. Code: ${error.code}, message: ${error.message}`);
      });
    }
  }
}
```
