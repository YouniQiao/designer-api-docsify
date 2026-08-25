# @ohos.net.policy(网络策略管理)

本模块提供网络策略管理能力，采用防火墙技术对用户使用数据流量进行控制管理。

> **说明：**&gt;
> 本模块首批接口从 API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.Communication.NetManager.Core

## 导入模块

```TypeScript
import { policy } from '@kit.NetworkKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getNetAccessPolicy(网络策略管理)](arkts-network-policy-getnetaccesspolicy-f.md) |
| [showAppNetPolicySettings(网络策略管理)](arkts-network-policy-showappnetpolicysettings-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getBackgroundPolicyByUid(网络策略管理)](arkts-network-policy-getbackgroundpolicybyuid-f-sys.md) |
| [getBackgroundPolicyByUid(网络策略管理)](arkts-network-policy-getbackgroundpolicybyuid-f-sys.md) |
| [getDeviceIdleTrustlist(网络策略管理)](arkts-network-policy-getdeviceidletrustlist-f-sys.md) |
| [getDeviceIdleTrustlist(网络策略管理)](arkts-network-policy-getdeviceidletrustlist-f-sys.md) |
| [getNetQuotaPolicies(网络策略管理)](arkts-network-policy-getnetquotapolicies-f-sys.md) |
| [getNetQuotaPolicies(网络策略管理)](arkts-network-policy-getnetquotapolicies-f-sys.md) |
| [getNetworkAccessPolicy(网络策略管理)](arkts-network-policy-getnetworkaccesspolicy-f-sys.md) |
| [getNetworkAccessPolicy(网络策略管理)](arkts-network-policy-getnetworkaccesspolicy-f-sys.md) |
| [getPolicyByUid(网络策略管理)](arkts-network-policy-getpolicybyuid-f-sys.md) |
| [getPolicyByUid(网络策略管理)](arkts-network-policy-getpolicybyuid-f-sys.md) |
| [getPowerSaveTrustlist(网络策略管理)](arkts-network-policy-getpowersavetrustlist-f-sys.md) |
| [getPowerSaveTrustlist(网络策略管理)](arkts-network-policy-getpowersavetrustlist-f-sys.md) |
| [getUidsByPolicy(网络策略管理)](arkts-network-policy-getuidsbypolicy-f-sys.md) |
| [getUidsByPolicy(网络策略管理)](arkts-network-policy-getuidsbypolicy-f-sys.md) |
| [isBackgroundAllowed(网络策略管理)](arkts-network-policy-isbackgroundallowed-f-sys.md) |
| [isBackgroundAllowed(网络策略管理)](arkts-network-policy-isbackgroundallowed-f-sys.md) |
| [isUidNetAllowed(网络策略管理)](arkts-network-policy-isuidnetallowed-f-sys.md) |
| [isUidNetAllowed(网络策略管理)](arkts-network-policy-isuidnetallowed-f-sys.md) |
| [isUidNetAllowed(网络策略管理)](arkts-network-policy-isuidnetallowed-f-sys.md) |
| [isUidNetAllowed(网络策略管理)](arkts-network-policy-isuidnetallowed-f-sys.md) |
| [off(网络策略管理)](arkts-network-policy-off-f-sys.md#offnetuidpolicychange) |
| [off(网络策略管理)](arkts-network-policy-off-f-sys.md#offnetuidrulechange) |
| [off(网络策略管理)](arkts-network-policy-off-f-sys.md#offnetmeteredifaceschange) |
| [off(网络策略管理)](arkts-network-policy-off-f-sys.md#offnetquotapolicychange) |
| [off(网络策略管理)](arkts-network-policy-off-f-sys.md#offnetbackgroundpolicychange) |
| [on(网络策略管理)](arkts-network-policy-on-f-sys.md#onnetuidpolicychange) |
| [on(网络策略管理)](arkts-network-policy-on-f-sys.md#onnetuidrulechange) |
| [on(网络策略管理)](arkts-network-policy-on-f-sys.md#onnetmeteredifaceschange) |
| [on(网络策略管理)](arkts-network-policy-on-f-sys.md#onnetquotapolicychange) |
| [on(网络策略管理)](arkts-network-policy-on-f-sys.md#onnetbackgroundpolicychange) |
| [resetPolicies(网络策略管理)](arkts-network-policy-resetpolicies-f-sys.md) |
| [resetPolicies(网络策略管理)](arkts-network-policy-resetpolicies-f-sys.md) |
| [restoreAllPolicies(网络策略管理)](arkts-network-policy-restoreallpolicies-f-sys.md) |
| [setBackgroundAllowed(网络策略管理)](arkts-network-policy-setbackgroundallowed-f-sys.md) |
| [setBackgroundAllowed(网络策略管理)](arkts-network-policy-setbackgroundallowed-f-sys.md) |
| [setDeviceIdleTrustlist(网络策略管理)](arkts-network-policy-setdeviceidletrustlist-f-sys.md) |
| [setDeviceIdleTrustlist(网络策略管理)](arkts-network-policy-setdeviceidletrustlist-f-sys.md) |
| [setNetQuotaPolicies(网络策略管理)](arkts-network-policy-setnetquotapolicies-f-sys.md) |
| [setNetQuotaPolicies(网络策略管理)](arkts-network-policy-setnetquotapolicies-f-sys.md) |
| [setNetworkAccessPolicy(网络策略管理)](arkts-network-policy-setnetworkaccesspolicy-f-sys.md) |
| [setPolicyByUid(网络策略管理)](arkts-network-policy-setpolicybyuid-f-sys.md) |
| [setPolicyByUid(网络策略管理)](arkts-network-policy-setpolicybyuid-f-sys.md) |
| [setPowerSaveTrustlist(网络策略管理)](arkts-network-policy-setpowersavetrustlist-f-sys.md) |
| [setPowerSaveTrustlist(网络策略管理)](arkts-network-policy-setpowersavetrustlist-f-sys.md) |
| [updateRemindPolicy(网络策略管理)](arkts-network-policy-updateremindpolicy-f-sys.md) |
| [updateRemindPolicy(网络策略管理)](arkts-network-policy-updateremindpolicy-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [NetAccessPolicy(网络策略管理)](arkts-network-policy-netaccesspolicy-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [NetQuotaPolicy(网络策略管理)](arkts-network-policy-netquotapolicy-i-sys.md) |
| [NetUidPolicyInfo(网络策略管理)](arkts-network-policy-netuidpolicyinfo-i-sys.md) |
| [NetUidRuleInfo(网络策略管理)](arkts-network-policy-netuidruleinfo-i-sys.md) |
| [NetworkAccessPolicy(网络策略管理)](arkts-network-policy-networkaccesspolicy-i-sys.md) |
| [NetworkMatchRule(网络策略管理)](arkts-network-policy-networkmatchrule-i-sys.md) |
| [QuotaPolicy(网络策略管理)](arkts-network-policy-quotapolicy-i-sys.md) |
| [UidNetworkAccessPolicy(网络策略管理)](arkts-network-policy-uidnetworkaccesspolicy-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [LimitAction(网络策略管理)](arkts-network-policy-limitaction-e-sys.md) |
| [NetBackgroundPolicy(网络策略管理)](arkts-network-policy-netbackgroundpolicy-e-sys.md) |
| [NetUidPolicy(网络策略管理)](arkts-network-policy-netuidpolicy-e-sys.md) |
| [NetUidRule(网络策略管理)](arkts-network-policy-netuidrule-e-sys.md) |
| [RemindType(网络策略管理)](arkts-network-policy-remindtype-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [NetBearType(网络策略管理)](arkts-network-policy-netbeartype-t.md) |
