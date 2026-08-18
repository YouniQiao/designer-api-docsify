# removeAllowedBluetoothDevices

## 导入模块

```TypeScript
```

## removeAllowedBluetoothDevices

```TypeScript
function removeAllowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void
```

移除蓝牙设备可用名单。

**起始版本：** 12

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-bluetoothManager-function removeAllowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void--><!--Device-bluetoothManager-function removeAllowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| deviceIds | Array & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

**示例**

```TypeScript
import { bluetoothManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

// 创建企业设备管理扩展组件
let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 定义蓝牙设备MAC地址数组（需根据实际情况进行替换）
let deviceIds: Array<string> = ["00:1A:2B:3C:4D:5E", "AA:BB:CC:DD:EE:FF"];
try {
  // 移除蓝牙设备允许名单
  bluetoothManager.removeAllowedBluetoothDevices(wantTemp, deviceIds);
  console.info(`Succeeded in removing allowed bluetooth devices.`);
} catch (err) {
  console.error(`Failed to remove allowed bluetooth devices. Code: ${err.code}, message: ${err.message}`);
}
```
