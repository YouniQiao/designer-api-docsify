# getDisallowedUsbDevices

## 导入模块

```TypeScript
import { usbManager } from 'kits/@kit.MDMKit';
```

## getDisallowedUsbDevices

```TypeScript
function getDisallowedUsbDevices(admin: Want): Array<UsbDeviceType>
```

获取禁止使用的USB设备类型。  
**使用场景**：  
- 设备管理员需要查看当前禁止使用的USB设备类型列表  
- 在修改禁用名单前，需要先获取现有名单进行比对  
- 管理界面需要展示当前的USB设备类型禁用策略配置

**起始版本：** 14

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_USB

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[UsbDeviceType](arkts-mdm-usbmanager-usbdevicetype-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## getDisallowedUsbDevices

```TypeScript
function getDisallowedUsbDevices(admin: Want | null): Array<UsbDeviceType>
```

获取禁止使用的USB设备类型。  
**使用场景**：  
- 设备管理员需要查看当前禁止使用的USB设备类型列表  
- 在修改禁用名单前，需要先获取现有名单进行比对  
- 管理界面需要展示当前的USB设备类型禁用策略配置

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_USB

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[UsbDeviceType](arkts-mdm-usbmanager-usbdevicetype-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
