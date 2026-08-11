# isMicrophoneDisabled

## isMicrophoneDisabled

```TypeScript
function isMicrophoneDisabled(admin: Want): boolean
```

查询麦克风是否被禁用。

**起始版本：** 11

**废弃版本：** 26.0.0

**替代接口：** [restrictions.getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md#getdisallowedpolicy)(admin:

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-restrictions-function isMicrophoneDisabled(admin: Want): boolean--><!--Device-restrictions-function isMicrophoneDisabled(admin: Want): boolean-End-->

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
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result = restrictions.isMicrophoneDisabled(wantTemp);
  console.info(`Succeeded in querying is microphone disabled : ${result}`);
} catch (err) {
  console.error(`Failed to query is microphone disabled or not. Code is ${err.code}, message is ${err.message}`);
}
```
