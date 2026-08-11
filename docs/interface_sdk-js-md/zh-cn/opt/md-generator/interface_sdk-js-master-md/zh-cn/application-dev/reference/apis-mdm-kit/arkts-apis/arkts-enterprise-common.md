# @ohos.enterprise.common(Enterprise公共模块)

本模块提供MDM Kit中常用公共能力的纯类型定义，包含枚举类型和数据结构。本模块仅导出类型声明，不包含具体实现逻辑或可执行代码。

**使用场景**：在企业设备管理应用开发中，当需要配置设备管控策略、管理应用实例、处理应用安装结果、监听策略变更等场景时，会使用本模块定义的类型。这些类型为MDM Kit中各子模块的接口提供统一的参数和返回值标准。

**收益**：通过标准化的类型定义，可以简化企业设备管理应用的开发流程，提高代码的可维护性和类型安全性，降低类型相关的运行时错误。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace common--><!--Device-unnamed-declare namespace common-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 汇总

### 接口

| 名称 |
| --- |
| [ApplicationInstance](arkts-mdm-common-applicationinstance-i.md) |
| [InstallationResult](arkts-mdm-common-installationresult-i.md) |
| [PolicyChangedEvent](arkts-mdm-common-policychangedevent-i.md) |

### 枚举

| 名称 |
| --- |
| [ManagedPolicy](arkts-mdm-common-managedpolicy-e.md) |
| [Result](arkts-mdm-common-result-e.md) |
| [StartupScene](arkts-mdm-common-startupscene-e.md) |

### 类型

| 名称 |
| --- |
| [EnterpriseAdminExtensionContext](arkts-mdm-common-enterpriseadminextensioncontext-t.md) |
