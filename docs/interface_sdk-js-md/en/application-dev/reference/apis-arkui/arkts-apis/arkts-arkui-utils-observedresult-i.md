# ObservedResult

对象是否可被观察的结果。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-unnamed-export interface ObservedResult--><!--Device-unnamed-export interface ObservedResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## decoratorInfo

```TypeScript
decoratorInfo: DecoratorInfo[]
```

对象可被观察时，数组中内容为对象关联的装饰器和组件信息。对象不可被观察时，此数组为空。

**Type:** [DecoratorInfo](arkts-arkui-arkui-statemanagement-decoratorinfo-i.md)[]

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ObservedResult-decoratorInfo: DecoratorInfo[]--><!--Device-ObservedResult-decoratorInfo: DecoratorInfo[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isObserved

```TypeScript
isObserved: boolean
```

对象是否可被观察。

true：表示是可被观察对象。

false：表示不是可被观察对象。

**Type:** boolean

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ObservedResult-isObserved: boolean--><!--Device-ObservedResult-isObserved: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reason

```TypeScript
reason: string
```

对象是否可被观察的原因。

不可被观察原因：对象本身是不可被观察的。

可被观察原因或使用场景：

1. 对象被[@Observed](../../../ui/state-management-static/arkts-static-observed-and-objectlink.md)装饰器装饰。 2. 对象被[@ObservedV2和@Trace](../../../ui/state-management-static/arkts-static-new-observedV2-and-trace.md)装饰。 3. 对象为被V1装饰器装饰或被[makeObserved](../../apis-arkts/arkts-apis/arkts-arkts-atomics-atomicreference-c.md/arkts-arkts-atomics-atomicreference-c.md#compareandswap)方法转换的interface字面量。 4. 对象为被V1/V2装饰器装饰或被makeObserved方法转换的Array/Map/Set/Date类型。5. 对象被@Observed装饰器装饰，但未使用在UI上。 6. 对象被@ObservedV2和@Trace装饰，但未使用在UI上。 7. 对象为被V1装饰器装饰或被makeObserved方法转换的interface字面量，但未用在UI上。 8. 对象为被V1/V2装饰器装饰或被makeObserved方法转换的Array/Map/Set/Date类型，但未用在UI上。

**Type:** string

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ObservedResult-reason: string--><!--Device-ObservedResult-reason: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

