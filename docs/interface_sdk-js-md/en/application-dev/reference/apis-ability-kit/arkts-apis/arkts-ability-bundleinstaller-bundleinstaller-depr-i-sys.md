# BundleInstaller (System API)

本模块提供设备上安装、升级和卸载应用的能力。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.bundle.installer:installer.BundleInstaller](arkts-ability-installer-bundleinstaller-i-sys.md)

<!--Device-unnamed-export interface BundleInstaller--><!--Device-unnamed-export interface BundleInstaller-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

## install

```TypeScript
install(bundleFilePaths: Array<string>, param: InstallParam, callback: AsyncCallback<InstallStatus>): void
```

在应用中安装hap，支持多hap安装。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.bundle.installer:installer.BundleInstaller.install](arkts-ability-installer-bundleinstaller-i-sys.md#install)

**Required permissions:** ohos.permission.INSTALL_BUNDLE

<!--Device-BundleInstaller-install(bundleFilePaths: Array<string>, param: InstallParam, callback: AsyncCallback<InstallStatus>): void--><!--Device-BundleInstaller-install(bundleFilePaths: Array<string>, param: InstallParam, callback: AsyncCallback<InstallStatus>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleFilePaths | Array&lt;string&gt; | Yes | 指示存储HAP的沙箱路径。 |
| param | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | Yes | 指定安装所需的其他参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;InstallStatus&gt; | Yes | [回调函数](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md/arkts-basicservices-base-asynccallback-i.md)，程序 启动作为入参的回调函数，返回安装状态信息。 |

## recover

```TypeScript
recover(bundleName: string, param: InstallParam, callback: AsyncCallback<InstallStatus>): void
```

恢复一个应用程序，使用callback异步回调。当预置应用被卸载后，可以通过此接口进行恢复。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.bundle.installer:installer.BundleInstaller.recover](arkts-ability-installer-bundleinstaller-i-sys.md#recover)

**Required permissions:** ohos.permission.INSTALL_BUNDLE

<!--Device-BundleInstaller-recover(bundleName: string, param: InstallParam, callback: AsyncCallback<InstallStatus>): void--><!--Device-BundleInstaller-recover(bundleName: string, param: InstallParam, callback: AsyncCallback<InstallStatus>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 应用Bundle名称。 |
| param | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | Yes | 指定应用恢复所需的其他参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;InstallStatus&gt; | Yes | [回调函数](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md/arkts-basicservices-base-asynccallback-i.md)，程序 启动作为入参的回调函数，返回安装状态信息。 |

## uninstall

```TypeScript
uninstall(bundleName: string, param: InstallParam, callback: AsyncCallback<InstallStatus>): void
```

卸载应用程序，使用callback异步回调，返回安装状态信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.bundle.installer:installer.BundleInstaller.uninstall](arkts-ability-installer-bundleinstaller-i-sys.md#uninstall)

**Required permissions:** ohos.permission.INSTALL_BUNDLE

<!--Device-BundleInstaller-uninstall(bundleName: string, param: InstallParam, callback: AsyncCallback<InstallStatus>): void--><!--Device-BundleInstaller-uninstall(bundleName: string, param: InstallParam, callback: AsyncCallback<InstallStatus>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 应用Bundle名称。 |
| param | [InstallParam](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-installparam-i.md) | Yes | 指定卸载所需的其他参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;InstallStatus&gt; | Yes | [回调函数](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md/arkts-basicservices-base-asynccallback-i.md)，程序 启动作为入参的回调函数，返回安装状态信息。 |

