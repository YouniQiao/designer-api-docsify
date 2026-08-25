# @ohos.enterprise.restrictions(限制类策略)

本模块提供设置通用限制类策略能力。可以全局禁用和解除禁用蓝牙、HDC、USB、Wi-Fi、蜂窝数据、相机、麦克风等特性。  
**使用场景**：  
- 企业设备管理场景下，管理员需要对员工设备进行功能限制，防止数据泄露或非授权使用。 - BYOD（Bring Your Own Device）场景下，企业空间需要限制设备功能以符合企业安全策略。 - 设备安全管控场景下，需要禁用特定功能以保护企业敏感信息。  
**能解决的问题**：  
- 防止员工通过蓝牙、USB等方式传输企业敏感数据。 - 限制设备调试能力（HDC）以提升设备安全性。 - 控制网络访问能力（Wi-Fi、蜂窝数据等）以符合企业网络策略。 - 管理设备多媒体能力（相机、麦克风等）以保护隐私和企业机密。  
**带来的收益**：  
- 提升企业设备安全性，降低数据泄露风险。 - 满足企业合规要求，符合安全审计标准。 - 实现精细化的设备功能管控，平衡安全与使用体验。

> **说明：**&gt;
> 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 导入模块

```TypeScript
import { restrictions } from '@kit.MDMKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [addDisallowedListForAccount(限制类策略)](arkts-mdm-restrictions-adddisallowedlistforaccount-f.md) |
| [getDisallowedListForAccount(限制类策略)](arkts-mdm-restrictions-getdisallowedlistforaccount-f.md) |
| [getDisallowedPolicy(限制类策略)](arkts-mdm-restrictions-getdisallowedpolicy-f.md) |
| [getDisallowedPolicy(限制类策略)](arkts-mdm-restrictions-getdisallowedpolicy-f.md) |
| [getDisallowedPolicyForAccount(限制类策略)](arkts-mdm-restrictions-getdisallowedpolicyforaccount-f.md) |
| [getDisallowedPolicyForAccount(限制类策略)](arkts-mdm-restrictions-getdisallowedpolicyforaccount-f.md) |
| [getUserRestricted(限制类策略)](arkts-mdm-restrictions-getuserrestricted-f.md) |
| [getUserRestricted(限制类策略)](arkts-mdm-restrictions-getuserrestricted-f.md) |
| [getUserRestrictedForAccount(限制类策略)](arkts-mdm-restrictions-getuserrestrictedforaccount-f.md) |
| [getUserRestrictedForAccount(限制类策略)](arkts-mdm-restrictions-getuserrestrictedforaccount-f.md) |
| [removeDisallowedListForAccount(限制类策略)](arkts-mdm-restrictions-removedisallowedlistforaccount-f.md) |
| [setDisallowedPolicy(限制类策略)](arkts-mdm-restrictions-setdisallowedpolicy-f.md) |
| [setDisallowedPolicy(限制类策略)](arkts-mdm-restrictions-setdisallowedpolicy-f.md) |
| [setDisallowedPolicyForAccount(限制类策略)](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md) |
| [setDisallowedPolicyForAccount(限制类策略)](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md) |
| [setUserRestriction(限制类策略)](arkts-mdm-restrictions-setuserrestriction-f.md) |
| [setUserRestriction(限制类策略)](arkts-mdm-restrictions-setuserrestriction-f.md) |
| [setUserRestrictionForAccount(限制类策略)](arkts-mdm-restrictions-setuserrestrictionforaccount-f.md) |
| [setUserRestrictionForAccount(限制类策略)](arkts-mdm-restrictions-setuserrestrictionforaccount-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [disableMicrophone(限制类策略)](arkts-mdm-restrictions-disablemicrophone-f-sys.md) |
| [isFingerprintAuthDisabled(限制类策略)](arkts-mdm-restrictions-isfingerprintauthdisabled-f-sys.md) |
| [isHdcDisabled(限制类策略)](arkts-mdm-restrictions-ishdcdisabled-f-sys.md) |
| [isHdcDisabled(限制类策略)](arkts-mdm-restrictions-ishdcdisabled-f-sys.md) |
| [isMicrophoneDisabled(限制类策略)](arkts-mdm-restrictions-ismicrophonedisabled-f-sys.md) |
| [isPrinterDisabled(限制类策略)](arkts-mdm-restrictions-isprinterdisabled-f-sys.md) |
| [isPrinterDisabled(限制类策略)](arkts-mdm-restrictions-isprinterdisabled-f-sys.md) |
| [setFingerprintAuthDisabled(限制类策略)](arkts-mdm-restrictions-setfingerprintauthdisabled-f-sys.md) |
| [setHdcDisabled(限制类策略)](arkts-mdm-restrictions-sethdcdisabled-f-sys.md) |
| [setHdcDisabled(限制类策略)](arkts-mdm-restrictions-sethdcdisabled-f-sys.md) |
| [setPrinterDisabled(限制类策略)](arkts-mdm-restrictions-setprinterdisabled-f-sys.md) |
| [setPrinterDisabled(限制类策略)](arkts-mdm-restrictions-setprinterdisabled-f-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [FeatureForAccount(限制类策略)](arkts-mdm-restrictions-featureforaccount-e.md) |
| [FeatureForDevice(限制类策略)](arkts-mdm-restrictions-featurefordevice-e.md) |
| [SettingsForAccount(限制类策略)](arkts-mdm-restrictions-settingsforaccount-e.md) |
| [SettingsForDevice(限制类策略)](arkts-mdm-restrictions-settingsfordevice-e.md) |
