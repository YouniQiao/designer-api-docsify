# ReactiveComponentContent

Defines ReactiveComponentContent.

**Inheritance/Implementation:** ReactiveComponentContent extends [ComponentContentBase](componentcontent-componentcontentbase-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class ReactiveComponentContent extends ComponentContentBase--><!--Device-unnamed-export declare class ReactiveComponentContent extends ComponentContentBase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(uiContext: UIContext, builder: CustomBuilder, options?: BuildOptions)
```

Constructor.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReactiveComponentContent-constructor(uiContext: UIContext, builder: CustomBuilder, options?: BuildOptions)--><!--Device-ReactiveComponentContent-constructor(uiContext: UIContext, builder: CustomBuilder, options?: BuildOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uiContext | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | uiContext used to create the ReactiveComponentContent |
| builder | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Defines the builder that will be called to build ReactiveComponentContent. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Defines the options that will be used when building. |

## dispose

```TypeScript
dispose(): void
```

Dispose the ReactiveComponentContent immediately.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReactiveComponentContent-dispose(): void--><!--Device-ReactiveComponentContent-dispose(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## flushState

```TypeScript
flushState(): void
```

Flushes the current state changes to update the ReactiveComponentContent immediately. This forces a synchronous update of the component with the latest state values.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReactiveComponentContent-flushState(): void--><!--Device-ReactiveComponentContent-flushState(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isDisposed

```TypeScript
isDisposed(): boolean
```

Get if the ReactiveComponentContent is disposed.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReactiveComponentContent-isDisposed(): boolean--><!--Device-ReactiveComponentContent-isDisposed(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | - Returns true if the ReactiveComponentContent is disposed, false otherwise. |

## isTransferred

```TypeScript
isTransferred(): boolean
```

Returns a flag indicating whether the current ReactiveComponentContent was obtained through dynamic-static conversion, includes conversions in both directions: dynamic-to-static and static-to-dynamic.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReactiveComponentContent-isTransferred(): boolean--><!--Device-ReactiveComponentContent-isTransferred(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | - Returns true if the ReactiveComponentContent was converted between dynamic and static |

## recycle

```TypeScript
recycle(): void
```

Recycle the ReactiveComponentContent.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReactiveComponentContent-recycle(): void--><!--Device-ReactiveComponentContent-recycle(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reuse

```TypeScript
reuse(param?: RecordData): void
```

Reuse the ReactiveComponentContent based on the provided parameters.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReactiveComponentContent-reuse(param?: RecordData): void--><!--Device-ReactiveComponentContent-reuse(param?: RecordData): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Parameters for reusing ReactiveComponentContent. These parameters will be directly applied to the reuse of all top-level custom components in the ReactiveComponentContent. They should include the content required for the constructor parameters of each custom component; otherwise,undefined behavior may occur. Calling this method will synchronously trigger the aboutToReuse lifecycle callback of the internal custom components, with these parameters passed as the callback's input. The default value is undefined, in which case the custom components in the ReactiveComponentContent will directly use the data source from the construction phase. |

## updateConfiguration

```TypeScript
updateConfiguration(): void
```

Notify ReactiveComponentContent to update the configuration to trigger a reload of the ReactiveComponentContent.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReactiveComponentContent-updateConfiguration(): void--><!--Device-ReactiveComponentContent-updateConfiguration(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

