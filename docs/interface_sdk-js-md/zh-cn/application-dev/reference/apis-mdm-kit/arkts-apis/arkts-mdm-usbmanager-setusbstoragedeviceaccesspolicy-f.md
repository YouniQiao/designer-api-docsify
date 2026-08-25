# setUsbStorageDeviceAccessPolicy

## 导入模块

```TypeScript
import { usbManager } from 'kits/@kit.MDMKit';
```

## setUsbStorageDeviceAccessPolicy

```TypeScript
function setUsbStorageDeviceAccessPolicy(admin: Want, usbPolicy: UsbPolicy): void
```

设置USB存储设备（baseClass = 0x08）访问策略。

> **说明：**&gt;
> 在调用接口前，确保已暂停USB存储设备的读写操作，保证操作的稳定性和数据的完整性，否则可能出现不可预期的异常。
> 以下情况下，通过本接口设置USB存储设备访问策略为可读可写/只读，会报策略冲突：
1. 已经通过[setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md)接口禁用了设备USB能力。
2. 已经通过[addDisallowedUsbDevices](arkts-mdm-usbmanager-adddisallowedusbdevices-f.md)接口将存储类型的USB设备添加为禁止使用的USB设备类型。
3. 已经通过[setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md)接口禁用了某用户USB存储设备写入能力。
以下情况下，通过本接口设置USB存储设备访问策略为禁用，会报策略冲突：
1. 已经通过[setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md)接口禁用了设备USB能力。
2. 已经通过[addAllowedUsbDevices](arkts-mdm-usbmanager-addallowedusbdevices-f.md)接口添加了USB设备可用名单。
3. 已经通过[setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md)接口禁用了某用户USB存储设备写入能力。
通过本接口设置，或者通过[addDisallowedUsbDevices](arkts-mdm-usbmanager-adddisallowedusbdevices-f.md)接口添加存储类型的USB设备，均可禁用USB存储设备。推荐使用后者。

**起始版本：** 12

**需要权限：** 
- API版本26.0.0+：ohos.permission.ENTERPRISE_MANAGE_USB or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS
- API版本12 - 24：ohos.permission.ENTERPRISE_MANAGE_USB

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| usbPolicy | [UsbPolicy](arkts-mdm-usbmanager-usbpolicy-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200007](../errorcode-enterpriseDeviceManager.md#9200007-系统服务工作异常) |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-策略冲突) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
