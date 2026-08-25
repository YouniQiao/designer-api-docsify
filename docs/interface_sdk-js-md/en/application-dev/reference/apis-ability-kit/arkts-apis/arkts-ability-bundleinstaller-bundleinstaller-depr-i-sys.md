# BundleInstaller (System API)

The module provides APIs for you to install, uninstall, and recover bundles on devices.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [BundleInstaller](arkts-ability-installer-bundleinstaller-i-sys.md)

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

## install

```TypeScript
install(bundleFilePaths: Array<string>, param: InstallParam, callback: AsyncCallback<InstallStatus>): void
```

Install an application in a HAP.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [install](arkts-ability-installer-bundleinstaller-i-sys.md#install)

**Required permissions:** ohos.permission.INSTALL_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleFilePaths | Array & lt;string & gt; | Yes |
| param | [InstallParam](arkts-ability-bundleinstaller-installparam-depr-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[InstallStatus](arkts-ability-bundleinstaller-installstatus-depr-i-sys.md)&gt; | Yes |

## recover

```TypeScript
recover(bundleName: string, param: InstallParam, callback: AsyncCallback<InstallStatus>): void
```

recover an application.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [recover](arkts-ability-installer-bundleinstaller-i-sys.md#recover)

**Required permissions:** ohos.permission.INSTALL_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| param | [InstallParam](arkts-ability-bundleinstaller-installparam-depr-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[InstallStatus](arkts-ability-bundleinstaller-installstatus-depr-i-sys.md)&gt; | Yes |

## uninstall

```TypeScript
uninstall(bundleName: string, param: InstallParam, callback: AsyncCallback<InstallStatus>): void
```

Uninstall an application.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [uninstall](arkts-ability-installer-bundleinstaller-i-sys.md#uninstall)

**Required permissions:** ohos.permission.INSTALL_BUNDLE

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| param | [InstallParam](arkts-ability-bundleinstaller-installparam-depr-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[InstallStatus](arkts-ability-bundleinstaller-installstatus-depr-i-sys.md)&gt; | Yes |
