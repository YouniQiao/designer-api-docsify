# NavPathStack

Indicates the information of NavDestinations. Providers methods for controlling destination page in the stack

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class NavPathStack--><!--Device-unnamed-export declare class NavPathStack-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## clear

```TypeScript
clear(animated?: boolean): void
```

Clears the stack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-clear(animated?: boolean): void--><!--Device-NavPathStack-clear(animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| animated | boolean | No | Indicates whether the transition is animated. |

## constructor

```TypeScript
constructor()
```

Creates an instance of NavPathStack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-constructor()--><!--Device-NavPathStack-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disableAnimation

```TypeScript
disableAnimation(value: boolean): void
```

disable or enable all transition animation in this navigation stack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-disableAnimation(value: boolean): void--><!--Device-NavPathStack-disableAnimation(value: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | Indicates whether the transition is animated. |

## getAllPathName

```TypeScript
getAllPathName(): Array<string>
```

Obtains all the NavDestination name in the stack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-getAllPathName(): Array<string>--><!--Device-NavPathStack-getAllPathName(): Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | Returns all the NavDestination name in the stack; |

## getIndexByName

```TypeScript
getIndexByName(name: string): Array<int>
```

Obtains the index of the specified NavDestination.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-getIndexByName(name: string): Array<int>--><!--Device-NavPathStack-getIndexByName(name: string): Array<int>-End-->

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
getParamByIndex(index: int): Object | null | undefined
```

Obtains the param of the specified NavDestination.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-getParamByIndex(index: int): Object | null | undefined--><!--Device-NavPathStack-getParamByIndex(index: int): Object | null | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Indicates the index of the NavDestination. |

**Return value:**

| Type | Description |
| --- | --- |
| Object \| null \| undefined | Returns the detailed parameter of the NavDestination if it exists in the stack, otherwise returns undefined; |

## getParamByName

```TypeScript
getParamByName(name: string): Array<Object | null | undefined>
```

Obtains the param of the specified NavDestination.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-getParamByName(name: string): Array<Object | null | undefined>--><!--Device-NavPathStack-getParamByName(name: string): Array<Object | null | undefined>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Indicates the name of the NavDestination. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;Object \| null \| undefined&gt; | Returns the detailed parameter of all the NavDestinations. |

## getParent

```TypeScript
getParent(): NavPathStack | null
```

Obtains the parent of the current stack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-getParent(): NavPathStack | null--><!--Device-NavPathStack-getParent(): NavPathStack | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [NavPathStack](arkts-na-navigation-navpathstack-c.md) \| null | Returns the parent of the current stack. If no parent, it returns null. |

## getPathStack

```TypeScript
getPathStack(): Array<NavPathInfo>
```

Get the NavPathInfo array.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-getPathStack(): Array<NavPathInfo>--><!--Device-NavPathStack-getPathStack(): Array<NavPathInfo>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[NavPathInfo](arkts-na-navigation-navpathinfo-c.md)&gt; | The NavPathInfo array. |

## moveIndexToTop

```TypeScript
moveIndexToTop(index: int, animated?: boolean): void
```

Moves the specified NavDestination to stack top.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-moveIndexToTop(index: int, animated?: boolean): void--><!--Device-NavPathStack-moveIndexToTop(index: int, animated?: boolean): void-End-->

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

Moves the specified NavDestination to stack top.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-moveToTop(name: string, animated?: boolean): int--><!--Device-NavPathStack-moveToTop(name: string, animated?: boolean): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Indicates the name of the NavDestination to be moved to the top. |
| animated | boolean | No | Indicates whether the transition is animated. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the index of the NavDestination if it exists in the stack, otherwise returns -1; |

## pop

```TypeScript
pop(animated?: boolean): NavPathInfo | undefined
```

Pops the top NavDestination out of the stack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-pop(animated?: boolean): NavPathInfo | undefined--><!--Device-NavPathStack-pop(animated?: boolean): NavPathInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| animated | boolean | No | Indicates whether the transition is animated <br>Default value: true. |

**Return value:**

| Type | Description |
| --- | --- |
| [NavPathInfo](arkts-na-navigation-navpathinfo-c.md) \| undefined | Returns the top NavPathInfo if the stack is not empty, otherwise returns undefined. |

## pop

```TypeScript
pop(result: Object, animated?: boolean): NavPathInfo | undefined
```

Pops the top NavDestination out of the stack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-pop(result: Object, animated?: boolean): NavPathInfo | undefined--><!--Device-NavPathStack-pop(result: Object, animated?: boolean): NavPathInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | Object | Yes | The result of the NavDestination. |
| animated | boolean | No | Indicates whether the transition is animated <br>Default value: true. |

**Return value:**

| Type | Description |
| --- | --- |
| [NavPathInfo](arkts-na-navigation-navpathinfo-c.md) \| undefined | Returns the top NavPathInfo if the stack is not empty, otherwise returns undefined. |

## popToIndex

```TypeScript
popToIndex(index: int, animated?: boolean): void
```

Pops the specified NavDestination out of the stack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-popToIndex(index: int, animated?: boolean): void--><!--Device-NavPathStack-popToIndex(index: int, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Indicates the index of the NavDestination to be popped. |
| animated | boolean | No | Indicates whether the transition is animated. |

## popToIndex

```TypeScript
popToIndex(index: int, result: Object, animated?: boolean): void
```

Pops the specified NavDestination out of the stack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-popToIndex(index: int, result: Object, animated?: boolean): void--><!--Device-NavPathStack-popToIndex(index: int, result: Object, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Indicates the index of the NavDestination to be popped. |
| result | Object | Yes | The result of the NavDestination. |
| animated | boolean | No | Indicates whether the transition is animated. |

## popToName

```TypeScript
popToName(name: string, animated?: boolean): int
```

Pops the specified NavDestination out of the stack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-popToName(name: string, animated?: boolean): int--><!--Device-NavPathStack-popToName(name: string, animated?: boolean): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Indicates the name of the NavDestination to be popped. |
| animated | boolean | No | Indicates whether the transition is animated. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the index of the NavDestination if it exists in the stack, otherwise returns -1; |

## popToName

```TypeScript
popToName(name: string, result: Object, animated?: boolean): int
```

Pops the specified NavDestination out of the stack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-popToName(name: string, result: Object, animated?: boolean): int--><!--Device-NavPathStack-popToName(name: string, result: Object, animated?: boolean): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Indicates the name of the NavDestination to be popped. |
| result | Object | Yes | The result of the NavDestination. |
| animated | boolean | No | Indicates whether the transition is animated. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the index of the NavDestination if it exists in the stack, otherwise returns -1; |

## preloadPath

```TypeScript
preloadPath(info: NavPathInfo, options?: PreloadOptions): Promise<void>
```

Preloads navigation destination page specified by **info**. The preload page will not be displayed immediately, but will be cached. When **pushPath** is called later with matching parameters, preloaded instance will be used for fast display.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-preloadPath(info: NavPathInfo, options?: PreloadOptions): Promise<void>--><!--Device-NavPathStack-preloadPath(info: NavPathInfo, options?: PreloadOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [NavPathInfo](arkts-na-navigation-navpathinfo-c.md) | Yes | Indicates NavDestination to be preloaded. |
| options | [PreloadOptions](arkts-na-navigation-preloadoptions-i.md) | No | Indicates options for preloading. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal error. |
| [100005](../../apis-arkui/errorcode-router.md#100005-builder-function-not-registered-during-navigation) | Builder function not registered. |
| [100006](../../apis-arkui/errorcode-router.md#100006-navdestination-not-found) | NavDestination not found. |

## pushDestination

```TypeScript
pushDestination(info: NavPathInfo, animated?: boolean): Promise<void>
```

Pushes the NavDestination into the stack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-pushDestination(info: NavPathInfo, animated?: boolean): Promise<void>--><!--Device-NavPathStack-pushDestination(info: NavPathInfo, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [NavPathInfo](arkts-na-navigation-navpathinfo-c.md) | Yes | Indicates the NavDestination to be pushed. |
| animated | boolean | No | Indicates whether the transition is animated. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal error. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| [100005](../../apis-arkui/errorcode-router.md#100005-builder-function-not-registered-during-navigation) | Builder function not registered. |
| [100006](../../apis-arkui/errorcode-router.md#100006-navdestination-not-found) | NavDestination not found. |

## pushDestination

```TypeScript
pushDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>
```

Pushes the NavDestination into the stack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-pushDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>--><!--Device-NavPathStack-pushDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [NavPathInfo](arkts-na-navigation-navpathinfo-c.md) | Yes | Indicates the NavDestination to be pushed. |
| options | [NavigationOptions](arkts-na-navigation-navigationoptions-i.md) | No | Indicates options of stack operation. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal error. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| [100005](../../apis-arkui/errorcode-router.md#100005-builder-function-not-registered-during-navigation) | Builder function not registered. |
| [100006](../../apis-arkui/errorcode-router.md#100006-navdestination-not-found) | NavDestination not found. |

## pushDestinationByName

```TypeScript
pushDestinationByName(name: string, param: Object, animated?: boolean): Promise<void>
```

Pushes the specified NavDestination into the stack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-pushDestinationByName(name: string, param: Object, animated?: boolean): Promise<void>--><!--Device-NavPathStack-pushDestinationByName(name: string, param: Object, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Indicates the name of the NavDestination to be pushed. |
| param | Object | Yes | Indicates the detailed parameter of the NavDestination to be pushed. |
| animated | boolean | No | Indicates whether the transition is animated. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal error. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| [100005](../../apis-arkui/errorcode-router.md#100005-builder-function-not-registered-during-navigation) | Builder function not registered. |
| [100006](../../apis-arkui/errorcode-router.md#100006-navdestination-not-found) | NavDestination not found. |

## pushDestinationByName

```TypeScript
pushDestinationByName(name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): Promise<void>
```

Pushes the specified NavDestination into the stack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-pushDestinationByName(name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): Promise<void>--><!--Device-NavPathStack-pushDestinationByName(name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Indicates the name of the NavDestination to be pushed. |
| param | Object | Yes | Indicates the detailed parameter of the NavDestination to be pushed. |
| onPop | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[PopInfo](arkts-na-navigation-popinfo-i.md)&gt; | Yes | The callback when next page returns. |
| animated | boolean | No | Indicates whether the transition is animated. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal error. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| [100005](../../apis-arkui/errorcode-router.md#100005-builder-function-not-registered-during-navigation) | Builder function not registered. |
| [100006](../../apis-arkui/errorcode-router.md#100006-navdestination-not-found) | NavDestination not found. |

## pushPath

```TypeScript
pushPath(info: NavPathInfo, animated?: boolean): void
```

Pushes the NavDestination into the stack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-pushPath(info: NavPathInfo, animated?: boolean): void--><!--Device-NavPathStack-pushPath(info: NavPathInfo, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [NavPathInfo](arkts-na-navigation-navpathinfo-c.md) | Yes | Indicates the NavDestination to be pushed. |
| animated | boolean | No | Indicates whether the transition is animated. |

## pushPath

```TypeScript
pushPath(info: NavPathInfo, options?: NavigationOptions): void
```

Pushes the NavDestination into the stack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-pushPath(info: NavPathInfo, options?: NavigationOptions): void--><!--Device-NavPathStack-pushPath(info: NavPathInfo, options?: NavigationOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [NavPathInfo](arkts-na-navigation-navpathinfo-c.md) | Yes | Indicates the NavDestination to be pushed. |
| options | [NavigationOptions](arkts-na-navigation-navigationoptions-i.md) | No | Indicates options of stack operation. |

## pushPathByName

```TypeScript
pushPathByName(name: string, param: Object | null | undefined, animated?: boolean): void
```

Pushes the specified NavDestination into the stack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-pushPathByName(name: string, param: Object | null | undefined, animated?: boolean): void--><!--Device-NavPathStack-pushPathByName(name: string, param: Object | null | undefined, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Indicates the name of the NavDestination to be pushed. |
| param | Object \| null \| undefined | Yes | Indicates the detailed parameter of the NavDestination to be pushed. |
| animated | boolean | No | Indicates whether the transition is animated. |

## pushPathByName

```TypeScript
pushPathByName(name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): void
```

Pushes the specified NavDestination into the stack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-pushPathByName(name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): void--><!--Device-NavPathStack-pushPathByName(name: string, param: Object, onPop: Callback<PopInfo>, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Indicates the name of the NavDestination to be pushed. |
| param | Object | Yes | Indicates the detailed parameter of the NavDestination to be pushed. |
| onPop | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[PopInfo](arkts-na-navigation-popinfo-i.md)&gt; | Yes | The callback when next page returns. |
| animated | boolean | No | Indicates whether the transition is animated. |

## removeByIndexes

```TypeScript
removeByIndexes(indexes: Array<int>): int
```

Remove the specified NavDestinations by indexes.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-removeByIndexes(indexes: Array<int>): int--><!--Device-NavPathStack-removeByIndexes(indexes: Array<int>): int-End-->

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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-removeByName(name: string): int--><!--Device-NavPathStack-removeByName(name: string): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Indicates the name of the NavDestination to be removed. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the number of removed NavDestinations. |

## removeByNavDestinationId

```TypeScript
removeByNavDestinationId(navDestinationId: string): boolean
```

Remove the specified NavDestination by its navDestinationId.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-removeByNavDestinationId(navDestinationId: string): boolean--><!--Device-NavPathStack-removeByNavDestinationId(navDestinationId: string): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| navDestinationId | string | Yes | Indicates the navDestinationId of the NavDestination to be removed. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if remove successfully, otherwise returns false. |

## replaceDestination

```TypeScript
replaceDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>
```

Replace the NavDestination into the stack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-replaceDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>--><!--Device-NavPathStack-replaceDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [NavPathInfo](arkts-na-navigation-navpathinfo-c.md) | Yes | Indicates the NavDestination to replace in stack. |
| options | [NavigationOptions](arkts-na-navigation-navigationoptions-i.md) | No | Indicates options of stack operation. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal error. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| [100005](../../apis-arkui/errorcode-router.md#100005-builder-function-not-registered-during-navigation) | Builder function not registered. |
| [100006](../../apis-arkui/errorcode-router.md#100006-navdestination-not-found) | NavDestination not found. |

## replacePath

```TypeScript
replacePath(info: NavPathInfo, animated?: boolean): void
```

Replace the current NavDestination with the specific one.The current NavDestination will be destroyed.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-replacePath(info: NavPathInfo, animated?: boolean): void--><!--Device-NavPathStack-replacePath(info: NavPathInfo, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [NavPathInfo](arkts-na-navigation-navpathinfo-c.md) | Yes | Indicates the new NavDestination in top of the stack. |
| animated | boolean | No | Indicates whether the transition is animated. |

## replacePath

```TypeScript
replacePath(info: NavPathInfo, options?: NavigationOptions): void
```

Replace the current NavDestination with the specific one.The current NavDestination will be destroyed.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-replacePath(info: NavPathInfo, options?: NavigationOptions): void--><!--Device-NavPathStack-replacePath(info: NavPathInfo, options?: NavigationOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [NavPathInfo](arkts-na-navigation-navpathinfo-c.md) | Yes | Indicates the new NavDestination in top of the stack. |
| options | [NavigationOptions](arkts-na-navigation-navigationoptions-i.md) | No | Indicates options of stack operation. |

## replacePathByName

```TypeScript
replacePathByName(name: string, param: Object, animated?: boolean): void
```

Replace the current NavDestination with the specific one.The current NavDestination will be destroyed.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-replacePathByName(name: string, param: Object, animated?: boolean): void--><!--Device-NavPathStack-replacePathByName(name: string, param: Object, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Indicates name of the new NavDestination in top of stack. |
| param | Object | Yes | Indicates the detailed parameter of the new NavDestination in top of the stack. |
| animated | boolean | No | Indicates whether the transition is animated. |

## setInterception

```TypeScript
setInterception(interception: NavigationInterception): void
```

set navigation transition interception.It will be called in navPathStack changes or navigation mode changes.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-setInterception(interception: NavigationInterception): void--><!--Device-NavPathStack-setInterception(interception: NavigationInterception): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| interception | [NavigationInterception](arkts-na-navigation-navigationinterception-i.md) | Yes | the instance to intercept in navigation changes. |

## setPathStack

```TypeScript
setPathStack(pathStack: Array<NavPathInfo>, animated?: boolean): void
```

Set the NavPathInfo array.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-setPathStack(pathStack: Array<NavPathInfo>, animated?: boolean): void--><!--Device-NavPathStack-setPathStack(pathStack: Array<NavPathInfo>, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pathStack | Array&lt;[NavPathInfo](arkts-na-navigation-navpathinfo-c.md)&gt; | Yes | The NavPathInfo array. |
| animated | boolean | No | Indicate whether the operation has animation. |

## size

```TypeScript
size(): int
```

Obtains the size of the stack.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavPathStack-size(): int--><!--Device-NavPathStack-size(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the size of the stack. |

