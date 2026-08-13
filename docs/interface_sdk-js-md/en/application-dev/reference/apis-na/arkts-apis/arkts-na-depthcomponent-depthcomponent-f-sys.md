# DepthComponent (System API)

## DepthComponent

```TypeScript
@ComponentBuilder
export declare function DepthComponent(
    background: ResourceStr | PixelMap,
    options?: DepthComponentOptions,
    content_?: CustomBuilder,
): DepthComponentAttribute
```

Defines DepthComponent Component

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function DepthComponent(    background: ResourceStr | PixelMap,    options?: DepthComponentOptions,    content_?: CustomBuilder,): DepthComponentAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function DepthComponent(    background: ResourceStr | PixelMap,    options?: DepthComponentOptions,    content_?: CustomBuilder,): DepthComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| background | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [PixelMap](../../apis-arkui/arkts-components/arkts-arkui-pixelmap-t.md) | Yes | Background resource (required). |
| options | [DepthComponentOptions](arkts-na-depthcomponent-depthcomponentoptions-i-sys.md) | No | DepthComponent options. |
| content_ | CustomBuilder | No | Subcomponents of DepthComponent. |

**Return value:**

| Type | Description |
| --- | --- |
| [DepthComponentAttribute](arkts-na-depthcomponent-depthcomponentattribute-i.md) |  |


## DepthComponent

```TypeScript
@Builder
export declare function DepthComponent(
  style_: CustomBuilderT<DepthComponentAttribute>,
  content_?: CustomBuilder,
): DepthComponentAttribute
```

Defines DepthComponent

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function DepthComponent(  style_: CustomBuilderT<DepthComponentAttribute>,  content_?: CustomBuilder,): DepthComponentAttribute--><!--Device-unnamed-@Builderexport declare function DepthComponent(  style_: CustomBuilderT<DepthComponentAttribute>,  content_?: CustomBuilder,): DepthComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;[DepthComponentAttribute](arkts-na-depthcomponent-depthcomponentattribute-i.md)&gt; | Yes | DepthComponent attribute instance |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [DepthComponentAttribute](arkts-na-depthcomponent-depthcomponentattribute-i.md) |  |

