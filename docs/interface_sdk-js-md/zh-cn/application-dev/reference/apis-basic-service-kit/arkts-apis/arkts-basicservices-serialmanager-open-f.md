# open

## open

```TypeScript
function open(portId: int): void
```

打开串口设备。

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为23。

<!--Device-serialManager-function open(portId: int): void--><!--Device-serialManager-function open(portId: int): void-End-->

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| portId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 目标设备的端口号，来自[getPortList](arkts-basicservices-serialmanager-getportlist-f.md#getPortList)获取的串口参数SerialPort。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [31400004](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-usb.md#31400004-串口设备被占用) | The serial port device is occupied. |
| [31400003](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-usb.md#31400003-端口号不存在) | PortId does not exist. |
| [31400002](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-usb.md#31400002-没有串口设备访问权限) | Access denied. Call requestSerialRight to request user authorization first. |
| [31400001](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-usb.md#31400001-串口服务异常) | Serial port management exception. |

## 示例

以下示例代码只是调用open接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```TypeScript
import serialManager from '@ohos.usbManager.serial';
import { BusinessError } from '@ohos.base';

// 获取串口列表
async function openExample() {
  let portList: serialManager.SerialPort[] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.error('usbSerial portList is empty');
    return;
  }
  let portId: int = portList[0].portId;

  // 检测设备是否可被应用访问
  if (!serialManager.hasSerialRight(portId)) {
    let result = await serialManager.requestSerialRight(portId);
    if (!result) {
      // 没有访问设备的权限且用户不授权则退出
      console.error('user is not granted the operation permission');
    } else {
      console.info('grant permission successfully');
    }
  }

  // 打开设备
  try {
    serialManager.open(portId)
    console.info('open usbSerial success, portId: ' + portId);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`Failed to open usbSerial. Code: ${err.code}, message: ${err.message}`);
  }

  // 关闭串口
  try {
    serialManager.close(portId);
    console.info('close usbSerial success, portId: ' + portId);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`Failed to close usbSerial. Code: ${err.code}, message: ${err.message}`);
  }
}
```

