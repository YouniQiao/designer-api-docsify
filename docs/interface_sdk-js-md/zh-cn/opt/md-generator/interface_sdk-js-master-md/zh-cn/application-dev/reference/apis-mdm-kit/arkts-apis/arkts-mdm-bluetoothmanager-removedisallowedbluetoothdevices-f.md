# removeDisallowedBluetoothDevices

## removeDisallowedBluetoothDevices

```TypeScript
function removeDisallowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void
```

移除蓝牙设备禁用名单。若移除禁用名单中的部分蓝牙设备，则当前设备不允许连接禁用名单内剩余的蓝牙设备。若移除禁用名单中的所有蓝牙设备，则当前设备可以连接任意的蓝牙设备。

**起始版本：** 20

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-bluetoothManager-function removeDisallowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void--><!--Device-bluetoothManager-function removeDisallowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| deviceIds | Array&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

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
let deviceIds: Array<string> = ["00:1A:2B:3C:4D:5E","AA:BB:CC:DD:EE:FF"];
try {
  // 移除蓝牙设备禁用名单
  bluetoothManager.removeDisallowedBluetoothDevices(wantTemp,deviceIds);
  console.info(`Succeeded in removing disallowed bluetooth devices.`);
} catch(err) {
  console.error(`Failed to remove disallowed bluetooth devices. Code: ${err.code}, message: ${err.message}`);
}
```
