# setLocationPolicy

## 导入模块

```TypeScript
import { locationManager } from 'kits/@kit.MDMKit';
```

## setLocationPolicy

```TypeScript
function setLocationPolicy(admin: Want, policy: LocationPolicy): void
```

设置位置服务管理策略。可用于企业管控场景，如：在涉密区域禁用位置服务以保护信息安全，或在物流配送应用中强制开启位置服务以追踪设备位置。

> **说明：**&gt;
> - 禁用：在需要保护隐私或节省电量的场景下设置。&gt;
> - 强制开启：在设备安全追踪、资产管理等场景下设置。&gt;
> - 默认：取消策略限制，由用户自主控制。

**起始版本：** 12

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_LOCATION

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| policy | [LocationPolicy](arkts-mdm-locationmanager-locationpolicy-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
