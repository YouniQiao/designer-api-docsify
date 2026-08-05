# DestroyAppCloneParam (System API)

Describes the parameters used for destroying an application clone.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-installer-export interface DestroyAppCloneParam--><!--Device-installer-export interface DestroyAppCloneParam-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## parameters

```TypeScript
parameters?: Array<Parameters>
```

Extended parameters, represented as an array of the Parameters type. The default value is empty. The options of **Parameters.key** are as follows: - **ohos.bms.param.renameInstall**: If the value is **true**, the installation package is moved from the application sandbox to the installation directory using a shared directory. Otherwise, it is copied from the application sandbox to the installation directory using a regular directory. - **ohos.bms.param.enterpriseForAllUser**: If the value is **true**, the enterprise app is installed for all users. This parameter takes effect only for applications whose [distribution type of the application signing certificate]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ is **enterprise\_mdm** or **enterprise\_normal**. - **ohos.bms.param.verifyUninstallRule**: If the value is **true**, an uninstallation handling rule is set to block application uninstallation. - **ohos.bms.param.enterpriseManifest**: The value is the sandbox path of the JSON file used to store the application's manifest, including the bundle name. It is used in the scenario of cloning enterprise applications. If this JSON file exists during cloning, the application package from the old device is copied to the new device for installation. - **ohos.bms.param.installBundleName**: The value is the bundle name of the application. It is used in application installation scenarios and supported since API version 23. If this field is passed during installation, the [getBundleInstallStatus]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ API can be called to obtain the installation status of the application. - **ohos.bms.param.installAllowDowngrade**: If the value is **true**, the application can be installed in downgrade mode (supported since API version 23). That is, if a higher version of the application is already installed on the device, a lower version can be installed over it. Only third-party applications with the signing certificate distribution type set to **app\_gallery** or the signing certificate type set to **debug** support downgrade installation. To use downgrade installation, you must request the ohos.permission.INSTALL\_BUNDLE and ohos.permission.INSTALL\_ALLOW\_DOWNGRADE permissions.

**Type:** Array&lt;Parameters&gt;

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-DestroyAppCloneParam-parameters?: Array<Parameters>--><!--Device-DestroyAppCloneParam-parameters?: Array<Parameters>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## userId

```TypeScript
userId?: int
```

ID of the user for whom the clone is to be destroyed. You can obtain the user ID by calling [getOsAccountLocalId]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ . The default value is the user ID of the caller.

**Type:** int

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-DestroyAppCloneParam-userId?: int--><!--Device-DestroyAppCloneParam-userId?: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

