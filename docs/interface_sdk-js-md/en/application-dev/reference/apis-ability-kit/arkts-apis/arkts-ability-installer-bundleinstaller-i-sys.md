# BundleInstaller (System API)

Bundle installer interface, include install uninstall recover.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-installer-interface BundleInstaller--><!--Device-installer-interface BundleInstaller-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { installer } from 'kits/@kit.AbilityKit';
```

## addExtResource

```TypeScript
addExtResource(bundleName: string, filePaths: Array<string>): Promise<void>
```

根据给定的bundleName和hsp文件路径添加扩展资源。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE

<!--Device-BundleInstaller-addExtResource(bundleName: string, filePaths: Array<string>): Promise<void>--><!--Device-BundleInstaller-addExtResource(bundleName: string, filePaths: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 要添加扩展资源的应用名称。 |
| filePaths | Array&lt;string&gt; | Yes | 要添加扩展资源的资源路径。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2 . Incorrect parameter types. |
| 17700301 | AddExtResource failed due to parse file failed. |
| 201 | Permission denied. |
| 202 | Permission denied, non-system app called system api. |
| 17700001 | The specified bundleName is not found. |

## Examples

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

创建应用分身。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_CLONE_BUNDLE

<!--Device-BundleInstaller-createAppClone(bundleName: string, createAppCloneParam?: CreateAppCloneParam): Promise<int>--><!--Device-BundleInstaller-createAppClone(bundleName: string, createAppCloneParam?: CreateAppCloneParam): Promise<int>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 待创建应用分身的包名。 |
| createAppCloneParam | [CreateAppCloneParam](arkts-ability-installer-createappcloneparam-i-sys.md) | No | 指定创建应用分身所需的其他参数，默认值：参照 [createAppCloneParam](arkts-ability-installer-createappcloneparam-i-sys.md)的默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象。返回创建的分身应用索引值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2 . Incorrect parameter types. |
| 17700061 | The appIndex is not in valid range or already exists. |
| 201 | Calling interface without permission 'ohos.permission.INSTALL_CLONE_BUNDLE'. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17700004 | The userId is invalid. |
| 17700069 | The app does not support the creation of an appClone instance. |
| 17700001 | The specified bundleName cannot be found or the bundle is not installed by the specified user. |

## Examples

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

删除应用分身。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.UNINSTALL_CLONE_BUNDLE

<!--Device-BundleInstaller-destroyAppClone(bundleName: string, appIndex: number, userId?: number): Promise<void>--><!--Device-BundleInstaller-destroyAppClone(bundleName: string, appIndex: number, userId?: number): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 待删除应用分身的包名。 |
| appIndex | number | Yes | 待删除应用分身的索引。 |
| userId | number | No | 待删除应用分身所属用户ID，可以通过 [getOsAccountLocalId接口](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) 获取。默认值：调用方所在用户。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2 . Incorrect parameter types. |
| 17700061 | AppIndex not in valid range. |
| 201 | Calling interface without permission 'ohos.permission.UNINSTALL_CLONE_BUNDLE'. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17700004 | The userId is invalid. |
| 17700001 | The specified bundleName cannot be found or the bundle is not installed by the specified user. |

## Examples

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

## destroyAppClone

```TypeScript
destroyAppClone(bundleName: string, appIndex: number, destroyAppCloneParam?: DestroyAppCloneParam): Promise<void>
```

删除应用分身。使用Promise异步回调。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Required permissions:** ohos.permission.UNINSTALL_CLONE_BUNDLE

<!--Device-BundleInstaller-destroyAppClone(bundleName: string, appIndex: number, destroyAppCloneParam?: DestroyAppCloneParam): Promise<void>--><!--Device-BundleInstaller-destroyAppClone(bundleName: string, appIndex: number, destroyAppCloneParam?: DestroyAppCloneParam): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 待删除应用分身的包名。 |
| appIndex | number | Yes | 待删除应用分身的索引。 |
| destroyAppCloneParam | [DestroyAppCloneParam](arkts-ability-installer-destroyappcloneparam-i-sys.md) | No | 指定删除应用分身所需的其他参数，默认值：参照 [DestroyAppCloneParam](arkts-ability-installer-destroyappcloneparam-i-sys.md)的默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17700062 | Failed to uninstall the app because the app is locked. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2 . Incorrect parameter types. |
| 17700061 | AppIndex not in valid range. |
| 201 | Calling interface without permission 'ohos.permission.UNINSTALL_CLONE_BUNDLE'. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17700004 | The userId is invalid. |
| 17700001 | The specified bundleName cannot be found or the bundle is not installed by the specified user. |

## Examples

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
destroyAppClone(bundleName: string, appIndex: int, options?: int | DestroyAppCloneParam): Promise<void>
```

Destroy clone instance for an application.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.UNINSTALL_CLONE_BUNDLE

<!--Device-BundleInstaller-destroyAppClone(bundleName: string, appIndex: int, options?: int | DestroyAppCloneParam): Promise<void>--><!--Device-BundleInstaller-destroyAppClone(bundleName: string, appIndex: int, options?: int | DestroyAppCloneParam): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Indicates the bundleName of clone app. |
| appIndex | int | Yes | Indicates the clone application's index. |
| options | int \| DestroyAppCloneParam | No | Indicates other parameters required for the uninstallation. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17700062 | Failed to uninstall the app because the app is locked. |
| 17700061 | AppIndex not in valid range. |
| 201 | Calling interface without permission 'ohos.permission.UNINSTALL_CLONE_BUNDLE'. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17700004 | The userId is invalid. |
| 17700001 | The specified bundleName cannot be found or the bundle is not installed by the specified user. |

