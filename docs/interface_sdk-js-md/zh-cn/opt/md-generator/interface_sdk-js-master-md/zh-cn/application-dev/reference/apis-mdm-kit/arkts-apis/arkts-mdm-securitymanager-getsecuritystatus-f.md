# getSecurityStatus

## getSecurityStatus

```TypeScript
function getSecurityStatus(admin: Want, item: string): string
```

获取当前设备安全策略信息。适用于设备合规性检查、安全状态审计、策略执行效果验证等场景，帮助企业管理员确认设备是否符合安全要求。企业可通过此接口实时监控设备的安全补丁状态和文件加密状态，及时发现设备安全风险并采取相应措施，保障企业设 备和数据安全。

**起始版本：** 12

**废弃版本：** -1

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-securityManager-function getSecurityStatus(admin: Want, item: string): string--><!--Device-securityManager-function getSecurityStatus(admin: Want, item: string): string-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| item | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: string = securityManager.getSecurityStatus(wantTemp, 'patch');
  console.info(`Succeeded in getting security patch tag. tag: ${result}`);
} catch (err) {
  console.error(`Failed to get security patch tag. Code: ${err.code}, message: ${err.message}`);
}
```
