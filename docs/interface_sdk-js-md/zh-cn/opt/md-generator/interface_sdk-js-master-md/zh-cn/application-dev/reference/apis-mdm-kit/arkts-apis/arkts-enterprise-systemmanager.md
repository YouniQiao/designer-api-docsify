# @ohos.enterprise.systemManager

本模块提供系统管理能力，包括NTP时间服务器设置、OTA升级策略管理、系统更新管理、按键事件处理策略、日志收集、设备激活锁管理等功能。适用于企业设备管理场景，帮助企业管理员统一管控设备系统配置、升级策略和安全策略，提升企业设备管理效率 和安全性。 > **说明：** > > 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace systemManager--><!--Device-unnamed-declare namespace systemManager-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 汇总

### 函数

| 名称 |
| --- |
| [addDisallowedNearLinkProtocols](arkts-mdm-systemmanager-adddisallowednearlinkprotocols-f.md#addDisallowedNearLinkProtocols) |
| [addKeyEventPolicies](arkts-mdm-systemmanager-addkeyeventpolicies-f.md#addKeyEventPolicies) |
| [finishLogCollected](arkts-mdm-systemmanager-finishlogcollected-f.md#finishLogCollected) |
| [getAutoUnlockAfterReboot](arkts-mdm-systemmanager-getautounlockafterreboot-f.md#getAutoUnlockAfterReboot) |
| [getAutoUnlockAfterReboot](arkts-mdm-systemmanager-getautounlockafterreboot-f.md#getAutoUnlockAfterReboot) |
| [getDisallowedNearLinkProtocols](arkts-mdm-systemmanager-getdisallowednearlinkprotocols-f.md#getDisallowedNearLinkProtocols) |
| [getInstallLocalEnterpriseAppEnabled](arkts-mdm-systemmanager-getinstalllocalenterpriseappenabled-f.md#getInstallLocalEnterpriseAppEnabled) |
| [getInstallLocalEnterpriseAppEnabledForAccount](arkts-mdm-systemmanager-getinstalllocalenterpriseappenabledforaccount-f.md#getInstallLocalEnterpriseAppEnabledForAccount) |
| [getKeyEventPolicies](arkts-mdm-systemmanager-getkeyeventpolicies-f.md#getKeyEventPolicies) |
| [getKeyEventPolicies](arkts-mdm-systemmanager-getkeyeventpolicies-f.md#getKeyEventPolicies) |
| [getNTPServer](arkts-mdm-systemmanager-getntpserver-f.md#getNTPServer) |
| [getOtaUpdatePolicy](arkts-mdm-systemmanager-getotaupdatepolicy-f.md#getOtaUpdatePolicy) |
| [getUpdateAuthData](arkts-mdm-systemmanager-getupdateauthdata-f.md#getUpdateAuthData) |
| [getUpdateResult](arkts-mdm-systemmanager-getupdateresult-f.md#getUpdateResult) |
| [isActivationLockDisabled](arkts-mdm-systemmanager-isactivationlockdisabled-f.md#isActivationLockDisabled) |
| [isOtaUpdateNonceEnable](arkts-mdm-systemmanager-isotaupdatenonceenable-f.md#isOtaUpdateNonceEnable) |
| [notifyUpdatePackages](arkts-mdm-systemmanager-notifyupdatepackages-f.md#notifyUpdatePackages) |
| [removeDisallowedNearLinkProtocols](arkts-mdm-systemmanager-removedisallowednearlinkprotocols-f.md#removeDisallowedNearLinkProtocols) |
| [removeKeyEventPolicies](arkts-mdm-systemmanager-removekeyeventpolicies-f.md#removeKeyEventPolicies) |
| [setActivationLockDisabled](arkts-mdm-systemmanager-setactivationlockdisabled-f.md#setActivationLockDisabled) |
| [setAutoUnlockAfterReboot](arkts-mdm-systemmanager-setautounlockafterreboot-f.md#setAutoUnlockAfterReboot) |
| [setInstallLocalEnterpriseAppEnabled](arkts-mdm-systemmanager-setinstalllocalenterpriseappenabled-f.md#setInstallLocalEnterpriseAppEnabled) |
| [setInstallLocalEnterpriseAppEnabledForAccount](arkts-mdm-systemmanager-setinstalllocalenterpriseappenabledforaccount-f.md#setInstallLocalEnterpriseAppEnabledForAccount) |
| [setNTPServer](arkts-mdm-systemmanager-setntpserver-f.md#setNTPServer) |
| [setOtaUpdateNonceEnable](arkts-mdm-systemmanager-setotaupdatenonceenable-f.md#setOtaUpdateNonceEnable) |
| [setOtaUpdatePolicy](arkts-mdm-systemmanager-setotaupdatepolicy-f.md#setOtaUpdatePolicy) |
| [startCollectLog](arkts-mdm-systemmanager-startcollectlog-f.md#startCollectLog) |

### 接口

| 名称 |
| --- |
| [ErrorInfo](arkts-mdm-systemmanager-errorinfo-i.md) |
| [KeyEvent](arkts-mdm-systemmanager-keyevent-i.md) |
| [KeyEventPolicy](arkts-mdm-systemmanager-keyeventpolicy-i.md) |
| [KeyItem](arkts-mdm-systemmanager-keyitem-i.md) |
| [NotifyDescription](arkts-mdm-systemmanager-notifydescription-i.md) |
| [OtaUpdatePolicy](arkts-mdm-systemmanager-otaupdatepolicy-i.md) |
| [Package](arkts-mdm-systemmanager-package-i.md) |
| [PackageDescription](arkts-mdm-systemmanager-packagedescription-i.md) |
| [SystemUpdateInfo](arkts-mdm-systemmanager-systemupdateinfo-i.md) |
| [UpdatePackageInfo](arkts-mdm-systemmanager-updatepackageinfo-i.md) |
| [UpdateResult](arkts-mdm-systemmanager-updateresult-i.md) |

### 枚举

| 名称 |
| --- |
| [KeyAction](arkts-mdm-systemmanager-keyaction-e.md) |
| [KeyCode](arkts-mdm-systemmanager-keycode-e.md) |
| [KeyPolicy](arkts-mdm-systemmanager-keypolicy-e.md) |
| [NearLinkProtocol](arkts-mdm-systemmanager-nearlinkprotocol-e.md) |
| [PackageType](arkts-mdm-systemmanager-packagetype-e.md) |
| [PolicyType](arkts-mdm-systemmanager-policytype-e.md) |
| [UpdateStatus](arkts-mdm-systemmanager-updatestatus-e.md) |
