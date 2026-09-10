# removeAllowedPrinterIPAddressesForDevice

## 导入模块

```TypeScript
import { systemManager } from '@kit.MDMKit';
```

## removeAllowedPrinterIPAddressesForDevice

```TypeScript
function removeAllowedPrinterIPAddressesForDevice(ipAddresses: Array<string>): void
```

Removes allowed printer IP addresses for device. The policy takes effect for all accounts.

**起始版本：** 26.1.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ipAddresses | Array&lt;string&gt; | 是 | ipAddresses indicate the IP address list of printer to be removed. Each IP address must be in IPv4 format or IPV6 format. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permission verification failed. The application does not have the permission required to call the API. |
| [801](../../errorcode-universal.md#801-该设备不支持此api) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) | The administrator application does not have permission to manage the device. |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) | Parameter verification failed. |
