# setSwitchStatus

## setSwitchStatus

```TypeScript
function setSwitchStatus(admin: Want, key: SwitchKey, status: SwitchStatus): void
```

设置开关的状态。支持设置星闪、蓝牙、Wi-Fi、NFC的状态为开启或关闭，设置完毕后，用户可以手动开关。支持设置蓝牙、NFC的状态为强制开启，设置完毕后，用户不可以手动开关。若已经通过  
[setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy) 接口禁用了某个开关，则通过本接口设置这个开关的状态会抛出错误码203，需通过[setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy) 接口解除该开关禁用策略。当设备有多个MDM应用时，各MDM应用设置开关状态不存在冲突，最后设置的策略生效。开启(用户可手动开启、关闭)、关闭(用户可手动开启、关闭)、强制开启(用户不可手动关闭)三个状态可以随意切换，也不存在冲突。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SETTINGS or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-deviceSettings-function setSwitchStatus(admin: Want, key: SwitchKey, status: SwitchStatus): void--><!--Device-deviceSettings-function setSwitchStatus(admin: Want, key: SwitchKey, status: SwitchStatus): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| key | [SwitchKey](arkts-mdm-devicesettings-switchkey-e.md) | 是 |
| status | [SwitchStatus](arkts-mdm-devicesettings-switchstatus-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [203](../../errorcode-universal.md#203-企业管理策略禁止使用此系统功能) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| 9201042 |

## 示例

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 需根据实际情况进行替换
  let key: deviceSettings.SwitchKey = deviceSettings.SwitchKey.BLUETOOTH;
  let status: deviceSettings.SwitchStatus  = deviceSettings.SwitchStatus.ON;
  deviceSettings.setSwitchStatus(wantTemp, key, status);
  console.info(`Succeeded in setting switch status.`);
} catch (err) {
  console.error(`Failed to set switch status. Code: ${err.code}, message: ${err.message}`);
}
```
