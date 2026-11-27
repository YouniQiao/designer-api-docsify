# CustomComponentAsyncLoadOptions

```TypeScript
export declare interface CustomComponentAsyncLoadOptions
```

Describes the configuration options for asynchronous loading of a custom component.

**Since:** 26.1.0

<!--Device-unnamed-export declare interface CustomComponentAsyncLoadOptions--><!--Device-unnamed-export declare interface CustomComponentAsyncLoadOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AppStorageV2, PersistenceV2, Type, UIUtils, ConnectOptions, Binding, MutableBinding, CustomComponentLifecycle, CustomComponentLifecycleObserver, CustomComponentLifecycleState, ComponentInit, ComponentAppear, ComponentBuilt, ComponentReuse, ComponentActive, ComponentInactive, ComponentRecycle, ComponentDisappear, CollectionType, ConnectOptionsCollections, CustomComponentContext, CustomComponentAsyncLoadOptions, IReusePool, IDefaultReusePool, IReusableInfo, StorageDefaultCreator, TypeConstructorWithArgs, PersistenceErrorCallback, TypeConstructor, TypeDecorator, MonitorCallback, MonitorOptions, GetterCallback, SetterCallback, ObservedResult, DecoratorInfo, ElementInfo, RecoverableStorage, RecoverableConnectOptions, RecoverableStorageError, NotifyOnErrorCallback } from '@kit.ArkUI';
```

## placeholder

```TypeScript
placeholder?: PlaceholderOptions
```

Placeholder displayed while the custom component is being loaded asynchronously. The value is a [PlaceholderOptions](arkts-arkui-arkui-placeholderregister-placeholderoptions-i.md) object: **id** refers to a template registered through [getPlaceholderRegister()](arkts-arkui-arkui-uicontext-uicontext-c.md#getplaceholderregister), and **size** is a layout suggestion of the **SizeOptions** type. When set, it acts as the ideal size of the placeholder root during measurement: numbers are in vp, unit-suffixed strings keep their units, and a Resource value is treated as unset. If **size** is not configured, or a dimension of it is unset or invalid, the placeholder is laid out based on the settings of the placeholder template itself.

If **placeholder** is not configured, or its **id** is empty or not registered, no placeholder is displayed before asynchronous loading completes.

**Type:** [PlaceholderOptions](arkts-arkui-arkui-placeholderregister-placeholderoptions-i.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-CustomComponentAsyncLoadOptions-placeholder?: PlaceholderOptions--><!--Device-CustomComponentAsyncLoadOptions-placeholder?: PlaceholderOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## timeout

```TypeScript
timeout?: number
```

Timeout threshold for asynchronous loading, in ms. The default value is **1000**.

The value can be any number. **NaN** is treated as the default value (**1000**), and **+/-Infinity** is treated as a negative value. A positive fractional value is rounded up to the next whole millisecond. If the component is not loaded within **timeout** ms, the framework force-loads it in subsequent frames, and the number of components force-loaded in a single frame does not exceed a system-defined limit. The value **0** means no waiting: the component is force-loaded in subsequent frames. A negative value means never timing out: the component keeps waiting until asynchronous loading completes.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-CustomComponentAsyncLoadOptions-timeout?: number--><!--Device-CustomComponentAsyncLoadOptions-timeout?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
