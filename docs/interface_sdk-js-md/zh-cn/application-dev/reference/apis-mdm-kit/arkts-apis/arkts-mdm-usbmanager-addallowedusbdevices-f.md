# addAllowedUsbDevices

## 导入模块

```TypeScript
import { usbManager } from 'kits/@kit.MDMKit';
```

## addAllowedUsbDevices

```TypeScript
function addAllowedUsbDevices(admin: Want, usbDeviceIds: Array<UsbDeviceId>): void
```

添加USB设备可用名单。  
**使用场景**：  
- 企业安全管理场景，需要限制只有特定的USB设备可以接入设备  
- 设备管理员需要精确控制哪些USB设备能够被识别和使用  
- 配合[removeAllowedUsbDevices](arkts-mdm-usbmanager-removeallowedusbdevices-f.md)接口实现USB设备的动态管理  
以下情况下，调用本接口会报策略冲突：
1. 已经通过[setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md)接口禁用了设备USB或者USB转串口能力。
2. 已经通过[setUsbStorageDeviceAccessPolicy](arkts-mdm-usbmanager-setusbstoragedeviceaccesspolicy-f.md)接口设置了USB存储设备访问策略为禁用。
3. 已经通过[addDisallowedUsbDevices](arkts-mdm-usbmanager-adddisallowedusbdevices-f.md)接口添加了禁止使用的USB设备类型。
4. 已经通过[addDisallowedPermissiveUsbDevices](arkts-mdm-usbmanager-adddisallowedpermissiveusbdevices-f.md)接口添加了禁止使用的USB设备类型。

**起始版本：** 12

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_USB

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| usbDeviceIds | Array&lt;[UsbDeviceId](arkts-mdm-usbmanager-usbdeviceid-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200007](../errorcode-enterpriseDeviceManager.md#9200007-系统服务工作异常) |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-策略冲突) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
