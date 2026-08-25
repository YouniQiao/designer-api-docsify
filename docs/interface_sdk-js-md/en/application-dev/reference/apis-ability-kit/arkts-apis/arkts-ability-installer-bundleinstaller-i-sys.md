# BundleInstaller (System API)

Bundle installer interface, include install uninstall recover.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { installer } from '@kit.AbilityKit';
```

## addExtResource

```TypeScript
addExtResource(bundleName: string, filePaths: Array<string>): Promise<void>
```

Adds extended resources based on the specified bundle name and HSP file path. This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| filePaths | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700301](../errorcode-bundle.md#17700301-failed-to-add-extended-resources) |

**Examples**

```TypeScript
import { installer } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName : string = 'com.ohos.demo';
let filePaths : Array<string> = ['/data/storage/el2/base/a.hsp'];
try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.addExtResource(bundleName, filePaths).then((data) => {
            hilog.info(0x0000, 'testTag', 'addExtResource successfully');
        }).catch((err: BusinessError) => {
            hilog.error(0x0000, 'testTag', 'addExtResource failed. Cause: %{public}s', err.message);
        });
    }).catch((error: BusinessError) => {
        console.error('getBundleInstaller failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

## createAppClone

ArkTS-Dyn:
```TypeScript
createAppClone(bundleName: string, createAppCloneParam?: CreateAppCloneParam): Promise<number>
```

ArkTS-Sta:
```TypeScript
createAppClone(bundleName: string, createAppCloneParam?: CreateAppCloneParam): Promise<int>
```

Creates an application clone. This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_CLONE_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| createAppCloneParam | [CreateAppCloneParam](arkts-ability-installer-createappcloneparam-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| ArkTS-Dyn: Promise & lt;number & gt;<br>ArkTS-Sta：Promise & lt;int & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700061](../errorcode-bundle.md#17700061-appindex-for-a-clone-is-invalid) |
| [17700069](../errorcode-bundle.md#17700069-application-clone-is-not-supported) |

**Examples**

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = 'com.ohos.camera';
let createAppCloneParam: installer.CreateAppCloneParam = {
    userId: 100,
    appIndex: 1,
};

try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.createAppClone(bundleName, createAppCloneParam)
            .then(() => {
                console.info('createAppClone successfully.');
        }).catch((error: BusinessError) => {
            console.error('createAppClone failed:' + error.message);
        });
    }).catch((error: BusinessError) => {
        console.error('getBundleInstaller failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

## destroyAppClone

```TypeScript
destroyAppClone(bundleName: string, appIndex: number, userId?: number): Promise<void>
```

Destroys an application clone. This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Required permissions:** ohos.permission.UNINSTALL_CLONE_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| appIndex | number | Yes |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700061](../errorcode-bundle.md#17700061-appindex-for-a-clone-is-invalid) |

**Examples**

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = 'com.ohos.camera';
let index = 1;
let userId = 100;

try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.destroyAppClone(bundleName, index, userId)
            .then(() => {
                console.info('destroyAppClone successfully.');
        }).catch((error: BusinessError) => {
            console.error('destroyAppClone failed:' + error.message);
        });
    }).catch((error: BusinessError) => {
        console.error('getBundleInstaller failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = 'com.ohos.camera';
let index = 1;
let userId = 100;
let key = 'ohos.bms.param.verifyUninstallRule';
let value = 'false';
let item: installer.Parameters = {key, value};
let destroyAppCloneOpt: installer.DestroyAppCloneParam = {
    userId: userId,
    parameters: [item]
};


try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.destroyAppClone(bundleName, index, destroyAppCloneOpt)
            .then(() => {
                console.info('destroyAppClone successfully.');
        }).catch((error: BusinessError) => {
            console.error('destroyAppClone failed:' + error.message);
        });
    }).catch((error: BusinessError) => {
        console.error('getBundleInstaller failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

## destroyAppClone

```TypeScript
destroyAppClone(bundleName: string, appIndex: number, destroyAppCloneParam?: DestroyAppCloneParam): Promise<void>
```

Destroys an application clone. This API uses a promise to return the result.

**Since:** 15

**ArkTS mode:** Supports only ArkTS-Dyn, since version 15.

**Required permissions:** ohos.permission.UNINSTALL_CLONE_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| appIndex | number | Yes |
| destroyAppCloneParam | [DestroyAppCloneParam](arkts-ability-installer-destroyappcloneparam-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700061](../errorcode-bundle.md#17700061-appindex-for-a-clone-is-invalid) |
| [17700062](../errorcode-bundle.md#17700062-failed-to-uninstall-an-application-configured-with-an-uninstallation-disposed-rule) |

**Examples**

See [destroyAppClone](#destroyappclone)

## destroyAppClone

```TypeScript
destroyAppClone(bundleName: string, appIndex: int, options?: int | DestroyAppCloneParam): Promise<void>
```

Destroy clone instance for an application.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.UNINSTALL_CLONE_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| appIndex | int | Yes |
| options | int \| [DestroyAppCloneParam](arkts-ability-installer-destroyappcloneparam-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700061](../errorcode-bundle.md#17700061-appindex-for-a-clone-is-invalid) |
| [17700062](../errorcode-bundle.md#17700062-failed-to-uninstall-an-application-configured-with-an-uninstallation-disposed-rule) |

**Examples**

See [destroyAppClone](#destroyappclone)

## install

```TypeScript
install(hapFilePaths: Array<string>, installParam: InstallParam, callback: AsyncCallback<void>): void
```

Installs an application. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> To install applications of different distribution types, the appropriate permissions must be requested. For
> details on distribution types, see the **appDistributionType** field in
> [ApplicationInfo](arkts-ability-applicationinfo-i.md).

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 23+: ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE or ohos.permission.INSTALL_INTERNALTESTING_BUNDLE or (ohos.permission.INSTALL_BUNDLE and ohos.permission.INSTALL_ALLOW_DOWNGRADE)
- API version 13 - 22: ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE or ohos.permission.INSTALL_INTERNALTESTING_BUNDLE
- API version 10 - 12: ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE
- API version 9: ohos.permission.INSTALL_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hapFilePaths | Array & lt;string & gt; | Yes |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700010](../errorcode-bundle.md#17700010-bundle-installation-failure-due-to-file-parsing-failure) |
| [17700011](../errorcode-bundle.md#17700011-bundle-installation-failure-due-to-signature-verification-failure) |
| [17700012](../errorcode-bundle.md#17700012-bundle-installation-failure-due-to-invalid-file-path-or-too-large-file) |
| [17700015](../errorcode-bundle.md#17700015-bundle-installation-failure-due-to-different-configuration-information-of-multiple-haps) |
| [17700016](../errorcode-bundle.md#17700016-bundle-installation-failure-due-to-insufficient-system-disk-space) |
| [17700017](../errorcode-bundle.md#17700017-bundle-installation-failure-because-the-version-to-install-is-too-earlier) |
| [17700018](../errorcode-bundle.md#17700018-bundle-installation-failure-because-the-dependent-module-does-not-exist) |
| [17700031](../errorcode-bundle.md#17700031-hap-installation-fails-due-to-overlay-feature-verification-failure) |
| [17700036](../errorcode-bundle.md#17700036-failure-in-installing-the-shared-library-because-of-no-allowappsharelibrary-privilege) |
| [17700039](../errorcode-bundle.md#17700039-failure-in-installing-an-inter-application-shared-library) |
| [17700041](../errorcode-bundle.md#17700041-application-installation-is-not-allowed-by-enterprise-device-management) |
| [17700042](../errorcode-bundle.md#17700042-incorrect-uri-in-the-data-proxy) |
| [17700043](../errorcode-bundle.md#17700043-incorrect-permission-configuration-in-the-data-proxy) |
| [17700044](../errorcode-bundle.md#17700044-field-isolationmode-in-the-hap-conflicts-with-the-device-isolation-mode) |
| [17700047](../errorcode-bundle.md#17700047-application-version-to-be-updated-is-not-later-than-the-current-version) |
| [17700048](../errorcode-bundle.md#17700048-code-signature-verification-failure) |
| [17700050](../errorcode-bundle.md#17700050-installation-of-enterprise-mdm-applications-and-standard-enterprise-applications-not-allowed) |
| [17700052](../errorcode-bundle.md#17700052-installation-of-debugging-applications-allowed-only-in-developer-mode) |
| [17700054](../errorcode-bundle.md#17700054-bundle-installation-failure-due-to-permission-verification-failure) |
| [17700058](../errorcode-bundle.md#17700058-specified-application-cannot-be-installed-on-this-device-or-by-this-user) |
| [17700066](../errorcode-bundle.md#17700066-failed-to-install-the-native-software-package) |
| [17700073](../errorcode-bundle.md#17700073-installation-failure-caused-by-an-application-with-the-same-bundle-name-but-different-signature-information) |
| [17700077](../errorcode-bundle.md#17700077-application-installation-fails-but-preinstallation-is-successful) |
| [17700076](../errorcode-bundle.md#17700076-application-installation-failure-due-to-unsupported-distribution-type-in-the-signing-certificate-profile) |

**Examples**

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let hapFilePaths = ['/data/storage/el2/base/haps/entry/files/'];
let installParam: installer.InstallParam = {
    userId: 100,
    isKeepData: false,
    installFlag: 1,
};

try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.install(hapFilePaths, installParam, (err: BusinessError) => {
            if (err) {
                console.error('install failed:' + err.message);
            } else {
                console.info('install successfully.');
            }
        });
    }).catch((error: BusinessError) => {
        console.error('getBundleInstaller failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let hapFilePaths = ['/data/storage/el2/base/haps/entry/files/'];

try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.install(hapFilePaths, (err: BusinessError) => {
            if (err) {
                console.error('install failed:' + err.message);
            } else {
                console.info('install successfully.');
            }
        });
    }).catch((error: BusinessError) => {
        console.error('getBundleInstaller failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let hapFilePaths = ['/data/storage/el2/base/haps/entry/files/'];
let installParam: installer.InstallParam = {
    userId: 100,
    isKeepData: false,
    installFlag: 1,
};

try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.install(hapFilePaths, installParam)
            .then((data: void) => {
                console.info('install successfully: ' + JSON.stringify(data));
        }).catch((error: BusinessError) => {
            console.error('install failed:' + error.message);
        });
    }).catch((error: BusinessError) => {
        console.error('getBundleInstaller failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

## install

```TypeScript
install(hapFilePaths: Array<string>, callback: AsyncCallback<void>): void
```

Installs an application. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> To install applications of different distribution types, the appropriate permissions must be requested. For
> details on distribution types, see the **appDistributionType** field in
> [ApplicationInfo](arkts-ability-applicationinfo-i.md).

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 23+: ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE or ohos.permission.INSTALL_INTERNALTESTING_BUNDLE or (ohos.permission.INSTALL_BUNDLE and ohos.permission.INSTALL_ALLOW_DOWNGRADE)
- API version 13 - 22: ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE or ohos.permission.INSTALL_INTERNALTESTING_BUNDLE
- API version 10 - 12: ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE
- API version 9: ohos.permission.INSTALL_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hapFilePaths | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700010](../errorcode-bundle.md#17700010-bundle-installation-failure-due-to-file-parsing-failure) |
| [17700011](../errorcode-bundle.md#17700011-bundle-installation-failure-due-to-signature-verification-failure) |
| [17700012](../errorcode-bundle.md#17700012-bundle-installation-failure-due-to-invalid-file-path-or-too-large-file) |
| [17700015](../errorcode-bundle.md#17700015-bundle-installation-failure-due-to-different-configuration-information-of-multiple-haps) |
| [17700016](../errorcode-bundle.md#17700016-bundle-installation-failure-due-to-insufficient-system-disk-space) |
| [17700017](../errorcode-bundle.md#17700017-bundle-installation-failure-because-the-version-to-install-is-too-earlier) |
| [17700018](../errorcode-bundle.md#17700018-bundle-installation-failure-because-the-dependent-module-does-not-exist) |
| [17700031](../errorcode-bundle.md#17700031-hap-installation-fails-due-to-overlay-feature-verification-failure) |
| [17700036](../errorcode-bundle.md#17700036-failure-in-installing-the-shared-library-because-of-no-allowappsharelibrary-privilege) |
| [17700039](../errorcode-bundle.md#17700039-failure-in-installing-an-inter-application-shared-library) |
| [17700041](../errorcode-bundle.md#17700041-application-installation-is-not-allowed-by-enterprise-device-management) |
| [17700042](../errorcode-bundle.md#17700042-incorrect-uri-in-the-data-proxy) |
| [17700043](../errorcode-bundle.md#17700043-incorrect-permission-configuration-in-the-data-proxy) |
| [17700044](../errorcode-bundle.md#17700044-field-isolationmode-in-the-hap-conflicts-with-the-device-isolation-mode) |
| [17700047](../errorcode-bundle.md#17700047-application-version-to-be-updated-is-not-later-than-the-current-version) |
| [17700048](../errorcode-bundle.md#17700048-code-signature-verification-failure) |
| [17700050](../errorcode-bundle.md#17700050-installation-of-enterprise-mdm-applications-and-standard-enterprise-applications-not-allowed) |
| [17700052](../errorcode-bundle.md#17700052-installation-of-debugging-applications-allowed-only-in-developer-mode) |
| [17700054](../errorcode-bundle.md#17700054-bundle-installation-failure-due-to-permission-verification-failure) |
| [17700058](../errorcode-bundle.md#17700058-specified-application-cannot-be-installed-on-this-device-or-by-this-user) |
| [17700066](../errorcode-bundle.md#17700066-failed-to-install-the-native-software-package) |
| [17700073](../errorcode-bundle.md#17700073-installation-failure-caused-by-an-application-with-the-same-bundle-name-but-different-signature-information) |
| [17700077](../errorcode-bundle.md#17700077-application-installation-fails-but-preinstallation-is-successful) |
| [17700076](../errorcode-bundle.md#17700076-application-installation-failure-due-to-unsupported-distribution-type-in-the-signing-certificate-profile) |

**Examples**

See [install](#install)

## install

```TypeScript
install(hapFilePaths: Array<string>, installParam?: InstallParam): Promise<void>
```

Installs an application. This API uses a promise to return the result.

> **NOTE：**&gt;
> To install applications of different distribution types, the appropriate permissions must be requested. For
> details on distribution types, see the **appDistributionType** field in
> [ApplicationInfo](arkts-ability-applicationinfo-i.md).

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 23+: ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE or ohos.permission.INSTALL_INTERNALTESTING_BUNDLE or (ohos.permission.INSTALL_BUNDLE and ohos.permission.INSTALL_ALLOW_DOWNGRADE)
- API version 13 - 22: ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE or ohos.permission.INSTALL_INTERNALTESTING_BUNDLE
- API version 10 - 12: ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE
- API version 9: ohos.permission.INSTALL_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hapFilePaths | Array & lt;string & gt; | Yes |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700010](../errorcode-bundle.md#17700010-bundle-installation-failure-due-to-file-parsing-failure) |
| [17700011](../errorcode-bundle.md#17700011-bundle-installation-failure-due-to-signature-verification-failure) |
| [17700012](../errorcode-bundle.md#17700012-bundle-installation-failure-due-to-invalid-file-path-or-too-large-file) |
| [17700015](../errorcode-bundle.md#17700015-bundle-installation-failure-due-to-different-configuration-information-of-multiple-haps) |
| [17700016](../errorcode-bundle.md#17700016-bundle-installation-failure-due-to-insufficient-system-disk-space) |
| [17700017](../errorcode-bundle.md#17700017-bundle-installation-failure-because-the-version-to-install-is-too-earlier) |
| [17700018](../errorcode-bundle.md#17700018-bundle-installation-failure-because-the-dependent-module-does-not-exist) |
| [17700031](../errorcode-bundle.md#17700031-hap-installation-fails-due-to-overlay-feature-verification-failure) |
| [17700036](../errorcode-bundle.md#17700036-failure-in-installing-the-shared-library-because-of-no-allowappsharelibrary-privilege) |
| [17700039](../errorcode-bundle.md#17700039-failure-in-installing-an-inter-application-shared-library) |
| [17700041](../errorcode-bundle.md#17700041-application-installation-is-not-allowed-by-enterprise-device-management) |
| [17700042](../errorcode-bundle.md#17700042-incorrect-uri-in-the-data-proxy) |
| [17700043](../errorcode-bundle.md#17700043-incorrect-permission-configuration-in-the-data-proxy) |
| [17700044](../errorcode-bundle.md#17700044-field-isolationmode-in-the-hap-conflicts-with-the-device-isolation-mode) |
| [17700047](../errorcode-bundle.md#17700047-application-version-to-be-updated-is-not-later-than-the-current-version) |
| [17700048](../errorcode-bundle.md#17700048-code-signature-verification-failure) |
| [17700050](../errorcode-bundle.md#17700050-installation-of-enterprise-mdm-applications-and-standard-enterprise-applications-not-allowed) |
| [17700052](../errorcode-bundle.md#17700052-installation-of-debugging-applications-allowed-only-in-developer-mode) |
| [17700054](../errorcode-bundle.md#17700054-bundle-installation-failure-due-to-permission-verification-failure) |
| [17700058](../errorcode-bundle.md#17700058-specified-application-cannot-be-installed-on-this-device-or-by-this-user) |
| [17700066](../errorcode-bundle.md#17700066-failed-to-install-the-native-software-package) |
| [17700073](../errorcode-bundle.md#17700073-installation-failure-caused-by-an-application-with-the-same-bundle-name-but-different-signature-information) |
| [17700077](../errorcode-bundle.md#17700077-application-installation-fails-but-preinstallation-is-successful) |
| [17700076](../errorcode-bundle.md#17700076-application-installation-failure-due-to-unsupported-distribution-type-in-the-signing-certificate-profile) |

**Examples**

See [install](#install)

## installPlugin

```TypeScript
installPlugin(hostBundleName: string, pluginFilePaths: Array<string>, pluginParam?: PluginParam): Promise<void>
```

Installs a plugin for an application. This API uses a promise to return the result.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_PLUGIN_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [hostBundleName](../../apis-form-kit/arkts-apis/arkts-form-forminfo-runningforminfo-i-sys.md) | string | Yes |
| pluginFilePaths | Array & lt;string & gt; | Yes |
| pluginParam | [PluginParam](arkts-ability-installer-pluginparam-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700010](../errorcode-bundle.md#17700010-bundle-installation-failure-due-to-file-parsing-failure) |
| [17700011](../errorcode-bundle.md#17700011-bundle-installation-failure-due-to-signature-verification-failure) |
| [17700012](../errorcode-bundle.md#17700012-bundle-installation-failure-due-to-invalid-file-path-or-too-large-file) |
| [17700015](../errorcode-bundle.md#17700015-bundle-installation-failure-due-to-different-configuration-information-of-multiple-haps) |
| [17700016](../errorcode-bundle.md#17700016-bundle-installation-failure-due-to-insufficient-system-disk-space) |
| [17700017](../errorcode-bundle.md#17700017-bundle-installation-failure-because-the-version-to-install-is-too-earlier) |
| [17700048](../errorcode-bundle.md#17700048-code-signature-verification-failure) |
| [17700052](../errorcode-bundle.md#17700052-installation-of-debugging-applications-allowed-only-in-developer-mode) |
| [17700073](../errorcode-bundle.md#17700073-installation-failure-caused-by-an-application-with-the-same-bundle-name-but-different-signature-information) |
| [17700087](../errorcode-bundle.md#17700087-unsupported-plugin-installation) |
| [17700088](../errorcode-bundle.md#17700088-plugin-installation-failure-due-to-no-permission) |
| [17700089](../errorcode-bundle.md#17700089-plugin-installation-failure-because-of-plugin-id-parsing-failure) |
| [17700090](../errorcode-bundle.md#17700090-plugin-installation-failure-because-of-plugin-id-verification-failure) |
| [17700091](../errorcode-bundle.md#17700091-plugin-installation-failure-because-of-the-same-plugin-name-and-host-bundle-name) |

**Examples**

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let hostBundleName = 'com.example.application';
let pluginFilePaths = ['/data/bms_app_install/test.hsp'];
let pluginParam : installer.PluginParam = {
    userId : 100,
};

try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.installPlugin(hostBundleName, pluginFilePaths, pluginParam)
            .then(() => {
                console.info('installPlugin successfully.');
        }).catch((error: BusinessError) => {
            console.error('installPlugin failed:' + error.message);
        });
    }).catch((error: BusinessError) => {
        console.error('installPlugin failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

## installPreexistingApp

ArkTS-Dyn:
```TypeScript
installPreexistingApp(bundleName: string, userId?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
installPreexistingApp(bundleName: string, userId?: int): Promise<void>
```

Installs an application. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API does not support the installation of applications whose
> [distribution type of the application signing certificate](arkts-ability-applicationinfo-i.md)
> is set to **enterprise**, **enterprise_mdm**, or **enterprise_normal**.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| userId | ArkTS-Dyn: number<br>ArkTS-Sta：int | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700071](../errorcode-bundle.md#17700071-enterprise-applications-cannot-be-installed) |
| [17700058](../errorcode-bundle.md#17700058-specified-application-cannot-be-installed-on-this-device-or-by-this-user) |

**Examples**

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = 'com.ohos.camera';
let userId = 100;

try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.installPreexistingApp(bundleName, userId)
            .then(() => {
                console.info('installPreexistingApp successfully.');
        }).catch((error: BusinessError) => {
            console.error('installPreexistingApp failed:' + error.message);
        });
    }).catch((error: BusinessError) => {
        console.error('getBundleInstaller failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

## recover

```TypeScript
recover(bundleName: string, installParam: InstallParam, callback: AsyncCallback<void>): void
```

Rolls back an application to the initial installation state. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE or ohos.permission.RECOVER_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700073](../errorcode-bundle.md#17700073-installation-failure-caused-by-an-application-with-the-same-bundle-name-but-different-signature-information) |
| [17700058](../errorcode-bundle.md#17700058-specified-application-cannot-be-installed-on-this-device-or-by-this-user) |

**Examples**

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = 'com.ohos.demo';
let installParam: installer.InstallParam = {
    userId: 100,
    isKeepData: false,
    installFlag: 1
};

try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.recover(bundleName, installParam, (err: BusinessError) => {
            if (err) {
                console.error('recover failed:' + err.message);
            } else {
                console.info('recover successfully.');
            }
        });
    }).catch((error: BusinessError) => {
        console.error('getBundleInstaller failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = 'com.ohos.demo';

try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.recover(bundleName, (err: BusinessError) => {
            if (err) {
                console.error('recover failed:' + err.message);
            } else {
                console.info('recover successfully.');
            }
        });
    }).catch((error: BusinessError) => {
        console.error('getBundleInstaller failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = 'com.ohos.demo';
let installParam: installer.InstallParam = {
    userId: 100,
    isKeepData: false,
    installFlag: 1,
};

try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.recover(bundleName, installParam)
            .then((data: void) => {
                console.info('recover successfully: ' + JSON.stringify(data));
        }).catch((error: BusinessError) => {
            console.error('recover failed:' + error.message);
        });
    }).catch((error: BusinessError) => {
        console.error('getBundleInstaller failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

## recover

```TypeScript
recover(bundleName: string, callback: AsyncCallback<void>): void
```

Rolls back an application to the initial installation state. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE or ohos.permission.RECOVER_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700073](../errorcode-bundle.md#17700073-installation-failure-caused-by-an-application-with-the-same-bundle-name-but-different-signature-information) |
| [17700058](../errorcode-bundle.md#17700058-specified-application-cannot-be-installed-on-this-device-or-by-this-user) |

**Examples**

See [recover](#recover)

## recover

```TypeScript
recover(bundleName: string, installParam?: InstallParam): Promise<void>
```

Rolls back an application to the initial installation state. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE or ohos.permission.RECOVER_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700073](../errorcode-bundle.md#17700073-installation-failure-caused-by-an-application-with-the-same-bundle-name-but-different-signature-information) |
| [17700058](../errorcode-bundle.md#17700058-specified-application-cannot-be-installed-on-this-device-or-by-this-user) |

**Examples**

See [recover](#recover)

## removeExtResource

```TypeScript
removeExtResource(bundleName: string, moduleNames: Array<string>): Promise<void>
```

Removes extended resources based on the specified bundle name and module names. This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE or ohos.permission.UNINSTALL_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| moduleNames | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700302](../errorcode-bundle.md#17700302-failed-to-delete-extended-resources) |

**Examples**

```TypeScript
import { installer } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName : string = 'com.ohos.demo';
let moduleNames : Array<string> = ['moduleTest'];
try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.removeExtResource(bundleName, moduleNames).then((data) => {
            hilog.info(0x0000, 'testTag', 'removeExtResource successfully');
        }).catch((err: BusinessError) => {
            hilog.error(0x0000, 'testTag', 'removeExtResource failed. Cause: %{public}s', err.message);
        });
    }).catch((error: BusinessError) => {
        console.error('getBundleInstaller failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

## uninstall

```TypeScript
uninstall(bundleName: string, installParam: InstallParam, callback: AsyncCallback<void>): void
```

Uninstalls an application. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE or ohos.permission.UNINSTALL_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700020](../errorcode-bundle.md#17700020-failure-to-uninstall-preinstalled-applications) |
| [17700040](../errorcode-bundle.md#17700040-failure-in-uninstalling-an-inter-application-shared-library) |
| [17700045](../errorcode-bundle.md#17700045-application-uninstall-is-not-allowed-by-enterprise-device-management) |
| [17700067](../errorcode-bundle.md#17700067-failed-to-uninstall-the-native-software-package) |
| [17700060](../errorcode-bundle.md#17700060-specified-application-cannot-be-uninstalled) |
| [17700062](../errorcode-bundle.md#17700062-failed-to-uninstall-an-application-configured-with-an-uninstallation-disposed-rule) |

**Examples**

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = 'com.ohos.demo';
let installParam: installer.InstallParam = {
    userId: 100,
    isKeepData: false,
    installFlag: 1
};

try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.uninstall(bundleName, installParam, (err: BusinessError) => {
            if (err) {
                console.error('uninstall failed:' + err.message);
            } else {
                console.info('uninstall successfully.');
            }
        });
    }).catch((error: BusinessError) => {
        console.error('getBundleInstaller failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = 'com.ohos.demo';

try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.uninstall(bundleName, (err: BusinessError) => {
            if (err) {
                console.error('uninstall failed:' + err.message);
            } else {
                console.info('uninstall successfully.');
            }
        });
    }).catch((error: BusinessError) => {
        console.error('getBundleInstaller failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = 'com.ohos.demo';
let installParam: installer.InstallParam = {
    userId: 100,
    isKeepData: false,
    installFlag: 1,
};

try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.uninstall(bundleName, installParam)
            .then((data: void) => {
                console.info('uninstall successfully: ' + JSON.stringify(data));
        }).catch((error: BusinessError) => {
            console.error('uninstall failed:' + error.message);
        });
    }).catch((error: BusinessError) => {
        console.error('getBundleInstaller failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uninstallParam: installer.UninstallParam = {
    bundleName: "com.ohos.demo",
};

try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.uninstall(uninstallParam, (err: BusinessError) => {
            if (err) {
                console.error('uninstall failed:' + err.message);
            } else {
                console.info('uninstall successfully.');
            }
        });
    }).catch((error: BusinessError) => {
        console.error('getBundleInstaller failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uninstallParam: installer.UninstallParam = {
    bundleName: "com.ohos.demo",
};

try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.uninstall(uninstallParam, (err: BusinessError) => {
            if (err) {
                console.error('uninstall failed:' + err.message);
            } else {
                console.info('uninstall successfully.');
            }
        });
    }).catch((error: BusinessError) => {
        console.error('getBundleInstaller failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

## uninstall

```TypeScript
uninstall(bundleName: string, callback: AsyncCallback<void>): void
```

Uninstalls an application. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE or ohos.permission.UNINSTALL_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700020](../errorcode-bundle.md#17700020-failure-to-uninstall-preinstalled-applications) |
| [17700040](../errorcode-bundle.md#17700040-failure-in-uninstalling-an-inter-application-shared-library) |
| [17700045](../errorcode-bundle.md#17700045-application-uninstall-is-not-allowed-by-enterprise-device-management) |
| [17700067](../errorcode-bundle.md#17700067-failed-to-uninstall-the-native-software-package) |
| [17700060](../errorcode-bundle.md#17700060-specified-application-cannot-be-uninstalled) |

**Examples**

See [uninstall](#uninstall)

## uninstall

```TypeScript
uninstall(bundleName: string, installParam?: InstallParam): Promise<void>
```

Uninstalls an application. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE or ohos.permission.UNINSTALL_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700020](../errorcode-bundle.md#17700020-failure-to-uninstall-preinstalled-applications) |
| [17700040](../errorcode-bundle.md#17700040-failure-in-uninstalling-an-inter-application-shared-library) |
| [17700045](../errorcode-bundle.md#17700045-application-uninstall-is-not-allowed-by-enterprise-device-management) |
| [17700067](../errorcode-bundle.md#17700067-failed-to-uninstall-the-native-software-package) |
| [17700060](../errorcode-bundle.md#17700060-specified-application-cannot-be-uninstalled) |
| [17700062](../errorcode-bundle.md#17700062-failed-to-uninstall-an-application-configured-with-an-uninstallation-disposed-rule) |

**Examples**

See [uninstall](#uninstall)

## uninstall

```TypeScript
uninstall(uninstallParam: UninstallParam, callback: AsyncCallback<void>): void
```

Uninstalls a shared package. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE or ohos.permission.UNINSTALL_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uninstallParam | [UninstallParam](arkts-ability-installer-uninstallparam-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700020](../errorcode-bundle.md#17700020-failure-to-uninstall-preinstalled-applications) |
| [17700037](../errorcode-bundle.md#17700037-failure-in-uninstalling-the-shared-library-due-to-dependency) |
| [17700038](../errorcode-bundle.md#17700038-shared-library-to-uninstall-does-not-exist) |

**Examples**

See [uninstall](#uninstall)

## uninstall

```TypeScript
uninstall(uninstallParam: UninstallParam): Promise<void>
```

Uninstalls a shared package. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE or ohos.permission.UNINSTALL_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uninstallParam | [UninstallParam](arkts-ability-installer-uninstallparam-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700020](../errorcode-bundle.md#17700020-failure-to-uninstall-preinstalled-applications) |
| [17700037](../errorcode-bundle.md#17700037-failure-in-uninstalling-the-shared-library-due-to-dependency) |
| [17700038](../errorcode-bundle.md#17700038-shared-library-to-uninstall-does-not-exist) |

**Examples**

See [uninstall](#uninstall)

## uninstallNewPreinstalledApps

```TypeScript
uninstallNewPreinstalledApps(bundleNames: Array<string>): Promise<void>
```

Uninstall new preinstalled applications. Only supports uninstalling pre installed applications added during device OTA upgrade. Asynchronous execution of application uninstallation tasks, the interface return value only indicates successful interface invocation and does not return uninstallation results.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.UNINSTALL_BUNDLE

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleNames | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## uninstallPlugin

```TypeScript
uninstallPlugin(hostBundleName: string, pluginBundleName: string, pluginParam?: PluginParam): Promise<void>
```

Uninstalls a plugin for an application. This API uses a promise to return the result.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.UNINSTALL_PLUGIN_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [hostBundleName](../../apis-form-kit/arkts-apis/arkts-form-forminfo-runningforminfo-i-sys.md) | string | Yes |
| [pluginBundleName](arkts-ability-pluginbundleinfo-i.md) | string | Yes |
| pluginParam | [PluginParam](arkts-ability-installer-pluginparam-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700092](../errorcode-bundle.md#17700092-plugin-uninstall-failure-because-of-nonexistent-plugin-bundle-name) |

**Examples**

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let hostBundleName = 'com.example.application';
let pluginBundleName = 'com.ohos.pluginDemo';
let pluginParam : installer.PluginParam = {
    userId : 100,
};

try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.uninstallPlugin(hostBundleName, pluginBundleName, pluginParam)
            .then(() => {
                console.info('uninstallPlugin successfully.');
        }).catch((error: BusinessError) => {
            console.error('uninstallPlugin failed:' + error.message);
        });
    }).catch((error: BusinessError) => {
        console.error('uninstallPlugin failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

## uninstallUpdates

```TypeScript
uninstallUpdates(bundleName: string, installParam?: InstallParam): Promise<void>
```

Uninstalls and updates a preinstalled application and restores it to the initial installation status. This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE or ohos.permission.UNINSTALL_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
| [17700045](../errorcode-bundle.md#17700045-application-uninstall-is-not-allowed-by-enterprise-device-management) |
| [17700057](../errorcode-bundle.md#17700057-specified-application-is-not-a-preset-application) |
| [17700060](../errorcode-bundle.md#17700060-specified-application-cannot-be-uninstalled) |
| [17700067](../errorcode-bundle.md#17700067-failed-to-uninstall-the-native-software-package) |
| [17700073](../errorcode-bundle.md#17700073-installation-failure-caused-by-an-application-with-the-same-bundle-name-but-different-signature-information) |

**Examples**

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = 'com.ohos.camera';
let installParam: installer.InstallParam = {
    isKeepData: true,
    installFlag: 1,
};

try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.uninstallUpdates(bundleName, installParam)
            .then(() => {
                console.info('uninstallUpdates successfully.');
        }).catch((error: BusinessError) => {
            console.error('uninstallUpdates failed:' + error.message);
        });
    }).catch((error: BusinessError) => {
        console.error('getBundleInstaller failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

## updateBundleForSelf

```TypeScript
updateBundleForSelf(hapFilePaths: Array<string>, installParam: InstallParam, callback: AsyncCallback<void>): void
```

Updates the current bundle. This API can be called only by enterprise MDM applications on enterprise devices, and the HAPs in **hapFilePaths** must belong to the current application. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_SELF_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hapFilePaths | Array & lt;string & gt; | Yes |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700010](../errorcode-bundle.md#17700010-bundle-installation-failure-due-to-file-parsing-failure) |
| [17700011](../errorcode-bundle.md#17700011-bundle-installation-failure-due-to-signature-verification-failure) |
| [17700012](../errorcode-bundle.md#17700012-bundle-installation-failure-due-to-invalid-file-path-or-too-large-file) |
| [17700015](../errorcode-bundle.md#17700015-bundle-installation-failure-due-to-different-configuration-information-of-multiple-haps) |
| [17700016](../errorcode-bundle.md#17700016-bundle-installation-failure-due-to-insufficient-system-disk-space) |
| [17700017](../errorcode-bundle.md#17700017-bundle-installation-failure-because-the-version-to-install-is-too-earlier) |
| [17700018](../errorcode-bundle.md#17700018-bundle-installation-failure-because-the-dependent-module-does-not-exist) |
| [17700039](../errorcode-bundle.md#17700039-failure-in-installing-an-inter-application-shared-library) |
| [17700041](../errorcode-bundle.md#17700041-application-installation-is-not-allowed-by-enterprise-device-management) |
| [17700042](../errorcode-bundle.md#17700042-incorrect-uri-in-the-data-proxy) |
| [17700043](../errorcode-bundle.md#17700043-incorrect-permission-configuration-in-the-data-proxy) |
| [17700044](../errorcode-bundle.md#17700044-field-isolationmode-in-the-hap-conflicts-with-the-device-isolation-mode) |
| [17700047](../errorcode-bundle.md#17700047-application-version-to-be-updated-is-not-later-than-the-current-version) |
| [17700048](../errorcode-bundle.md#17700048-code-signature-verification-failure) |
| [17700049](../errorcode-bundle.md#17700049-update-failure-because-of-incorrect-bundle-name) |
| [17700050](../errorcode-bundle.md#17700050-installation-of-enterprise-mdm-applications-and-standard-enterprise-applications-not-allowed) |
| [17700051](../errorcode-bundle.md#17700051-hap-installation-failure-due-to-incorrect-distribution-type-in-the-signing-certificate-profile-of-the-caller) |

**Examples**

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let hapFilePaths = ['/data/storage/el2/base/haps/entry/files/'];
let installParam: installer.InstallParam = {
    userId: 100,
    isKeepData: false,
    installFlag: 1,
};

try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.updateBundleForSelf(hapFilePaths, installParam, (err: BusinessError) => {
            if (err) {
                console.error('updateBundleForSelf failed:' + err.message);
            } else {
                console.info('updateBundleForSelf successfully.');
            }
        });
    }).catch((error: BusinessError) => {
        console.error('getBundleInstaller failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let hapFilePaths = ['/data/storage/el2/base/haps/entry/files/'];

try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.updateBundleForSelf(hapFilePaths, (err: BusinessError) => {
            if (err) {
                console.error('updateBundleForSelf failed:' + err.message);
            } else {
                console.info('updateBundleForSelf successfully.');
            }
        });
    }).catch((error: BusinessError) => {
        console.error('getBundleInstaller failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

```TypeScript
import { installer } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let hapFilePaths = ['/data/storage/el2/base/haps/entry/files/'];
let installParam: installer.InstallParam = {
    userId: 100,
    isKeepData: false,
    installFlag: 1,
};

try {
    installer.getBundleInstaller().then((data: installer.BundleInstaller) => {
        data.updateBundleForSelf(hapFilePaths, installParam)
            .then((data: void) => {
                console.info('updateBundleForSelf successfully: ' + JSON.stringify(data));
        }).catch((error: BusinessError) => {
            console.error('updateBundleForSelf failed:' + error.message);
        });
    }).catch((error: BusinessError) => {
        console.error('getBundleInstaller failed. Cause: ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('getBundleInstaller failed. Cause: ' + message);
}
```

## updateBundleForSelf

```TypeScript
updateBundleForSelf(hapFilePaths: Array<string>, callback: AsyncCallback<void>): void
```

Updates the current bundle. This API can be called only by enterprise MDM applications on enterprise devices, and the HAPs in **hapFilePaths** must belong to the current application. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_SELF_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hapFilePaths | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700010](../errorcode-bundle.md#17700010-bundle-installation-failure-due-to-file-parsing-failure) |
| [17700011](../errorcode-bundle.md#17700011-bundle-installation-failure-due-to-signature-verification-failure) |
| [17700012](../errorcode-bundle.md#17700012-bundle-installation-failure-due-to-invalid-file-path-or-too-large-file) |
| [17700015](../errorcode-bundle.md#17700015-bundle-installation-failure-due-to-different-configuration-information-of-multiple-haps) |
| [17700016](../errorcode-bundle.md#17700016-bundle-installation-failure-due-to-insufficient-system-disk-space) |
| [17700017](../errorcode-bundle.md#17700017-bundle-installation-failure-because-the-version-to-install-is-too-earlier) |
| [17700018](../errorcode-bundle.md#17700018-bundle-installation-failure-because-the-dependent-module-does-not-exist) |
| [17700039](../errorcode-bundle.md#17700039-failure-in-installing-an-inter-application-shared-library) |
| [17700041](../errorcode-bundle.md#17700041-application-installation-is-not-allowed-by-enterprise-device-management) |
| [17700042](../errorcode-bundle.md#17700042-incorrect-uri-in-the-data-proxy) |
| [17700043](../errorcode-bundle.md#17700043-incorrect-permission-configuration-in-the-data-proxy) |
| [17700044](../errorcode-bundle.md#17700044-field-isolationmode-in-the-hap-conflicts-with-the-device-isolation-mode) |
| [17700047](../errorcode-bundle.md#17700047-application-version-to-be-updated-is-not-later-than-the-current-version) |
| [17700048](../errorcode-bundle.md#17700048-code-signature-verification-failure) |
| [17700049](../errorcode-bundle.md#17700049-update-failure-because-of-incorrect-bundle-name) |
| [17700050](../errorcode-bundle.md#17700050-installation-of-enterprise-mdm-applications-and-standard-enterprise-applications-not-allowed) |
| [17700051](../errorcode-bundle.md#17700051-hap-installation-failure-due-to-incorrect-distribution-type-in-the-signing-certificate-profile-of-the-caller) |

**Examples**

See [updateBundleForSelf](#updatebundleforself)

## updateBundleForSelf

```TypeScript
updateBundleForSelf(hapFilePaths: Array<string>, installParam?: InstallParam): Promise<void>
```

Updates the current bundle. This API can be called only by enterprise MDM applications on enterprise devices, and the HAPs in **hapFilePaths** must belong to the current application. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_SELF_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hapFilePaths | Array & lt;string & gt; | Yes |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700010](../errorcode-bundle.md#17700010-bundle-installation-failure-due-to-file-parsing-failure) |
| [17700011](../errorcode-bundle.md#17700011-bundle-installation-failure-due-to-signature-verification-failure) |
| [17700012](../errorcode-bundle.md#17700012-bundle-installation-failure-due-to-invalid-file-path-or-too-large-file) |
| [17700015](../errorcode-bundle.md#17700015-bundle-installation-failure-due-to-different-configuration-information-of-multiple-haps) |
| [17700016](../errorcode-bundle.md#17700016-bundle-installation-failure-due-to-insufficient-system-disk-space) |
| [17700017](../errorcode-bundle.md#17700017-bundle-installation-failure-because-the-version-to-install-is-too-earlier) |
| [17700018](../errorcode-bundle.md#17700018-bundle-installation-failure-because-the-dependent-module-does-not-exist) |
| [17700039](../errorcode-bundle.md#17700039-failure-in-installing-an-inter-application-shared-library) |
| [17700041](../errorcode-bundle.md#17700041-application-installation-is-not-allowed-by-enterprise-device-management) |
| [17700042](../errorcode-bundle.md#17700042-incorrect-uri-in-the-data-proxy) |
| [17700043](../errorcode-bundle.md#17700043-incorrect-permission-configuration-in-the-data-proxy) |
| [17700044](../errorcode-bundle.md#17700044-field-isolationmode-in-the-hap-conflicts-with-the-device-isolation-mode) |
| [17700047](../errorcode-bundle.md#17700047-application-version-to-be-updated-is-not-later-than-the-current-version) |
| [17700048](../errorcode-bundle.md#17700048-code-signature-verification-failure) |
| [17700049](../errorcode-bundle.md#17700049-update-failure-because-of-incorrect-bundle-name) |
| [17700050](../errorcode-bundle.md#17700050-installation-of-enterprise-mdm-applications-and-standard-enterprise-applications-not-allowed) |
| [17700051](../errorcode-bundle.md#17700051-hap-installation-failure-due-to-incorrect-distribution-type-in-the-signing-certificate-profile-of-the-caller) |

**Examples**

See [updateBundleForSelf](#updatebundleforself)
