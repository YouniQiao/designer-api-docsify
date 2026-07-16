# IReusableInfo

The **IReusableInfo** API provides information about the current number and maximum number of reusable components managed by the reuse pool.

**Since:** 26.0.0

<!--Device-unnamed-export declare interface IReusableInfo--><!--Device-unnamed-export declare interface IReusableInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { Binding, ComponentReuse, CustomComponentLifecycleState, ComponentInactive, PersistenceV2, ComponentDisappear, MutableBinding, CustomComponentLifecycleObserver, AppStorageV2, Type, ConnectOptionsCollections, CollectionType, CustomComponentContext, IReusePool, ConnectOptions, UIUtils, ComponentActive, CustomComponentLifecycle, ComponentInit, ComponentAppear, ComponentBuilt, ComponentRecycle, IReusableInfo } from '@kit.ArkUI';
```

## count

```TypeScript
readonly count: number
```

Current number of @Reuseable/V2 component instances in pool.count is usually <= maxCount. It is allowed to be larger for short time because pool clean happens asynchronously.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-IReusableInfo-readonly count: number--><!--Device-IReusableInfo-readonly count: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxCount

```TypeScript
maxCount: number
```

Maximum number of permissible @Reusable/V2 component instances.The default value is 100, the maximum value is 200.Setting to a negative number will be treated as setting to 0.Setting to a number greater than maximum will be treated as setting to 200.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-IReusableInfo-maxCount: number--><!--Device-IReusableInfo-maxCount: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reuseId

```TypeScript
readonly reuseId?: string
```

reuse id.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-IReusableInfo-readonly reuseId?: string--><!--Device-IReusableInfo-readonly reuseId?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

