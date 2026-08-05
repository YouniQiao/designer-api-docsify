# InstallParam (System API)

Defines the parameters that need to be specified for bundle installation, uninstall, or recovering.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-installer-export interface InstallParam--><!--Device-installer-export interface InstallParam-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## additionalInfo

```TypeScript
additionalInfo?: string
```

Additional information during application installation (usually an enterprise application). By default, no value is passed. The maximum length is 3,000 bytes. This field is usually specified by the application market of the operating system operator.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InstallParam-additionalInfo?: string--><!--Device-InstallParam-additionalInfo?: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## crowdtestDeadline

```TypeScript
crowdtestDeadline?: long
```

End date of crowdtesting. The default value is **-1**, indicating that no end date is specified for crowdtesting.

**Type:** long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InstallParam-crowdtestDeadline?: long--><!--Device-InstallParam-crowdtestDeadline?: long-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## hashParams

```TypeScript
hashParams?: Array<HashParam>
```

Hash parameters. By default, no value is passed.

**Type:** Array&lt;HashParam&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InstallParam-hashParams?: Array<HashParam>--><!--Device-InstallParam-hashParams?: Array<HashParam>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## installFlag

```TypeScript
installFlag?: int
```

Installation flag. The value **0x00** means initial installation, **0x01** means overwrite installation, and **0x10** means installation-free. The default value is **0x00**.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InstallParam-installFlag?: int--><!--Device-InstallParam-installFlag?: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## isKeepData

```TypeScript
isKeepData?: boolean
```

Whether to retain the data directory during bundle uninstall. The default value is **false**. **true** to retain, **false** otherwise.

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InstallParam-isKeepData?: boolean--><!--Device-InstallParam-isKeepData?: boolean-End-->

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

<!--Device-InstallParam-parameters?: Array<Parameters>--><!--Device-InstallParam-parameters?: Array<Parameters>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## pgoParams

```TypeScript
pgoParams?: Array<PGOParam>
```

Parameters of the Profile-guided Optimization (PGO) configuration file. The default value is null.

**Type:** Array&lt;PGOParam&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-InstallParam-pgoParams?: Array<PGOParam>--><!--Device-InstallParam-pgoParams?: Array<PGOParam>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## sharedBundleDirPaths

```TypeScript
sharedBundleDirPaths?: Array<string>
```

Paths of the shared bundle files. By default, no value is passed.

**Type:** Array&lt;string&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InstallParam-sharedBundleDirPaths?: Array<string>--><!--Device-InstallParam-sharedBundleDirPaths?: Array<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## specifiedDistributionType

```TypeScript
specifiedDistributionType?: string
```

\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ specified during application installation. By default, no value is passed. The maximum length is 128 bytes. This field is usually specified by the application market of the operating system operator.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InstallParam-specifiedDistributionType?: string--><!--Device-InstallParam-specifiedDistributionType?: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## userId

```TypeScript
userId?: int
```

User ID. The default value is the user ID of the caller. The value must be greater than or equal to 0. You can call [queryOsAccountLocalIdFromProcess]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to obtain the user ID of the current process. When a driver application is installed, uninstalled, or restored, this parameter is ignored and the operation is executed for all users.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InstallParam-userId?: int--><!--Device-InstallParam-userId?: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## verifyCodeParams

```TypeScript
verifyCodeParams?: Array<VerifyCodeParam>
```

Information about the code signature file. The default value is null. **NOTE** Starting from API version 10, the code signature file of an application is integrated into the installation package, rather than being specified by using this field. This field is deprecated since API version 11.

**Type:** Array&lt;VerifyCodeParam&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 11

<!--Device-InstallParam-verifyCodeParams?: Array<VerifyCodeParam>--><!--Device-InstallParam-verifyCodeParams?: Array<VerifyCodeParam>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

