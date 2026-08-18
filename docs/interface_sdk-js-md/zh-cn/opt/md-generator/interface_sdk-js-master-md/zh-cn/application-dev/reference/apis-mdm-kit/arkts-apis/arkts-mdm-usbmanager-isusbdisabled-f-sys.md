# isUsbDisabled（系统接口）

## 导入模块

```TypeScript
```

## isUsbDisabled

```TypeScript
function isUsbDisabled(admin: Want): boolean
```

查询USB是否禁用。

**起始版本：** 11

**废弃版本：** 26.0.0

**替代接口：** [getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md#getdisallowedpolicy)(admin: Want | null, feature: FeatureForDevice)

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_USB

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-usbManager-function isUsbDisabled(admin: Want): boolean--><!--Device-usbManager-function isUsbDisabled(admin: Want): boolean-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

**示例**

```TypeScript
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let isDisabled = usbManager.isUsbDisabled(wantTemp);
  console.info(`Succeeded in querying if USB is disabled: ${isDisabled}`);
} catch (err) {
  console.error(`Failed to query if USB is disabled. Code: ${err.code}, message: ${err.message}`);
}
```
