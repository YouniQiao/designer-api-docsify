# @ohos.dlpPermission

Data loss prevention (DLP) is a system solution provided to prevent data disclosure. This module provides APIs for cross-device file access management, encrypted storage, and access authorization. DLP protects sensitive files through encryption and generates encrypted files in .dlp format (DLP files). When opening a DLP file, the system automatically creates an isolated DLP sandbox environment to ensure that the file content is not leaked to unauthorized environments. > **NOTE：**> > - The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a > superscript to indicate their earliest API version. > > - The kit to which **@ohos.dlpPermission** belongs has been changed from `DataLossPreventionKit` to ` > DataProtectionKit`. You are advised to use the new module name `@ > kit.DataProtectionKit` to import the module. If `@ > kit.DataLossPreventionKit` is imported, only the APIs before the change can be called and the APIs after the change > cannot be used.

**Since:** 10

<!--Device-unnamed-declare namespace dlpPermission--><!--Device-unnamed-declare namespace dlpPermission-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cancelRetentionState](arkts-dataprotection-dlppermission-cancelretentionstate-f.md#cancelretentionstate) |
| [cancelRetentionState](arkts-dataprotection-dlppermission-cancelretentionstate-f.md#cancelretentionstate) |
| [cleanSandboxAppConfig](arkts-dataprotection-dlppermission-cleansandboxappconfig-f.md#cleansandboxappconfig) |
| [closeOpenedEnterpriseDlpFiles](arkts-dataprotection-dlppermission-closeopenedenterprisedlpfiles-f.md#closeopenedenterprisedlpfiles) |
| [getControlledAppLists](arkts-dataprotection-dlppermission-getcontrolledapplists-f.md#getcontrolledapplists) |
| [getDLPFileAccessRecords](arkts-dataprotection-dlppermission-getdlpfileaccessrecords-f.md#getdlpfileaccessrecords) |
| [getDLPFileAccessRecords](arkts-dataprotection-dlppermission-getdlpfileaccessrecords-f.md#getdlpfileaccessrecords) |
| [getDLPPermissionInfo](arkts-dataprotection-dlppermission-getdlppermissioninfo-f.md#getdlppermissioninfo) |
| [getDLPPermissionInfo](arkts-dataprotection-dlppermission-getdlppermissioninfo-f.md#getdlppermissioninfo) |
| [getDLPSuffix](arkts-dataprotection-dlppermission-getdlpsuffix-f.md#getdlpsuffix) |
| [getDLPSupportedFileTypes](arkts-dataprotection-dlppermission-getdlpsupportedfiletypes-f.md#getdlpsupportedfiletypes) |
| [getDLPSupportedFileTypes](arkts-dataprotection-dlppermission-getdlpsupportedfiletypes-f.md#getdlpsupportedfiletypes) |
| [getOriginalFileName](arkts-dataprotection-dlppermission-getoriginalfilename-f.md#getoriginalfilename) |
| [getRetentionSandboxList](arkts-dataprotection-dlppermission-getretentionsandboxlist-f.md#getretentionsandboxlist) |
| [getRetentionSandboxList](arkts-dataprotection-dlppermission-getretentionsandboxlist-f.md#getretentionsandboxlist) |
| [getRetentionSandboxList](arkts-dataprotection-dlppermission-getretentionsandboxlist-f.md#getretentionsandboxlist) |
| [getSandboxAppConfig](arkts-dataprotection-dlppermission-getsandboxappconfig-f.md#getsandboxappconfig) |
| [isDLPFeatureProvided](arkts-dataprotection-dlppermission-isdlpfeatureprovided-f.md#isdlpfeatureprovided) |
| [isDLPFile](arkts-dataprotection-dlppermission-isdlpfile-f.md#isdlpfile) |
| [isDLPFile](arkts-dataprotection-dlppermission-isdlpfile-f.md#isdlpfile) |
| [isInSandbox](arkts-dataprotection-dlppermission-isinsandbox-f.md#isinsandbox) |
| [isInSandbox](arkts-dataprotection-dlppermission-isinsandbox-f.md#isinsandbox) |
| [off_openDLPFile](arkts-dataprotection-dlppermission-offopendlpfile-f.md#offopendlpfile) |
| [on_openDLPFile](arkts-dataprotection-dlppermission-onopendlpfile-f.md#onopendlpfile) |
| [processPluginCommand](arkts-dataprotection-dlppermission-processplugincommand-f.md#processplugincommand) |
| [queryOpenedEnterpriseDlpFiles](arkts-dataprotection-dlppermission-queryopenedenterprisedlpfiles-f.md#queryopenedenterprisedlpfiles) |
| [setControlledAppLists](arkts-dataprotection-dlppermission-setcontrolledapplists-f.md#setcontrolledapplists) |
| [setEnterprisePolicy](arkts-dataprotection-dlppermission-setenterprisepolicy-f.md#setenterprisepolicy) |
| [setRetentionState](arkts-dataprotection-dlppermission-setretentionstate-f.md#setretentionstate) |
| [setRetentionState](arkts-dataprotection-dlppermission-setretentionstate-f.md#setretentionstate) |
| [setSandboxAppConfig](arkts-dataprotection-dlppermission-setsandboxappconfig-f.md#setsandboxappconfig) |
| [startDLPManagerForResult](arkts-dataprotection-dlppermission-startdlpmanagerforresult-f.md#startdlpmanagerforresult) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [decryptDlpFile](arkts-dataprotection-dlppermission-decryptdlpfile-f-sys.md#decryptdlpfile-system-api) |
| [generateDLPFile](arkts-dataprotection-dlppermission-generatedlpfile-f-sys.md#generatedlpfile-system-api) |
| [generateDLPFile](arkts-dataprotection-dlppermission-generatedlpfile-f-sys.md#generatedlpfile-system-api) |
| [generateDlpFileForEnterprise](arkts-dataprotection-dlppermission-generatedlpfileforenterprise-f-sys.md#generatedlpfileforenterprise-system-api) |
| [getDLPGatheringPolicy](arkts-dataprotection-dlppermission-getdlpgatheringpolicy-f-sys.md#getdlpgatheringpolicy-system-api) |
| [getDLPGatheringPolicy](arkts-dataprotection-dlppermission-getdlpgatheringpolicy-f-sys.md#getdlpgatheringpolicy-system-api) |
| [installDLPSandbox](arkts-dataprotection-dlppermission-installdlpsandbox-f-sys.md#installdlpsandbox-system-api) |
| [installDLPSandbox](arkts-dataprotection-dlppermission-installdlpsandbox-f-sys.md#installdlpsandbox-system-api) |
| [off_uninstallDLPSandbox](arkts-dataprotection-dlppermission-offuninstalldlpsandbox-f-sys.md#offuninstalldlpsandbox) |
| [on_uninstallDLPSandbox](arkts-dataprotection-dlppermission-onuninstalldlpsandbox-f-sys.md#onuninstalldlpsandbox) |
| [openDLPFile](arkts-dataprotection-dlppermission-opendlpfile-f-sys.md#opendlpfile-system-api) |
| [openDLPFile](arkts-dataprotection-dlppermission-opendlpfile-f-sys.md#opendlpfile-system-api) |
| [queryDlpPolicy](arkts-dataprotection-dlppermission-querydlppolicy-f-sys.md#querydlppolicy-system-api) |
| [uninstallDLPSandbox](arkts-dataprotection-dlppermission-uninstalldlpsandbox-f-sys.md#uninstalldlpsandbox-system-api) |
| [uninstallDLPSandbox](arkts-dataprotection-dlppermission-uninstalldlpsandbox-f-sys.md#uninstalldlpsandbox-system-api) |
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
