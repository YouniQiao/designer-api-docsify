# @ohos.app.ability.errorManager(错误管理模块)

ErrorManager模块提供对应用运行时各类异常的全局观测能力，包括注册和注销错误观测器，主要用于监测应用崩溃（JS_CRASH）、应用冻屏（APP_FREEZE）、未捕获的Promise异常、资源超基线等错误场景。 通过设置监听器，开发者可以实时捕获异常信息、追踪问题根源、记录关键指标，从而提高应用的稳定性监控能力，加快故障排查和定位效率，提升应用质量和用户体验。

**起始版本：** 9

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { errorManager } from 'kits/@kit.AbilityKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [off(错误管理模块)](arkts-ability-errormanager-off-f.md#offerror) |
| [off(错误管理模块)](arkts-ability-errormanager-off-f.md#offerror) |
| [off(错误管理模块)](arkts-ability-errormanager-off-f.md#offloopobserver) |
| [off(错误管理模块)](arkts-ability-errormanager-off-f.md#offunhandledrejection) |
| [off(错误管理模块)](arkts-ability-errormanager-off-f.md#offglobalunhandledrejectiondetected) |
| [off(错误管理模块)](arkts-ability-errormanager-off-f.md#offfreeze) |
| [off(错误管理模块)](arkts-ability-errormanager-off-f.md#offglobalerroroccurred) |
| [on(错误管理模块)](arkts-ability-errormanager-on-f.md#onerror) |
| [on(错误管理模块)](arkts-ability-errormanager-on-f.md#onloopobserver) |
| [on(错误管理模块)](arkts-ability-errormanager-on-f.md#onunhandledrejection) |
| [on(错误管理模块)](arkts-ability-errormanager-on-f.md#onglobalunhandledrejectiondetected) |
| [on(错误管理模块)](arkts-ability-errormanager-on-f.md#onfreeze) |
| [on(错误管理模块)](arkts-ability-errormanager-on-f.md#onglobalerroroccurred) |
| [setDefaultErrorHandler(错误管理模块)](arkts-ability-errormanager-setdefaulterrorhandler-f.md) |
| [setDefaultFreezeObserver(错误管理模块)](arkts-ability-errormanager-setdefaultfreezeobserver-f.md) |
| [setDefaultResourceUsageObserver(错误管理模块)](arkts-ability-errormanager-setdefaultresourceusageobserver-f.md) |

### 接口

| 名称 |
| --- |
| [GlobalError(错误管理模块)](arkts-ability-errormanager-globalerror-i.md) |

### 枚举

| 名称 |
| --- |
| [InstanceType(错误管理模块)](arkts-ability-errormanager-instancetype-e.md) |
| [ResourceType(错误管理模块)](arkts-ability-errormanager-resourcetype-e.md) |

### 类型

| 名称 |
| --- |
| [ErrorHandler(错误管理模块)](arkts-ability-errormanager-errorhandler-t.md) |
| [ErrorObserver(错误管理模块)](arkts-ability-errormanager-errorobserver-t.md) |
| [FreezeObserver(错误管理模块)](arkts-ability-errormanager-freezeobserver-t.md) |
| [GlobalObserver(错误管理模块)](arkts-ability-errormanager-globalobserver-t.md) |
| [LoopObserver(错误管理模块)](arkts-ability-errormanager-loopobserver-t.md) |
| [ResourceUsageObserver(错误管理模块)](arkts-ability-errormanager-resourceusageobserver-t.md) |
| [UnhandledRejectionObserver(错误管理模块)](arkts-ability-errormanager-unhandledrejectionobserver-t.md) |
