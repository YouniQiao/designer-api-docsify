# addDisallowedPermissiveUsbDevices

## 导入模块

```TypeScript
import { usbManager } from 'kits/@kit.MDMKit';
```

## addDisallowedPermissiveUsbDevices

```TypeScript
function addDisallowedPermissiveUsbDevices(admin: Want, usbDevices: Array<PermissiveUsbDeviceType>): void
```

添加禁止使用的USB设备类型。与[addDisallowedUsbDevices](arkts-mdm-usbmanager-adddisallowedusbdevices-f.md)接口不同的是，本接口可以不按照 [defined-class-codes](https://www.usb.org/defined-class-codes)标准进行匹配。对已连接的USB设备热生效，无需重新插拔，例如USB线控耳机正常使用时，调用本接口禁用该耳 机，会导致耳机不可用。以下情况下，调用本接口会报策略冲突：
1. 已经通过[addDisallowedUsbDevices](arkts-mdm-usbmanager-adddisallowedusbdevices-f.md)接口添加了禁止使用的USB设备类型。
2. 已经通过[setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md)接口禁用了设备USB能力。
3. 已经通过[addAllowedUsbDevices](arkts-mdm-usbmanager-addallowedusbdevices-f.md)接口添加了USB设备可用名单。
4. 已经通过[setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md)接口禁用了某用户USB存储设备写入能力。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_USB

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| usbDevices | Array&lt;[PermissiveUsbDeviceType](arkts-mdm-usbmanager-permissiveusbdevicetype-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-策略冲突) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
