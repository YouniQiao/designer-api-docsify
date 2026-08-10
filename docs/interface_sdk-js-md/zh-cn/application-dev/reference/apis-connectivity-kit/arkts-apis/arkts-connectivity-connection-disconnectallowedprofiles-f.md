# disconnectAllowedProfiles

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.ConnectivityKit';
```

## disconnectAllowedProfiles

```TypeScript
function disconnectAllowedProfiles(deviceId: string): Promise<void>
```

Disconnects all allowed bluetooth profiles between the local and remote device.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**需要权限：** 
- API版本26.0.0+：ohos.permission.ACCESS_BLUETOOTH
- API版本11 - 24：ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-connection-function disconnectAllowedProfiles(deviceId: string): Promise<void>--><!--Device-connection-function disconnectAllowedProfiles(deviceId: string): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | Indicates device ID. For example, "11:22:33:AA:BB:FF". |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Returns the promise object. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.<br>**适用版本：** 11 - 24 |
| 801 | Capability not supported. Failed to call the API when the short-range chip is not inserted on 2in1 device. |
| 201 | Permission denied. |
| 202 | Non-system applications are not allowed to use system APIs.<br>**适用版本：** 11 - 24 |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

## 示例

```TypeScript
try {
  await connection.disconnectAllowedProfiles('68:13:24:79:4C:8C');
} catch (err) {
  console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
    connection.disconnectAllowedProfiles('68:13:24:79:4C:8C').then(() => {
        console.info('disconnectAllowedProfiles');
    }, (err: BusinessError) => {
        console.error('disconnectAllowedProfiles:errCode' + err.code + ', errMessage: ' + err.message);
    });
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

