# TabsController

Provides methods for switching tabs.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare class TabsController--><!--Device-unnamed-export declare class TabsController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## changeIndex

```TypeScript
changeIndex(value: int): void
```

Switches to the specified tab.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabsController-changeIndex(value: int): void--><!--Device-TabsController-changeIndex(value: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | Index of the tab. If this parameter is set to a value less than 0 or greater than the maximum number, the default value 0 is used. |

## constructor

```TypeScript
constructor()
```

constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabsController-constructor()--><!--Device-TabsController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## preloadItems

```TypeScript
preloadItems(indices: Array<int> | undefined): Promise<void>
```

Called when need to preload specified tab content.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabsController-preloadItems(indices: Array<int> | undefined): Promise<void>--><!--Device-TabsController-preloadItems(indices: Array<int> | undefined): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| indices | Array&lt;int&gt; \| undefined | Yes | Indices of tab content to be preloaded. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter invalid. Possible causes: <br> 1. The parameter type is not Array&lt;int&gt;. <br> 2. The parameter is an empty array. <br> 3. The parameter contains an invalid index. |

## setTabBarOpacity

```TypeScript
setTabBarOpacity(opacity: double): void
```

Set tab bar opacity.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabsController-setTabBarOpacity(opacity: double): void--><!--Device-TabsController-setTabBarOpacity(opacity: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| opacity | double | Yes | opacity |

## setTabBarTranslate

```TypeScript
setTabBarTranslate(translate: TranslateOptions): void
```

Set tab bar translate.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabsController-setTabBarTranslate(translate: TranslateOptions): void--><!--Device-TabsController-setTabBarTranslate(translate: TranslateOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| translate | [TranslateOptions](../../apis-arkui/arkts-components/arkts-arkui-translateoptions-i.md) | Yes | translate options |

