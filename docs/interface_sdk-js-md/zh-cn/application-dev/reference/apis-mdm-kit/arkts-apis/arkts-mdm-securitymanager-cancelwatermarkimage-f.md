# cancelWatermarkImage

## 导入模块

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## cancelWatermarkImage

```TypeScript
function cancelWatermarkImage(admin: Want, bundleName: string, accountId: number): void
```

取消指定用户的水印策略。当应用不再需要水印保护或需要更换水印时，企业可调用此接口取消水印策略。

**起始版本：** 14

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| bundleName | string | 是 |
| accountId | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
