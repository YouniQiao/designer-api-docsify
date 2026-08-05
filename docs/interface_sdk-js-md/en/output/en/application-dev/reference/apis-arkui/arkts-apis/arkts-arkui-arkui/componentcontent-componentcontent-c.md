# ComponentContent

Defines ComponentContent.

**Inheritance/Implementation:** ComponentContent extends [ComponentContentBase](componentcontent-componentcontentbase-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class ComponentContent<T = undefined> extends ComponentContentBase--><!--Device-unnamed-export declare class ComponentContent<T = undefined> extends ComponentContentBase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(uiContext: UIContext, builder: WrappedBuilder<CustomBuilder>)
```

Constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentContent-constructor(uiContext: UIContext, builder: WrappedBuilder<CustomBuilder>)--><!--Device-ComponentContent-constructor(uiContext: UIContext, builder: WrappedBuilder<CustomBuilder>)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uiContext | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | uiContext used to create the ComponentContent |
| builder | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; | Yes | Defines the builder that will be called to build ComponentContent. |

## constructor

```TypeScript
constructor(uiContext: UIContext, builder: WrappedBuilder<CustomBuilderT<T>>, args: T)
```

Constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentContent-constructor(uiContext: UIContext, builder: WrappedBuilder<CustomBuilderT<T>>, args: T)--><!--Device-ComponentContent-constructor(uiContext: UIContext, builder: WrappedBuilder<CustomBuilderT<T>>, args: T)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uiContext | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | uiContext used to create the ComponentContent |
| builder | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;CustomBuilderT&lt;T&gt;&gt; | Yes | Defines the builder that will be called to build ComponentContent. |
| args | T | Yes | Parameters used to update the ComponentContent. |

## constructor

```TypeScript
constructor(uiContext: UIContext, builder: WrappedBuilder<CustomBuilderT<T>>, args: T, options: BuildOptions)
```

Constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentContent-constructor(uiContext: UIContext, builder: WrappedBuilder<CustomBuilderT<T>>, args: T, options: BuildOptions)--><!--Device-ComponentContent-constructor(uiContext: UIContext, builder: WrappedBuilder<CustomBuilderT<T>>, args: T, options: BuildOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uiContext | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | uiContext used to create the ComponentContent |
| builder | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;CustomBuilderT&lt;T&gt;&gt; | Yes | Defines the builder that will be called to build ComponentContent.ComponentContent. |
| args | T | Yes | Parameters used to update the ComponentContent. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Defines the options that will be used when building. |

## dispose

```TypeScript
dispose(): void
```

Dispose the ComponentContent immediately.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentContent-dispose(): void--><!--Device-ComponentContent-dispose(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isDisposed

```TypeScript
isDisposed(): boolean
```

Get if the ComponentContent is disposed.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentContent-isDisposed(): boolean--><!--Device-ComponentContent-isDisposed(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | - Returns true if the ComponentContent is disposed, false otherwise. |

## isTransferred

```TypeScript
isTransferred(): boolean
```

Returns a flag indicating whether the current ComponentContent was obtained through dynamic-static conversion, includes conversions in both directions: dynamic-to-static and static-to-dynamic.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentContent-isTransferred(): boolean--><!--Device-ComponentContent-isTransferred(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | - Returns true if the ComponentContent was converted between dynamic and static states, |

## recycle

```TypeScript
recycle(): void
```

Recycle the ComponentContent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentContent-recycle(): void--><!--Device-ComponentContent-recycle(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reuse

```TypeScript
reuse(param?: RecordData): void
```

Reuse the ComponentContent based on the provided parameters.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentContent-reuse(param?: RecordData): void--><!--Device-ComponentContent-reuse(param?: RecordData): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Parameters for reusing ComponentContent. These parameters will be directly applied to the reuse of all top-level custom components in the ComponentContent. They should include the content required for the constructor parameters of each custom component; otherwise, undefined behavior may occur. Calling this method will synchronously trigger the aboutToReuse lifecycle callback of the internal custom components, with these parameters passed as the callback's input. The default value is undefined,in which case the custom components in the ComponentContent will directly use the data source from the construction phase. |

## update

```TypeScript
update(args: T): void
```

Update the ComponentContent based on the provided parameters.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentContent-update(args: T): void--><!--Device-ComponentContent-update(args: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| args | T | Yes | Parameters used to update the ComponentContent, which must match the types required by the builder bound to the ComponentContent. |

## updateConfiguration

```TypeScript
updateConfiguration(): void
```

Notify ComponentContent to update the configuration to trigger a reload of the ComponentContent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ComponentContent-updateConfiguration(): void--><!--Device-ComponentContent-updateConfiguration(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

