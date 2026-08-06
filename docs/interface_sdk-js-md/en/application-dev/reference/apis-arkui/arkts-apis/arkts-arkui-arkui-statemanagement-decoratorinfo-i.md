# DecoratorInfo

Defines the decorator and component information associated with the observable object.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-unnamed-export interface DecoratorInfo--><!--Device-unnamed-export interface DecoratorInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## decoratorName

```TypeScript
decoratorName: string
```

Decorator name.

For a V1 object, the value is the name of the decorator associated with the object.

If the V1 object uses \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_, the value is **'@Track'**.

If the V2 object uses \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_, the value is  
**'@Trace'**.

If the V2 object uses [makeObserved]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, the value is **'MakeObserved'**.

If the V2 object uses [enableV2Compatibility]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_, the value is  
**'EnableV2Compatible'**.

If the V2 object uses built-in data, the value is **'ProxyObservedV2'**.

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

Information about the component that uses the observable object. If the object is not used in any UI, an empty array is returned.

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

Component ID.

For a V1 object, the component ID is returned.

For the V1 object whose properties are decorated by the \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_decorator or for the V2 object, **-1** is returned instead of the component ID.

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

Component or object name.

For a V1 object, the component name is returned.

For a V1 object whose properties are decorated by the \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_decorator, the object name is returned.

For a V2 object, the object name is returned.

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

Name of the attribute decorated by the decorator.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-DecoratorInfo-stateVariableName: string--><!--Device-DecoratorInfo-stateVariableName: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

