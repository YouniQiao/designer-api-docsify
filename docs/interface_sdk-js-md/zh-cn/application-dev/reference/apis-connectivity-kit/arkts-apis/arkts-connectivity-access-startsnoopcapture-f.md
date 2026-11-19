# startSnoopCapture

## 导入模块

```TypeScript
import { access } from '@kit.ConnectivityKit';
```

## startSnoopCapture

```TypeScript
function startSnoopCapture(): number
```

启动HCI报文嗅探，返回携带实时HCI数据流的socket文件描述符。

数据流以标准btsnoop格式封装，可以转发到PC机进行实时解析（例如Wireshark）。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-access-function startSnoopCapture(): int--><!--Device-access-function startSnoopCapture(): int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回携带实时HCI数据流的套接字文件描述符。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | Permission verification failed. The application does not have the permission required to call the API. |
| [204](../../errorcode-universal.md#204-用户访问控制策略拦截访问被拒绝) | Access denied due to user access control policy. Possible causes: <br>1. The operation is restricted by the OS-account constraint; <br>2. The required privilege for the operation has not been granted. |
| [801](../../errorcode-universal.md#801-api功能在部分设备不支持) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| [2900003](../errorcode-bluetoothManager.md#2900003-蓝牙开关关闭) | Bluetooth disabled. |
| 2900020 | Another HCI sniffing session is in progress. |
| [2900099](../errorcode-bluetoothManager.md#2900099-操作失败) | Operation failed. |
