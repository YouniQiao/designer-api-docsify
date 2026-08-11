# shutdown

## shutdown

```TypeScript
function shutdown(admin: Want): void
```

使设备关机。

**起始版本：** 11

**废弃版本：** 26.0.0

**替代接口：** [deviceControl.operateDevice](arkts-mdm-devicecontrol-operatedevice-f.md#operatedevice)(admin:

**需要权限：** ohos.permission.ENTERPRISE_REBOOT

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-deviceControl-function shutdown(admin: Want): void--><!--Device-deviceControl-function shutdown(admin: Want): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { deviceControl } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  deviceControl.shutdown(wantTemp);
} catch (err) {
  console.error(`Failed to shutdown device. Code is ${err.code}, message is ${err.message}`);
}
```
