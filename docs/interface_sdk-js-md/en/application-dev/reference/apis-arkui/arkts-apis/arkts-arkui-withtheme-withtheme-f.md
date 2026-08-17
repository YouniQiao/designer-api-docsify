# WithTheme

## WithTheme

```TypeScript
@ComponentBuilder
export declare function WithTheme(
    options: WithThemeOptions | undefined, 
    content_?: CustomBuilder,
): WithThemeAttribute
```

Defines WithTheme Component

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function WithTheme(    options: WithThemeOptions | undefined,     content_?: CustomBuilder,): WithThemeAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function WithTheme(    options: WithThemeOptions | undefined,     content_?: CustomBuilder,): WithThemeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [WithThemeOptions](arkts-arkui-withtheme-withthemeoptions-i.md) \| undefined | Yes | options of WithTheme. |
| content_ | CustomBuilder | No | the content of the component |

**Return value:**

| Type | Description |
| --- | --- |
| [WithThemeAttribute](arkts-arkui-withtheme-withthemeattribute-i.md) |  |


## WithTheme

```TypeScript
@Builder
export declare function WithTheme(
    style_: CustomBuilderT<WithThemeAttribute>,
    content_?: CustomBuilder,
): WithThemeAttribute
```

Defines the WithTheme component

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function WithTheme(    style_: CustomBuilderT<WithThemeAttribute>,    content_?: CustomBuilder,): WithThemeAttribute--><!--Device-unnamed-@Builderexport declare function WithTheme(    style_: CustomBuilderT<WithThemeAttribute>,    content_?: CustomBuilder,): WithThemeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;[WithThemeAttribute](arkts-arkui-withtheme-withthemeattribute-i.md)&gt; | Yes | WithTheme attribute instance |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [WithThemeAttribute](arkts-arkui-withtheme-withthemeattribute-i.md) | WithThemeAttribute |

