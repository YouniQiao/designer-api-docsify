# setUserRestrictionForAccount

## setUserRestrictionForAccount

```TypeScript
function setUserRestrictionForAccount(admin: Want, settingsItem: string, accountId: number, restricted: boolean): void
```

设置指定用户行为的限制规则。

**起始版本：** 23

**废弃版本：** 26.0.0

**替代接口：** [setUserRestrictionForAccount](#setUserRestrictionForAccount)(admin: Want, settingsItem: SettingsForAccount, accountId: int, restricted: boolean)

**需要权限：** ohos.permission.ENTERPRISE_SET_USER_RESTRICTION

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-restrictions-function setUserRestrictionForAccount(admin: Want, settingsItem: string, accountId: int, restricted: boolean): void--><!--Device-restrictions-function setUserRestrictionForAccount(admin: Want, settingsItem: string, accountId: int, restricted: boolean): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| settingsItem | string | 是 |
| accountId | number | 是 |
| restricted | boolean | 是 |

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
import { restrictions } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let userId = 100;
let settingsItem: string = "modifyWallpaper";
try {
  restrictions.setUserRestrictionForAccount(wantTemp, settingsItem, userId, true);
  console.info('Succeeded in restricting from setting modifyWallpaper');
} catch (err) {
  console.error(`Failed to restrict from setting modifyWallpaper. Code is ${err.code}, message is ${err.message}`);
}
```


## setUserRestrictionForAccount

```TypeScript
function setUserRestrictionForAccount(admin: Want, settingsItem: SettingsForAccount, accountId: number, restricted: boolean): void
```

限制指定用户修改指定的设置项。

**起始版本：** 26.0.0

**废弃版本：** -1

**需要权限：** ohos.permission.ENTERPRISE_SET_USER_RESTRICTION

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-restrictions-function setUserRestrictionForAccount(admin: Want, settingsItem: SettingsForAccount, accountId: int, restricted: boolean): void--><!--Device-restrictions-function setUserRestrictionForAccount(admin: Want, settingsItem: SettingsForAccount, accountId: int, restricted: boolean): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| settingsItem | [SettingsForAccount](arkts-mdm-restrictions-settingsforaccount-e.md) | 是 |
| accountId | number | 是 |
| restricted | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
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
  // 参数需根据实际情况进行替换
  restrictions.setUserRestrictionForAccount(wantTemp, restrictions.SettingsForAccount.MODIFY_WALLPAPER, 100, true);
  console.info('Succeeded in restricting from setting modifyWallpaper');
} catch (err) {
  console.error(`Failed to restrict from setting modifyWallpaper. Code is ${err.code}, message is ${err.message}`);
}
```
