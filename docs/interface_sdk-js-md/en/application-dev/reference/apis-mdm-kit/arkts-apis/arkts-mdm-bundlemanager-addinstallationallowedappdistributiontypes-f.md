# addInstallationAllowedAppDistributionTypes

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.MDMKit';
```

## addInstallationAllowedAppDistributionTypes

```TypeScript
function addInstallationAllowedAppDistributionTypes(admin: Want, appDistributionTypes: Array<AppDistributionType>): void
```

Adds the distribution type of the application that can be installed. Only applications of the distribution type that is added to [AppDistributionType](arkts-mdm-bundlemanager-appdistributiontype-e.md) can be installed on the current device.For details about the distribution type of the application signing certificate, refer to the **appDistributionType** attribute in [ApplicationInfo](../../apis-ability-kit/arkts-apis/arkts-ability-applicationinfo-i.md).

**Since:** 20

**Required permissions:** ohos.permission.ENTERPRISE_SET_BUNDLE_INSTALL_POLICY

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| appDistributionTypes | Array & lt;AppDistributionType & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
