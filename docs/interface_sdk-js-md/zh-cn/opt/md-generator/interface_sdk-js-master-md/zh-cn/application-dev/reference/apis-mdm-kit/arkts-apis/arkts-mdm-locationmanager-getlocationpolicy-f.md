# getLocationPolicy

## getLocationPolicy

```TypeScript
function getLocationPolicy(admin: Want): LocationPolicy
```

查询位置服务管理策略。可在企业设备管理应用中检查当前设备的位置服务策略状态，用于策略合规性验证或策略调整前的状态确认。适用于确认当前策略配置、设备管理应用启动时读取策略状态、排查位置服务问题时检查策略等场景。

**起始版本：** 12

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_LOCATION

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-locationManager-function getLocationPolicy(admin: Want): LocationPolicy--><!--Device-locationManager-function getLocationPolicy(admin: Want): LocationPolicy-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [LocationPolicy](arkts-mdm-locationmanager-locationpolicy-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { locationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: locationManager.LocationPolicy = locationManager.getLocationPolicy(wantTemp);
  console.info(`Succeeded in getting location policy. policy: ${result}`);
} catch(err) {
  console.error(`Failed to get location policy. Code: ${err.code}, message: ${err.message}`);
}
```


## getLocationPolicy

```TypeScript
function getLocationPolicy(admin: Want | null): LocationPolicy
```

查询位置服务管理策略。可在企业设备管理应用中检查当前设备的位置服务策略状态，用于策略合规性验证或策略调整前的状态确认。适用于确认当前策略配置、设备管理应用启动时读取策略状态、排查位置服务问题时检查策略等场景。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_LOCATION

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-locationManager-function getLocationPolicy(admin: Want | null): LocationPolicy--><!--Device-locationManager-function getLocationPolicy(admin: Want | null): LocationPolicy-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | 是 |

**返回值：**

| 类型 |
| --- |
| [LocationPolicy](arkts-mdm-locationmanager-locationpolicy-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { locationManager } from '@kit.MDMKit';

try {
  // 参数需根据实际情况进行替换
  let result: locationManager.LocationPolicy = locationManager.getLocationPolicy(null);
  console.info(`Succeeded in getting location policy. policy: ${result}`);
} catch(err) {
  console.error(`Failed to get location policy. Code: ${err.code}, message: ${err.message}`);
}
```
