# addDisallowedBluetoothDevices

## 导入模块

```TypeScript
import { bluetoothManager } from 'kits/@kit.MDMKit';
```

## addDisallowedBluetoothDevices

```TypeScript
function addDisallowedBluetoothDevices(admin: Want, deviceIds: Array<string>): void
```

添加蓝牙设备禁用名单。添加禁用名单后当前设备不允许连接该名单下的蓝牙设备。从API version 22开始，数组中的MAC地址必须符合蓝牙MAC规范（例如：00:1A:2B:3C:4D:5E），添加时会移除不合法的MAC地址，仅 添加合法的MAC地址。以下情况下，通过本接口添加蓝牙设备禁用名单，会报策略冲突：
1. 已经通过[setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md)接口禁用了蓝牙。通过[setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md)接口启用蓝牙后，可解除冲突。
2. 已经通过[addAllowedBluetoothDevices](arkts-mdm-bluetoothmanager-addallowedbluetoothdevices-f.md)接口添加了蓝牙设备可用名单。通过[removeAllowedBluetoothDevices](arkts-mdm-bluetoothmanager-removeallowedbluetoothdevices-f.md)移除蓝牙设备可用名单后，可解除冲突。

**起始版本：** 20

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| deviceIds | Array & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-策略冲突) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
