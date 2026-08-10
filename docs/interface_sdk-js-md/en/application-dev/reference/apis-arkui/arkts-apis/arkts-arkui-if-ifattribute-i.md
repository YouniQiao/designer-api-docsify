# IfAttribute

支持[ElseIf](../../../reference/apis-arkui/arkui-ts/ts-rendering-control-ifelse-sta.md#elseif)、  
[Else](../../../reference/apis-arkui/arkui-ts/ts-rendering-control-ifelse-sta.md#else)和  
[debugLine](../../../reference/apis-arkui/arkui-ts/ts-rendering-control-ifelse-sta.md#debugline24)属性。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface IfAttribute--><!--Device-unnamed-export declare interface IfAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Else

```TypeScript
Else(
        content_: CustomBuilder
    ): void
```

定义Else分支。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IfAttribute-Else(        content_: CustomBuilder    ): void--><!--Device-IfAttribute-Else(        content_: CustomBuilder    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | Yes | ElseIf分支代码 |

## ElseIf

```TypeScript
ElseIf(
        condition: boolean,
        content_: CustomBuilder
    ): this
```

定义ElseIf分支。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IfAttribute-ElseIf(        condition: boolean,        content_: CustomBuilder    ): this--><!--Device-IfAttribute-ElseIf(        condition: boolean,        content_: CustomBuilder    ): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| condition | boolean | Yes | 分支判断条件。&lt;br&gt;true: 执行该分支的UI描述。&lt;br&gt;false: 不执行该分支的UI描述。 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | Yes | ElseIf分支代码 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## applyAttributesFinish

```TypeScript
applyAttributesFinish(): void
```

如果已完成设置其属性，则通知。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IfAttribute-applyAttributesFinish(): void--><!--Device-IfAttribute-applyAttributesFinish(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## debugLine

```TypeScript
debugLine(sourceLine: string, moduleName?: string): this
```

设置组件源码重定向信息。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IfAttribute-debugLine(sourceLine: string, moduleName?: string): this--><!--Device-IfAttribute-debugLine(sourceLine: string, moduleName?: string): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sourceLine | string | Yes | 源码行号。 |
| moduleName | string | No | 组件所属模块名。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setIfOptions

```TypeScript
setIfOptions(condition: boolean): this
```

设置If选项

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IfAttribute-setIfOptions(condition: boolean): this--><!--Device-IfAttribute-setIfOptions(condition: boolean): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| condition | boolean | Yes | 条件分支。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | IfAttribute实例 |

