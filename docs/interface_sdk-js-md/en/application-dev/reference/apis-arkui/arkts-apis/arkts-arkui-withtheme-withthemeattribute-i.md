# WithThemeAttribute

不支持[通用属性](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md)和[通用事件](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface WithThemeAttribute--><!--Device-unnamed-export declare interface WithThemeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## applyAttributesFinish

```TypeScript
default applyAttributesFinish(): void
```

通知组件已完成设置其属性。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WithThemeAttribute-default applyAttributesFinish(): void--><!--Device-WithThemeAttribute-default applyAttributesFinish(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## debugLine

```TypeScript
default debugLine(sourceLine: string, moduleName?: string): this
```

设置组件的源码跳转信息。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WithThemeAttribute-default debugLine(sourceLine: string, moduleName?: string): this--><!--Device-WithThemeAttribute-default debugLine(sourceLine: string, moduleName?: string): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sourceLine | string | Yes | 源代码行。 |
| moduleName | string | No | 组件所属的模块。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setWithThemeOptions

```TypeScript
default setWithThemeOptions(options: WithThemeOptions | undefined): this
```

设置WithTheme选项。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WithThemeAttribute-default setWithThemeOptions(options: WithThemeOptions | undefined): this--><!--Device-WithThemeAttribute-default setWithThemeOptions(options: WithThemeOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [WithThemeOptions](arkts-arkui-withthemeoptions-i.md) \| undefined | Yes | 创建WithTheme的选项。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回WithThemeAttribute的实例。 |

