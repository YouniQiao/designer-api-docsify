# isOtaUpdateNonceEnable

## isOtaUpdateNonceEnable

```TypeScript
function isOtaUpdateNonceEnable(admin: Want): boolean
```

查询OTA更新Nonce是否启用。适用于需要验证设备OTA更新安全配置的场景，帮助企业管理员确认Nonce校验功能状态，保障系统更新安全性。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-systemManager-function isOtaUpdateNonceEnable(admin: Want): boolean--><!--Device-systemManager-function isOtaUpdateNonceEnable(admin: Want): boolean-End-->

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-服务超时) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { systemManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let result: boolean = systemManager.isOtaUpdateNonceEnable(wantTemp);
  console.info(`Succeeded in querying OTA update Nonce enable: ${result}`);
} catch (err) {
  console.error(`Failed to query OTA update Nonce enable. Code is ${err.code}, message is ${err.message}`);
}
```
