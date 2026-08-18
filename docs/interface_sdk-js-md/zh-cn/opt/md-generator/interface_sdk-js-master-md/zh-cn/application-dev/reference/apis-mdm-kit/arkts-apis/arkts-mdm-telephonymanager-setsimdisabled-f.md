# setSimDisabled

## 导入模块

```TypeScript
```

## setSimDisabled

```TypeScript
function setSimDisabled(admin: Want, slotId: number): void
```

禁用指定卡槽的SIM卡。禁用后，无法使用该卡槽的SIM卡接打电话、收发短信、上网。例如，企业设备管理员可在员工离职或设备丢失时，禁用SIM卡防止未授权使用。适用于企业需要限制员工设备通话能力的场景，例如员工离职或设备遗失时防止 SIM卡被滥用，保障企业通信安全和成本控制。

**起始版本：** 20

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-telephonyManager-function setSimDisabled(admin: Want, slotId: number): void--><!--Device-telephonyManager-function setSimDisabled(admin: Want, slotId: number): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| slotId | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

**示例**

```TypeScript
import { Want } from '@kit.AbilityKit';
import { telephonyManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  // 设置要禁用的卡槽ID
  let slotId: number = 0;
  // 禁用指定卡槽的SIM卡
  telephonyManager.setSimDisabled(wantTemp, slotId);
  console.info(`Succeeded in setting slotId: ${slotId} disabled.`);
} catch (err) {
  console.error(`Failed to set slotId disabled. Code: ${err.code}, message: ${err.message}`);
}
```
