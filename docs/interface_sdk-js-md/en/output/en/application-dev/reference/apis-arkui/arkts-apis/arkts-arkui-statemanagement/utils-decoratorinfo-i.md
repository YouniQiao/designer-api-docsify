# DecoratorInfo

The UI component information associated with the object data.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-unnamed-export interface DecoratorInfo--><!--Device-unnamed-export interface DecoratorInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## decoratorName

```TypeScript
decoratorName: string
```

Decorator name of the object data.

**Type:** string

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DecoratorInfo-decoratorName: string--><!--Device-DecoratorInfo-decoratorName: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dependentInfo

```TypeScript
dependentInfo: ElementInfo[]
```

Dependent component information including custom component and UI component (Text, Image) for the object data. For the V2 @Monitor or @Computed scenario, will return the id and decorated function name by @Monitor or @Computed. For V2 scenario, if it is not used in the UI, nor on @Monitor or @Computed, return an empty array. For V1 scenario, if it is not used in the UI, will return an empty array.

**Type:** ElementInfo[]

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DecoratorInfo-dependentInfo: ElementInfo[]--><!--Device-DecoratorInfo-dependentInfo: ElementInfo[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## owningComponentId

```TypeScript
owningComponentId: int
```

The custom component id that the object data belongs to. In the V1 scenario, return the custom component id, in the V2 @ObservedV2 scenario, return -1.

**Type:** int

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DecoratorInfo-owningComponentId: int--><!--Device-DecoratorInfo-owningComponentId: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## owningComponentOrClassName

```TypeScript
owningComponentOrClassName: string
```

The custom component name that the object data belongs to. In the V1 scenario, return the custom component name, in the V2 @ObservedV2 scenario, return class name.

**Type:** string

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DecoratorInfo-owningComponentOrClassName: string--><!--Device-DecoratorInfo-owningComponentOrClassName: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stateVariableName

```TypeScript
stateVariableName: string
```

State Variable name of the object data.

**Type:** string

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DecoratorInfo-stateVariableName: string--><!--Device-DecoratorInfo-stateVariableName: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

