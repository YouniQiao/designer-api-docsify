# addUserNonStopApps

## Modules to Import

```TypeScript
import { applicationManager } from 'kits/@kit.MDMKit';
```

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

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function addUserNonStopApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void--><!--Device-applicationManager-function addUserNonStopApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| applicationInstances | Array&lt;common.ApplicationInstance&gt; | Yes | 不可关停应用名单数组。不可关停应用名单最多支持包含10个应用，该数量限制不区分用户，即所有用户 下添加应用的总和的最大限制为10个。例如：若当前名单中已有3个应用，则最多还能通过本接口为指定用户添加7个应用。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 9200012 | Parameter verification failed. |
| 9200010 | A conflict policy has been configured.<br>**Applicable version:** 26.0.0 and later |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { applicationManager, common } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let applicationInstances: Array<common.ApplicationInstance> = [
  // Replace it as required.
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

