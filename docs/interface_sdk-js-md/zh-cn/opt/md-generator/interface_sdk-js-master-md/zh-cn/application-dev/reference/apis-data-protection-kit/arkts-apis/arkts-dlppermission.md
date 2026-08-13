# @ohos.dlpPermission

数据防泄漏（Data Loss Prevention，简称为DLP）是系统级的数据防泄漏解决方案，提供跨设备文件的权限管理、加密存储、授权访问等能力。DLP通过加密技术对敏感文件进行保护，生成.dlp格式的加密文件（称为DLP文件）。 当打开DLP文件时，系统会自动创建隔离的DLP沙箱环境，确保文件内容不会泄漏到非授权环境。 > **说明：** > > - 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 > - @ohos.dlpPermission归属的Kit已由`DataLossPreventionKit`变更为`DataProtectionKit`，建议开发者使用新模块名`@ > kit.DataProtectionKit`完成模块导入。如果使用`@ > kit.DataLossPreventionKit`导入，仅能调用改名前的接口，无法使用新增接口。

**起始版本：** 10

**废弃版本：** -1

<!--Device-unnamed-declare namespace dlpPermission--><!--Device-unnamed-declare namespace dlpPermission-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

## 汇总

### 函数

| 名称 |
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
| [queryOpenedEnterpriseDlpFiles](arkts-dataprotection-dlppermission-queryopenedenterprisedlpfiles-f.md#queryOpenedEnterpriseDlpFiles) |
| [setControlledAppLists](arkts-dataprotection-dlppermission-setcontrolledapplists-f.md#setControlledAppLists) |
| [setEnterprisePolicy](arkts-dataprotection-dlppermission-setenterprisepolicy-f.md#setEnterprisePolicy) |
| [setRetentionState](arkts-dataprotection-dlppermission-setretentionstate-f.md#setRetentionState) |
| [setRetentionState](arkts-dataprotection-dlppermission-setretentionstate-f.md#setRetentionState) |
| [setSandboxAppConfig](arkts-dataprotection-dlppermission-setsandboxappconfig-f.md#setSandboxAppConfig) |
| [startDLPManagerForResult](arkts-dataprotection-dlppermission-startdlpmanagerforresult-f.md#startDLPManagerForResult) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [decryptDlpFile](arkts-dataprotection-dlppermission-decryptdlpfile-f-sys.md#decryptDlpFile（系统接口）) |
| [generateDLPFile](arkts-dataprotection-dlppermission-generatedlpfile-f-sys.md#generateDLPFile（系统接口）) |
| [generateDLPFile](arkts-dataprotection-dlppermission-generatedlpfile-f-sys.md#generateDLPFile（系统接口）) |
| [generateDlpFileForEnterprise](arkts-dataprotection-dlppermission-generatedlpfileforenterprise-f-sys.md#generateDlpFileForEnterprise（系统接口）) |
| [getDLPGatheringPolicy](arkts-dataprotection-dlppermission-getdlpgatheringpolicy-f-sys.md#getDLPGatheringPolicy（系统接口）) |
| [getDLPGatheringPolicy](arkts-dataprotection-dlppermission-getdlpgatheringpolicy-f-sys.md#getDLPGatheringPolicy（系统接口）) |
| [installDLPSandbox](arkts-dataprotection-dlppermission-installdlpsandbox-f-sys.md#installDLPSandbox（系统接口）) |
| [installDLPSandbox](arkts-dataprotection-dlppermission-installdlpsandbox-f-sys.md#installDLPSandbox（系统接口）) |
| [off_uninstallDLPSandbox](arkts-dataprotection-dlppermission-offuninstalldlpsandbox-f-sys.md#off_uninstallDLPSandbox) |
| [on_uninstallDLPSandbox](arkts-dataprotection-dlppermission-onuninstalldlpsandbox-f-sys.md#on_uninstallDLPSandbox) |
| [openDLPFile](arkts-dataprotection-dlppermission-opendlpfile-f-sys.md#openDLPFile（系统接口）) |
| [openDLPFile](arkts-dataprotection-dlppermission-opendlpfile-f-sys.md#openDLPFile（系统接口）) |
| [queryDlpPolicy](arkts-dataprotection-dlppermission-querydlppolicy-f-sys.md#queryDlpPolicy（系统接口）) |
| [uninstallDLPSandbox](arkts-dataprotection-dlppermission-uninstalldlpsandbox-f-sys.md#uninstallDLPSandbox（系统接口）) |
| [uninstallDLPSandbox](arkts-dataprotection-dlppermission-uninstalldlpsandbox-f-sys.md#uninstallDLPSandbox（系统接口）) |
<!--DelEnd-->

### 类

| 名称 |
| --- |
| [DlpConnManager](arkts-dataprotection-dlppermission-dlpconnmanager-c.md) |

### 接口

| 名称 |
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
### 接口（系统接口）

| 名称 |
| --- |
| [AuthUser](arkts-dataprotection-dlppermission-authuser-i-sys.md) |
| [CustomProperty](arkts-dataprotection-dlppermission-customproperty-i-sys.md) |
| [DLPFile](arkts-dataprotection-dlppermission-dlpfile-i-sys.md) |
| [DLPProperty](arkts-dataprotection-dlppermission-dlpproperty-i-sys.md) |
| [DLPSandboxInfo](arkts-dataprotection-dlppermission-dlpsandboxinfo-i-sys.md) |
| [DLPSandboxState](arkts-dataprotection-dlppermission-dlpsandboxstate-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [AccountType](arkts-dataprotection-dlppermission-accounttype-e.md) |
| [ActionFlagType](arkts-dataprotection-dlppermission-actionflagtype-e.md) |
| [DLPFileAccess](arkts-dataprotection-dlppermission-dlpfileaccess-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [AccountType](arkts-dataprotection-dlppermission-accounttype-e-sys.md) |
| [ActionType](arkts-dataprotection-dlppermission-actiontype-e-sys.md) |
| [GatheringPolicyType](arkts-dataprotection-dlppermission-gatheringpolicytype-e-sys.md) |
<!--DelEnd-->