## install

```TypeScript
install(hapFilePaths: Array<string>, installParam: InstallParam, callback: AsyncCallback<void>): void
```

安装指定应用。使用callback异步回调。

> **说明：**
> 
> 安装不同分发类型的应用需要申请相应的权限，分发类型可以参考[ApplicationInfo](arkts-ability-applicationinfo-i.md)中的
> appDistributionType字段说明。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 23+: ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE or ohos.permission.INSTALL_INTERNALTESTING_BUNDLE or (ohos.permission.INSTALL_BUNDLE and ohos.permission.INSTALL_ALLOW_DOWNGRADE)
- API version 13 - 22: ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE or ohos.permission.INSTALL_INTERNALTESTING_BUNDLE
- API version 10 - 12: ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE
- API version 9: ohos.permission.INSTALL_BUNDLE

<!--Device-BundleInstaller-install(hapFilePaths: Array<string>, installParam: InstallParam, callback: AsyncCallback<void>): void--><!--Device-BundleInstaller-install(hapFilePaths: Array<string>, installParam: InstallParam, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hapFilePaths | Array&lt;string&gt; | Yes | 存储应用程序包的路径。路径应该是当前应用程序中存放HAP的数据目录。当传入的路径是一个目录时， 该目录下只能放同一个应用的HAP，且这些HAP的签 名需要保持一致。 |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | Yes | 指定安装所需的其他参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | [回调函数](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md/arkts-basicservices-base-asynccallback-i.md)，安装应用成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17700047 | Failed to install the HAP because the VersionCode to be updated is not greater than the current VersionCode. |
| 17700044 | Failed to install the HAP because the isolationMode configured is not supported. |
| 17700042 | Failed to install the HAP because of incorrect URI in the data proxy. |
| 17700043 | Failed to install the HAP because of low APL in the non-system data proxy (required APL: system_basic or system_core). |
| 17700041 | Failed to install because enterprise device management disallow install. |
| 201 | Calling interface without permission 'ohos.permission.INSTALL_BUNDLE' or ' ohos.permission.INSTALL_ENTERPRISE_BUNDLE' or 'ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE' or 'ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE' or 'ohos.permission.INSTALL_INTERNALTESTING_BUNDLE' or ('ohos.permission.INSTALL_BUNDLE' and 'ohos.permission.INSTALL_ALLOW_DOWNGRADE'). |
| 17700039 | Failed to install because disallow install a shared bundle by hapFilePaths. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17700036 | Failed to install the HSP because lacks appropriate permissions. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2 . Incorrect parameter types; 3. Parameter hapFiles is needed for code signature; 4. The size of specifiedDistributionType is greater than 128; 5. The size of additionalInfo is greater than 3000. |
| 17700058 | Failed to install the HAP because the device has been controlled.<br>**Applicable version:** 12 and later |
| 17700054 | Failed to install the HAP because the HAP requests wrong permissions.<br>**Applicable version:** 11 and later |
| 17700052 | Failed to install the HAP because debug bundle cannot be installed under non -developer mode.<br>**Applicable version:** 11 and later |
| 17700050 | Failed to install the HAP because enterprise normal/MDM bundle cannot be installed on non-enterprise device.<br>**Applicable version:** 10 and later |
| 17700048 | Failed to install the HAP because the code signature verification is failed.<br>**Applicable version:** 10 and later |
| 17700015 | Failed to install the HAPs because they have different configuration information. |
| 17700012 | Failed to install the HAP because the HAP path is invalid or the HAP is too large. |
| 17700076 | Failed to install the HAP or HSP because the app distribution type is not allowed.<br>**Applicable version:** 18 and later |
| 17700077 | Failed to install the HAP and restore to preinstalled bundle.<br>**Applicable version:** 17 and later |
| 17700010 | Failed to install the HAP because the HAP fails to be parsed. |
| 17700011 | Failed to install the HAP because the HAP signature fails to be verified. |
| 17700073 | Failed to install the HAP because an application with the same &lt;br&gt;bundle name but different signature information exists on the device.<br>**Applicable version:** 13 and later |
| 17700004 | The specified user ID is not found. |
| 17700066 | Failed to install the HAP because installing the native package failed.<br>**Applicable version:** 12 and later |
| 17700031 | Failed to install the HAP because the overlay check of the HAP is failed. |
| 17700018 | Failed to install because the dependent module does not exist. |
| 17700016 | Failed to install the HAP because of insufficient system disk space. |
| 17700017 | Failed to install the HAP since the version of the HAP to install is too early. |

## Examples

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

## install

```TypeScript
install(hapFilePaths: Array<string>, callback: AsyncCallback<void>): void
```

安装指定应用。使用callback异步回调。

> **说明：**
> 
> 安装不同分发类型的应用需要申请相应的权限，分发类型可以参考[ApplicationInfo](arkts-ability-applicationinfo-i.md)中的
> appDistributionType字段说明。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 23+: ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE or ohos.permission.INSTALL_INTERNALTESTING_BUNDLE or (ohos.permission.INSTALL_BUNDLE and ohos.permission.INSTALL_ALLOW_DOWNGRADE)
- API version 13 - 22: ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE or ohos.permission.INSTALL_INTERNALTESTING_BUNDLE
- API version 10 - 12: ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE
- API version 9: ohos.permission.INSTALL_BUNDLE

<!--Device-BundleInstaller-install(hapFilePaths: Array<string>, callback: AsyncCallback<void>): void--><!--Device-BundleInstaller-install(hapFilePaths: Array<string>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hapFilePaths | Array&lt;string&gt; | Yes | 存储应用程序包的路径。路径应该是当前应用程序中存放HAP的数据目录。当传入的路径是一个目录时， 该目录下只能放同一个应用的HAP，且这些HAP的签 名需要保持一致。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | [回调函数](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md/arkts-basicservices-base-asynccallback-i.md)，安装应用成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17700047 | Failed to install the HAP because the VersionCode to be updated is not greater than the current VersionCode. |
| 17700044 | Failed to install the HAP because the isolationMode configured is not supported. |
| 17700042 | Failed to install the HAP because of incorrect URI in the data proxy. |
| 17700043 | Failed to install the HAP because of low APL in the non-system data proxy (required APL: system_basic or system_core). |
| 17700041 | Failed to install because enterprise device management disallow install. |
| 201 | Calling interface without permission 'ohos.permission.INSTALL_BUNDLE' or ' ohos.permission.INSTALL_ENTERPRISE_BUNDLE' or 'ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE' or 'ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE' or 'ohos.permission.INSTALL_INTERNALTESTING_BUNDLE' or ('ohos.permission.INSTALL_BUNDLE' and 'ohos.permission.INSTALL_ALLOW_DOWNGRADE'). |
| 17700039 | Failed to install because disallow install a shared bundle by hapFilePaths. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17700036 | Failed to install the HSP because lacks appropriate permissions. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2 . Incorrect parameter types. |
| 17700058 | Failed to install the HAP because the device has been controlled.<br>**Applicable version:** 12 and later |
| 17700054 | Failed to install the HAP because the HAP requests wrong permissions.<br>**Applicable version:** 11 and later |
| 17700052 | Failed to install the HAP because debug bundle cannot be installed under non -developer mode.<br>**Applicable version:** 11 and later |
| 17700050 | Failed to install the HAP because enterprise normal/MDM bundle cannot be installed on non-enterprise device.<br>**Applicable version:** 10 and later |
| 17700048 | Failed to install the HAP because the code signature verification is failed.<br>**Applicable version:** 10 and later |
| 17700015 | Failed to install the HAPs because they have different configuration information. |
| 17700012 | Failed to install the HAP because the HAP path is invalid or the HAP is too large. |
| 17700076 | Failed to install the HAP or HSP because the app distribution type is not allowed.<br>**Applicable version:** 18 and later |
| 17700077 | Failed to install the HAP and restore to preinstalled bundle.<br>**Applicable version:** 17 and later |
| 17700010 | Failed to install the HAP because the HAP fails to be parsed. |
| 17700011 | Failed to install the HAP because the HAP signature fails to be verified. |
| 17700073 | Failed to install the HAP because an application with the same &lt;br&gt;bundle name but different signature information exists on the device.<br>**Applicable version:** 13 and later |
| 17700066 | Failed to install the HAP because installing the native package failed.<br>**Applicable version:** 12 and later |
| 17700031 | Failed to install the HAP because the overlay check of the HAP is failed. |
| 17700018 | Failed to install because the dependent module does not exist. |
| 17700016 | Failed to install the HAP because of insufficient system disk space. |
| 17700017 | Failed to install the HAP since the version of the HAP to install is too early. |

## Examples

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

## install

```TypeScript
install(hapFilePaths: Array<string>, installParam?: InstallParam): Promise<void>
```

安装指定应用。使用Promise异步回调。

> **说明：**
> 
> 安装不同分发类型的应用需要申请相应的权限，分发类型可以参考[ApplicationInfo](arkts-ability-applicationinfo-i.md)中的
> appDistributionType字段说明。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 23+: ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE or ohos.permission.INSTALL_INTERNALTESTING_BUNDLE or (ohos.permission.INSTALL_BUNDLE and ohos.permission.INSTALL_ALLOW_DOWNGRADE)
- API version 13 - 22: ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE or ohos.permission.INSTALL_INTERNALTESTING_BUNDLE
- API version 10 - 12: ohos.permission.INSTALL_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE or ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE
- API version 9: ohos.permission.INSTALL_BUNDLE

<!--Device-BundleInstaller-install(hapFilePaths: Array<string>, installParam?: InstallParam): Promise<void>--><!--Device-BundleInstaller-install(hapFilePaths: Array<string>, installParam?: InstallParam): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hapFilePaths | Array&lt;string&gt; | Yes | 存储应用程序包的路径。路径应该是当前应用程序中存放HAP的数据目录。当传入的路径是一个目录时， 该目录下只能放同一个应用的HAP，且这些HAP的签 名需要保持一致。 |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | No | 指定安装所需的其他参数，默认值：参照[InstallParam](arkts-ability-installer-installparam-i-sys.md)的默认值 。<br>**Since:** 12 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17700047 | Failed to install the HAP because the VersionCode to be updated is not greater than the current VersionCode. |
| 17700044 | Failed to install the HAP because the isolationMode configured is not supported. |
| 17700042 | Failed to install the HAP because of incorrect URI in the data proxy. |
| 17700043 | Failed to install the HAP because of low APL in the non-system data proxy (required APL: system_basic or system_core). |
| 17700041 | Failed to install because enterprise device management disallow install. |
| 201 | Calling interface without permission 'ohos.permission.INSTALL_BUNDLE' or ' ohos.permission.INSTALL_ENTERPRISE_BUNDLE' or 'ohos.permission.INSTALL_ENTERPRISE_MDM_BUNDLE' or 'ohos.permission.INSTALL_ENTERPRISE_NORMAL_BUNDLE' or 'ohos.permission.INSTALL_INTERNALTESTING_BUNDLE' or ('ohos.permission.INSTALL_BUNDLE' and 'ohos.permission.INSTALL_ALLOW_DOWNGRADE'). |
| 17700039 | Failed to install because disallow install a shared bundle by hapFilePaths. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17700036 | Failed to install the HSP because lacks appropriate permissions. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2 . Incorrect parameter types; 3. Parameter hapFiles is needed for code signature; 4. The size of specifiedDistributionType is greater than 128; 5. The size of additionalInfo is greater than 3000. |
| 17700058 | Failed to install the HAP because the device has been controlled.<br>**Applicable version:** 12 and later |
| 17700054 | Failed to install the HAP because the HAP requests wrong permissions.<br>**Applicable version:** 11 and later |
| 17700052 | Failed to install the HAP because debug bundle cannot be installed under non -developer mode.<br>**Applicable version:** 11 and later |
| 17700050 | Failed to install the HAP because enterprise normal/MDM bundle cannot be installed on non-enterprise device.<br>**Applicable version:** 10 and later |
| 17700048 | Failed to install the HAP because the code signature verification is failed.<br>**Applicable version:** 10 and later |
| 17700015 | Failed to install the HAPs because they have different configuration information. |
| 17700012 | Failed to install the HAP because the HAP path is invalid or the HAP is too large. |
| 17700076 | Failed to install the HAP or HSP because the app distribution type is not allowed.<br>**Applicable version:** 18 and later |
| 17700077 | Failed to install the HAP and restore to preinstalled bundle.<br>**Applicable version:** 17 and later |
| 17700010 | Failed to install the HAP because the HAP fails to be parsed. |
| 17700011 | Failed to install the HAP because the HAP signature fails to be verified. |
| 17700073 | Failed to install the HAP because an application with the same &lt;br&gt;bundle name but different signature information exists on the device.<br>**Applicable version:** 13 and later |
| 17700004 | The specified user ID is not found. |
| 17700066 | Failed to install the HAP because installing the native package failed.<br>**Applicable version:** 12 and later |
| 17700031 | Failed to install the HAP because the overlay check of the HAP is failed. |
| 17700018 | Failed to install because the dependent module does not exist. |
| 17700016 | Failed to install the HAP because of insufficient system disk space. |
| 17700017 | Failed to install the HAP since the version of the HAP to install is too early. |

## Examples

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

## installPlugin

```TypeScript
installPlugin(hostBundleName: string, pluginFilePaths: Array<string>, pluginParam?: PluginParam): Promise<void>
```

应用安装插件。使用Promise异步回调。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_PLUGIN_BUNDLE

<!--Device-BundleInstaller-installPlugin(hostBundleName: string, pluginFilePaths: Array<string>, pluginParam?: PluginParam): Promise<void>--><!--Device-BundleInstaller-installPlugin(hostBundleName: string, pluginFilePaths: Array<string>, pluginParam?: PluginParam): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hostBundleName | string | Yes | 待安装插件的应用包名。 |
| pluginFilePaths | Array&lt;string&gt; | Yes | 存储插件程序包的路径。当传入多个文件路径或者一个目录时，需确保这些文件是同一插件程序的HSP，且这些HSP的签名需要保持一致。 |
| pluginParam | [PluginParam](arkts-ability-installer-pluginparam-i-sys.md) | No | 指定安装插件所需的参数，默认值：参照 [PluginParam](arkts-ability-installer-pluginparam-i-sys.md) 的默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17700015 | Failed to install the plugin because they have different configuration information. |
| 17700012 | Failed to install the plugin because the HSP path is invalid or the HSP is too large. |
| 17700010 | Failed to install the plugin because the plugin fails to be parsed. |
| 17700011 | Failed to install the plugin because the plugin signature fails to be verified. |
| 17700073 | Failed to install the plugin because a plugin with the same &lt;br&gt;bundle name but different signature information exists on the device. |
| 201 | Calling interface without permission 'ohos.permission.INSTALL_PLUGIN_BUNDLE'. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17700004 | The userId is invalid. |
| 17700001 | The specified hostBundleName cannot be found or the bundle is not installed by the specified user. |
| 17700090 | Failed to install the plugin because the plugin id fails to be verified. |
| 17700091 | Failed to install the plugin because the plugin name is same as host bundle name. |
| 17700088 | Failed to install the plugin because the host application lacks ohos.permission.kernel.SUPPORT_PLUGIN. |
| 17700089 | Failed to install the plugin because the plugin id fails to be parsed. |
| 17700087 | Failed to install the plugin because the current device does not support plugin. |
| 17700052 | Failed to install the plugin because debug bundle cannot be installed under non-developer mode. |
| 17700016 | Failed to install the plugin because of insufficient system disk space. |
| 17700048 | Failed to install the plugin because the code signature verification is failed. |
| 17700017 | Failed to install the plugin since the version of the plugin to install is too early. |

## Examples

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

在指定用户下安装指定bundleName的应用。使用Promise异步回调。

> **说明：**
> 
> 该接口不支持安装[签名证书的分发类型](arkts-ability-applicationinfo-i.md)为enterprise，enterprise_mdm和
> enterprise_normal的应用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE

<!--Device-BundleInstaller-installPreexistingApp(bundleName: string, userId?: int): Promise<void>--><!--Device-BundleInstaller-installPreexistingApp(bundleName: string, userId?: int): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 需要安装应用的包名。 |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 需要安装应用的用户ID，可以通过 [getOsAccountLocalId接口](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) 获取，userId需要大于0。默认值：调用方所在用户。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2 . Incorrect parameter types. |
| 17700058 | Failed to install the HAP because this application is prohibited &lt;br&gt;from being installed on this device or by specified users.<br>**Applicable version:** 14 and later |
| 201 | Calling interface without permission 'ohos.permission.INSTALL_BUNDLE'. |
| 17700071 | It is not allowed to install the enterprise bundle. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17700004 | The userId is invalid. |
| 17700001 | The specified bundleName cannot be found or the bundle is not installed by the specified user. |

## Examples

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

回滚应用到初次安装时的状态。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE or ohos.permission.RECOVER_BUNDLE

<!--Device-BundleInstaller-recover(bundleName: string, installParam: InstallParam, callback: AsyncCallback<void>): void--><!--Device-BundleInstaller-recover(bundleName: string, installParam: InstallParam, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 待恢复应用的包名。 |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | Yes | 指定安装所需的其他参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | [回调函数](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md/arkts-basicservices-base-asynccallback-i.md)，回滚应用成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2 . Incorrect parameter types. |
| 17700058 | Failed to install the HAP because this application is prohibited &lt;br&gt;from being installed on this device or by specified users.<br>**Applicable version:** 14 and later |
| 17700073 | Failed to install the HAP because an application with the same &lt;br&gt;bundle name but different signature information exists on the device.<br>**Applicable version:** 13 and later |
| 201 | Calling interface without permission 'ohos.permission.INSTALL_BUNDLE' or ' ohos.permission.RECOVER_BUNDLE'. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17700004 | The specified user ID is not found. |
| 17700001 | The specified bundle name is not found. |

## Examples

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

## recover

```TypeScript
recover(bundleName: string, callback: AsyncCallback<void>): void
```

回滚应用到初次安装时的状态。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE or ohos.permission.RECOVER_BUNDLE

<!--Device-BundleInstaller-recover(bundleName: string, callback: AsyncCallback<void>): void--><!--Device-BundleInstaller-recover(bundleName: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 待恢复应用的包名。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | [回调函数](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md/arkts-basicservices-base-asynccallback-i.md)，回滚应用成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2 . Incorrect parameter types. |
| 17700058 | Failed to install the HAP because this application is prohibited &lt;br&gt;from being installed on this device or by specified users.<br>**Applicable version:** 14 and later |
| 17700073 | Failed to install the HAP because an application with the same &lt;br&gt;bundle name but different signature information exists on the device.<br>**Applicable version:** 13 and later |
| 201 | Calling interface without permission 'ohos.permission.INSTALL_BUNDLE' or ' ohos.permission.RECOVER_BUNDLE'. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17700001 | The specified bundle name is not found. |

## Examples

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

## recover

```TypeScript
recover(bundleName: string, installParam?: InstallParam): Promise<void>
```

回滚应用到初次安装时的状态。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE or ohos.permission.RECOVER_BUNDLE

<!--Device-BundleInstaller-recover(bundleName: string, installParam?: InstallParam): Promise<void>--><!--Device-BundleInstaller-recover(bundleName: string, installParam?: InstallParam): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 待卸载应用的包名。 |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | No | 指定安装所需的其他参数，默认值：参照[InstallParam](arkts-ability-installer-installparam-i-sys.md)的默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2 . Incorrect parameter types. |
| 17700058 | Failed to install the HAP because this application is prohibited &lt;br&gt;from being installed on this device or by specified users.<br>**Applicable version:** 14 and later |
| 17700073 | Failed to install the HAP because an application with the same &lt;br&gt;bundle name but different signature information exists on the device.<br>**Applicable version:** 13 and later |
| 201 | Calling interface without permission 'ohos.permission.INSTALL_BUNDLE' or ' ohos.permission.RECOVER_BUNDLE'. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17700004 | The specified user ID is not found. |
| 17700001 | The specified bundle name is not found. |

## Examples

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

## removeExtResource

```TypeScript
removeExtResource(bundleName: string, moduleNames: Array<string>): Promise<void>
```

根据给定的bundleName和moduleNames删除扩展资源。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE or ohos.permission.UNINSTALL_BUNDLE

<!--Device-BundleInstaller-removeExtResource(bundleName: string, moduleNames: Array<string>): Promise<void>--><!--Device-BundleInstaller-removeExtResource(bundleName: string, moduleNames: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 要删除扩展资源的应用名称。 |
| moduleNames | Array&lt;string&gt; | Yes | 要删除扩展资源的moduleNames。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17700302 | RemoveExtResource failed due to module does not exist. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2 . Incorrect parameter types. |
| 201 | Permission denied. |
| 202 | Permission denied, non-system app called system api. |
| 17700001 | The specified bundleName is not found. |

## Examples

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

卸载应用。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE or ohos.permission.UNINSTALL_BUNDLE

<!--Device-BundleInstaller-uninstall(bundleName: string, installParam: InstallParam, callback: AsyncCallback<void>): void--><!--Device-BundleInstaller-uninstall(bundleName: string, installParam: InstallParam, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 待卸载应用的包名。 |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | Yes | 指定安装所需的其他参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | [回调函数](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md/arkts-basicservices-base-asynccallback-i.md)，卸载应用成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17700062 | Failed to uninstall the app because the app is locked.<br>**Applicable version:** 15 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2 . Incorrect parameter types. |
| 17700060 | The specified application cannot be uninstalled.<br>**Applicable version:** 13 and later |
| 17700045 | Failed to uninstall the HAP because uninstall is not allowed by the enterprise device management. |
| 17700040 | The specified bundle is a shared bundle and cannot be uninstalled. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17700004 | The specified user ID is not found. |
| 17700020 | The specified bundle is a pre-installed bundle and cannot be uninstalled. |
| 17700067 | Failed to uninstall the HAP because uninstalling the native package failed.<br>**Applicable version:** 12 and later |
| 17700001 | The specified bundle name is not found. |

## Examples

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

## uninstall

```TypeScript
uninstall(bundleName: string, callback: AsyncCallback<void>): void
```

卸载应用。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE or ohos.permission.UNINSTALL_BUNDLE

<!--Device-BundleInstaller-uninstall(bundleName: string, callback: AsyncCallback<void>): void--><!--Device-BundleInstaller-uninstall(bundleName: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 待卸载应用的包名。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | [回调函数](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md/arkts-basicservices-base-asynccallback-i.md)，卸载应用成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2 . Incorrect parameter types. |
| 17700060 | The specified application cannot be uninstalled.<br>**Applicable version:** 13 and later |
| 17700045 | Failed to uninstall the HAP because uninstall is not allowed by the enterprise device management. |
| 17700040 | The specified bundle is a shared bundle and cannot be uninstalled. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17700020 | The specified bundle is a pre-installed bundle and cannot be uninstalled. |
| 17700067 | Failed to uninstall the HAP because uninstalling the native package failed.<br>**Applicable version:** 12 and later |
| 17700001 | The specified bundle name is not found. |

## Examples

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

## uninstall

```TypeScript
uninstall(bundleName: string, installParam?: InstallParam): Promise<void>
```

卸载应用。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE or ohos.permission.UNINSTALL_BUNDLE

<!--Device-BundleInstaller-uninstall(bundleName: string, installParam?: InstallParam): Promise<void>--><!--Device-BundleInstaller-uninstall(bundleName: string, installParam?: InstallParam): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 待卸载应用的包名。 |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | No | 指定安装所需的其他参数，默认值：参照[InstallParam](arkts-ability-installer-installparam-i-sys.md)的默认值 。<br>**Since:** 15 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17700062 | Failed to uninstall the app because the app is locked.<br>**Applicable version:** 15 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2 . Incorrect parameter types. |
| 17700060 | The specified application cannot be uninstalled.<br>**Applicable version:** 13 and later |
| 17700045 | Failed to uninstall the HAP because uninstall is not allowed by the enterprise device management. |
| 17700040 | The specified bundle is a shared bundle and cannot be uninstalled. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17700004 | The specified user ID is not found. |
| 17700020 | The specified bundle is a pre-installed bundle and cannot be uninstalled. |
| 17700067 | Failed to uninstall the HAP because uninstalling the native package failed.<br>**Applicable version:** 12 and later |
| 17700001 | The specified bundle name is not found. |

## Examples

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

## uninstall

```TypeScript
uninstall(uninstallParam: UninstallParam, callback: AsyncCallback<void>): void
```

卸载一个共享包。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE or ohos.permission.UNINSTALL_BUNDLE

<!--Device-BundleInstaller-uninstall(uninstallParam: UninstallParam, callback: AsyncCallback<void>): void--><!--Device-BundleInstaller-uninstall(uninstallParam: UninstallParam, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uninstallParam | [UninstallParam](arkts-ability-installer-uninstallparam-i-sys.md) | Yes | 共享包卸载需指定的参数信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | [回调函数](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md/arkts-basicservices-base-asynccallback-i.md)，卸载应用成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2 . Incorrect parameter types. |
| 17700038 | The specified shared bundle does not exist. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17700020 | The specified bundle is a pre-installed bundle and cannot be uninstalled. |
| 17700037 | The version of shared bundle is dependent on other applications. |

## Examples

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
uninstall(uninstallParam: UninstallParam): Promise<void>
```

卸载一个共享包。使用Promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE or ohos.permission.UNINSTALL_BUNDLE

<!--Device-BundleInstaller-uninstall(uninstallParam: UninstallParam): Promise<void>--><!--Device-BundleInstaller-uninstall(uninstallParam: UninstallParam): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uninstallParam | [UninstallParam](arkts-ability-installer-uninstallparam-i-sys.md) | Yes | 共享包卸载需指定的参数信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2 . Incorrect parameter types. |
| 17700038 | The specified shared bundle does not exist. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17700020 | The specified bundle is a pre-installed bundle and cannot be uninstalled. |
| 17700037 | The version of shared bundle is dependent on other applications. |

## Examples

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

## uninstallNewPreinstalledApps

```TypeScript
uninstallNewPreinstalledApps(bundleNames: Array<string>): Promise<void>
```

批量卸载新增的预置应用。使用Promise异步回调。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.UNINSTALL_BUNDLE

**Model restriction:** This API can be used only in the stage model.

<!--Device-BundleInstaller-uninstallNewPreinstalledApps(bundleNames: Array<string>): Promise<void>--><!--Device-BundleInstaller-uninstallNewPreinstalledApps(bundleNames: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleNames | Array&lt;string&gt; | Yes | 待卸载的应用的包名列表。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 202 | Permission denied, non-system app called system api. |

## uninstallPlugin

```TypeScript
uninstallPlugin(hostBundleName: string, pluginBundleName: string, pluginParam?: PluginParam): Promise<void>
```

应用卸载插件。使用Promise异步回调。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.UNINSTALL_PLUGIN_BUNDLE

<!--Device-BundleInstaller-uninstallPlugin(hostBundleName: string, pluginBundleName: string, pluginParam?: PluginParam): Promise<void>--><!--Device-BundleInstaller-uninstallPlugin(hostBundleName: string, pluginBundleName: string, pluginParam?: PluginParam): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hostBundleName | string | Yes | 待卸载插件的应用包名。 |
| pluginBundleName | string | Yes | 插件的包名。 |
| pluginParam | [PluginParam](arkts-ability-installer-pluginparam-i-sys.md) | No | 指定卸载插件所需的参数，默认值：参照 [PluginParam](arkts-ability-installer-pluginparam-i-sys.md) 的默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17700092 | Failed to uninstall the plugin because the specified plugin is not found. |
| 201 | Calling interface without permission 'ohos.permission.UNINSTALL_PLUGIN_BUNDLE'. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17700004 | The user id is invalid. |
| 17700001 | The specified bundle name is not found. |

## Examples

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

对预置应用进行卸载更新，恢复到初次安装时的状态。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_BUNDLE or ohos.permission.UNINSTALL_BUNDLE

<!--Device-BundleInstaller-uninstallUpdates(bundleName: string, installParam?: InstallParam): Promise<void>--><!--Device-BundleInstaller-uninstallUpdates(bundleName: string, installParam?: InstallParam): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 待卸载更新应用的包名。 |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | No | 指定卸载更新所需的其他参数，默认值：参照[InstallParam](arkts-ability-installer-installparam-i-sys.md)的默认值。其中 userId无法指定，调用本接口将对所有已安装相应应用的用户进行卸载更新操作。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2 . Incorrect parameter types. |
| 17700060 | The specified application cannot be uninstalled.<br>**Applicable version:** 13 and later |
| 17700045 | Failed to uninstall because enterprise device management disallow uninstall. |
| 17700057 | Failed to uninstall updates because the HAP is not pre-installed. |
| 17700073 | Failed to install the HAP because an application with the same &lt;br&gt;bundle name but different signature information exists on the device.<br>**Applicable version:** 13 and later |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17700067 | Failed to uninstall the HAP because uninstalling the native package failed.<br>**Applicable version:** 13 and later |
| 17700001 | The specified bundle name is not found. |

## Examples

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

更新当前应用，仅限企业设备上的企业MDM应用调用，且传入的hapFilePaths中的hap必须都属于当前应用。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_SELF_BUNDLE

<!--Device-BundleInstaller-updateBundleForSelf(hapFilePaths: Array<string>, installParam: InstallParam, callback: AsyncCallback<void>): void--><!--Device-BundleInstaller-updateBundleForSelf(hapFilePaths: Array<string>, installParam: InstallParam, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hapFilePaths | Array&lt;string&gt; | Yes | 存储应用程序包的路径。路径应该是当前应用程序中存放HAP的数据目录。当传入的路径是一个目录时， 该目录下只能放同一个应用的HAP，且这些HAP的签 名需要保持一致。 |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | Yes | 指定安装所需的其他参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | [回调函数](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md/arkts-basicservices-base-asynccallback-i.md)，安装应用成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17700015 | Failed to install the HAPs because they have different configuration information. |
| 17700047 | Failed to install the HAP because the VersionCode to be updated is not greater than the current VersionCode. |
| 17700012 | Failed to install the HAP because the HAP path is invalid or the HAP is too large. |
| 17700044 | Failed to install the HAP because the isolationMode configured is not supported. |
| 17700010 | Failed to install the HAP because the HAP fails to be parsed. |
| 17700042 | Failed to install the HAP because of incorrect URI in the data proxy. |
| 17700011 | Failed to install the HAP because the HAP signature fails to be verified. |
| 17700043 | Failed to install the HAP because of low APL in the non-system data proxy (required APL: system_basic or system_core). |
| 17700041 | Failed to install because enterprise device management disallow install. |
| 201 | Calling interface without permission 'ohos.permission.INSTALL_SELF_BUNDLE'. |
| 17700039 | Failed to install because disallow install a shared bundle by hapFilePaths. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17700004 | The specified user ID is not found. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter hapFiles is needed for code signature; 4. The size of specifiedDistributionType is greater than 128; 5. The size of additionalInfo is greater than 3 000. |
| 17700018 | Failed to install because the dependent module does not exist. |
| 17700050 | Failed to install the HAP because enterprise normal/MDM bundle cannot be installed on non-enterprise device. |
| 17700051 | Failed to install the HAP because the distribution type of caller application is not enterprise_mdm. |
| 17700016 | Failed to install the HAP because of insufficient system disk space. |
| 17700048 | Failed to install the HAP because the code signature verification is failed. |
| 17700017 | Failed to install the HAP since the version of the HAP to install is too early. |
| 17700049 | Failed to install the HAP because the bundleName is different from the bundleName of the caller application. |

## Examples

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

## updateBundleForSelf

```TypeScript
updateBundleForSelf(hapFilePaths: Array<string>, callback: AsyncCallback<void>): void
```

更新当前应用，仅限企业设备上的企业MDM应用调用，且传入的hapFilePaths中的hap必须都属于当前应用。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_SELF_BUNDLE

<!--Device-BundleInstaller-updateBundleForSelf(hapFilePaths: Array<string>, callback: AsyncCallback<void>): void--><!--Device-BundleInstaller-updateBundleForSelf(hapFilePaths: Array<string>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hapFilePaths | Array&lt;string&gt; | Yes | 存储应用程序包的路径。路径应该是当前应用程序中存放HAP的数据目录。当传入的路径是一个目录时， 该目录下只能放同一个应用的HAP，且这些HAP的签 名需要保持一致。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | [回调函数](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md/arkts-basicservices-base-asynccallback-i.md)，安装应用成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17700015 | Failed to install the HAPs because they have different configuration information. |
| 17700047 | Failed to install the HAP because the VersionCode to be updated is not greater than the current VersionCode. |
| 17700012 | Failed to install the HAP because the HAP path is invalid or the HAP is too large. |
| 17700044 | Failed to install the HAP because the isolationMode configured is not supported. |
| 17700010 | Failed to install the HAP because the HAP fails to be parsed. |
| 17700042 | Failed to install the HAP because of incorrect URI in the data proxy. |
| 17700011 | Failed to install the HAP because the HAP signature fails to be verified. |
| 17700043 | Failed to install the HAP because of low APL in the non-system data proxy (required APL: system_basic or system_core). |
| 17700041 | Failed to install because enterprise device management disallow install. |
| 201 | Calling interface without permission 'ohos.permission.INSTALL_SELF_BUNDLE'. |
| 17700039 | Failed to install because disallow install a shared bundle by hapFilePaths. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2 . Incorrect parameter types. |
| 17700018 | Failed to install because the dependent module does not exist. |
| 17700050 | Failed to install the HAP because enterprise normal/MDM bundle cannot be installed on non-enterprise device. |
| 17700051 | Failed to install the HAP because the distribution type of caller application is not enterprise_mdm. |
| 17700016 | Failed to install the HAP because of insufficient system disk space. |
| 17700048 | Failed to install the HAP because the code signature verification is failed. |
| 17700017 | Failed to install the HAP since the version of the HAP to install is too early. |
| 17700049 | Failed to install the HAP because the bundleName is different from the bundleName of the caller application. |

## Examples

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

## updateBundleForSelf

```TypeScript
updateBundleForSelf(hapFilePaths: Array<string>, installParam?: InstallParam): Promise<void>
```

更新当前应用，仅限企业设备上的企业MDM应用调用，且传入的hapFilePaths中的hap必须都属于当前应用。使用Promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INSTALL_SELF_BUNDLE

<!--Device-BundleInstaller-updateBundleForSelf(hapFilePaths: Array<string>, installParam?: InstallParam): Promise<void>--><!--Device-BundleInstaller-updateBundleForSelf(hapFilePaths: Array<string>, installParam?: InstallParam): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hapFilePaths | Array&lt;string&gt; | Yes | 存储应用程序包的路径。路径应该是当前应用程序中存放HAP的数据目录。当传入的路径是一个目录时， 该目录下只能放同一个应用的HAP，且这些HAP的签 名需要保持一致。 |
| installParam | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | No | 指定安装所需的其他参数，默认值：参照[InstallParam](arkts-ability-installer-installparam-i-sys.md)的默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17700015 | Failed to install the HAPs because they have different configuration information. |
| 17700047 | Failed to install the HAP because the VersionCode to be updated is not greater than the current VersionCode. |
| 17700012 | Failed to install the HAP because the HAP path is invalid or the HAP is too large. |
| 17700044 | Failed to install the HAP because the isolationMode configured is not supported. |
| 17700010 | Failed to install the HAP because the HAP fails to be parsed. |
| 17700042 | Failed to install the HAP because of incorrect URI in the data proxy. |
| 17700011 | Failed to install the HAP because the HAP signature fails to be verified. |
| 17700043 | Failed to install the HAP because of low APL in the non-system data proxy (required APL: system_basic or system_core). |
| 17700041 | Failed to install because enterprise device management disallow install. |
| 201 | Calling interface without permission 'ohos.permission.INSTALL_SELF_BUNDLE'. |
| 17700039 | Failed to install because disallow install a shared bundle by hapFilePaths. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 17700004 | The specified user ID is not found. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter hapFiles is needed for code signature; 4. The size of specifiedDistributionType is greater than 128; 5. The size of additionalInfo is greater than 3 000. |
| 17700018 | Failed to install because the dependent module does not exist. |
| 17700050 | Failed to install the HAP because enterprise normal/MDM bundle cannot be installed on non-enterprise device. |
| 17700051 | Failed to install the HAP because the distribution type of caller application is not enterprise_mdm. |
| 17700016 | Failed to install the HAP because of insufficient system disk space. |
| 17700048 | Failed to install the HAP because the code signature verification is failed. |
| 17700017 | Failed to install the HAP since the version of the HAP to install is too early. |
| 17700049 | Failed to install the HAP because the bundleName is different from the bundleName of the caller application. |

## Examples

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

