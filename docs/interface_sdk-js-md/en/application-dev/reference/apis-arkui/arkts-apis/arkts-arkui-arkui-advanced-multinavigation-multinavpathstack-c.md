# MultiNavPathStack

MultiNavPathStack is used for storing pages when shown as split mode.

**Inheritance/Implementation:** MultiNavPathStack extends [NavPathStack](NavPathStack)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class MultiNavPathStack extends NavPathStack--><!--Device-unnamed-export declare class MultiNavPathStack extends NavPathStack-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { MultiNavPathStack, MultiNavigation, SplitPolicy } from '@kit.ArkUI';
```

## clear

```TypeScript
clear(animated?: boolean): void
```

Clear the stack. When keepBottomPage sets true, the page at the bottom of the stack will be retained.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-clear(animated?: boolean): void--><!--Device-MultiNavPathStack-clear(animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| animated | boolean | No | Indicates whether the transition is animated. |

## constructor

```TypeScript
constructor()
```

Creates an instance of MultiNavPathStack.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-constructor()--><!--Device-MultiNavPathStack-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disableAnimation

```TypeScript
disableAnimation(disable: boolean): void
```

disable or enable all transition animation in this MultiNavigation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-disableAnimation(disable: boolean): void--><!--Device-MultiNavPathStack-disableAnimation(disable: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| disable | boolean | Yes | Indicates whether to disable the transition animation. |

## getAllPathName

```TypeScript
getAllPathName(): Array<string>
```

Obtains all the NavDestination name in the stack.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-getAllPathName(): Array<string>--><!--Device-MultiNavPathStack-getAllPathName(): Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | Returns all the NavDestination name in the stack. |

## getIndexByName

```TypeScript
getIndexByName(name: string): Array<int>
```

Obtains the index of all NavDestination pages specified by name.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-getIndexByName(name: string): Array<int>--><!--Device-MultiNavPathStack-getIndexByName(name: string): Array<int>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Indicates the name of the NavDestination. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;int&gt; | Returns the index of all the NavDestinations. |

## getParamByIndex

```TypeScript
getParamByIndex(index: int): Object | undefined
```

Obtains parameter information of the NavDestination page specified by index.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-getParamByIndex(index: int): Object | undefined--><!--Device-MultiNavPathStack-getParamByIndex(index: int): Object | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index of NavDestination page. |

**Return value:**

| Type | Description |
| --- | --- |
| Object | Returns the detailed parameter of the NavDestination if it exists in the stack, otherwise returns undefined. |

## getParamByName

```TypeScript
getParamByName(name: string): Array<Object | null | undefined>
```

Obtains parameter information of all NavDestination pages specified by name.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-getParamByName(name: string): Array<Object | null | undefined>--><!--Device-MultiNavPathStack-getParamByName(name: string): Array<Object | null | undefined>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Indicates the name of the NavDestination. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;Object \| null \| undefined&gt; | Returns the detailed parameter of all the NavDestinations. |

## keepBottomPage

```TypeScript
keepBottomPage(keepBottom: boolean): void
```

Indicates whether to retain the bottom NavDestination of the stack when doing pop or clear.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-keepBottomPage(keepBottom: boolean): void--><!--Device-MultiNavPathStack-keepBottomPage(keepBottom: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keepBottom | boolean | Yes | Indicates whether to retain the bottom NavDestination of the stack. |

## moveIndexToTop

```TypeScript
moveIndexToTop(index: int, animated?: boolean): void
```

Move the first NavDestination of specified index to the top of the stack.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-moveIndexToTop(index: int, animated?: boolean): void--><!--Device-MultiNavPathStack-moveIndexToTop(index: int, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Indicates the index of the NavDestination to be moved to the top. |
| animated | boolean | No | Indicates whether the transition is animated. |

## moveToTop

```TypeScript
moveToTop(name: string, animated?: boolean): int
```

Move the first NavDestination of specified name to the top of the stack. Always the first one in the stack from bottom up when several NavDestinations match the same name.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-moveToTop(name: string, animated?: boolean): int--><!--Device-MultiNavPathStack-moveToTop(name: string, animated?: boolean): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Indicates the name of the NavDestination to be moved to the top. |
| animated | boolean | No | Indicates whether the transition is animated. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the index of the NavDestination if it exists in the stack, otherwise returns -1. |

## pop

```TypeScript
pop(result?: Object, animated?: boolean): NavPathInfo | undefined
```

Pop the top NavDestination of the stack. When keepBottomPage sets true, the page at the bottom of the stack will be retained.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-pop(result?: Object, animated?: boolean): NavPathInfo | undefined--><!--Device-MultiNavPathStack-pop(result?: Object, animated?: boolean): NavPathInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | Object | No | Page Customization processing results. |
| animated | boolean | No | Indicates whether the transition is animated. |

**Return value:**

| Type | Description |
| --- | --- |
| NavPathInfo | Returns the top NavPathInfo if the stack is not empty, otherwise returns undefined. |

## popToIndex

```TypeScript
popToIndex(index: int, animated?: boolean): void
```

Pop to the NavDestination of specified index. Do nothing if index is invalid.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-popToIndex(index: int, animated?: boolean): void--><!--Device-MultiNavPathStack-popToIndex(index: int, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index of NavDestination page. |
| animated | boolean | No | Indicates whether the transition is animated. |

## popToIndex

```TypeScript
popToIndex(index: int, result: Object, animated?: boolean): void
```

Pop to the NavDestination of specified index. Do nothing if index is invalid.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-popToIndex(index: int, result: Object, animated?: boolean): void--><!--Device-MultiNavPathStack-popToIndex(index: int, result: Object, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index of NavDestination page. |
| result | Object | Yes | Page Customization processing results. |
| animated | boolean | No | Indicates whether the transition is animated. |

## popToName

```TypeScript
popToName(name: string, animated?: boolean): int
```

Pop to the NavDestination of specified name. Always the first one in the stack from bottom up when several NavDestinations match the same name.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-popToName(name: string, animated?: boolean): int--><!--Device-MultiNavPathStack-popToName(name: string, animated?: boolean): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the NavDestination. |
| animated | boolean | No | Indicates whether the transition is animated. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the index of the NavDestination if it exists in the stack, otherwise returns -1. |

## popToName

```TypeScript
popToName(name: string, result: Object, animated?: boolean): int
```

Pop to the NavDestination of specified name. Always the first one in the stack from bottom up when several NavDestinations match the same name.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-popToName(name: string, result: Object, animated?: boolean): int--><!--Device-MultiNavPathStack-popToName(name: string, result: Object, animated?: boolean): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the NavDestination. |
| result | Object | Yes | Page Customization processing results. |
| animated | boolean | No | Indicates whether the transition is animated. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the index of the NavDestination if it exists in the stack, otherwise returns -1. |

## pushPath

```TypeScript
pushPath(info: NavPathInfo, animated?: boolean, policy?: SplitPolicy): void
```

Pushes the NavDestination into the stack.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-pushPath(info: NavPathInfo, animated?: boolean, policy?: SplitPolicy): void--><!--Device-MultiNavPathStack-pushPath(info: NavPathInfo, animated?: boolean, policy?: SplitPolicy): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | NavPathInfo | Yes | Indicates the NavDestination to be pushed. |
| animated | boolean | No | Indicates whether the transition is animated. |
| policy | [SplitPolicy](arkts-arkui-arkui-advanced-multinavigation-splitpolicy-e.md) | No | SplitPolicy of the NavDestination which is currently pushed in stack. Default splitPolicy is DETAIL_PAGE. |

## pushPath

```TypeScript
pushPath(info: NavPathInfo, options?: NavigationOptions, policy?: SplitPolicy): void
```

Pushes the NavDestination into the stack.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-pushPath(info: NavPathInfo, options?: NavigationOptions, policy?: SplitPolicy): void--><!--Device-MultiNavPathStack-pushPath(info: NavPathInfo, options?: NavigationOptions, policy?: SplitPolicy): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | NavPathInfo | Yes | Indicates the NavDestination to be pushed. |
| options | NavigationOptions | No | Indicates options of stack operation. |
| policy | [SplitPolicy](arkts-arkui-arkui-advanced-multinavigation-splitpolicy-e.md) | No | SplitPolicy of the NavDestination which is currently pushed in stack. Default splitPolicy is DETAIL_PAGE. |

## pushPathByName

```TypeScript
pushPathByName(name: string, param: Object, animated?: boolean, policy?: SplitPolicy): void
```

Pushes the NavDestination of specified name into the stack.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-pushPathByName(name: string, param: Object, animated?: boolean, policy?: SplitPolicy): void--><!--Device-MultiNavPathStack-pushPathByName(name: string, param: Object, animated?: boolean, policy?: SplitPolicy): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Indicates the name of the NavDestination to be pushed. |
| param | Object | Yes | Indicates the detailed parameter of the NavDestination to be pushed. |
| animated | boolean | No | Indicates whether the transition is animated. |
| policy | [SplitPolicy](arkts-arkui-arkui-advanced-multinavigation-splitpolicy-e.md) | No | SplitPolicy of the NavDestination which is currently pushed in stack. Default splitPolicy is DETAIL_PAGE. |

## pushPathByName

```TypeScript
pushPathByName(
    name: string, param: Object, onPop?: Callback<PopInfo>, animated?: boolean, policy?: SplitPolicy): void
