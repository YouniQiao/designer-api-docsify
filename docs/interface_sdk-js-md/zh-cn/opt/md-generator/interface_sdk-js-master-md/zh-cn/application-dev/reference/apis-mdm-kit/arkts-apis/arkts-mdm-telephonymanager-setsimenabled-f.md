# setSimEnabled

## setSimEnabled

```TypeScript
function setSimEnabled(admin: Want, slotId: number): void
```

解除指定卡槽的SIM卡禁用。使用setSimDisabled禁用SIM卡后，再用setSimEnabled启用SIM卡，需要到设置-移动网络-SIM卡管理界面手动打开SIM卡开关。

**起始版本：** 20

**废弃版本：** -1

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-telephonyManager-function setSimEnabled(admin: Want, slotId: number): void--><!--Device-telephonyManager-function setSimEnabled(admin: Want, slotId: number): void-End-->

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

## 示例

```TypeScript
import { Want } from '@kit.AbilityKit';
import { telephonyManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  // 设置要启用的卡槽ID
  let slotId: number = 0;
  // 启用指定卡槽的SIM卡
  telephonyManager.setSimEnabled(wantTemp, slotId);
  console.info(`Succeeded in setting slotId: ${slotId} enabled.`);
} catch (err) {
  console.error(`Failed to set slotId enabled. Code: ${err.code}, message: ${err.message}`);
}
```
