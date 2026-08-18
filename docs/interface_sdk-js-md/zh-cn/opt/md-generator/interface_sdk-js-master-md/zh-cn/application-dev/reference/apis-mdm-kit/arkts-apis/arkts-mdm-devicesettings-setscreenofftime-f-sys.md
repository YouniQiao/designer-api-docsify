# setScreenOffTime（系统接口）

## 导入模块

```TypeScript
```

## setScreenOffTime

```TypeScript
function setScreenOffTime(admin: Want, time: number): void
```

设置设备息屏时间。

**起始版本：** 11

**废弃版本：** 26.0.0

**替代接口：** [setValue](arkts-mdm-devicesettings-setvalue-f.md#setvalue)

**需要权限：** ohos.permission.ENTERPRISE_SET_SCREENOFF_TIME

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-deviceSettings-function setScreenOffTime(admin: Want, time: number): void--><!--Device-deviceSettings-function setScreenOffTime(admin: Want, time: number): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| time | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

**示例**

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  // 参数需根据实际情况进行替换
  deviceSettings.setScreenOffTime(wantTemp, 30000);
  console.info(`Succeeded in setting screen off time`);
} catch(err) {
  console.error(`Failed to set screen off time. Code: ${err.code}, message: ${err.message}`);
}
```
