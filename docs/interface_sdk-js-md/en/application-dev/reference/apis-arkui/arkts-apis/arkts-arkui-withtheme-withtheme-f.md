# WithTheme

## WithTheme

```TypeScript
export declare function WithTheme(
    options: WithThemeOptions | undefined, 
    content_?: CustomBuilder,
): WithThemeAttribute
```

Defines WithTheme Component

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function WithTheme(    options: WithThemeOptions | undefined,     content_?: CustomBuilder,): WithThemeAttribute--><!--Device-unnamed-export declare function WithTheme(    options: WithThemeOptions | undefined,     content_?: CustomBuilder,): WithThemeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [WithThemeOptions](arkts-arkui-withtheme-withthemeoptions-i.md) \| undefined | Yes | options of WithTheme. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No | the content of the component |

**Return value:**

| Type | Description |
| --- | --- |
| [WithThemeAttribute](arkts-arkui-withtheme-withthemeattribute-i.md) |  |


## WithTheme

```TypeScript
export declare function WithTheme(
    style_: CustomBuilderT<WithThemeAttribute>,
    content_?: CustomBuilder,
): WithThemeAttribute
```

Defines the WithTheme component

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function WithTheme(    style_: CustomBuilderT<WithThemeAttribute>,    content_?: CustomBuilder,): WithThemeAttribute--><!--Device-unnamed-export declare function WithTheme(    style_: CustomBuilderT<WithThemeAttribute>,    content_?: CustomBuilder,): WithThemeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[WithThemeAttribute](arkts-arkui-withtheme-withthemeattribute-i.md)&gt; | Yes | WithTheme attribute instance |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [WithThemeAttribute](arkts-arkui-withtheme-withthemeattribute-i.md) | WithThemeAttribute |

