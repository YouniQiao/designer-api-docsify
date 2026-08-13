# @ohos.enterprise.restrictions

本模块提供设置通用限制类策略能力。可以全局禁用和解除禁用蓝牙、HDC、USB、Wi-Fi、蜂窝数据、相机、麦克风等特性。 **使用场景**： - 企业设备管理场景下，管理员需要对员工设备进行功能限制，防止数据泄露或非授权使用。 - BYOD（Bring Your Own Device）场景下，企业空间需要限制设备功能以符合企业安全策略。 - 设备安全管控场景下，需要禁用特定功能以保护企业敏感信息。 **能解决的问题**： - 防止员工通过蓝牙、USB等方式传输企业敏感数据。 - 限制设备调试能力（HDC）以提升设备安全性。 - 控制网络访问能力（Wi-Fi、蜂窝数据等）以符合企业网络策略。 - 管理设备多媒体能力（相机、麦克风等）以保护隐私和企业机密。 **带来的收益**： - 提升企业设备安全性，降低数据泄露风险。 - 满足企业合规要求，符合安全审计标准。 - 实现精细化的设备功能管控，平衡安全与使用体验。 > **说明：** > > 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 10

**废弃版本：** -1

<!--Device-unnamed-declare namespace restrictions--><!--Device-unnamed-declare namespace restrictions-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

## 汇总

### 函数

| 名称 |
| --- |
| [addDisallowedListForAccount](arkts-mdm-restrictions-adddisallowedlistforaccount-f.md#addDisallowedListForAccount) |
| [getDisallowedListForAccount](arkts-mdm-restrictions-getdisallowedlistforaccount-f.md#getDisallowedListForAccount) |
| [getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md#getDisallowedPolicy) |
| [getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md#getDisallowedPolicy) |
| [getDisallowedPolicyForAccount](arkts-mdm-restrictions-getdisallowedpolicyforaccount-f.md#getDisallowedPolicyForAccount) |
| [getDisallowedPolicyForAccount](arkts-mdm-restrictions-getdisallowedpolicyforaccount-f.md#getDisallowedPolicyForAccount) |
| [getUserRestricted](arkts-mdm-restrictions-getuserrestricted-f.md#getUserRestricted) |
| [getUserRestricted](arkts-mdm-restrictions-getuserrestricted-f.md#getUserRestricted) |
| [getUserRestrictedForAccount](arkts-mdm-restrictions-getuserrestrictedforaccount-f.md#getUserRestrictedForAccount) |
| [getUserRestrictedForAccount](arkts-mdm-restrictions-getuserrestrictedforaccount-f.md#getUserRestrictedForAccount) |
| [removeDisallowedListForAccount](arkts-mdm-restrictions-removedisallowedlistforaccount-f.md#removeDisallowedListForAccount) |
| [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setDisallowedPolicy) |
| [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setDisallowedPolicy) |
| [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setDisallowedPolicyForAccount) |
| [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setDisallowedPolicyForAccount) |
| [setUserRestriction](arkts-mdm-restrictions-setuserrestriction-f.md#setUserRestriction) |
| [setUserRestriction](arkts-mdm-restrictions-setuserrestriction-f.md#setUserRestriction) |
| [setUserRestrictionForAccount](arkts-mdm-restrictions-setuserrestrictionforaccount-f.md#setUserRestrictionForAccount) |
| [setUserRestrictionForAccount](arkts-mdm-restrictions-setuserrestrictionforaccount-f.md#setUserRestrictionForAccount) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [disableMicrophone](arkts-mdm-restrictions-disablemicrophone-f-sys.md#disableMicrophone（系统接口）) |
| [isFingerprintAuthDisabled](arkts-mdm-restrictions-isfingerprintauthdisabled-f-sys.md#isFingerprintAuthDisabled（系统接口）) |
| [isHdcDisabled](arkts-mdm-restrictions-ishdcdisabled-f-sys.md#isHdcDisabled（系统接口）) |
| [isHdcDisabled](arkts-mdm-restrictions-ishdcdisabled-f-sys.md#isHdcDisabled（系统接口）) |
| [isMicrophoneDisabled](arkts-mdm-restrictions-ismicrophonedisabled-f-sys.md#isMicrophoneDisabled（系统接口）) |
| [isPrinterDisabled](arkts-mdm-restrictions-isprinterdisabled-f-sys.md#isPrinterDisabled（系统接口）) |
| [isPrinterDisabled](arkts-mdm-restrictions-isprinterdisabled-f-sys.md#isPrinterDisabled（系统接口）) |
| [setFingerprintAuthDisabled](arkts-mdm-restrictions-setfingerprintauthdisabled-f-sys.md#setFingerprintAuthDisabled（系统接口）) |
| [setHdcDisabled](arkts-mdm-restrictions-sethdcdisabled-f-sys.md#setHdcDisabled（系统接口）) |
| [setHdcDisabled](arkts-mdm-restrictions-sethdcdisabled-f-sys.md#setHdcDisabled（系统接口）) |
| [setPrinterDisabled](arkts-mdm-restrictions-setprinterdisabled-f-sys.md#setPrinterDisabled（系统接口）) |
| [setPrinterDisabled](arkts-mdm-restrictions-setprinterdisabled-f-sys.md#setPrinterDisabled（系统接口）) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [FeatureForAccount](arkts-mdm-restrictions-featureforaccount-e.md) |
| [FeatureForDevice](arkts-mdm-restrictions-featurefordevice-e.md) |
| [SettingsForAccount](arkts-mdm-restrictions-settingsforaccount-e.md) |
| [SettingsForDevice](arkts-mdm-restrictions-settingsfordevice-e.md) |
