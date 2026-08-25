# UIUtils

Provides APIs for handling data transformations related to state management.

**Since:** 12

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AppStorageV2, PersistenceV2, Type, UIUtils, ConnectOptions, Binding, MutableBinding, CustomComponentLifecycle, CustomComponentLifecycleObserver, CustomComponentLifecycleState, ComponentInit, ComponentAppear, ComponentBuilt, ComponentReuse, ComponentActive, ComponentInactive, ComponentRecycle, ComponentDisappear, CollectionType, ConnectOptionsCollections, CustomComponentContext, IReusePool, IReusableInfo } from 'kits/@kit.ArkUI';
```

## addMonitor

```TypeScript
static addMonitor(target: object, path: string | string[], monitorCallback: MonitorCallback, options?: MonitorOptions): void
```

Dynamically adds a listener to the state variable of state management V2. For details, see [addMonitor and clearMonitor APIs: Dynamically Adding and Removing Listeners](../../../ui/state-management/arkts-new-addMonitor-clearMonitor.md).

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | object | Yes |
| path | string \| string[] | Yes |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | Yes |
| options | [MonitorOptions](arkts-arkui-arkui-statemanagement-monitoroptions-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [130000](../errorcode-stateManagement.md#130000-invalid-target-object-for-addmonitorclearmonitor) |
| [130001](../errorcode-stateManagement.md#130001-invalid-path-for-addmonitorclearmonitor) |
| [130002](../errorcode-stateManagement.md#130002-invalid-callback-for-addmonitorclearmonitor) |

## applySync

```TypeScript
static applySync<T>(task: TaskCallback): T
```

Synchronously updates a specified state variable. This API receives a closure function and updates only the internal modifications, including the updates of [@Computed](../../../ui/state-management/arkts-new-computed.md) and [@Monitor](../../../ui/state-management/arkts-new-monitor.md) decorators, and re-rendering of the UI nodes. For details, see [applySync/flushUpdates/flushUIUpdates APIs: Synchronous Update](../../../ui/state-management/arkts-new-applySync-flushUpdates-flushUIUpdates.md).

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| task | [TaskCallback](arkts-arkui-taskcallback-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

**Error codes:**

| Error Code ID |
| --- |
| [140001](../errorcode-stateManagement.md#140001-invalid-invocation-of-applysync-flushupdates-or-flushuiupdates) |

## canBeObserved

```TypeScript
static canBeObserved<T extends object>(source: T): ObservedResult
```

Determines whether a data object can be observed and returns the observation result. For details, see [canBeObserved API: Determining Whether an Object Can Be Observed](../../../ui/state-management/arkts-new-canBeObserved.md).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ObservedResult](arkts-arkui-arkui-statemanagement-observedresult-i.md) |

## clearMonitor

```TypeScript
static clearMonitor(target: object, path: string | string[], monitorCallback?: MonitorCallback) : void
```

Deletes the listener added to the state variable of the state management V2 by calling the [addMonitor](#addmonitor) API. For details, see [addMonitor and clearMonitor APIs: Dynamically Adding and Removing Listeners](../../../ui/state-management/arkts-new-addMonitor-clearMonitor.md).

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| target | object | Yes |
| path | string \| string[] | Yes |
| monitorCallback | [MonitorCallback](arkts-arkui-monitorcallback-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [130000](../errorcode-stateManagement.md#130000-invalid-target-object-for-addmonitorclearmonitor) |
| [130001](../errorcode-stateManagement.md#130001-invalid-path-for-addmonitorclearmonitor) |
| [130002](../errorcode-stateManagement.md#130002-invalid-callback-for-addmonitorclearmonitor) |

## enableV2Compatibility

```TypeScript
static enableV2Compatibility<T extends object>(source: T): T
```

Enables V1 state variables to be observable in @ComponentV2. This API is primarily used in scenarios where V1 and V 2 state management are mixed. For details, see [Mixed Use of State Management V1 and V2 (API Version 19 and Later)](../../../ui/state-management/arkts-v1-v2-mixusage.md).

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## flushUIUpdates

```TypeScript
static flushUIUpdates(): void
```

Processes all state variable modifications before this API call and synchronizes the [dirty](../../../ui/state-management/arkts-state-management-introduce.md#triggering-updates) UI nodes. However, it does not synchronize the execution of @Computed and @Monitor decorators. For details, see [applySync/flushUpdates/flushUIUpdates APIs: Synchronous Update](../../../ui/state-management/arkts-new-applySync-flushUpdates-flushUIUpdates.md).

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Error codes:**

| Error Code ID |
| --- |
| [140001](../errorcode-stateManagement.md#140001-invalid-invocation-of-applysync-flushupdates-or-flushuiupdates) |
| [140002](../errorcode-stateManagement.md#140002-invalid-invocation-of-flushupdates-or-flushuiupdates) |

## flushUpdates

```TypeScript
static flushUpdates(): void
```

Synchronously updates all state variable modifications before this API call, including the updates of @Computed and @Monitor decorators, and re-rendering of the UI nodes. For details, see [applySync/flushUpdates/flushUIUpdates APIs: Synchronous Update](../../../ui/state-management/arkts-new-applySync-flushUpdates-flushUIUpdates.md).

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Error codes:**

| Error Code ID |
| --- |
| [140001](../errorcode-stateManagement.md#140001-invalid-invocation-of-applysync-flushupdates-or-flushuiupdates) |
| [140002](../errorcode-stateManagement.md#140002-invalid-invocation-of-flushupdates-or-flushuiupdates) |

## getCustomComponentContext

```TypeScript
static getCustomComponentContext<T extends BaseCustomComponent>(customComponent: T): CustomComponentContext
```

Obtains [CustomComponentContext](arkts-arkui-arkui-statemanagement-customcomponentcontext-i.md) of the given @Component(V1) or @ComponentV2. **CustomComponentContext** can be used to access the reuse pool of the component. For details about the reuse pool, see [Global Reuse: Centralized Component Recycling and Reuse](../../../ui/state-management/arkts-global-reuse-pool.md).

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| customComponent | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CustomComponentContext](arkts-arkui-arkui-statemanagement-customcomponentcontext-i.md) |

## getLifecycle

```TypeScript
static getLifecycle<T extends BaseCustomComponent>(customComponent: T): CustomComponentLifecycle
```

Obtains the lifecycle of a custom component.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| customComponent | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CustomComponentLifecycle](arkts-arkui-arkui-statemanagement-customcomponentlifecycle-i.md) |

## getTarget

```TypeScript
static getTarget<T extends object>(source: T): T
```

Obtains the original object from a proxy object wrapped by the state management framework. For details, see [getTarget API: Obtaining Original Objects](../../../ui/state-management/arkts-new-getTarget.md).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## makeBinding

```TypeScript
static makeBinding<T>(getter: GetterCallback<T>): Binding<T>
```

Creates a read-only one-way data binding instance, which is used to construct the arguments of the **Binding** type in the [\@Builder](../../../ui/state-management/arkts-builder.md) function.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| getter | [GetterCallback](arkts-arkui-gettercallback-t.md)&lt;T&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Binding](arkts-arkui-arkui-statemanagement-binding-c.md)&lt;T&gt; |

## makeBinding

```TypeScript
static makeBinding<T>(getter: GetterCallback<T>, setter: SetterCallback<T>): MutableBinding<T>
```

Creates a mutable two-way data binding instance, which is used to construct the argument of the **MutableBinding** type in the \@Builder function.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| getter | [GetterCallback](arkts-arkui-gettercallback-t.md)&lt;T&gt; | Yes |
| [setter](../../apis-ability-kit/arkts-apis/arkts-ability-appmanager-keepalivebundleinfo-i-sys.md) | [SetterCallback](arkts-arkui-settercallback-t.md)&lt;T&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MutableBinding](arkts-arkui-arkui-statemanagement-mutablebinding-c.md)&lt;T&gt; |

## makeObserved

```TypeScript
static makeObserved<T extends object>(source: T): T
```

Converts ordinary unobservable data into observable data. For details, see [makeObserved API: Changing Unobservable Data to Observable Data](../../../ui/state-management/arkts-new-makeObserved.md).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## makeV1Observed

```TypeScript
static makeV1Observed<T extends object>(source: T): T
```

Wraps an unobservable object into an object that is observable by V1 state management. This API is equivalent to @ Observed and can be used to initialize @ObjectLink.This API can be used together with [enableV2Compatibility](#enablev2compatibility) in scenarios where state management V1 and V2 are used together. For details, see [Mixed Use of State Management V1 and V2 (API Version 19 and Later)](../../../ui/state-management/arkts-v1-v2-mixusage.md).

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |
