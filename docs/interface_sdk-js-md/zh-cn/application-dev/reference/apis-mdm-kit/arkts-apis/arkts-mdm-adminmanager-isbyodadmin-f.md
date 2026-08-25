# isByodAdmin

## 导入模块

```TypeScript
import { adminManager } from 'kits/@kit.MDMKit';
```

## isByodAdmin

```TypeScript
function isByodAdmin(admin: Want): boolean
```

根据企业设备管理扩展组件查询当前应用是否被激活为BYOD设备管理应用。

**起始版本：** 20

**需要权限：** ohos.permission.START_PROVISIONING_MESSAGE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
