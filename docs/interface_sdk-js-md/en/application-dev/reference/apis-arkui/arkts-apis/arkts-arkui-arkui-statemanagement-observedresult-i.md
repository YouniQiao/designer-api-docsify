# ObservedResult

Provides the result of whether the object can be observed.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-unnamed-export interface ObservedResult--><!--Device-unnamed-export interface ObservedResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## decoratorInfo

```TypeScript
decoratorInfo: Array<DecoratorInfo>
```

Decorator and component information associated with the observable object. If the object cannot be observed, the array is empty.

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

Whether an object can be observed.

**true**: The object can be observed.

**false**: The object cannot be observed.

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

Reason for the object's observability.

For the object that cannot be observed: The object itself cannot be observed.

For the object that can be observed:

1. The V1 object is decorated by the \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_decorator or the object is converted by the [makeV1Observed]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_ method.2. The V1 object is decorated by the \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_decorator or the object is converted by the [makeV1Observed]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_ method, but the object is not used by the UI component.3. The V1 object is converted by the [enableV2Compatibility]\_\_\_JSDOC\_LINK\_DESC\_USD\_6\_\_\_ method and then passed to the V2 component.4. The V1 object is converted by the [enableV2Compatibility]\_\_\_JSDOC\_LINK\_DESC\_USD\_7\_\_\_ method and then passed to the V2 component, but is not used by the V2 component.5. The V2 object is decorated by the  
\_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_ decorator.6. The V2 object is converted by the [makeObserved]\_\_\_JSDOC\_LINK\_DESC\_USD\_8\_\_\_ method.7. The V2 object is of the Array, Map, Set, or Date type.8. The V2 object is decorated by the  
\_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_ decorator,but is not used by the UI component.9. The V2 object is converted by the [makeObserved]\_\_\_JSDOC\_LINK\_DESC\_USD\_9\_\_\_ method, but the object is not used by the UI component.10. The V2 object is of the Array, Map, Set, or Date type, but is not used by the UI component.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ObservedResult-reason: string--><!--Device-ObservedResult-reason: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

