# stopSnoopCapture

## 导入模块

```TypeScript
import { access } from '@kit.ConnectivityKit';
```

## stopSnoopCapture

```TypeScript
function stopSnoopCapture(): void
```

停止HCI报文嗅探。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-access-function stopSnoopCapture(): void--><!--Device-access-function stopSnoopCapture(): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | Permission verification failed. The application does not have the permission required to call the API. |
| [204](../../errorcode-universal.md#204-用户访问控制策略拦截访问被拒绝) | Access denied due to user access control policy. Possible causes: <br>1. The operation is restricted by the OS-account constraint; <br>2. The required privilege for the operation has not been granted. |
| [801](../../errorcode-universal.md#801-api功能在部分设备不支持) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| [2900003](../errorcode-bluetoothManager.md#2900003-蓝牙开关关闭) | Bluetooth disabled. |
| 2900021 | The HCI capture session is initiated by another application. |
| [2900099](../errorcode-bluetoothManager.md#2900099-操作失败) | Operation failed. |
