# @ohos.app.ability.errorManager

ErrorManager模块提供对错误观测器的注册和注销的能力，主要是观测应用发生js crash和appfreeze等错误。

**起始版本：** 24

**废弃版本：** -1

<!--Device-unnamed-declare namespace errorManager--><!--Device-unnamed-declare namespace errorManager-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 汇总

### 函数

| 名称 |
| --- |
| [offFreeze](arkts-ability-errormanager-offfreeze-f.md#offFreeze) |
| [offUnhandledRejection](arkts-ability-errormanager-offunhandledrejection-f.md#offUnhandledRejection) |
| [off_error](arkts-ability-errormanager-offerror-f.md#off_error) |
| [off_error](arkts-ability-errormanager-offerror-f.md#off_error) |
| [off_freeze](arkts-ability-errormanager-offfreeze-f.md) |
| [off_globalErrorOccurred](arkts-ability-errormanager-offglobalerroroccurred-f.md#off_globalErrorOccurred) |
| [off_globalUnhandledRejectionDetected](arkts-ability-errormanager-offglobalunhandledrejectiondetected-f.md#off_globalUnhandledRejectionDetected) |
| [off_loopObserver](arkts-ability-errormanager-offloopobserver-f.md#off_loopObserver) |
| [off_unhandledRejection](arkts-ability-errormanager-offunhandledrejection-f.md) |
| [onFreeze](arkts-ability-errormanager-onfreeze-f.md#onFreeze) |
| [onUnhandledRejection](arkts-ability-errormanager-onunhandledrejection-f.md#onUnhandledRejection) |
| [on_error](arkts-ability-errormanager-onerror-f.md#on_error) |
| [on_freeze](arkts-ability-errormanager-onfreeze-f.md) |
| [on_globalErrorOccurred](arkts-ability-errormanager-onglobalerroroccurred-f.md#on_globalErrorOccurred) |
| [on_globalUnhandledRejectionDetected](arkts-ability-errormanager-onglobalunhandledrejectiondetected-f.md#on_globalUnhandledRejectionDetected) |
| [on_loopObserver](arkts-ability-errormanager-onloopobserver-f.md#on_loopObserver) |
| [on_unhandledRejection](arkts-ability-errormanager-onunhandledrejection-f.md) |
| [setDefaultErrorHandler](arkts-ability-errormanager-setdefaulterrorhandler-f.md#setDefaultErrorHandler) |
| [setDefaultFreezeObserver](arkts-ability-errormanager-setdefaultfreezeobserver-f.md#setDefaultFreezeObserver) |
| [setDefaultResourceUsageObserver](arkts-ability-errormanager-setdefaultresourceusageobserver-f.md#setDefaultResourceUsageObserver) |

### 接口

| 名称 |
| --- |
| [GlobalError](arkts-ability-errormanager-globalerror-i.md) |

### 枚举

| 名称 |
| --- |
| [InstanceType](arkts-ability-errormanager-instancetype-e.md) |
| [ResourceType](arkts-ability-errormanager-resourcetype-e.md) |

### 类型

| 名称 |
| --- |
| [ErrorHandler](arkts-ability-errormanager-errorhandler-t.md) |
| [ErrorObserver](arkts-ability-errormanager-errorobserver-t.md) |
| [FreezeObserver](arkts-ability-errormanager-freezeobserver-t.md) |
| [GlobalObserver](arkts-ability-errormanager-globalobserver-t.md) |
| [LoopObserver](arkts-ability-errormanager-loopobserver-t.md) |
| [ResourceUsageObserver](arkts-ability-errormanager-resourceusageobserver-t.md) |
| [UnhandledRejectionObserver](arkts-ability-errormanager-unhandledrejectionobserver-t.md) |
