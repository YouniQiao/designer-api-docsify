# ObservedResult

对象是否可被观察的结果。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-unnamed-export interface ObservedResult--><!--Device-unnamed-export interface ObservedResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { Binding, ComponentReuse, CustomComponentLifecycleState, ComponentInactive, PersistenceV2, ComponentDisappear, MutableBinding, CustomComponentLifecycleObserver, AppStorageV2, Type, ConnectOptionsCollections, CollectionType, CustomComponentContext, IReusePool, ConnectOptions, UIUtils, ComponentActive, CustomComponentLifecycle, ComponentInit, ComponentAppear, ComponentBuilt, ComponentRecycle, IReusableInfo } from 'kits/@kit.ArkUI';
```

## decoratorInfo

```TypeScript
decoratorInfo: Array<DecoratorInfo>
```

对象可被观察时，数组中内容为对象关联的装饰器和组件信息。对象不可被观察时，此数组为空。

**Type:** Array&lt;DecoratorInfo&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ObservedResult-decoratorInfo: Array<DecoratorInfo>--><!--Device-ObservedResult-decoratorInfo: Array<DecoratorInfo>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isObserved

```TypeScript
isObserved: boolean
```

对象是否可被观察。

true：表示是可被观察对象。

false：表示不是可被观察对象。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ObservedResult-isObserved: boolean--><!--Device-ObservedResult-isObserved: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reason

```TypeScript
reason: string
```

对象是否可被观察的原因。

不可被观察原因：对象本身是不可被观察的。

可被观察原因或使用场景：

1. V1对象被[@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md)装饰器装饰或对象是被[makeV1Observed](arkts-arkui-arkui-statemanagement-uiutils-c.md#makev1observed)方法转换的。 2. V1对象被[@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md)装饰器装饰或对象是被[makeV1Observed](arkts-arkui-arkui-statemanagement-uiutils-c.md#makev1observed)方法转换的，但对象没有被UI组件使用。 3. V1对象被[enableV2Compatibility](arkts-arkui-arkui-statemanagement-uiutils-c.md#enablev2compatibility)方法转换后传入V2组件。 4. V1对象被[enableV2Compatibility](arkts-arkui-arkui-statemanagement-uiutils-c.md#enablev2compatibility)方法转换后传入V2组件，但没有被V2组件使用。 5. V2对象是被[@ObservedV2/@Trace](../../../ui/state-management/arkts-new-observedV2-and-trace.md)装饰的。6. V2对象是被[makeObserved](arkts-arkui-arkui-statemanagement-uiutils-c.md#makeobserved)方法转换的。 7. V2对象属于Array/Map/Set/Date类型。 8. V2对象是被[@ObservedV2/@Trace](../../../ui/state-management/arkts-new-observedV2-and-trace.md)装饰的，但对象没有被UI组件使用。 9. V2对象是被[makeObserved](arkts-arkui-arkui-statemanagement-uiutils-c.md#makeobserved)方法转换的，但没有被UI组件使用。 10. V2对象属于Array/Map/Set/Date类型，但没有被UI组件使用。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ObservedResult-reason: string--><!--Device-ObservedResult-reason: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

