# installForResult

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.MDMKit';
```

## installForResult

```TypeScript
function installForResult(admin: Want, hapFilePaths: Array<string>, installParam?: InstallParam): Promise<void>
```

Installs the application bundle in the specified path and returns the installation result. This API uses a promise to return the result.

This API can be used to install only applications of the **enterprise_mdm** (MDM application) or  
**enterprise_normal** (common enterprise application) distribution type. You can call the  
[getBundleInfoForSelf](../../apis-ability-kit/arkts-apis/arkts-ability-bundlemanager-getbundleinfoforself-f.md#getBundleInfoForSelf) API to query the  
[BundleInfo](./bundleManager/BundleInfo) of an application, where **BundleInfo.appInfo.appDistributionType**indicates the distribution type.

> **NOTE：**
> 
> This API is time-consuming. Subsequent calls to other synchronous APIs in the application main thread must wait
> for the asynchronous return of this API.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_INSTALL_BUNDLE

**Model restriction:** This API can be used only in the stage model.

<!--Device-bundleManager-function installForResult(admin: Want, hapFilePaths: Array<string>, installParam?: InstallParam): Promise<void>--><!--Device-bundleManager-function installForResult(admin: Want, hapFilePaths: Array<string>, installParam?: InstallParam): Promise<void>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| hapFilePaths | Array & lt;string & gt; | Yes |
| installParam | [InstallParam](arkts-mdm-bundlemanager-installparam-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [9201036](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201036-app-installation-failed-due-to-incorrect-data-proxy-uri) |
| [9201037](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201037-app-installation-failed-due-to-incorrect-data-proxy-permission-configuration) |
| [9201038](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201038-application-installation-failed-due-to-code-signature-verification-failure) |
| [9201039](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201039-application-installation-failed-due-to-enterprise-device-verification-failure) |
| [9201032](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201032-specified-user-does-not-exist) |
| [9201033](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201033-application-installation-failed-due-to-overlay-check-failure) |
| [9201002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201002-failed-to-install-the-enterprise-application) |
| [9201034](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201034-application-installation-failed-due-to-lack-of-required-permissions-in-the-hsp) |
| [9201035](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201035-application-installation-failed-because-crossapplication-shared-library-installation-is-not-allowed) |
| [9201028](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201028-application-installation-failed-due-to-unsupported-isolationmode-configuration) |
| [9201029](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201029-application-installation-failed-due-to-outdated-hap-version) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [9201030](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201030-application-installation-failed-because-versioncode-is-not-greater-than-the-current-version) |
| [9201031](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201031-application-installation-failed-because-the-dependent-module-does-not-exist) |
| [9201024](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201024-application-installation-failed-due-to-hap-parsing-failure) |
| [9200001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9201025](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201025-application-installation-failed-due-to-hap-signature-verification-failure) |
| [9200002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9201026](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201026-application-installation-failed-due-to-an-invalid-hap-path-or-an-extralarge-hap) |
| [9201027](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201027-installation-failed-due-to-inconsistent-hap-configuration-information) |
| [9201022](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201022-application-installation-failure-due-to-insufficient-system-disk-space) |
| [9201023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201023-application-installation-failure-due-to-prohibition-by-enterprise-device-management) |
