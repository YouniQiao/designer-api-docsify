# WithThemeAttribute

Defines the WithTheme attribute functions..

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface WithThemeAttribute--><!--Device-unnamed-export declare interface WithThemeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## applyAttributesFinish

```TypeScript
default applyAttributesFinish(): void
```

Notify the component is finished setting up its attributes.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WithThemeAttribute-default applyAttributesFinish(): void--><!--Device-WithThemeAttribute-default applyAttributesFinish(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## debugLine

```TypeScript
default debugLine(sourceLine: string, moduleName?: string): this
```

Set the component's source code redirection information.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WithThemeAttribute-default debugLine(sourceLine: string, moduleName?: string): this--><!--Device-WithThemeAttribute-default debugLine(sourceLine: string, moduleName?: string): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sourceLine | string | Yes | the source code line. |
| moduleName | string | No | module to which the component belongs. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setWithThemeOptions

```TypeScript
default setWithThemeOptions(options: WithThemeOptions | undefined): this
```

Sets the WithTheme options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WithThemeAttribute-default setWithThemeOptions(options: WithThemeOptions | undefined): this--><!--Device-WithThemeAttribute-default setWithThemeOptions(options: WithThemeOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [WithThemeOptions](arkts-arkui-withthemeoptions-i.md) \| undefined | Yes | The options to create a WithTheme. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns instance of WithThemeAttribute. |

