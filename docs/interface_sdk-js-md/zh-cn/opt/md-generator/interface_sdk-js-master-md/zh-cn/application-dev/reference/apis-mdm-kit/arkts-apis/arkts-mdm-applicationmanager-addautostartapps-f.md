# addAutoStartApps

## addAutoStartApps

```TypeScript
function addAutoStartApps(admin: Want, autoStartApps: Array<Want>): void
```

为当前用户添加开机自启动应用名单。通过本接口添加至自启动名单的应用，禁止用户在设备上手动取消应用自启动，但可通过 [removeAutoStartApps](arkts-mdm-applicationmanager-removeautostartapps-f.md#removeAutoStartApps)接口将应用从自启动名单中移除。

**起始版本：** 12

**废弃版本：** -1

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-applicationManager-function addAutoStartApps(admin: Want, autoStartApps: Array<Want>): void--><!--Device-applicationManager-function addAutoStartApps(admin: Want, autoStartApps: Array<Want>): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| autoStartApps | Array&lt;[Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let autoStartApps: Array<Want> = [
  {
    // 需根据实际情况进行替换
    bundleName: 'com.example.autoStartApplication',
    abilityName: 'EntryAbility',
    // 下面为非必选参数
    parameters: {
      // 从API version 24开始支持，配置应用开机自启时，是否隐藏UI界面，true代表隐藏，该参数设置为true时，应用需接入状态栏，否则自启设置失败，抛出401异常。
      isHiddenStart: true 
    }
  }
];

try {
  applicationManager.addAutoStartApps(wantTemp, autoStartApps);
  console.info('Succeeded in adding auto start applications.');
} catch(err) {
  console.error(`Failed to add auto start applications. Code: ${err.code}, message: ${err.message}`);
}
```


## addAutoStartApps

```TypeScript
function addAutoStartApps(admin: Want, autoStartApps: Array<Want>, accountId: number, disallowModify: boolean): void
```

为指定用户添加开机自启动应用名单，并设置是否禁止该用户手动取消应用自启动。 通过本接口、[addAutoStartApps](#addAutoStartApps)接口均可添加开机自启动应用名单，两个接口的设置可同时生效。同一用户下，开机自启动应用名单最多支持 包含10个应用。例如：若当前名单中已有3个应用，则最多还能通过本接口为当前用户添加7个应用。

**起始版本：** 20

**废弃版本：** -1

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-applicationManager-function addAutoStartApps(admin: Want, autoStartApps: Array<Want>, accountId: number, disallowModify: boolean): void--><!--Device-applicationManager-function addAutoStartApps(admin: Want, autoStartApps: Array<Want>, accountId: number, disallowModify: boolean): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| autoStartApps | Array&lt;[Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)&gt; | 是 |
| accountId | number | 是 |
| disallowModify | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let autoStartApps: Array<Want> = [
  // 需根据实际情况进行替换
  {
    bundleName: 'com.example.autoStartApplication',
    abilityName: 'EntryAbility',
    // 下面为非必选参数
    parameters: {
      // 从API version 24开始支持，配置应用开机自启时，是否隐藏UI界面，true代表隐藏，该参数设置为true时，应用需接入状态栏，否则自启设置失败，抛出401异常。
      isHiddenStart: true 
    }
  }
];

try {
  applicationManager.addAutoStartApps(wantTemp, autoStartApps, 100, true);
  console.info('Succeeded in adding auto start applications and set disallowModify.');
} catch(err) {
  console.error(`Failed to add auto start applications and set disallowModify. Code: ${err.code}, message: ${err.message}`);
}
```
