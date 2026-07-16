# Binding

Represents the generic class for read-only data binding, which can bind data of any type.

**Since:** 20

<!--Device-unnamed-export declare class Binding<T>--><!--Device-unnamed-export declare class Binding<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { Binding, ComponentReuse, CustomComponentLifecycleState, ComponentInactive, PersistenceV2, ComponentDisappear, MutableBinding, CustomComponentLifecycleObserver, AppStorageV2, Type, ConnectOptionsCollections, CollectionType, CustomComponentContext, IReusePool, ConnectOptions, UIUtils, ComponentActive, CustomComponentLifecycle, ComponentInit, ComponentAppear, ComponentBuilt, ComponentRecycle, IReusableInfo } from '@kit.ArkUI';
```

## value

```TypeScript
get value(): T
```

Obtains a bound value.

**Type:** T

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Binding-get value(): T--><!--Device-Binding-get value(): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

