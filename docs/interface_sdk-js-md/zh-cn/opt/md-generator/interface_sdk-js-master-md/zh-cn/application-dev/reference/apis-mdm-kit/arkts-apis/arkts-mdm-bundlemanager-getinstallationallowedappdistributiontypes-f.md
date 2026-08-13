# getInstallationAllowedAppDistributionTypes

## getInstallationAllowedAppDistributionTypes

```TypeScript
function getInstallationAllowedAppDistributionTypes(admin: Want): Array<AppDistributionType>
```

获取可安装的应用程序签名证书的分发类型。

**起始版本：** 20

**废弃版本：** -1

**需要权限：** ohos.permission.ENTERPRISE_SET_BUNDLE_INSTALL_POLICY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-bundleManager-function getInstallationAllowedAppDistributionTypes(admin: Want): Array<AppDistributionType>--><!--Device-bundleManager-function getInstallationAllowedAppDistributionTypes(admin: Want): Array<AppDistributionType>-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;AppDistributionType & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { Want } from '@kit.AbilityKit';
import { bundleManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.edmtest',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let result: Array<bundleManager.AppDistributionType> = bundleManager.getInstallationAllowedAppDistributionTypes(wantTemp);
  console.info(`Succeeded in getting allowed appDistributionTypes. Result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get allowed appDistributionTypes. Code: ${err.code}, message: ${err.message}`);
}
```


## getInstallationAllowedAppDistributionTypes

```TypeScript
function getInstallationAllowedAppDistributionTypes(admin: Want | null): Array<AppDistributionType>
```

获取可安装的应用程序签名证书的分发类型。

**起始版本：** 26.0.0

**废弃版本：** -1

**需要权限：** ohos.permission.ENTERPRISE_SET_BUNDLE_INSTALL_POLICY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-bundleManager-function getInstallationAllowedAppDistributionTypes(admin: Want | null): Array<AppDistributionType>--><!--Device-bundleManager-function getInstallationAllowedAppDistributionTypes(admin: Want | null): Array<AppDistributionType>-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;AppDistributionType & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { bundleManager } from '@kit.MDMKit';

try {
  // 参数需根据实际情况进行替换
  let result: Array<bundleManager.AppDistributionType> = bundleManager.getInstallationAllowedAppDistributionTypes(null);
  console.info(`Succeeded in getting allowed appDistributionTypes. Result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get allowed appDistributionTypes. Code: ${err.code}, message: ${err.message}`);
}
```
