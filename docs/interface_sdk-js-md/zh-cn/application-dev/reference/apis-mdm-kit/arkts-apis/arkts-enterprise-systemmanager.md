# @ohos.enterprise.systemManager(系统管理)

本模块提供系统管理能力，包括NTP时间服务器设置、OTA升级策略管理、系统更新管理、按键事件处理策略、日志收集、设备激活锁管理等功能。适用于企业设备管理场景，帮助企业管理员统一管控设备系统配置、升级策略和安全策略，提升企业设备管理效率 和安全性。

> **说明：**&gt;
> 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 导入模块

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [addDisallowedNearLinkProtocols(系统管理)](arkts-mdm-systemmanager-adddisallowednearlinkprotocols-f.md) |
| [addKeyEventPolicies(系统管理)](arkts-mdm-systemmanager-addkeyeventpolicies-f.md) |
| [finishLogCollected(系统管理)](arkts-mdm-systemmanager-finishlogcollected-f.md) |
| [getAutoUnlockAfterReboot(系统管理)](arkts-mdm-systemmanager-getautounlockafterreboot-f.md) |
| [getAutoUnlockAfterReboot(系统管理)](arkts-mdm-systemmanager-getautounlockafterreboot-f.md) |
| [getDisallowedNearLinkProtocols(系统管理)](arkts-mdm-systemmanager-getdisallowednearlinkprotocols-f.md) |
| [getInstallLocalEnterpriseAppEnabled(系统管理)](arkts-mdm-systemmanager-getinstalllocalenterpriseappenabled-f.md) |
| [getInstallLocalEnterpriseAppEnabledForAccount(系统管理)](arkts-mdm-systemmanager-getinstalllocalenterpriseappenabledforaccount-f.md) |
| [getKeyEventPolicies(系统管理)](arkts-mdm-systemmanager-getkeyeventpolicies-f.md) |
| [getKeyEventPolicies(系统管理)](arkts-mdm-systemmanager-getkeyeventpolicies-f.md) |
| [getNTPServer(系统管理)](arkts-mdm-systemmanager-getntpserver-f.md) |
| [getOtaUpdatePolicy(系统管理)](arkts-mdm-systemmanager-getotaupdatepolicy-f.md) |
| [getUpdateAuthData(系统管理)](arkts-mdm-systemmanager-getupdateauthdata-f.md) |
| [getUpdateResult(系统管理)](arkts-mdm-systemmanager-getupdateresult-f.md) |
| [isActivationLockDisabled(系统管理)](arkts-mdm-systemmanager-isactivationlockdisabled-f.md) |
| [isOtaUpdateNonceEnable(系统管理)](arkts-mdm-systemmanager-isotaupdatenonceenable-f.md) |
| [notifyUpdatePackages(系统管理)](arkts-mdm-systemmanager-notifyupdatepackages-f.md) |
| [removeDisallowedNearLinkProtocols(系统管理)](arkts-mdm-systemmanager-removedisallowednearlinkprotocols-f.md) |
| [removeKeyEventPolicies(系统管理)](arkts-mdm-systemmanager-removekeyeventpolicies-f.md) |
| [setActivationLockDisabled(系统管理)](arkts-mdm-systemmanager-setactivationlockdisabled-f.md) |
| [setAutoUnlockAfterReboot(系统管理)](arkts-mdm-systemmanager-setautounlockafterreboot-f.md) |
| [setInstallLocalEnterpriseAppEnabled(系统管理)](arkts-mdm-systemmanager-setinstalllocalenterpriseappenabled-f.md) |
| [setInstallLocalEnterpriseAppEnabledForAccount(系统管理)](arkts-mdm-systemmanager-setinstalllocalenterpriseappenabledforaccount-f.md) |
| [setNTPServer(系统管理)](arkts-mdm-systemmanager-setntpserver-f.md) |
| [setOtaUpdateNonceEnable(系统管理)](arkts-mdm-systemmanager-setotaupdatenonceenable-f.md) |
| [setOtaUpdatePolicy(系统管理)](arkts-mdm-systemmanager-setotaupdatepolicy-f.md) |
| [startCollectLog(系统管理)](arkts-mdm-systemmanager-startcollectlog-f.md) |

### 接口

| 名称 |
| --- |
| [ErrorInfo(系统管理)](arkts-mdm-systemmanager-errorinfo-i.md) |
| [KeyEvent(系统管理)](arkts-mdm-systemmanager-keyevent-i.md) |
| [KeyEventPolicy(系统管理)](arkts-mdm-systemmanager-keyeventpolicy-i.md) |
| [KeyItem(系统管理)](arkts-mdm-systemmanager-keyitem-i.md) |
| [NotifyDescription(系统管理)](arkts-mdm-systemmanager-notifydescription-i.md) |
| [OtaUpdatePolicy(系统管理)](arkts-mdm-systemmanager-otaupdatepolicy-i.md) |
| [Package(系统管理)](arkts-mdm-systemmanager-package-i.md) |
| [PackageDescription(系统管理)](arkts-mdm-systemmanager-packagedescription-i.md) |
| [SystemUpdateInfo(系统管理)](arkts-mdm-systemmanager-systemupdateinfo-i.md) |
| [UpdatePackageInfo(系统管理)](arkts-mdm-systemmanager-updatepackageinfo-i.md) |
| [UpdateResult(系统管理)](arkts-mdm-systemmanager-updateresult-i.md) |

### 枚举

| 名称 |
| --- |
| [KeyAction(系统管理)](arkts-mdm-systemmanager-keyaction-e.md) |
| [KeyCode(系统管理)](arkts-mdm-systemmanager-keycode-e.md) |
| [KeyPolicy(系统管理)](arkts-mdm-systemmanager-keypolicy-e.md) |
| [NearLinkProtocol(系统管理)](arkts-mdm-systemmanager-nearlinkprotocol-e.md) |
| [PackageType(系统管理)](arkts-mdm-systemmanager-packagetype-e.md) |
| [PolicyType(系统管理)](arkts-mdm-systemmanager-policytype-e.md) |
| [UpdateStatus(系统管理)](arkts-mdm-systemmanager-updatestatus-e.md) |
