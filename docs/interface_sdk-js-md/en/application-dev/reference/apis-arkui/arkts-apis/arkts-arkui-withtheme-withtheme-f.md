# WithTheme

## WithTheme

```TypeScript
export declare function WithTheme(
    options: WithThemeOptions | undefined, 
    content_?: CustomBuilder,
): WithThemeAttribute
```

设置应用局部页面自定义主题风格。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function WithTheme(    options: WithThemeOptions | undefined,     content_?: CustomBuilder,): WithThemeAttribute--><!--Device-unnamed-export declare function WithTheme(    options: WithThemeOptions | undefined,     content_?: CustomBuilder,): WithThemeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [WithThemeOptions](arkts-arkui-withthemeoptions-i.md) \| undefined | Yes | 设置作用域内组件配色。 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 支持单个子组件。 |

**Return value:**

| Type | Description |
| --- | --- |
| [WithThemeAttribute](arkts-arkui-withthemeattribute-c.md) |  |


## WithTheme

```TypeScript
export declare function WithTheme(
    style_: CustomBuilderT<WithThemeAttribute>,
    content_?: CustomBuilder,
): WithThemeAttribute
```

用于WithTheme定义

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function WithTheme(    style_: CustomBuilderT<WithThemeAttribute>,    content_?: CustomBuilder,): WithThemeAttribute--><!--Device-unnamed-export declare function WithTheme(    style_: CustomBuilderT<WithThemeAttribute>,    content_?: CustomBuilder,): WithThemeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;WithThemeAttribute&gt; | Yes | WithTheme属性实例 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 容器 |

**Return value:**

| Type | Description |
| --- | --- |
| [WithThemeAttribute](arkts-arkui-withthemeattribute-c.md) | WithTheme属性 |

