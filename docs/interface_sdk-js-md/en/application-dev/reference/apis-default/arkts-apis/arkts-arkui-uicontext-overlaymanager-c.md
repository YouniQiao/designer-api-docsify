# OverlayManager

class OverlayManager

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class OverlayManager--><!--Device-unnamed-export declare class OverlayManager-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## addComponentContent

```TypeScript
addComponentContent<T>(content: ComponentContent<T>, index?: int): void
```

Add the ComponentContent to the OverlayManager.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OverlayManager-addComponentContent<T>(content: ComponentContent<T>, index?: int): void--><!--Device-OverlayManager-addComponentContent<T>(content: ComponentContent<T>, index?: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | ComponentContent&lt;T&gt; | Yes | The content will be added to the OverlayManager. |
| index | int | No |  |

## addComponentContentWithOrder

```TypeScript
addComponentContentWithOrder<T>(content: ComponentContent<T>, levelOrder?: LevelOrder): void
```

Add the ComponentContent to the OverlayManager with order.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OverlayManager-addComponentContentWithOrder<T>(content: ComponentContent<T>, levelOrder?: LevelOrder): void--><!--Device-OverlayManager-addComponentContentWithOrder<T>(content: ComponentContent<T>, levelOrder?: LevelOrder): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | ComponentContent&lt;T&gt; | Yes | The content will be added to the OverlayManager. |
| levelOrder | [LevelOrder](../../apis-arkui/arkts-apis/arkts-arkui-promptaction-levelorder-c.md) | No |  |

## hideAllComponentContents

```TypeScript
hideAllComponentContents(): void
```

Hide all ComponentContents on the OverlayManager.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OverlayManager-hideAllComponentContents(): void--><!--Device-OverlayManager-hideAllComponentContents(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hideComponentContent

```TypeScript
hideComponentContent<T>(content: ComponentContent<T>): void
```

Hide the ComponentContent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OverlayManager-hideComponentContent<T>(content: ComponentContent<T>): void--><!--Device-OverlayManager-hideComponentContent<T>(content: ComponentContent<T>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | ComponentContent&lt;T&gt; | Yes | The content will be hidden. |

## openOrderOverlay

```TypeScript
openOrderOverlay(content: ComponentContent<Object>, options?: OrderOverlayOptions): Promise<void>
```

Opens an overlay with the specified ComponentContent and options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OverlayManager-openOrderOverlay(content: ComponentContent<Object>, options?: OrderOverlayOptions): Promise<void>--><!--Device-OverlayManager-openOrderOverlay(content: ComponentContent<Object>, options?: OrderOverlayOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | ComponentContent&lt;Object&gt; | Yes | The content will be added to the OverlayManager. |
| options | [OrderOverlayOptions](arkts-arkui-uicontext-orderoverlayoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [103307](../../apis-arkui/errorcode-promptAction.md#103307-failed-to-open-the-overlay-due-to-a-system-pop-up-window) | The overlay cannot be opened due to the system pop-up window. |

## removeComponentContent

```TypeScript
removeComponentContent<T>(content: ComponentContent<T>): void
```

Remove the ComponentContent from the OverlayManager.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OverlayManager-removeComponentContent<T>(content: ComponentContent<T>): void--><!--Device-OverlayManager-removeComponentContent<T>(content: ComponentContent<T>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | ComponentContent&lt;T&gt; | Yes | The content will be removed from the OverlayManager. |

## showAllComponentContents

```TypeScript
showAllComponentContents(): void
```

Show all ComponentContents on the OverlayManager.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OverlayManager-showAllComponentContents(): void--><!--Device-OverlayManager-showAllComponentContents(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showComponentContent

```TypeScript
showComponentContent<T>(content: ComponentContent<T>): void
```

Show the ComponentContent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OverlayManager-showComponentContent<T>(content: ComponentContent<T>): void--><!--Device-OverlayManager-showComponentContent<T>(content: ComponentContent<T>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | ComponentContent&lt;T&gt; | Yes | The content will be shown. |

