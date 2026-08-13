# Path

## Path

```TypeScript
@ComponentBuilder
export declare function Path(
    options?: PathOptions
): PathAttribute
```

Path is returned when the parameter is transferred.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Path(    options?: PathOptions): PathAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Path(    options?: PathOptions): PathAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PathOptions](arkts-arkui-path-pathoptions-i.md) | No | The options to create a Path |

**Return value:**

| Type | Description |
| --- | --- |
| [PathAttribute](arkts-arkui-path-pathattribute-i.md) | The attribute of the Path. |


## Path

```TypeScript
@Builder
export declare function Path(
    style: CustomBuilderT<PathAttribute>,
): PathAttribute
```

Defines Path Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Path(    style: CustomBuilderT<PathAttribute>,): PathAttribute--><!--Device-unnamed-@Builderexport declare function Path(    style: CustomBuilderT<PathAttribute>,): PathAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | CustomBuilderT&lt;[PathAttribute](arkts-arkui-path-pathattribute-i.md)&gt; | Yes | the callback to set up component's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [PathAttribute](arkts-arkui-path-pathattribute-i.md) |  |

