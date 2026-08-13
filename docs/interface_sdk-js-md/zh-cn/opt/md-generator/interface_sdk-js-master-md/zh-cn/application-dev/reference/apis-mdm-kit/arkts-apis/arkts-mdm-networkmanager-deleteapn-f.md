# deleteApn

## deleteApn

```TypeScript
function deleteApn(admin: Want, apnId: string): void
```

删除APN。适用于企业移动网络配置管理场景，例如清理无效的APN配置、调整移动网络接入点配置、防止使用错误的APN配置，帮助企业维护正确的移动网络配置，确保设备使用正确的接入点连接移动网络。

**起始版本：** 20

**废弃版本：** -1

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APN

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-networkManager-function deleteApn(admin: Want, apnId: string): void--><!--Device-networkManager-function deleteApn(admin: Want, apnId: string): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| apnId | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { Want } from '@kit.AbilityKit';
import { networkManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};
let apnId: string = "1"; // 需根据实际情况进行替换
try {
  networkManager.deleteApn(wantTemp, apnId);
  console.info(`Succeeded in deleting apn.`);
} catch (err) {
  console.error(`Failed to delete apn. Code: ${err.code}, message: ${err.message}`);
}
```
