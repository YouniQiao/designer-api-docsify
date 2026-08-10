# isValidRandomDeviceId

## 导入模块

```TypeScript
import { access } from 'kits/@kit.ConnectivityKit';
```

## isValidRandomDeviceId

```TypeScript
function isValidRandomDeviceId(deviceId: string): boolean
```

Determine whether the randomized device address application can still be used.

**起始版本：** 16

**ArkTS模式：** ArkTS-Dyn起始版本为16；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**原子化服务API：** 从API版本16开始，该接口支持在原子化服务API中使用。

<!--Device-access-function isValidRandomDeviceId(deviceId: string): boolean--><!--Device-access-function isValidRandomDeviceId(deviceId: string): boolean-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | the randomized address of remote device. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns whether the randomized device address is valid. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Check persistent device address failed. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let deviceId = '11:22:33:44:55:66'  // 该地址可通过BLE扫描获取
    let isValid = access.isValidRandomDeviceId(deviceId);
    console.info("isValid: " + isValid);
} catch (err) {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```

