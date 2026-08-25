# @ohos.dlpPermission(数据防泄漏)

数据防泄漏（Data Loss Prevention，简称为DLP）是系统级的数据防泄漏解决方案，提供跨设备文件的权限管理、加密存储、授权访问等能力。DLP通过加密技术对敏感文件进行保护，生成.dlp格式的加密文件（称为DLP文件）。 当打开DLP文件时，系统会自动创建隔离的DLP沙箱环境，确保文件内容不会泄漏到非授权环境。

> **说明：**&gt;
> - 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
> - @ohos.dlpPermission归属的Kit已由`DataLossPreventionKit`变更为`DataProtectionKit`，建议开发者使用新模块名`@
> kit.DataProtectionKit`完成模块导入。如果使用`@
> kit.DataLossPreventionKit`导入，仅能调用改名前的接口，无法使用新增接口。

**起始版本：** 10

**系统能力：** SystemCapability.Security.DataLossPrevention

## 导入模块

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [cancelRetentionState(数据防泄漏)](arkts-dataprotection-dlppermission-cancelretentionstate-f.md) |
| [cancelRetentionState(数据防泄漏)](arkts-dataprotection-dlppermission-cancelretentionstate-f.md) |
| [cleanSandboxAppConfig(数据防泄漏)](arkts-dataprotection-dlppermission-cleansandboxappconfig-f.md) |
| [closeOpenedEnterpriseDlpFiles(数据防泄漏)](arkts-dataprotection-dlppermission-closeopenedenterprisedlpfiles-f.md) |
| [decryptDlpFile(数据防泄漏)](arkts-dataprotection-dlppermission-decryptdlpfile-f.md) |
| [generateDlpFileForEnterprise(数据防泄漏)](arkts-dataprotection-dlppermission-generatedlpfileforenterprise-f.md) |
| [getControlledAppLists(数据防泄漏)](arkts-dataprotection-dlppermission-getcontrolledapplists-f.md) |
| [getDLPFileAccessRecords(数据防泄漏)](arkts-dataprotection-dlppermission-getdlpfileaccessrecords-f.md) |
| [getDLPFileAccessRecords(数据防泄漏)](arkts-dataprotection-dlppermission-getdlpfileaccessrecords-f.md) |
| [getDLPPermissionInfo(数据防泄漏)](arkts-dataprotection-dlppermission-getdlppermissioninfo-f.md) |
| [getDLPPermissionInfo(数据防泄漏)](arkts-dataprotection-dlppermission-getdlppermissioninfo-f.md) |
| [getDLPSuffix(数据防泄漏)](arkts-dataprotection-dlppermission-getdlpsuffix-f.md) |
| [getDLPSupportedFileTypes(数据防泄漏)](arkts-dataprotection-dlppermission-getdlpsupportedfiletypes-f.md) |
| [getDLPSupportedFileTypes(数据防泄漏)](arkts-dataprotection-dlppermission-getdlpsupportedfiletypes-f.md) |
| [getOriginalFileName(数据防泄漏)](arkts-dataprotection-dlppermission-getoriginalfilename-f.md) |
| [getRetentionSandboxList(数据防泄漏)](arkts-dataprotection-dlppermission-getretentionsandboxlist-f.md) |
| [getRetentionSandboxList(数据防泄漏)](arkts-dataprotection-dlppermission-getretentionsandboxlist-f.md) |
| [getRetentionSandboxList(数据防泄漏)](arkts-dataprotection-dlppermission-getretentionsandboxlist-f.md) |
| [getSandboxAppConfig(数据防泄漏)](arkts-dataprotection-dlppermission-getsandboxappconfig-f.md) |
| [isDLPFeatureProvided(数据防泄漏)](arkts-dataprotection-dlppermission-isdlpfeatureprovided-f.md) |
| [isDLPFile(数据防泄漏)](arkts-dataprotection-dlppermission-isdlpfile-f.md) |
| [isDLPFile(数据防泄漏)](arkts-dataprotection-dlppermission-isdlpfile-f.md) |
| [isInSandbox(数据防泄漏)](arkts-dataprotection-dlppermission-isinsandbox-f.md) |
| [isInSandbox(数据防泄漏)](arkts-dataprotection-dlppermission-isinsandbox-f.md) |
| [off(数据防泄漏)](arkts-dataprotection-dlppermission-off-f.md#offopendlpfile) |
| [on(数据防泄漏)](arkts-dataprotection-dlppermission-on-f.md#onopendlpfile) |
| [queryDlpPolicy(数据防泄漏)](arkts-dataprotection-dlppermission-querydlppolicy-f.md) |
| [queryOpenedEnterpriseDlpFiles(数据防泄漏)](arkts-dataprotection-dlppermission-queryopenedenterprisedlpfiles-f.md) |
| [setControlledAppLists(数据防泄漏)](arkts-dataprotection-dlppermission-setcontrolledapplists-f.md) |
| [setEnterprisePolicy(数据防泄漏)](arkts-dataprotection-dlppermission-setenterprisepolicy-f.md) |
| [setRetentionState(数据防泄漏)](arkts-dataprotection-dlppermission-setretentionstate-f.md) |
| [setRetentionState(数据防泄漏)](arkts-dataprotection-dlppermission-setretentionstate-f.md) |
| [setSandboxAppConfig(数据防泄漏)](arkts-dataprotection-dlppermission-setsandboxappconfig-f.md) |
| [startDLPManagerForResult(数据防泄漏)](arkts-dataprotection-dlppermission-startdlpmanagerforresult-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [generateDLPFile(数据防泄漏)](arkts-dataprotection-dlppermission-generatedlpfile-f-sys.md) |
| [generateDLPFile(数据防泄漏)](arkts-dataprotection-dlppermission-generatedlpfile-f-sys.md) |
| [getDLPGatheringPolicy(数据防泄漏)](arkts-dataprotection-dlppermission-getdlpgatheringpolicy-f-sys.md) |
| [getDLPGatheringPolicy(数据防泄漏)](arkts-dataprotection-dlppermission-getdlpgatheringpolicy-f-sys.md) |
| [installDLPSandbox(数据防泄漏)](arkts-dataprotection-dlppermission-installdlpsandbox-f-sys.md) |
| [installDLPSandbox(数据防泄漏)](arkts-dataprotection-dlppermission-installdlpsandbox-f-sys.md) |
| [off(数据防泄漏)](arkts-dataprotection-dlppermission-uninstalldlpsandbox-f-sys.md) |
| [on(数据防泄漏)](arkts-dataprotection-dlppermission-uninstalldlpsandbox-f-sys.md) |
| [openDLPFile(数据防泄漏)](arkts-dataprotection-dlppermission-opendlpfile-f-sys.md) |
| [openDLPFile(数据防泄漏)](arkts-dataprotection-dlppermission-opendlpfile-f-sys.md) |
| [uninstallDLPSandbox(数据防泄漏)](arkts-dataprotection-dlppermission-uninstalldlpsandbox-f-sys.md) |
| [uninstallDLPSandbox(数据防泄漏)](arkts-dataprotection-dlppermission-uninstalldlpsandbox-f-sys.md) |
<!--DelEnd-->

### 类

| 名称 |
| --- |
| [DlpConnManager(数据防泄漏)](arkts-dataprotection-dlppermission-dlpconnmanager-c.md) |

### 接口

| 名称 |
| --- |
| [AccessedDLPFileInfo(数据防泄漏)](arkts-dataprotection-dlppermission-accesseddlpfileinfo-i.md) |
| [AuthUser(数据防泄漏)](arkts-dataprotection-dlppermission-authuser-i.md) |
| [CustomProperty(数据防泄漏)](arkts-dataprotection-dlppermission-customproperty-i.md) |
| [DlpConnPlugin(数据防泄漏)](arkts-dataprotection-dlppermission-dlpconnplugin-i.md) |
| [DlpFileQueryOptions(数据防泄漏)](arkts-dataprotection-dlppermission-dlpfilequeryoptions-i.md) |
| [DLPManagerResult(数据防泄漏)](arkts-dataprotection-dlppermission-dlpmanagerresult-i.md) |
| [DLPPermissionInfo(数据防泄漏)](arkts-dataprotection-dlppermission-dlppermissioninfo-i.md) |
| [DLPProperty(数据防泄漏)](arkts-dataprotection-dlppermission-dlpproperty-i.md) |
| [EnterprisePolicy(数据防泄漏)](arkts-dataprotection-dlppermission-enterprisepolicy-i.md) |
| [RetentionSandboxInfo(数据防泄漏)](arkts-dataprotection-dlppermission-retentionsandboxinfo-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [DLPFile(数据防泄漏)](arkts-dataprotection-dlppermission-dlpfile-i-sys.md) |
| [DLPSandboxInfo(数据防泄漏)](arkts-dataprotection-dlppermission-dlpsandboxinfo-i-sys.md) |
| [DLPSandboxState(数据防泄漏)](arkts-dataprotection-dlppermission-dlpsandboxstate-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [AccountType(数据防泄漏)](arkts-dataprotection-dlppermission-accounttype-e.md) |
| [ActionFlagType(数据防泄漏)](arkts-dataprotection-dlppermission-actionflagtype-e.md) |
| [ActionType(数据防泄漏)](arkts-dataprotection-dlppermission-actiontype-e.md) |
| [DLPFileAccess(数据防泄漏)](arkts-dataprotection-dlppermission-dlpfileaccess-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [GatheringPolicyType(数据防泄漏)](arkts-dataprotection-dlppermission-gatheringpolicytype-e-sys.md) |
<!--DelEnd-->
