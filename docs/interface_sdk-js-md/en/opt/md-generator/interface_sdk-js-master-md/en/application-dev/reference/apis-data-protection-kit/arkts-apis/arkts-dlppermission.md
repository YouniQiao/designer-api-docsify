# @ohos.dlpPermission(DLP)

Data loss prevention (DLP) is a system solution provided to prevent data disclosure. This module provides APIs for cross-device file access management, encrypted storage, and access authorization. DLP protects sensitive files through encryption and generates encrypted files in .dlp format (DLP files). When opening a DLP file, the system automatically creates an isolated DLP sandbox environment to ensure that the file content is not leaked to unauthorized environments.

> **NOTE：**
> 
> - The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a
> superscript to indicate their earliest API version.
> 
> - The kit to which **@ohos.dlpPermission** belongs has been changed from `DataLossPreventionKit` to `
> DataProtectionKit`. You are advised to use the new module name `@
> kit.DataProtectionKit` to import the module. If `@
> kit.DataLossPreventionKit` is imported, only the APIs before the change can be called and the APIs after the change
> cannot be used.

**Since:** 10

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
| [cancelRetentionState](arkts-dataprotection-dlppermission-cancelretentionstate-f.md#cancelretentionstate) |
| [cancelRetentionState](arkts-dataprotection-dlppermission-cancelretentionstate-f.md#cancelretentionstate-1) |
| [cleanSandboxAppConfig](arkts-dataprotection-dlppermission-cleansandboxappconfig-f.md#cleansandboxappconfig) |
| [closeOpenedEnterpriseDlpFiles](arkts-dataprotection-dlppermission-closeopenedenterprisedlpfiles-f.md#closeopenedenterprisedlpfiles) |
| [decryptDlpFile](arkts-dataprotection-dlppermission-decryptdlpfile-f.md#decryptdlpfile) |
| [generateDlpFileForEnterprise](arkts-dataprotection-dlppermission-generatedlpfileforenterprise-f.md#generatedlpfileforenterprise) |
| [getControlledAppLists](arkts-dataprotection-dlppermission-getcontrolledapplists-f.md#getcontrolledapplists) |
| [getDLPFileAccessRecords](arkts-dataprotection-dlppermission-getdlpfileaccessrecords-f.md#getdlpfileaccessrecords) |
| [getDLPFileAccessRecords](arkts-dataprotection-dlppermission-getdlpfileaccessrecords-f.md#getdlpfileaccessrecords-1) |
| [getDLPPermissionInfo](arkts-dataprotection-dlppermission-getdlppermissioninfo-f.md#getdlppermissioninfo) |
| [getDLPPermissionInfo](arkts-dataprotection-dlppermission-getdlppermissioninfo-f.md#getdlppermissioninfo-1) |
| [getDLPSuffix](arkts-dataprotection-dlppermission-getdlpsuffix-f.md#getdlpsuffix) |
| [getDLPSupportedFileTypes](arkts-dataprotection-dlppermission-getdlpsupportedfiletypes-f.md#getdlpsupportedfiletypes) |
| [getDLPSupportedFileTypes](arkts-dataprotection-dlppermission-getdlpsupportedfiletypes-f.md#getdlpsupportedfiletypes-1) |
| [getOriginalFileName](arkts-dataprotection-dlppermission-getoriginalfilename-f.md#getoriginalfilename) |
| [getRetentionSandboxList](arkts-dataprotection-dlppermission-getretentionsandboxlist-f.md#getretentionsandboxlist) |
| [getRetentionSandboxList](arkts-dataprotection-dlppermission-getretentionsandboxlist-f.md#getretentionsandboxlist-1) |
| [getRetentionSandboxList](arkts-dataprotection-dlppermission-getretentionsandboxlist-f.md#getretentionsandboxlist-2) |
| [getSandboxAppConfig](arkts-dataprotection-dlppermission-getsandboxappconfig-f.md#getsandboxappconfig) |
| [isDLPFeatureProvided](arkts-dataprotection-dlppermission-isdlpfeatureprovided-f.md#isdlpfeatureprovided) |
| [isDLPFile](arkts-dataprotection-dlppermission-isdlpfile-f.md#isdlpfile) |
| [isDLPFile](arkts-dataprotection-dlppermission-isdlpfile-f.md#isdlpfile-1) |
| [isInSandbox](arkts-dataprotection-dlppermission-isinsandbox-f.md#isinsandbox) |
| [isInSandbox](arkts-dataprotection-dlppermission-isinsandbox-f.md#isinsandbox-1) |
| [off](arkts-dataprotection-dlppermission-off-f.md#off) |
| [on](arkts-dataprotection-dlppermission-on-f.md#on) |
| [processPluginCommand](arkts-dataprotection-dlppermission-processplugincommand-f.md#processplugincommand) |
| [queryDlpPolicy](arkts-dataprotection-dlppermission-querydlppolicy-f.md#querydlppolicy) |
| [queryOpenedEnterpriseDlpFiles](arkts-dataprotection-dlppermission-queryopenedenterprisedlpfiles-f.md#queryopenedenterprisedlpfiles) |
| [setControlledAppLists](arkts-dataprotection-dlppermission-setcontrolledapplists-f.md#setcontrolledapplists) |
| [setEnterprisePolicy](arkts-dataprotection-dlppermission-setenterprisepolicy-f.md#setenterprisepolicy) |
| [setRetentionState](arkts-dataprotection-dlppermission-setretentionstate-f.md#setretentionstate) |
| [setRetentionState](arkts-dataprotection-dlppermission-setretentionstate-f.md#setretentionstate-1) |
| [setSandboxAppConfig](arkts-dataprotection-dlppermission-setsandboxappconfig-f.md#setsandboxappconfig) |
| [startDLPManagerForResult](arkts-dataprotection-dlppermission-startdlpmanagerforresult-f.md#startdlpmanagerforresult) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [generateDLPFile](arkts-dataprotection-dlppermission-generatedlpfile-f-sys.md#generatedlpfile) |
| [generateDLPFile](arkts-dataprotection-dlppermission-generatedlpfile-f-sys.md#generatedlpfile-1) |
| [getDLPGatheringPolicy](arkts-dataprotection-dlppermission-getdlpgatheringpolicy-f-sys.md#getdlpgatheringpolicy) |
| [getDLPGatheringPolicy](arkts-dataprotection-dlppermission-getdlpgatheringpolicy-f-sys.md#getdlpgatheringpolicy-1) |
| [installDLPSandbox](arkts-dataprotection-dlppermission-installdlpsandbox-f-sys.md#installdlpsandbox) |
| [installDLPSandbox](arkts-dataprotection-dlppermission-installdlpsandbox-f-sys.md#installdlpsandbox-1) |
| [off](arkts-dataprotection-dlppermission-off-f-sys.md#off-1) |
| [on](arkts-dataprotection-dlppermission-on-f-sys.md#on-1) |
| [openDLPFile](arkts-dataprotection-dlppermission-opendlpfile-f-sys.md#opendlpfile) |
| [openDLPFile](arkts-dataprotection-dlppermission-opendlpfile-f-sys.md#opendlpfile-1) |
| [uninstallDLPSandbox](arkts-dataprotection-dlppermission-uninstalldlpsandbox-f-sys.md#uninstalldlpsandbox) |
| [uninstallDLPSandbox](arkts-dataprotection-dlppermission-uninstalldlpsandbox-f-sys.md#uninstalldlpsandbox-1) |
<!--DelEnd-->

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DlpConnManager](arkts-dataprotection-dlppermission-dlpconnmanager-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AccessedDLPFileInfo](arkts-dataprotection-dlppermission-accesseddlpfileinfo-i.md) |
| [AuthUser](arkts-dataprotection-dlppermission-authuser-i.md) |
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
| [DLPFile](arkts-dataprotection-dlppermission-dlpfile-i-sys.md) |
| [DLPSandboxInfo](arkts-dataprotection-dlppermission-dlpsandboxinfo-i-sys.md) |
| [DLPSandboxState](arkts-dataprotection-dlppermission-dlpsandboxstate-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AccountType](arkts-dataprotection-dlppermission-accounttype-e.md) |
| [ActionFlagType](arkts-dataprotection-dlppermission-actionflagtype-e.md) |
| [ActionType](arkts-dataprotection-dlppermission-actiontype-e.md) |
| [DLPFileAccess](arkts-dataprotection-dlppermission-dlpfileaccess-e.md) |
| [PluginCmd](arkts-dataprotection-dlppermission-plugincmd-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [GatheringPolicyType](arkts-dataprotection-dlppermission-gatheringpolicytype-e-sys.md) |
<!--DelEnd-->
