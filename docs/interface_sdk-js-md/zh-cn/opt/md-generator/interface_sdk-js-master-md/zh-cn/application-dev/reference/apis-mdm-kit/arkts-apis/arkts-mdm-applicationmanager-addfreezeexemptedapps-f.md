# addFreezeExemptedApps

## addFreezeExemptedApps

```TypeScript
function addFreezeExemptedApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void
```

为指定用户添加后台防冻结应用名单，仅可对已安装应用设置该策略。若参数列表中存在未安装应用，则返回9200012错误码。若设置策略后，名单中有应用被卸载，则卸载的应用将从名单中移除。若添加已存在于名单中的应用，返回成功，但已设置策略 名单中不会重复添加该应用。 冻结操作：对目标应用的挂起、软件资源代理、硬件资源代理和高功耗管控等操作。

**起始版本：** 22

**废弃版本：** -1

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-applicationManager-function addFreezeExemptedApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void--><!--Device-applicationManager-function addFreezeExemptedApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| applicationInstances | Array & lt;common.ApplicationInstance & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { applicationManager, common } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let applicationInstances: Array<common.ApplicationInstance> = [
  // 需根据实际情况进行替换
  {
    appIdentifier: '0123456789123456789',
    accountId: 100,
    appIndex: 0
  }
];

try {
  applicationManager.addFreezeExemptedApps(wantTemp, applicationInstances);
  console.info('Succeeded in adding FreezeExempted applications.');
} catch(err) {
  console.error(`Failed to add FreezeExempted applications. Code: ${err.code}, message: ${err.message}`);
}
```
