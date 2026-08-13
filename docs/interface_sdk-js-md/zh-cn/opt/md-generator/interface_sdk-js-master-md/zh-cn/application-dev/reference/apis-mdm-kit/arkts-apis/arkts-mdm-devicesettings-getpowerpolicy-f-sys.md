# getPowerPolicy（系统接口）

## getPowerPolicy

```TypeScript
function getPowerPolicy(admin: Want, powerScene: PowerScene): PowerPolicy
```

获取电源策略。

**起始版本：** 11

**废弃版本：** 26.0.0

**替代接口：** [getValue](arkts-mdm-devicesettings-getvalue-f.md#getValue)

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SETTINGS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-deviceSettings-function getPowerPolicy(admin: Want, powerScene: PowerScene): PowerPolicy--><!--Device-deviceSettings-function getPowerPolicy(admin: Want, powerScene: PowerScene): PowerPolicy-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| powerScene | [PowerScene](arkts-mdm-devicesettings-powerscene-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [PowerPolicy](arkts-mdm-devicesettings-powerpolicy-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

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
  let powerScene: deviceSettings.PowerScene = deviceSettings.PowerScene.TIME_OUT;
  let powerPolicy: deviceSettings.PowerPolicy = deviceSettings.getPowerPolicy(wantTemp, powerScene);
  console.info(`Succeeded in getting power policy ${JSON.stringify(powerPolicy)}`);
} catch (err) {
  console.error(`Failed to get power policy. Code: ${err.code}, message: ${err.message}`);
}
```
