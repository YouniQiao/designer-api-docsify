# cancelPairingDevice

## 导入模块

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## cancelPairingDevice

```TypeScript
function cancelPairingDevice(deviceId: string, callback: AsyncCallback<void>): void
```

取消当前应用发起的与对端设备的配对。使用Callback异步回调。

本接口用于取消正在进行的配对流程，对端设备未处于配对中时调用本接口会失败。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-connection-function cancelPairingDevice(deviceId: string, callback: AsyncCallback<void>): void--><!--Device-connection-function cancelPairingDevice(deviceId: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示要取消配对的对端设备MAC地址，由12个十六进制字符和5个冒号（:）组成，例如：“11:22:33:AA:BB:FF”。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当取消配对成功，err为undefined，否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | Permission verification failed. The application does not have the permission required to call the API. |
| [401](../../errorcode-universal.md#401-函数参数数量或参数类型不匹配) | [Sync] Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api功能在部分设备不支持) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| [2900001](../errorcode-bluetoothManager.md#2900001-蓝牙服务停止) | Service stopped. |
| [2900003](../errorcode-bluetoothManager.md#2900003-蓝牙开关关闭) | Bluetooth disabled. |
| 2900018 | The pairing is initiated by another application and cannot be cancelled.<br>**适用版本：** 26.1.0+ |
| 2900019 | The device is not in the pairing state.<br>**适用版本：** 26.1.0+ |
| [2900099](../errorcode-bluetoothManager.md#2900099-操作失败) | Operation failed. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
    connection.cancelPairingDevice('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```


## cancelPairingDevice

```TypeScript
function cancelPairingDevice(deviceId: string): Promise<void>
```

取消当前应用发起的与对端设备的配对。使用Promise异步回调。

本接口用于取消正在进行的配对流程，对端设备未处于配对中时调用本接口会失败。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-connection-function cancelPairingDevice(deviceId: string): Promise<void>--><!--Device-connection-function cancelPairingDevice(deviceId: string): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示要取消配对的对端设备MAC地址，由12个十六进制字符和5个冒号（:）组成，例如：“11:22:33:AA:BB:FF”。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | Permission verification failed. The application does not have the permission required to call the API. |
| [401](../../errorcode-universal.md#401-函数参数数量或参数类型不匹配) | [Sync] Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api功能在部分设备不支持) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| [2900001](../errorcode-bluetoothManager.md#2900001-蓝牙服务停止) | Service stopped. |
| [2900003](../errorcode-bluetoothManager.md#2900003-蓝牙开关关闭) | Bluetooth disabled. |
| 2900018 | The pairing is initiated by another application and cannot be cancelled.<br>**适用版本：** 26.1.0+ |
| 2900019 | The device is not in the pairing state.<br>**适用版本：** 26.1.0+ |
| [2900099](../errorcode-bluetoothManager.md#2900099-操作失败) | Operation failed. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
    connection.cancelPairingDevice('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
