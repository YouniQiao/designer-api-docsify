# turnOnWifi

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.MDMKit';
```

## turnOnWifi

```TypeScript
function turnOnWifi(admin: Want, isForce: boolean): void
```

打开Wi-Fi开关。适用于企业设备远程管理场景，例如管理员远程控制员工设备开启Wi-Fi或在特定策略执行时确保Wi-Fi已开启。以下情况下，通过本接口打开Wi-Fi开关，会打开失败并提示"系统功能被禁用"：​已经通过[setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md)接口禁用了Wi-Fi。需通过 [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md)接口启用Wi-Fi，解决"系统功能被禁用"报错。

**起始版本：** 20

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| isForce | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [203](../../errorcode-universal.md#203-企业管理策略禁止使用此系统功能) |
