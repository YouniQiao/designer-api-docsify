# @ohos.enterprise.browser(浏览器管理)

本模块提供浏览器管理能力，包括设置/取消浏览器策略、获取浏览器策略等。适用于企业设备管理、员工上网行为管控、安全合规审计等场景。浏览器策略指通过配置或管理浏览器行为的一系列规则和设置，以确保安全性、合规性、性能优化和用户体验的一致性。

> **说明：**&gt;
> 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 导入模块

```TypeScript
import { browser } from '@kit.MDMKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getManagedBrowserPolicy(浏览器管理)](arkts-mdm-browser-getmanagedbrowserpolicy-f.md) |
| [getPoliciesSync(浏览器管理)](arkts-mdm-browser-getpoliciessync-f.md) |
| [getPoliciesSync(浏览器管理)](arkts-mdm-browser-getpoliciessync-f.md) |
| [getSelfManagedBrowserPolicy(浏览器管理)](arkts-mdm-browser-getselfmanagedbrowserpolicy-f.md) |
| [getSelfManagedBrowserPolicyVersion(浏览器管理)](arkts-mdm-browser-getselfmanagedbrowserpolicyversion-f.md) |
| [setManagedBrowserPolicy(浏览器管理)](arkts-mdm-browser-setmanagedbrowserpolicy-f.md) |
| [setPolicySync(浏览器管理)](arkts-mdm-browser-setpolicysync-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getPolicies(浏览器管理)](arkts-mdm-browser-getpolicies-f-sys.md) |
| [getPolicies(浏览器管理)](arkts-mdm-browser-getpolicies-f-sys.md) |
| [setPolicies(浏览器管理)](arkts-mdm-browser-setpolicies-f-sys.md) |
| [setPolicies(浏览器管理)](arkts-mdm-browser-setpolicies-f-sys.md) |
<!--DelEnd-->
