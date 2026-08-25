# startAdminProvision

## 导入模块

```TypeScript
import { adminManager } from 'kits/@kit.MDMKit';
```

## startAdminProvision

```TypeScript
function startAdminProvision(admin: Want, type: AdminType, context: common.Context, parameters: Record<string, string>): void
```

设备管理应用拉起BYOD管理员激活页面进行激活。

**起始版本：** 15

**需要权限：** ohos.permission.START_PROVISIONING_MESSAGE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| type | [AdminType](arkts-mdm-adminmanager-admintype-e.md) | 是 |
| context | common.Context | 是 |
| parameters | Record & lt;string, string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