```

Pushes the NavDestination of specified name into the stack.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-pushPathByName(    name: string, param: Object, onPop?: Callback<PopInfo>, animated?: boolean, policy?: SplitPolicy): void--><!--Device-MultiNavPathStack-pushPathByName(    name: string, param: Object, onPop?: Callback<PopInfo>, animated?: boolean, policy?: SplitPolicy): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Indicates the name of the NavDestination to be pushed. |
| param | Object | Yes | Indicates the detailed parameter of the NavDestination to be pushed. |
| onPop | Callback&lt;PopInfo&gt; | No | The callback when next page returns. |
| animated | boolean | No | Indicates whether the transition is animated. |
| policy | [SplitPolicy](arkts-arkui-arkui-advanced-multinavigation-splitpolicy-e.md) | No | SplitPolicy of the NavDestination which is currently pushed in stack. Default splitPolicy is DETAIL_PAGE. |

## removeByIndexes

```TypeScript
removeByIndexes(indexes: Array<int>): int
```

Remove the specified NavDestinations by indexes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-removeByIndexes(indexes: Array<int>): int--><!--Device-MultiNavPathStack-removeByIndexes(indexes: Array<int>): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| indexes | Array&lt;int&gt; | Yes | Indicates the indexes of the NavDestinations to be removed. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the number of removed pages. Invalid indexes will be ignored. |

## removeByName

```TypeScript
removeByName(name: string): int
```

Remove the specified NavDestination by name.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-removeByName(name: string): int--><!--Device-MultiNavPathStack-removeByName(name: string): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Indicates the name of the NavDestination to be removed. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the number of removed NavDestinations. |

## replacePath

```TypeScript
replacePath(info: NavPathInfo, animated?: boolean): void
```

Replace the current NavDestination with the one specificed by NavPathInfo.The current NavDestination will be destroyed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-replacePath(info: NavPathInfo, animated?: boolean): void--><!--Device-MultiNavPathStack-replacePath(info: NavPathInfo, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | NavPathInfo | Yes | Indicates the new NavDestination in top of the stack. |
| animated | boolean | No | Indicates whether the transition is animated. |

## replacePath

```TypeScript
replacePath(info: NavPathInfo, options?: NavigationOptions): void
```

Replace the current NavDestination with the one specificed by NavPathInfo.The current NavDestination will be destroyed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-replacePath(info: NavPathInfo, options?: NavigationOptions): void--><!--Device-MultiNavPathStack-replacePath(info: NavPathInfo, options?: NavigationOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | NavPathInfo | Yes | Indicates the new NavDestination in top of the stack. |
| options | NavigationOptions | No | Indicates options of stack operation. |

## replacePathByName

```TypeScript
replacePathByName(name: string, param: Object, animated?: boolean): void
```

Replace the current NavDestination with the one specificed by name.The current NavDestination will be destroyed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-replacePathByName(name: string, param: Object, animated?: boolean): void--><!--Device-MultiNavPathStack-replacePathByName(name: string, param: Object, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Indicates name of the new NavDestination in top of stack. |
| param | Object | Yes | Indicates the detailed parameter of the new NavDestination in top of the stack. |
| animated | boolean | No | Indicates whether the transition is animated. |

## setHomeWidthRange

```TypeScript
setHomeWidthRange(minPercent: double, maxPercent: double): void
```

Sets the dragable range of the home page width.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-setHomeWidthRange(minPercent: double, maxPercent: double): void--><!--Device-MultiNavPathStack-setHomeWidthRange(minPercent: double, maxPercent: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| minPercent | double | Yes | Minimum Home Width Percentage. |
| maxPercent | double | Yes | Maximum Home Width Percentage. |

## setPlaceholderPage

```TypeScript
setPlaceholderPage(info: NavPathInfo): void
```

Set placeholder NavDestination.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-setPlaceholderPage(info: NavPathInfo): void--><!--Device-MultiNavPathStack-setPlaceholderPage(info: NavPathInfo): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | NavPathInfo | Yes | info of placeHolder NavDestination. |

## size

```TypeScript
size(): int
```

Obtains the size of the stack.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-size(): int--><!--Device-MultiNavPathStack-size(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the size of the stack. |

## switchFullScreenState

```TypeScript
switchFullScreenState(isFullScreen?: boolean): boolean
```

Switches the details page of the split-mode page on the top stack to full screen (true)or split (false).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiNavPathStack-switchFullScreenState(isFullScreen?: boolean): boolean--><!--Device-MultiNavPathStack-switchFullScreenState(isFullScreen?: boolean): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isFullScreen | boolean | No | Whether to switch to full screen. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns switch result success(true) or failure(false). |

