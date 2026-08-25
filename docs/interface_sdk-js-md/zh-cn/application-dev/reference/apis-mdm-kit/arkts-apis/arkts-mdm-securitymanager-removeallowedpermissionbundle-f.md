# removeAllowedPermissionBundle

## 导入模块

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## removeAllowedPermissionBundle

```TypeScript
function removeAllowedPermissionBundle(admin: Want, permission: string, applicationInstance: common.ApplicationInstance): void
```

从权限使用例外名单中移除指定应用，移除后该应用不能继续使用对应的权限。

> **说明：**&gt;
> 必须先通过[setDisallowedPermission](arkts-mdm-securitymanager-setdisallowedpermission-f.md)接口禁用权限后，才能从权限使用例外名单移除应用，否则返回错误码92010
> 44。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| permission | string | 是 |
| applicationInstance | common.ApplicationInstance | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [9201044](../errorcode-enterpriseDeviceManager.md#9201044-指定权限未被禁用) |
