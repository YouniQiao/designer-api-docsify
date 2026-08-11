# @ohos.enterprise.restrictions(限制类策略)

本模块提供设置通用限制类策略能力。可以全局禁用和解除禁用蓝牙、HDC、USB、Wi-Fi、蜂窝数据、相机、麦克风等特性。

**使用场景**：

- 企业设备管理场景下，管理员需要对员工设备进行功能限制，防止数据泄露或非授权使用。  
- BYOD（Bring Your Own Device）场景下，企业空间需要限制设备功能以符合企业安全策略。  
- 设备安全管控场景下，需要禁用特定功能以保护企业敏感信息。

**能解决的问题**：

- 防止员工通过蓝牙、USB等方式传输企业敏感数据。  
- 限制设备调试能力（HDC）以提升设备安全性。  
- 控制网络访问能力（Wi-Fi、蜂窝数据等）以符合企业网络策略。  
- 管理设备多媒体能力（相机、麦克风等）以保护隐私和企业机密。

**带来的收益**：

- 提升企业设备安全性，降低数据泄露风险。  
- 满足企业合规要求，符合安全审计标准。  
- 实现精细化的设备功能管控，平衡安全与使用体验。

> **说明：**
> 
> 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 12

<!--Device-unnamed-declare namespace restrictions--><!--Device-unnamed-declare namespace restrictions-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 汇总

### 函数

| 名称 |
| --- |
| [addDisallowedListForAccount](arkts-mdm-restrictions-adddisallowedlistforaccount-f.md#adddisallowedlistforaccount) |
| [disableMicrophone](arkts-mdm-restrictions-disablemicrophone-f.md#disablemicrophone) |
| [getDisallowedListForAccount](arkts-mdm-restrictions-getdisallowedlistforaccount-f.md#getdisallowedlistforaccount) |
| [getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md#getdisallowedpolicy) |
| [getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md#getdisallowedpolicy-1) |
| [getDisallowedPolicyForAccount](arkts-mdm-restrictions-getdisallowedpolicyforaccount-f.md#getdisallowedpolicyforaccount) |
| [getDisallowedPolicyForAccount](arkts-mdm-restrictions-getdisallowedpolicyforaccount-f.md#getdisallowedpolicyforaccount-1) |
| [getUserRestricted](arkts-mdm-restrictions-getuserrestricted-f.md#getuserrestricted) |
| [getUserRestricted](arkts-mdm-restrictions-getuserrestricted-f.md#getuserrestricted-1) |
| [getUserRestrictedForAccount](arkts-mdm-restrictions-getuserrestrictedforaccount-f.md#getuserrestrictedforaccount) |
| [getUserRestrictedForAccount](arkts-mdm-restrictions-getuserrestrictedforaccount-f.md#getuserrestrictedforaccount-1) |
| [isFingerprintAuthDisabled](arkts-mdm-restrictions-isfingerprintauthdisabled-f.md#isfingerprintauthdisabled) |
| [isHdcDisabled](arkts-mdm-restrictions-ishdcdisabled-f.md#ishdcdisabled) |
| [isHdcDisabled](arkts-mdm-restrictions-ishdcdisabled-f.md#ishdcdisabled-1) |
| [isMicrophoneDisabled](arkts-mdm-restrictions-ismicrophonedisabled-f.md#ismicrophonedisabled) |
| [isPrinterDisabled](arkts-mdm-restrictions-isprinterdisabled-f.md#isprinterdisabled) |
| [isPrinterDisabled](arkts-mdm-restrictions-isprinterdisabled-f.md#isprinterdisabled-1) |
| [removeDisallowedListForAccount](arkts-mdm-restrictions-removedisallowedlistforaccount-f.md#removedisallowedlistforaccount) |
| [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy) |
| [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy-1) |
| [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setdisallowedpolicyforaccount) |
| [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setdisallowedpolicyforaccount-1) |
| [setFingerprintAuthDisabled](arkts-mdm-restrictions-setfingerprintauthdisabled-f.md#setfingerprintauthdisabled) |
| [setHdcDisabled](arkts-mdm-restrictions-sethdcdisabled-f.md#sethdcdisabled) |
| [setHdcDisabled](arkts-mdm-restrictions-sethdcdisabled-f.md#sethdcdisabled-1) |
| [setPrinterDisabled](arkts-mdm-restrictions-setprinterdisabled-f.md#setprinterdisabled) |
| [setPrinterDisabled](arkts-mdm-restrictions-setprinterdisabled-f.md#setprinterdisabled-1) |
| [setUserRestriction](arkts-mdm-restrictions-setuserrestriction-f.md#setuserrestriction) |
| [setUserRestriction](arkts-mdm-restrictions-setuserrestriction-f.md#setuserrestriction-1) |
| [setUserRestrictionForAccount](arkts-mdm-restrictions-setuserrestrictionforaccount-f.md#setuserrestrictionforaccount) |
| [setUserRestrictionForAccount](arkts-mdm-restrictions-setuserrestrictionforaccount-f.md#setuserrestrictionforaccount-1) |

### 枚举

| 名称 |
| --- |
| [FeatureForAccount](arkts-mdm-restrictions-featureforaccount-e.md) |
| [FeatureForDevice](arkts-mdm-restrictions-featurefordevice-e.md) |
| [SettingsForAccount](arkts-mdm-restrictions-settingsforaccount-e.md) |
| [SettingsForDevice](arkts-mdm-restrictions-settingsfordevice-e.md) |
