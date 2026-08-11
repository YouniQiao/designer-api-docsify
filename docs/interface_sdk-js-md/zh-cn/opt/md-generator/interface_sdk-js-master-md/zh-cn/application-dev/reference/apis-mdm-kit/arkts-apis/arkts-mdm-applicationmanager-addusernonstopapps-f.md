# addUserNonStopApps

## addUserNonStopApps

```TypeScript
function addUserNonStopApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void
```

为指定用户添加不可关停应用名单，仅可对已安装应用设置该策略。若参数列表中存在未安装应用，则返回9200012错误码。若设置策略后，名单中有应用被卸载，则卸载的应用将从名单中移除。若添加已存在于名单中的应用，返回成功，但已设置策略名单中不会重复添加该应用。

不可关停应用在Phone和Tablet设备的效果：用户不能在任务中心上滑关闭应用；在设置-应用和元服务中点击应用名称进入详情页面后，页面中的强行停止按钮呈灰色不可用，页面中的停用按钮功能无效。

不可关停应用在PC/2in1设备的效果：用户在设置-应用和元服务中点击应用名称进入详情页面后，页面中的强行停止按钮呈灰色不可用，页面中的停用按钮功能无效。

从API版本26.0.0开始，调用  
[setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setdisallowedpolicyforaccount)接口禁用  
[SUPER_HUB](arkts-mdm-restrictions-featureforaccount-e.md)后，再调用该接口将中转站添加到不可关停应用名单时，会发生策略冲突，抛出9200010错误码。

**起始版本：** 22

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-applicationManager-function addUserNonStopApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void--><!--Device-applicationManager-function addUserNonStopApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| applicationInstances | Array&lt;common.ApplicationInstance&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-策略冲突) |
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
  applicationManager.addUserNonStopApps(wantTemp, applicationInstances);
  console.info('Succeeded in adding UserNonStop applications.');
} catch(err) {
  console.error(`Failed to add UserNonStop applications. Code: ${err.code}, message: ${err.message}`);
}
```
