# @ohos.dlpPermission(DLP)

Data loss prevention (DLP) is a system solution provided to prevent data disclosure. This module provides APIs for cross-device file access management, encrypted storage, and access authorization. DLP protects sensitive files through encryption and generates encrypted files in .dlp format (DLP files). When opening a DLP file, the system automatically creates an isolated DLP sandbox environment to ensure that the file content is not leaked to unauthorized environments.

> **NOTE：**&gt;
> - The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a
> superscript to indicate their earliest API version.&gt;
> - The kit to which **@ohos.dlpPermission** belongs has been changed from `DataLossPreventionKit` to `
> DataProtectionKit`. You are advised to use the new module name `@
> kit.DataProtectionKit` to import the module. If `@
> kit.DataLossPreventionKit` is imported, only the APIs before the change can be called and the APIs after the change
> cannot be used.

**Since:** 10

**System capability:** SystemCapability.Security.DataLossPrevention

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cancelRetentionState(DLP)](arkts-dataprotection-dlppermission-cancelretentionstate-f.md) |
| [cancelRetentionState(DLP)](arkts-dataprotection-dlppermission-cancelretentionstate-f.md) |
| [cleanSandboxAppConfig(DLP)](arkts-dataprotection-dlppermission-cleansandboxappconfig-f.md) |
| [closeOpenedEnterpriseDlpFiles(DLP)](arkts-dataprotection-dlppermission-closeopenedenterprisedlpfiles-f.md) |
| [decryptDlpFile(DLP)](arkts-dataprotection-dlppermission-decryptdlpfile-f.md) |
| [generateDlpFileForEnterprise(DLP)](arkts-dataprotection-dlppermission-generatedlpfileforenterprise-f.md) |
| [getControlledAppLists(DLP)](arkts-dataprotection-dlppermission-getcontrolledapplists-f.md) |
| [getDLPFileAccessRecords(DLP)](arkts-dataprotection-dlppermission-getdlpfileaccessrecords-f.md) |
| [getDLPFileAccessRecords(DLP)](arkts-dataprotection-dlppermission-getdlpfileaccessrecords-f.md) |
| [getDLPPermissionInfo(DLP)](arkts-dataprotection-dlppermission-getdlppermissioninfo-f.md) |
| [getDLPPermissionInfo(DLP)](arkts-dataprotection-dlppermission-getdlppermissioninfo-f.md) |
| [getDLPSuffix(DLP)](arkts-dataprotection-dlppermission-getdlpsuffix-f.md) |
| [getDLPSupportedFileTypes(DLP)](arkts-dataprotection-dlppermission-getdlpsupportedfiletypes-f.md) |
| [getDLPSupportedFileTypes(DLP)](arkts-dataprotection-dlppermission-getdlpsupportedfiletypes-f.md) |
| [getOriginalFileName(DLP)](arkts-dataprotection-dlppermission-getoriginalfilename-f.md) |
| [getRetentionSandboxList(DLP)](arkts-dataprotection-dlppermission-getretentionsandboxlist-f.md) |
| [getRetentionSandboxList(DLP)](arkts-dataprotection-dlppermission-getretentionsandboxlist-f.md) |
| [getRetentionSandboxList(DLP)](arkts-dataprotection-dlppermission-getretentionsandboxlist-f.md) |
| [getSandboxAppConfig(DLP)](arkts-dataprotection-dlppermission-getsandboxappconfig-f.md) |
| [isDLPFeatureProvided(DLP)](arkts-dataprotection-dlppermission-isdlpfeatureprovided-f.md) |
| [isDLPFile(DLP)](arkts-dataprotection-dlppermission-isdlpfile-f.md) |
| [isDLPFile(DLP)](arkts-dataprotection-dlppermission-isdlpfile-f.md) |
| [isInSandbox(DLP)](arkts-dataprotection-dlppermission-isinsandbox-f.md) |
| [isInSandbox(DLP)](arkts-dataprotection-dlppermission-isinsandbox-f.md) |
| [off(DLP)](arkts-dataprotection-dlppermission-off-f.md#offopendlpfile) |
| [on(DLP)](arkts-dataprotection-dlppermission-on-f.md#onopendlpfile) |
| [processPluginCommand(DLP)](arkts-dataprotection-dlppermission-processplugincommand-f.md) |
| [queryDlpPolicy(DLP)](arkts-dataprotection-dlppermission-querydlppolicy-f.md) |
| [queryOpenedEnterpriseDlpFiles(DLP)](arkts-dataprotection-dlppermission-queryopenedenterprisedlpfiles-f.md) |
| [setControlledAppLists(DLP)](arkts-dataprotection-dlppermission-setcontrolledapplists-f.md) |
| [setEnterprisePolicy(DLP)](arkts-dataprotection-dlppermission-setenterprisepolicy-f.md) |
| [setRetentionState(DLP)](arkts-dataprotection-dlppermission-setretentionstate-f.md) |
| [setRetentionState(DLP)](arkts-dataprotection-dlppermission-setretentionstate-f.md) |
| [setSandboxAppConfig(DLP)](arkts-dataprotection-dlppermission-setsandboxappconfig-f.md) |
| [startDLPManagerForResult(DLP)](arkts-dataprotection-dlppermission-startdlpmanagerforresult-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [generateDLPFile(DLP)](arkts-dataprotection-dlppermission-generatedlpfile-f-sys.md) |
| [generateDLPFile(DLP)](arkts-dataprotection-dlppermission-generatedlpfile-f-sys.md) |
| [getDLPGatheringPolicy(DLP)](arkts-dataprotection-dlppermission-getdlpgatheringpolicy-f-sys.md) |
| [getDLPGatheringPolicy(DLP)](arkts-dataprotection-dlppermission-getdlpgatheringpolicy-f-sys.md) |
| [installDLPSandbox(DLP)](arkts-dataprotection-dlppermission-installdlpsandbox-f-sys.md) |
| [installDLPSandbox(DLP)](arkts-dataprotection-dlppermission-installdlpsandbox-f-sys.md) |
| [off(DLP)](arkts-dataprotection-dlppermission-uninstalldlpsandbox-f-sys.md) |
| [on(DLP)](arkts-dataprotection-dlppermission-uninstalldlpsandbox-f-sys.md) |
| [openDLPFile(DLP)](arkts-dataprotection-dlppermission-opendlpfile-f-sys.md) |
| [openDLPFile(DLP)](arkts-dataprotection-dlppermission-opendlpfile-f-sys.md) |
| [uninstallDLPSandbox(DLP)](arkts-dataprotection-dlppermission-uninstalldlpsandbox-f-sys.md) |
| [uninstallDLPSandbox(DLP)](arkts-dataprotection-dlppermission-uninstalldlpsandbox-f-sys.md) |
<!--DelEnd-->

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DlpConnManager(DLP)](arkts-dataprotection-dlppermission-dlpconnmanager-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AccessedDLPFileInfo(DLP)](arkts-dataprotection-dlppermission-accesseddlpfileinfo-i.md) |
| [AuthUser(DLP)](arkts-dataprotection-dlppermission-authuser-i.md) |
| [CustomProperty(DLP)](arkts-dataprotection-dlppermission-customproperty-i.md) |
| [DlpConnPlugin(DLP)](arkts-dataprotection-dlppermission-dlpconnplugin-i.md) |
| [DlpFileQueryOptions(DLP)](arkts-dataprotection-dlppermission-dlpfilequeryoptions-i.md) |
| [DLPManagerResult(DLP)](arkts-dataprotection-dlppermission-dlpmanagerresult-i.md) |
| [DLPPermissionInfo(DLP)](arkts-dataprotection-dlppermission-dlppermissioninfo-i.md) |
| [DLPProperty(DLP)](arkts-dataprotection-dlppermission-dlpproperty-i.md) |
| [EnterprisePolicy(DLP)](arkts-dataprotection-dlppermission-enterprisepolicy-i.md) |
| [RetentionSandboxInfo(DLP)](arkts-dataprotection-dlppermission-retentionsandboxinfo-i.md) |

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DLPFile(DLP)](arkts-dataprotection-dlppermission-dlpfile-i-sys.md) |
| [DLPSandboxInfo(DLP)](arkts-dataprotection-dlppermission-dlpsandboxinfo-i-sys.md) |
| [DLPSandboxState(DLP)](arkts-dataprotection-dlppermission-dlpsandboxstate-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AccountType(DLP)](arkts-dataprotection-dlppermission-accounttype-e.md) |
| [ActionFlagType(DLP)](arkts-dataprotection-dlppermission-actionflagtype-e.md) |
| [ActionType(DLP)](arkts-dataprotection-dlppermission-actiontype-e.md) |
| [DLPFileAccess(DLP)](arkts-dataprotection-dlppermission-dlpfileaccess-e.md) |
| [PluginCmd(DLP)](arkts-dataprotection-dlppermission-plugincmd-e.md) |

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [GatheringPolicyType(DLP)](arkts-dataprotection-dlppermission-gatheringpolicytype-e-sys.md) |
<!--DelEnd-->
