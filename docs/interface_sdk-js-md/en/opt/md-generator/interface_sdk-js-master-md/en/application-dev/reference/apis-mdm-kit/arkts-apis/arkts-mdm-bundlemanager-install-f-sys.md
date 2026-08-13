# install (System API)

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.MDMKit';
```

## install

```TypeScript
function install(admin: Want, hapFilePaths: Array<string>, callback: AsyncCallback<void>): void
```

Installs specified applications. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [install](arkts-mdm-bundlemanager-install-f.md#install)(admin: Want, hapFilePaths: Array&lt;string&gt;, installParam?: InstallParam)

**Required permissions:** ohos.permission.ENTERPRISE_INSTALL_BUNDLE

**Model restriction:** This API can be used only in the stage model.

<!--Device-bundleManager-function install(admin: Want, hapFilePaths: Array<string>, callback: AsyncCallback<void>): void--><!--Device-bundleManager-function install(admin: Want, hapFilePaths: Array<string>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| hapFilePaths | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
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

**Substitutes:** [install](arkts-mdm-bundlemanager-install-f.md#install)(admin: Want, hapFilePaths: Array&lt;string&gt;, installParam?: InstallParam)

**Required permissions:** ohos.permission.ENTERPRISE_INSTALL_BUNDLE

**Model restriction:** This API can be used only in the stage model.

<!--Device-bundleManager-function install(admin: Want, hapFilePaths: Array<string>, installParam: InstallParam, callback: AsyncCallback<void>): void--><!--Device-bundleManager-function install(admin: Want, hapFilePaths: Array<string>, installParam: InstallParam, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| hapFilePaths | Array & lt;string & gt; | Yes |
| installParam | [InstallParam](arkts-mdm-bundlemanager-installparam-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
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
