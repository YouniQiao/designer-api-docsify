# InstallStatus (System API)

```TypeScript
export interface InstallStatus
```

Describes the bundle installation or uninstall status.

**Since:** 7

**Deprecated since:** 9

<!--Device-unnamed-export interface InstallStatus--><!--Device-unnamed-export interface InstallStatus-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

## status

```TypeScript
status: bundle.InstallErrorCode
```

Installation or uninstall error code. The value must be defined in [InstallErrorCode](arkts-ability-bundle-installerrorcode-e.md).

**Type:** [bundle.InstallErrorCode](arkts-ability-bundle-installerrorcode-e.md)

**Default:** Indicates the install or uninstall error code

**Since:** 7

**Deprecated since:** 9

<!--Device-InstallStatus-status: bundle.InstallErrorCode--><!--Device-InstallStatus-status: bundle.InstallErrorCode-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

## statusMessage

```TypeScript
statusMessage: string
```

String result information indicating installation or uninstallation. The value range includes:

"SUCCESS" : Installation succeeded.&lt;/br&gt; "STATUS_INSTALL_FAILURE": Installation failure (the installation file does not exist).&lt;/br&gt; "STATUS_INSTALL_FAILURE_ABORTED": Installation aborted. &lt;/br&gt; "STATUS_INSTALL_FAILURE_INVALID": Invalid installation parameter. &lt;/br&gt; "STATUS_INSTALL_FAILURE_CONFLICT": Installation conflict (commonly caused by inconsistent basic information between the upgrade and the existing application). &lt;/br&gt; "STATUS_INSTALL_FAILURE_STORAGE": Failed to store the bundle information. &lt;/br&gt; "STATUS_INSTALL_FAILURE_INCOMPATIBLE": Installation incompatible (commonly caused by a downgrade installation or incorrect signature information). &lt;/br &gt; "STATUS_UNINSTALL_FAILURE": Uninstallation failure (the application to uninstall does not exist). &lt;/br&gt; " STATUS_UNINSTALL_FAILURE_ABORTED": Uninstallation aborted (not used). &lt;/br&gt; "STATUS_UNINSTALL_FAILURE_CONFLICT":Uninstallation conflict (failed to uninstall a system application or failed to terminate the application process). &lt;/br&gt; "STATUS_INSTALL_FAILURE_DOWNLOAD_TIMEOUT": Installation failure (download timed out).&lt;/br&gt; "STATUS_INSTALL_FAILURE_DOWNLOAD_FAILED": Installation failure (download failed). &lt;/br&gt; "STATUS_RECOVER_FAILURE_INVALID": Failed to recover the preset application. &lt;/br&gt; "STATUS_ABILITY_NOT_FOUND":Ability not found.&lt;/br&gt; "STATUS_BMS_SERVICE_ERROR": BMS service error. &lt;/br&gt; "STATUS_FAILED_NO_SPACE_LEFT": Insufficient device space.&lt;/br&gt; "STATUS_GRANT_REQUEST_PERMISSIONS_FAILED": Failed to grant application permissions. &lt;/br&gt; "STATUS_INSTALL_PERMISSION_DENIED": Installation permission missing. &lt;/br&gt; "STATUS_UNINSTALL_PERMISSION_DENIED": Uninstallation permission missing.

**Type:** string

**Default:** Indicates the install or uninstall result string message

**Since:** 7

**Deprecated since:** 9

<!--Device-InstallStatus-statusMessage: string--><!--Device-InstallStatus-statusMessage: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.
