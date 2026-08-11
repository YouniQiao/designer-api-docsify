# install

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.MDMKit';
```

## install

```TypeScript
function install(admin: Want, hapFilePaths: Array<string>, callback: AsyncCallback<void>): void
```

Installs specified applications. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [bundleManager.install](arkts-mdm-bundlemanager-install-f.md#install)(admin:

**Required permissions:** ohos.permission.ENTERPRISE_INSTALL_BUNDLE

**Model restriction:** This API can be used only in the stage model.

<!--Device-bundleManager-function install(admin: Want, hapFilePaths: Array<string>, callback: AsyncCallback<void>): void--><!--Device-bundleManager-function install(admin: Want, hapFilePaths: Array<string>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| hapFilePaths | Array&lt;string&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [9201002](../errorcode-enterpriseDeviceManager.md#9201002-failed-to-install-the-enterprise-application) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { bundleManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let hapFilePaths: Array<string> = ['/data/storage/el2/base/haps/entry/testinstall/ExtensionTest.hap'];

bundleManager.install(wantTemp, hapFilePaths, (err) => {
  if (err) {
    console.error(`Failed to install bundles. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in installing bundles');
});
```


## install

```TypeScript
function install(admin: Want, hapFilePaths: Array<string>, installParam: InstallParam, callback: AsyncCallback<void>): void
```

Installs applications with specified parameters. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [bundleManager.install](arkts-mdm-bundlemanager-install-f.md#install)(admin:

**Required permissions:** ohos.permission.ENTERPRISE_INSTALL_BUNDLE

**Model restriction:** This API can be used only in the stage model.

<!--Device-bundleManager-function install(admin: Want, hapFilePaths: Array<string>, installParam: InstallParam, callback: AsyncCallback<void>): void--><!--Device-bundleManager-function install(admin: Want, hapFilePaths: Array<string>, installParam: InstallParam, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| hapFilePaths | Array&lt;string&gt; | Yes |
| installParam | [InstallParam](arkts-mdm-bundlemanager-installparam-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [9201002](../errorcode-enterpriseDeviceManager.md#9201002-failed-to-install-the-enterprise-application) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { bundleManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let hapFilePaths: Array<string> = ['/data/storage/el2/base/haps/entry/testinstall/ExtensionTest.hap'];
let installParam: bundleManager.InstallParam = {
  userId: 100,
  installFlag: 1,
};

bundleManager.install(wantTemp, hapFilePaths, installParam, (err) => {
  if (err) {
    console.error(`Failed to install bundles. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in installing bundles');
});
```


## install

```TypeScript
function install(admin: Want, hapFilePaths: Array<string>, installParam?: InstallParam): Promise<void>
```

Installs specified applications. This API uses a promise to return the result.

This API can be used to install only applications of the **enterprise_mdm** (MDM application) or  
**enterprise_normal** (common enterprise application) distribution type. You can call the  
[getBundleInfoForSelf](../../apis-ability-kit/arkts-apis/arkts-ability-bundlemanager-getbundleinfoforself-f.md/arkts-ability-bundlemanager-getbundleinfoforself-f.md#getbundleinfoforself) API to query the  
[BundleInfo](arkts-mdm-bundlemanager-bundleinfo-i.md) of an application, where **BundleInfo.appInfo.appDistributionType**indicates the distribution type. Since API version 26.0.0, you are advised to use  
[installForResult](arkts-mdm-bundlemanager-installforresult-f.md#installforresult) to obtain more detailed error code return values.

> **NOTE：**
> 
> This API is time-consuming. Subsequent calls to other synchronous APIs in the application main thread must wait
> for the asynchronous return of this API.

**Since:** 12

**Required permissions:** ohos.permission.ENTERPRISE_INSTALL_BUNDLE

**Model restriction:** This API can be used only in the stage model.

<!--Device-bundleManager-function install(admin: Want, hapFilePaths: Array<string>, installParam?: InstallParam): Promise<void>--><!--Device-bundleManager-function install(admin: Want, hapFilePaths: Array<string>, installParam?: InstallParam): Promise<void>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| hapFilePaths | Array&lt;string&gt; | Yes |
| installParam | [InstallParam](arkts-mdm-bundlemanager-installparam-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [9201002](../errorcode-enterpriseDeviceManager.md#9201002-failed-to-install-the-enterprise-application) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { bundleManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Install the application for the current user.
let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let hapFilePaths: Array<string> = ['/data/storage/el2/base/haps/entry/testinstall/ExtensionTest.hap'];

bundleManager.install(wantTemp, hapFilePaths).then(() => {
  console.info('Succeeded in installing bundles.');
}).catch((err: BusinessError) => {
  console.error(`Failed to install bundles. Code is ${err.code}, message is ${err.message}`);
});
```

```TypeScript
import { bundleManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Install the application for all users.
let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let hapFilePaths: Array<string> = ['/data/storage/el2/base/haps/entry/testinstall/ExtensionTest.hap'];
const params: Record<string, string> = {
  'ohos.bms.param.enterpriseForAllUser': 'true'
};
let installParam: bundleManager.InstallParam = {
  // Replace with actual values.
  userId: 100,
  installFlag: 0,
  parameters: params
};
bundleManager.install(wantTemp, hapFilePaths, installParam).then(() => {
  console.info('Succeeded in installing bundles.');
}).catch((err: BusinessError) => {
  console.error(`Failed to install bundles. Code is ${err.code}, message is ${err.message}`);
});
```
