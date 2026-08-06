# InstallStatus (System API)

Describes the bundle installation or uninstall status.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-unnamed-export interface InstallStatus--><!--Device-unnamed-export interface InstallStatus-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

## status

```TypeScript
status: bundle.InstallErrorCode
```

Installation or uninstall error code. The value must be defined in  
[InstallErrorCode]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Type:** bundle.InstallErrorCode

**Default:** Indicates the install or uninstall error code

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-InstallStatus-status: bundle.InstallErrorCode--><!--Device-InstallStatus-status: bundle.InstallErrorCode-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

## statusMessage

```TypeScript
statusMessage: string
```

Installation or uninstall status message.

**SUCCESS**: Installation succeeded.

**STATUS\_INSTALL\_FAILURE**: Installation failed (no installation file exists).

**STATUS\_INSTALL\_FAILURE\_ABORTED**: Installation aborted.

**STATUS\_INSTALL\_FAILURE\_INVALID**: Invalid installation parameter.

**STATUS\_INSTALL\_FAILURE\_CONFLICT**: Installation conflict. (The basic information of the application to update is inconsistent with that of the existing application.)

**STATUS\_INSTALL\_FAILURE\_STORAGE**: Failed to store the bundle information.

**STATUS\_INSTALL\_FAILURE\_INCOMPATIBLE**: Installation incompatibility. (A downgrade occurs or the signature information is incorrect.)

**STATUS\_UNINSTALL\_FAILURE**: Uninstallation failed. (The application to be uninstalled is not found.)

**STATUS\_UNINSTALL\_FAILURE\_ABORTED**: Uninstallation aborted. (This error code is not in use.)

**STATUS\_UNINSTALL\_FAILURE\_ABORTED**: Uninstallation conflict. (Failed to uninstall a system application or end the application process.)

**STATUS\_INSTALL\_FAILURE\_DOWNLOAD\_TIMEOUT**: Installation failed. (Download timed out.)

**STATUS\_INSTALL\_FAILURE\_DOWNLOAD\_FAILED**: Installation failed. (Download failed.)

**STATUS\_RECOVER\_FAILURE\_INVALID**: Failed to restore the pre-installed application.

**STATUS\_ABILITY\_NOT\_FOUND**: Ability not found.

**STATUS\_BMS\_SERVICE\_ERROR**: BMS service error.

**STATUS\_FAILED\_NO\_SPACE\_LEFT**: Insufficient device space.

**STATUS\_GRANT\_REQUEST\_PERMISSIONS\_FAILED**: Application authorization failed.

**STATUS\_INSTALL\_PERMISSION\_DENIED**: No installation permission.

**STATUS\_UNINSTALL\_PERMISSION\_DENIED**: No uninstallation permission.

**Type:** string

**Default:** Indicates the install or uninstall result string message

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-InstallStatus-statusMessage: string--><!--Device-InstallStatus-statusMessage: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

