# @ohos.dlpPermission

Data loss prevention (DLP) is a system solution provided to prevent data disclosure. This module provides APIs for cross-device file access management, encrypted storage, and access authorization. DLP protects sensitive files through encryption and generates encrypted files in .dlp format (DLP files). When opening a DLP file, the system automatically creates an isolated DLP sandbox environment to ensure that the file content is not leaked to unauthorized environments. > **NOTE：**> > - The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a > superscript to indicate their earliest API version. > > - The kit to which **@ohos.dlpPermission** belongs has been changed from `DataLossPreventionKit` to ` > DataProtectionKit`. You are advised to use the new module name `@ > kit.DataProtectionKit` to import the module. If `@ > kit.DataLossPreventionKit` is imported, only the APIs before the change can be called and the APIs after the change > cannot be used.

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare namespace dlpPermission--><!--Device-unnamed-declare namespace dlpPermission-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## Modules to Import

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cancelRetentionState](arkts-dataprotection-dlppermission-cancelretentionstate-f.md#cancelRetentionState) |
| [cancelRetentionState](arkts-dataprotection-dlppermission-cancelretentionstate-f.md#cancelRetentionState) |
| [cleanSandboxAppConfig](arkts-dataprotection-dlppermission-cleansandboxappconfig-f.md#cleanSandboxAppConfig) |
| [closeOpenedEnterpriseDlpFiles](arkts-dataprotection-dlppermission-closeopenedenterprisedlpfiles-f.md#closeOpenedEnterpriseDlpFiles) |
| [getControlledAppLists](arkts-dataprotection-dlppermission-getcontrolledapplists-f.md#getControlledAppLists) |
| [getDLPFileAccessRecords](arkts-dataprotection-dlppermission-getdlpfileaccessrecords-f.md#getDLPFileAccessRecords) |
| [getDLPFileAccessRecords](arkts-dataprotection-dlppermission-getdlpfileaccessrecords-f.md#getDLPFileAccessRecords) |
| [getDLPPermissionInfo](arkts-dataprotection-dlppermission-getdlppermissioninfo-f.md#getDLPPermissionInfo) |
| [getDLPPermissionInfo](arkts-dataprotection-dlppermission-getdlppermissioninfo-f.md#getDLPPermissionInfo) |
| [getDLPSuffix](arkts-dataprotection-dlppermission-getdlpsuffix-f.md#getDLPSuffix) |
| [getDLPSupportedFileTypes](arkts-dataprotection-dlppermission-getdlpsupportedfiletypes-f.md#getDLPSupportedFileTypes) |
| [getDLPSupportedFileTypes](arkts-dataprotection-dlppermission-getdlpsupportedfiletypes-f.md#getDLPSupportedFileTypes) |
| [getOriginalFileName](arkts-dataprotection-dlppermission-getoriginalfilename-f.md#getOriginalFileName) |
| [getRetentionSandboxList](arkts-dataprotection-dlppermission-getretentionsandboxlist-f.md#getRetentionSandboxList) |
| [getRetentionSandboxList](arkts-dataprotection-dlppermission-getretentionsandboxlist-f.md#getRetentionSandboxList) |
| [getRetentionSandboxList](arkts-dataprotection-dlppermission-getretentionsandboxlist-f.md#getRetentionSandboxList) |
| [getSandboxAppConfig](arkts-dataprotection-dlppermission-getsandboxappconfig-f.md#getSandboxAppConfig) |
| [isDLPFeatureProvided](arkts-dataprotection-dlppermission-isdlpfeatureprovided-f.md#isDLPFeatureProvided) |
| [isDLPFile](arkts-dataprotection-dlppermission-isdlpfile-f.md#isDLPFile) |
| [isDLPFile](arkts-dataprotection-dlppermission-isdlpfile-f.md#isDLPFile) |
| [isInSandbox](arkts-dataprotection-dlppermission-isinsandbox-f.md#isInSandbox) |
| [isInSandbox](arkts-dataprotection-dlppermission-isinsandbox-f.md#isInSandbox) |
| [off_openDLPFile](arkts-dataprotection-dlppermission-offopendlpfile-f.md#off_openDLPFile) |
| [on_openDLPFile](arkts-dataprotection-dlppermission-onopendlpfile-f.md#on_openDLPFile) |
| [processPluginCommand](arkts-dataprotection-dlppermission-processplugincommand-f.md#processPluginCommand) |
| [queryOpenedEnterpriseDlpFiles](arkts-dataprotection-dlppermission-queryopenedenterprisedlpfiles-f.md#queryOpenedEnterpriseDlpFiles) |
| [setControlledAppLists](arkts-dataprotection-dlppermission-setcontrolledapplists-f.md#setControlledAppLists) |
| [setEnterprisePolicy](arkts-dataprotection-dlppermission-setenterprisepolicy-f.md#setEnterprisePolicy) |
| [setRetentionState](arkts-dataprotection-dlppermission-setretentionstate-f.md#setRetentionState) |
| [setRetentionState](arkts-dataprotection-dlppermission-setretentionstate-f.md#setRetentionState) |
| [setSandboxAppConfig](arkts-dataprotection-dlppermission-setsandboxappconfig-f.md#setSandboxAppConfig) |
| [startDLPManagerForResult](arkts-dataprotection-dlppermission-startdlpmanagerforresult-f.md#startDLPManagerForResult) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [decryptDlpFile](arkts-dataprotection-dlppermission-decryptdlpfile-f-sys.md#decryptDlpFile-(System-API)) |
| [generateDLPFile](arkts-dataprotection-dlppermission-generatedlpfile-f-sys.md#generateDLPFile-(System-API)) |
| [generateDLPFile](arkts-dataprotection-dlppermission-generatedlpfile-f-sys.md#generateDLPFile-(System-API)) |
| [generateDlpFileForEnterprise](arkts-dataprotection-dlppermission-generatedlpfileforenterprise-f-sys.md#generateDlpFileForEnterprise-(System-API)) |
| [getDLPGatheringPolicy](arkts-dataprotection-dlppermission-getdlpgatheringpolicy-f-sys.md#getDLPGatheringPolicy-(System-API)) |
| [getDLPGatheringPolicy](arkts-dataprotection-dlppermission-getdlpgatheringpolicy-f-sys.md#getDLPGatheringPolicy-(System-API)) |
| [installDLPSandbox](arkts-dataprotection-dlppermission-installdlpsandbox-f-sys.md#installDLPSandbox-(System-API)) |
| [installDLPSandbox](arkts-dataprotection-dlppermission-installdlpsandbox-f-sys.md#installDLPSandbox-(System-API)) |
| [off_uninstallDLPSandbox](arkts-dataprotection-dlppermission-offuninstalldlpsandbox-f-sys.md#off_uninstallDLPSandbox) |
| [on_uninstallDLPSandbox](arkts-dataprotection-dlppermission-onuninstalldlpsandbox-f-sys.md#on_uninstallDLPSandbox) |
| [openDLPFile](arkts-dataprotection-dlppermission-opendlpfile-f-sys.md#openDLPFile-(System-API)) |
| [openDLPFile](arkts-dataprotection-dlppermission-opendlpfile-f-sys.md#openDLPFile-(System-API)) |
| [queryDlpPolicy](arkts-dataprotection-dlppermission-querydlppolicy-f-sys.md#queryDlpPolicy-(System-API)) |
| [uninstallDLPSandbox](arkts-dataprotection-dlppermission-uninstalldlpsandbox-f-sys.md#uninstallDLPSandbox-(System-API)) |
| [uninstallDLPSandbox](arkts-dataprotection-dlppermission-uninstalldlpsandbox-f-sys.md#uninstallDLPSandbox-(System-API)) |
<!--DelEnd-->

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DlpConnManager](arkts-dataprotection-dlppermission-dlpconnmanager-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AccessedDLPFileInfo](arkts-dataprotection-dlppermission-accesseddlpfileinfo-i.md) |
| [CustomProperty](arkts-dataprotection-dlppermission-customproperty-i.md) |
| [DLPManagerResult](arkts-dataprotection-dlppermission-dlpmanagerresult-i.md) |
| [DLPPermissionInfo](arkts-dataprotection-dlppermission-dlppermissioninfo-i.md) |
| [DLPProperty](arkts-dataprotection-dlppermission-dlpproperty-i.md) |
| [DlpConnPlugin](arkts-dataprotection-dlppermission-dlpconnplugin-i.md) |
| [DlpFileQueryOptions](arkts-dataprotection-dlppermission-dlpfilequeryoptions-i.md) |
| [EnterprisePolicy](arkts-dataprotection-dlppermission-enterprisepolicy-i.md) |
| [RetentionSandboxInfo](arkts-dataprotection-dlppermission-retentionsandboxinfo-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AuthUser](arkts-dataprotection-dlppermission-authuser-i-sys.md) |
| [CustomProperty](arkts-dataprotection-dlppermission-customproperty-i-sys.md) |
| [DLPFile](arkts-dataprotection-dlppermission-dlpfile-i-sys.md) |
| [DLPProperty](arkts-dataprotection-dlppermission-dlpproperty-i-sys.md) |
| [DLPSandboxInfo](arkts-dataprotection-dlppermission-dlpsandboxinfo-i-sys.md) |
| [DLPSandboxState](arkts-dataprotection-dlppermission-dlpsandboxstate-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AccountType](arkts-dataprotection-dlppermission-accounttype-e.md) |
| [ActionFlagType](arkts-dataprotection-dlppermission-actionflagtype-e.md) |
| [DLPFileAccess](arkts-dataprotection-dlppermission-dlpfileaccess-e.md) |
| [PluginCmd](arkts-dataprotection-dlppermission-plugincmd-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AccountType](arkts-dataprotection-dlppermission-accounttype-e-sys.md) |
| [ActionType](arkts-dataprotection-dlppermission-actiontype-e-sys.md) |
| [GatheringPolicyType](arkts-dataprotection-dlppermission-gatheringpolicytype-e-sys.md) |
<!--DelEnd-->
