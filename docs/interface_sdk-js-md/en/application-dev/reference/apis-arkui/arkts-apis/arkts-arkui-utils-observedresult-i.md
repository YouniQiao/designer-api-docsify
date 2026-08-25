# ObservedResult

The return result that defines whether the object data is observable.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## decoratorInfo

```TypeScript
decoratorInfo: DecoratorInfo[]
```

The UI component information associated with the object data. If the data object can not be observed, will return empty array.

**Type:** [DecoratorInfo](arkts-arkui-utils-decoratorinfo-i.md)[]

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isObserved

```TypeScript
isObserved: boolean
```

Whether the object data of class/Array/Map/Set/Date type is observable. if true, the object data can be observed. if false, the object data can not be not observed.

**Type:** boolean

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reason

```TypeScript
reason: string
```

Reasons why the object data of class/Array/Map/Set/Date type can be observed or not. 1 The object data is not an observable object. 2 The object data is observed data for the following reasons: 2.1 The object data is decorated with @Observed. 2.2 The object data is decorated with V2 @ObservedV2 and @Trace. 2.3 The object data is object literal decorated with V1 decorators or wrapped by makeObserved. 2.4 The object data is built-in type data (Array/Map/Set/Date) decorated with V1/V2 decorators or wrapped by makeObserved. 2.5 The object data is decorated with @Observed, but not used in UI. 2.6 The object data is decorated with V2 @ObservedV2 and @Trace, but not used in UI. 2.7 The object data is object literal decorated with V1 decorators or wrapped by makeObserved, but not used in UI. 2.8 The object data is built-in type data (Array/Map/Set/Date) decorated with V1/V2 decorators or wrapped by makeObserved, but not used in UI.

**Type:** string

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
