# DecoratorInfo

可被观察对象关联的装饰器和组件信息。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-unnamed-export interface DecoratorInfo--><!--Device-unnamed-export interface DecoratorInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { Binding, ComponentReuse, CustomComponentLifecycleState, ComponentInactive, PersistenceV2, ComponentDisappear, MutableBinding, CustomComponentLifecycleObserver, AppStorageV2, Type, ConnectOptionsCollections, CollectionType, CustomComponentContext, IReusePool, ConnectOptions, UIUtils, ComponentActive, CustomComponentLifecycle, ComponentInit, ComponentAppear, ComponentBuilt, ComponentRecycle, IReusableInfo } from 'kits/@kit.ArkUI';
```

## decoratorName

```TypeScript
decoratorName: string
```

当对象是V1对象时，值是对象关联的装饰器名称。

当V1对象使用[@Track](../../../ui/state-management/arkts-track.md)时，值为：'@Track'。

当V2对象使用[@Trace](../../../ui/state-management/arkts-new-observedV2-and-trace.md)时，值为：'@Trace'。

当V2对象使用[makeObserved](arkts-arkui-arkui-statemanagement-uiutils-c.md#makeobserved)时，值为：'MakeObserved'。

当V2对象使用[enableV2Compatibility](arkts-arkui-arkui-statemanagement-uiutils-c.md#enablev2compatibility)时，值为：'EnableV2Compatible'。 

当V2对象使用built-in类型数据时，值为：'ProxyObservedV2'。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-DecoratorInfo-decoratorName: string--><!--Device-DecoratorInfo-decoratorName: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dependentInfo

```TypeScript
dependentInfo: Array<ElementInfo>
```

使用该可观察对象的组件信息。若对象没有用在任何UI上，则返回空数组。

**Type:** Array&lt;ElementInfo&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-DecoratorInfo-dependentInfo: Array<ElementInfo>--><!--Device-DecoratorInfo-dependentInfo: Array<ElementInfo>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## owningComponentId

```TypeScript
owningComponentId: number
```

V1对象返回被使用的组件id。

**当V1对象有属性使用[@Track](../../../ui/state-management/arkts-track.md)装饰器时，无组件id，返回-1；V2对象同样无组件id，返回-1。**

**Type:** number

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-DecoratorInfo-owningComponentId: number--><!--Device-DecoratorInfo-owningComponentId: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## owningComponentOrClassName

```TypeScript
owningComponentOrClassName: string
```

V1对象返回被使用的组件名称。

V1对象有属性使用[@Track](../../../ui/state-management/arkts-track.md)装饰器时返回对象名称。

V2对象返回对象名称。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-DecoratorInfo-owningComponentOrClassName: string--><!--Device-DecoratorInfo-owningComponentOrClassName: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stateVariableName

```TypeScript
stateVariableName: string
```

被装饰器装饰的属性名称。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-DecoratorInfo-stateVariableName: string--><!--Device-DecoratorInfo-stateVariableName: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

