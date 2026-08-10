# addSerialRight（系统接口）

## 导入模块

```TypeScript
import { serialManager } from 'kits/@kit.BasicServicesKit';
```

## addSerialRight

```TypeScript
function addSerialRight(tokenId: int, portId: int): void
```

为应用程序添加访问串口设备权限。serialManager.requestSerialRight会触发弹窗请求用户授权；addSerialRight不会触发弹窗，而是直接添加应用程序访问设备的权限。应用退出自动移除对串口设备的访问权限，在应用重启后需要重新申请授权。

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_USB_CONFIG

<!--Device-serialManager-function addSerialRight(tokenId: int, portId: int): void--><!--Device-serialManager-function addSerialRight(tokenId: int, portId: int): void-End-->

**系统能力：** SystemCapability.USB.USBManager.Serial

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tokenId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 需要访问权限的tokenId。 |
| portId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 目标设备的端口号，来自[getPortList](arkts-basicservices-serialmanager-getportlist-f.md#getportlist)获取的串口参数SerialPort。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 31400003 | PortId does not exist. |
| 14400005 | Database operation exception. |
| 31400001 | Serial port management exception. |

## 示例

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { serialManager } from '@kit.BasicServicesKit';


function addSerialRight() {
  // 获取串口列表
  let portList: serialManager.SerialPort[] = serialManager.getPortList();
  console.info('portList: ', JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('portList is empty');
    return;
  }

  let portId: number = portList[0].portId;
  let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_DEFAULT;

  bundleManager.getBundleInfoForSelf(bundleFlags).then((bundleInfo) => {
    console.info('getBundleInfoForSelf successfully. Data: %{public}s', JSON.stringify(bundleInfo));
    let tokenId = bundleInfo.appInfo.accessTokenId;
    try {
      // 串口增加权限
      serialManager.addSerialRight(tokenId, portId);
      console.info('addSerialRight success, portId: ' + portId);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(`Failed to add serial right. Code: ${err.code}, message: ${err.message}`);
    }
  }).catch((error: BusinessError) => {
    console.error(`Failed to get bundle info for self. Code: ${error.code}, message: ${error.message}`);
  });
}
```

