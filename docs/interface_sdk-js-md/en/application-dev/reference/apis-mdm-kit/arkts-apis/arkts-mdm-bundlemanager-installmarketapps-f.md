# installMarketApps

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.MDMKit';
```

## installMarketApps

```TypeScript
function installMarketApps(admin: Want, bundleNames: Array<string>): void
```

Downloads and installs an application from AppGallery.

> **NOTE：**&gt;
> After this API is successfully called, an application download task is generated on the home screen. The task is
> the same as that created during download from AppGallery. Upon completion of the download and installation, the
> installation result is returned through the
> [EnterpriseAdminExtensionAbility.onMarketAppInstallResult](arkts-mdm-enterprise-enterpriseadminextensionability-enterpriseadminextensionability-c.md#onmarketappinstallresult)
> callback.

**Since:** 22

**Required permissions:** ohos.permission.ENTERPRISE_INSTALL_BUNDLE

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| bundleNames | Array & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [9201002](../errorcode-enterpriseDeviceManager.md#9201002-failed-to-install-the-enterprise-application) |
| [201](../../errorcode-universal.md#201-permission-denied) |
