# getDisallowedInstallBundlesSync

## getDisallowedInstallBundlesSync

```TypeScript
function getDisallowedInstallBundlesSync(admin: Want, accountId?: number): Array<string>
```

获取当前/指定用户下的应用程序包安装禁止名单。

**起始版本：** 12

**需要权限：** ohos.permission.ENTERPRISE_SET_BUNDLE_INSTALL_POLICY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-bundleManager-function getDisallowedInstallBundlesSync(admin: Want, accountId?: number): Array<string>--><!--Device-bundleManager-function getDisallowedInstallBundlesSync(admin: Want, accountId?: number): Array<string>-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| accountId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;string&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { bundleManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  let result: Array<string> = bundleManager.getDisallowedInstallBundlesSync(wantTemp, 100);
  console.info(`Succeeded in getting disallowed install bundles, result : ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get disallowed install bundles. Code is ${err.code}, message is ${err.message}`);
}
```


## getDisallowedInstallBundlesSync

```TypeScript
function getDisallowedInstallBundlesSync(admin: Want | null, accountId?: number): Array<string>
```

获取当前/指定用户下的应用程序包安装禁止名单。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_SET_BUNDLE_INSTALL_POLICY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-bundleManager-function getDisallowedInstallBundlesSync(admin: Want | null, accountId?: number): Array<string>--><!--Device-bundleManager-function getDisallowedInstallBundlesSync(admin: Want | null, accountId?: number): Array<string>-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | 是 |
| accountId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;string&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { bundleManager } from '@kit.MDMKit';

try {
  // 参数需根据实际情况进行替换
  // 参数需根据实际情况进行替换
  let result: Array<string> = bundleManager.getDisallowedInstallBundlesSync(null, 100);
  console.info(`Succeeded in getting disallowed install bundles, result : ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get disallowed install bundles. Code is ${err.code}, message is ${err.message}`);
}
```
