# @ohos.app.ability.errorManager

ErrorManager模块提供对错误观测器的注册和注销的能力，主要是观测应用发生js crash和appfreeze等错误。

**起始版本：** 24

<!--Device-unnamed-declare namespace errorManager--><!--Device-unnamed-declare namespace errorManager-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [offFreeze](arkts-ability-errormanager-offfreeze-f.md#offfreeze) |
| [offUnhandledRejection](arkts-ability-errormanager-offunhandledrejection-f.md#offunhandledrejection) |
| [off_error](arkts-ability-errormanager-offerror-f.md#offerror) |
| [off_error](arkts-ability-errormanager-offerror-f.md#offerror-1) |
| [off_freeze](arkts-ability-errormanager-offfreeze-f.md#offfreeze) |
| [off_globalErrorOccurred](arkts-ability-errormanager-offglobalerroroccurred-f.md#offglobalerroroccurred) |
| [off_globalUnhandledRejectionDetected](arkts-ability-errormanager-offglobalunhandledrejectiondetected-f.md#offglobalunhandledrejectiondetected) |
| [off_loopObserver](arkts-ability-errormanager-offloopobserver-f.md#offloopobserver) |
| [off_unhandledRejection](arkts-ability-errormanager-offunhandledrejection-f.md#offunhandledrejection) |
| [onFreeze](arkts-ability-errormanager-onfreeze-f.md#onfreeze) |
| [onUnhandledRejection](arkts-ability-errormanager-onunhandledrejection-f.md#onunhandledrejection) |
| [on_error](arkts-ability-errormanager-onerror-f.md#onerror) |
| [on_freeze](arkts-ability-errormanager-onfreeze-f.md#onfreeze) |
| [on_globalErrorOccurred](arkts-ability-errormanager-onglobalerroroccurred-f.md#onglobalerroroccurred) |
| [on_globalUnhandledRejectionDetected](arkts-ability-errormanager-onglobalunhandledrejectiondetected-f.md#onglobalunhandledrejectiondetected) |
| [on_loopObserver](arkts-ability-errormanager-onloopobserver-f.md#onloopobserver) |
| [on_unhandledRejection](arkts-ability-errormanager-onunhandledrejection-f.md#onunhandledrejection) |
| [setDefaultErrorHandler](arkts-ability-errormanager-setdefaulterrorhandler-f.md#setdefaulterrorhandler) |
| [setDefaultFreezeObserver](arkts-ability-errormanager-setdefaultfreezeobserver-f.md#setdefaultfreezeobserver) |
| [setDefaultResourceUsageObserver](arkts-ability-errormanager-setdefaultresourceusageobserver-f.md#setdefaultresourceusageobserver) |

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
