# disableUsb（系统接口）

## 导入模块

```TypeScript
import { usbManager } from 'kits/@kit.MDMKit';
```

## disableUsb

```TypeScript
function disableUsb(admin: Want, disable: boolean): void
```

设置禁用或启用USB。

**起始版本：** 11

**废弃版本：** 26.0.0

**替代接口：** [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md)(admin: Want, feature: FeatureForDevice, disallow: boolean)

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_USB

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| disable | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-策略冲突) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
