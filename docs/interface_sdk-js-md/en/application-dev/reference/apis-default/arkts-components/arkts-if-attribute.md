# IfAttribute

The IfAttribute.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare interface IfAttribute--><!--Device-unnamed-export declare interface IfAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Else

```TypeScript
Else(
        content_: CustomBuilder
    ): void
```

Defines 'Else' branch.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IfAttribute-Else(        content_: CustomBuilder    ): void--><!--Device-IfAttribute-Else(        content_: CustomBuilder    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | Yes | code for the branch |

## ElseIf

```TypeScript
ElseIf(
        condition: boolean,
        content_: CustomBuilder
    ): this
```

Defines 'ElseIf' branch.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IfAttribute-ElseIf(        condition: boolean,        content_: CustomBuilder    ): this--><!--Device-IfAttribute-ElseIf(        condition: boolean,        content_: CustomBuilder    ): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| condition | boolean | Yes | condition of the branch. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | Yes | code for the branch |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## applyAttributesFinish

```TypeScript
applyAttributesFinish(): void
```

Notify If has finished setting up its attributes.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IfAttribute-applyAttributesFinish(): void--><!--Device-IfAttribute-applyAttributesFinish(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## debugLine

```TypeScript
debugLine(sourceLine: string, moduleName?: string): this
```

Set the component's source code redirection information.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IfAttribute-debugLine(sourceLine: string, moduleName?: string): this--><!--Device-IfAttribute-debugLine(sourceLine: string, moduleName?: string): this-End-->

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

## setIfOptions

```TypeScript
setIfOptions(condition: boolean): this
```

Sets If options.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IfAttribute-setIfOptions(condition: boolean): this--><!--Device-IfAttribute-setIfOptions(condition: boolean): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| condition | boolean | Yes | condition of the branch. |

**Return value:**

| Type | Description |
| --- | --- |
| this | IfAttribute instance |

