# setDisallowedPermission

## 导入模块

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## setDisallowedPermission

```TypeScript
function setDisallowedPermission(admin: Want, permission: string, disallow: boolean, accountId: number): void
```

禁用指定用户下的指定权限，禁用后指定用户下的所有应用申请和使用指定权限时默认拒绝。适用于企业安全合规场景，如禁用相机、麦克风等高风险权限防止隐私泄露，或禁用特定功能（如蓝牙分享）防止企业数据外传。

> **说明：**&gt;
> 1.只能禁用[权限APL等级](../../../security/AccessToken/app-permission-mgmt-overview.md#权限机制中的基本概念)为normal或system_basic的权
> 限，否则返回错误码9201045。&gt;
> 2.单个用户下最多可以禁用200个权限。&gt;
> 3.权限禁用后，仅影响应用（系统应用和普通应用）使用对应的权限，不影响系统SA使用对应的权限。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| permission | string | 是 |
| disallow | boolean | 是 |
| accountId | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [9201045](../errorcode-enterpriseDeviceManager.md#9201045-指定权限不可被禁用) |
