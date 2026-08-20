# Circle

## Circle

```TypeScript
@ComponentBuilder
export declare function Circle(
    options?: CircleOptions
): CircleAttribute
```

Circle is returned when the parameter is transferred.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Circle(    options?: CircleOptions): CircleAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Circle(    options?: CircleOptions): CircleAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CircleOptions](arkts-arkui-circle-circleoptions-i.md) | No | The options to create a Circle. |

**Return value:**

| Type | Description |
| --- | --- |
| [CircleAttribute](arkts-arkui-circle-attribute.md) | The attribute of the Circle. |


## Circle

```TypeScript
@Builder
export declare function Circle(
    style: CustomBuilderT<CircleAttribute>
): CircleAttribute
```

Defines Circle Component.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Circle(    style: CustomBuilderT<CircleAttribute>): CircleAttribute--><!--Device-unnamed-@Builderexport declare function Circle(    style: CustomBuilderT<CircleAttribute>): CircleAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;[CircleAttribute](arkts-arkui-circle-attribute.md)&gt; | Yes | Circle options. |

**Return value:**

| Type | Description |
| --- | --- |
| [CircleAttribute](arkts-arkui-circle-attribute.md) |  |

