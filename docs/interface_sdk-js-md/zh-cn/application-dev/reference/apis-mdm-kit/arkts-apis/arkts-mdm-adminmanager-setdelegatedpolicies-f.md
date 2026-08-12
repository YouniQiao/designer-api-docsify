# setDelegatedPolicies

## setDelegatedPolicies

```TypeScript
function setDelegatedPolicies(admin: Want, bundleName: string, policies: Array<string>): void
```

委托其他应用来设置设备的管控策略。被委托的其他应用需申请委托策略对应接口所需权限。

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为14。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_DELEGATED_POLICY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-adminManager-function setDelegatedPolicies(admin: Want, bundleName: string, policies: Array<string>): void--><!--Device-adminManager-function setDelegatedPolicies(admin: Want, bundleName: string, policies: Array<string>): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleName | string | 是 | 被委托应用包名。被委托应用的分发类型需为enterprise_normal和enterprise_mdm，可以通过 [getBundleInfoForSelf](../../apis-ability-kit/arkts-apis/arkts-ability-bundlemanager-getbundleinfoforself-f.md#getBundleInfoForSelf)接口查询应用自身的 [BundleInfo](./bundleManager/BundleInfo)，其中BundleInfo.appInfo.appDistributionType为应用的分发类型。 |
| policies | Array&lt;string&gt; | 是 | [委托策略列表](../../../mdm/mdm-kit-appendix.md#可委托策略列表)。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [9200009](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200009-授予应用权限失败) | Failed to grant the permission to the application. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) | The application is not an administrator application of the device. |
| [9200002](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) | The administrator application does not have permission to manage the device. |

## 示例

```TypeScript
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let admin: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let policies: Array<string> = ["disabled_hdc"];

try {
  // 参数需根据实际情况进行替换
  adminManager.setDelegatedPolicies(admin, "com.example.enterprise.xxx", policies);
  console.info('Succeeded in setting delegated policies.');
} catch (err) {
  console.error(`Failed to set delegated policies. Code: ${err.code}, message: ${err.message}`);
}
```


## setDelegatedPolicies

```TypeScript
function setDelegatedPolicies(bundleName: string, accountId: number, policies: Array<string>): void
```

委托其他应用来设置设备的管控策略。被委托的其他应用需申请委托策略对应接口所需权限。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为20。

**需要权限：** ohos.permission.MANAGE_ENTERPRISE_DEVICE_ADMIN

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-adminManager-function setDelegatedPolicies(bundleName: string, accountId: number, policies: Array<string>): void--><!--Device-adminManager-function setDelegatedPolicies(bundleName: string, accountId: number, policies: Array<string>): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 将要被委托的管理应用的包名。被委托应用的分发类型需为enterprise_normal和enterprise_mdm，可以通过 [bundleManager.getBundleInfoForSelf](../../apis-ability-kit/arkts-apis/arkts-ability-bundlemanager-getbundleinfoforself-f.md#getBundleInfoForSelf)接口查询应用 自身的BundleInfo，其中BundleInfo.appInfo.appDistributionType为应用的分发类型。 |
| accountId | number | 是 | 用户ID，指定具体用户，取值范围：大于等于0。可以通过 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md#getOsAccountLocalId) |
| policies | Array&lt;string&gt; | 是 | [委托策略列表](../../../mdm/mdm-kit-appendix.md#可委托策略列表)。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [9200009](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200009-授予应用权限失败) | Failed to grant the permission to the application. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Permission verification failed. A non-system application calls a system API. |

## 示例

```TypeScript
import { adminManager } from '@kit.MDMKit';
import { common, Want } from '@kit.AbilityKit';

// 需根据实际情况进行替换
let bundleName = 'com.example.myapplication';
let userId = 100;
let policies: Array<string> = ["disabled_hdc"];

try {
  adminManager.setDelegatedPolicies(bundleName, userId, policies);
  console.info(`Succeeded in setting delegated policies.`);
} catch (err) {
  console.error(`Failed to set delegated policies. Code: ${err.code}, message: ${err.message}`);
}
```

