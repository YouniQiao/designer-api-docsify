# NavPathStack

A navigation controller that manages all child pages in the **Navigation** component with a stack data structure and provides stack operation methods for controlling page transitions. Starting from API version 12, **NavPathStack** is inheritable. Objects of a derived class can replace those of the base class. For details, see [Example 10](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md#example-10-defining-a-derived-class-of-navpathstack). > **NOTE：**> > 1. When multiple navigation controller operations are triggered in succession, the intermediate states are > bypassed, and only the final result of the operations is rendered. > For example, if a Page1 is popped and then immediately pushed back, the system considers that the states before and > after these operations are identical, leading to no actual change in the stack. To ensure that a new instance of > Page1 is pushed onto the stack despite the consecutive operations, use the **NEW_INSTANCE** mode. > > 2. Avoid relying on lifecycle event listeners as a means to manage the navigation controller. > > 3. When the application is in the background, calling stack operation APIs of **NavPathStack** will trigger a > refresh upon the application's return to the foreground.

**Since:** 10

<!--Device-unnamed-declare class NavPathStack--><!--Device-unnamed-declare class NavPathStack-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## clear

```TypeScript
clear(animated?: boolean): void
```

Clears the routing stack.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavPathStack-clear(animated?: boolean): void--><!--Device-NavPathStack-clear(animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| animated | boolean | No |

## constructor

```TypeScript
constructor()
```

Creates a **NavPathStack** object.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavPathStack-constructor()--><!--Device-NavPathStack-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disableAnimation

```TypeScript
disableAnimation(value: boolean): void
```

Disables or enables the transition animation in the **Navigation** component.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPathStack-disableAnimation(value: boolean): void--><!--Device-NavPathStack-disableAnimation(value: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## getAllPathName

```TypeScript
getAllPathName(): Array<string>
```

Obtains the names of all navigation destination pages in the routing stack.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavPathStack-getAllPathName(): Array<string>--><!--Device-NavPathStack-getAllPathName(): Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

## getIndexByName

```TypeScript
getIndexByName(name: string): Array<number>
```

Obtains the indexes of all the navigation destination pages that match **name**.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavPathStack-getIndexByName(name: string): Array<number>--><!--Device-NavPathStack-getIndexByName(name: string): Array<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;number & gt; |

## getParamByIndex

```TypeScript
getParamByIndex(index: number): unknown | undefined
```

Obtains the parameter information of the navigation destination page specified by **index**.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavPathStack-getParamByIndex(index: number): unknown | undefined--><!--Device-NavPathStack-getParamByIndex(index: number): unknown | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| unknown |

## getParamByName

```TypeScript
getParamByName(name: string): Array<unknown>
```

Obtains the parameter information of all **NavDestination** pages with the specified name, and sorts the information in ascending order by page index.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavPathStack-getParamByName(name: string): Array<unknown>--><!--Device-NavPathStack-getParamByName(name: string): Array<unknown>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;unknown & gt; |

## getParent

```TypeScript
getParent(): NavPathStack | null
```

Obtains the parent navigation path stack. When a **Navigation** component is nested (directly or indirectly) inside another **Navigation** component, the **NavPathStack** of the inner component can obtain the **NavPathStack** of the outer component.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavPathStack-getParent(): NavPathStack | null--><!--Device-NavPathStack-getParent(): NavPathStack | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NavPathStack](arkts-arkui-navpathstack-c.md) |

## getPathStack

```TypeScript
getPathStack(): Array<NavPathInfo>
```

Obtains the array of route page information from this routing stack.

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-NavPathStack-getPathStack(): Array<NavPathInfo>--><!--Device-NavPathStack-getPathStack(): Array<NavPathInfo>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[NavPathInfo](arkts-arkui-navpathinfo-c.md)&gt; |

## moveIndexToTop

```TypeScript
moveIndexToTop(index: number, animated?: boolean): void
```

Moves to the top of the routing stack the navigation destination page specified by **index**.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavPathStack-moveIndexToTop(index: number, animated?: boolean): void--><!--Device-NavPathStack-moveIndexToTop(index: number, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| animated | boolean | No |

## moveToTop

```TypeScript
moveToTop(name: string, animated?: boolean): number
```

Moves the first navigation destination page that matches **name** from the bottom of the routing stack to the top of the stack.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavPathStack-moveToTop(name: string, animated?: boolean): number--><!--Device-NavPathStack-moveToTop(name: string, animated?: boolean): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| animated | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## pop

```TypeScript
pop(animated?: boolean): NavPathInfo | undefined
```

Pops the top element out of the routing stack. > **NOTE：**> > When multiple navigation controller methods are called consecutively, any pages popped during the sequence are > cached. If a page with the same name is later pushed, the system reuses the cached instance instead of > instantiating a new page. > Example: > pathStack: NavPathStack = new NavPathStack() > //The initial page stack is [A]. > pathStack.pop() > pathStack.pushPath(A) > pathStack.pushPath(B) > // The page stack after the operation is [A B]. > In this case, page A is reused, and the new creation process is not performed.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavPathStack-pop(animated?: boolean): NavPathInfo | undefined--><!--Device-NavPathStack-pop(animated?: boolean): NavPathInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| animated | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NavPathInfo](arkts-arkui-navpathinfo-c.md) |

## pop

```TypeScript
pop(result: Object, animated?: boolean): NavPathInfo | undefined
```

Pops the top element out of the routing stack and invokes the **onPop** callback to pass the page processing result. > **NOTE：**> > When multiple navigation controller methods are called consecutively, any pages popped during the sequence are > cached. If a page with the same name is later pushed, the system reuses the cached instance instead of > instantiating a new page. > Example: > pathStack: NavPathStack = new NavPathStack() > //The initial page stack is [A]. > pathStack.pop() > pathStack.pushPath(A) > pathStack.pushPath(B) > // The page stack after the operation is [A B]. > In this case, page A is reused, and the new creation process is not performed.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPathStack-pop(result: Object, animated?: boolean): NavPathInfo | undefined--><!--Device-NavPathStack-pop(result: Object, animated?: boolean): NavPathInfo | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | Object | Yes |
| animated | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NavPathInfo](arkts-arkui-navpathinfo-c.md) |

## popToIndex

```TypeScript
popToIndex(index: number, animated?: boolean): void
```

Returns the routing stack to the page specified by **index**.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavPathStack-popToIndex(index: number, animated?: boolean): void--><!--Device-NavPathStack-popToIndex(index: number, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| animated | boolean | No |

## popToIndex

```TypeScript
popToIndex(index: number, result: Object, animated?: boolean): void
```

Returns the routing stack to the page specified by **index** and invokes the **onPop** callback to pass the page processing result.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavPathStack-popToIndex(index: number, result: Object, animated?: boolean): void--><!--Device-NavPathStack-popToIndex(index: number, result: Object, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| result | Object | Yes |
| animated | boolean | No |

## popToName

```TypeScript
popToName(name: string, animated?: boolean): number
```

Pops pages until the first navigation destination page that matches **name** from the bottom of the routing stack is at the top of the stack.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavPathStack-popToName(name: string, animated?: boolean): number--><!--Device-NavPathStack-popToName(name: string, animated?: boolean): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| animated | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## popToName

```TypeScript
popToName(name: string, result: Object, animated?: boolean): number
```

Pops pages until the first navigation destination page that matches **name** from the bottom of the routing stack is at the top of the stack. This API uses the **onPop** callback to pass in the page processing result.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPathStack-popToName(name: string, result: Object, animated?: boolean): number--><!--Device-NavPathStack-popToName(name: string, result: Object, animated?: boolean): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| result | Object | Yes |
| animated | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## preloadPath

```TypeScript
preloadPath(info: NavPathInfo, options?: PreloadOptions): Promise<void>
```

Preloads navigation destination page specified by **info**. The preload page will not be displayed immediately, but will be cached. When **pushPath** is called later with matching parameters, preloaded instance will be used for fast display.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-NavPathStack-preloadPath(info: NavPathInfo, options?: PreloadOptions): Promise<void>--><!--Device-NavPathStack-preloadPath(info: NavPathInfo, options?: PreloadOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [NavPathInfo](arkts-arkui-navpathinfo-c.md) | Yes |
| options | [PreloadOptions](arkts-arkui-preloadoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [100005](../errorcode-router.md#100005-builder-function-not-registered-during-navigation) |
| [100006](../errorcode-router.md#100006-navdestination-not-found) |

## pushDestination

```TypeScript
pushDestination(info: NavPathInfo, animated?: boolean): Promise<void>
```

Pushes the navigation destination page specified by **info** onto the routing stack. This API uses a promise to return the result. > **NOTE：**> > You are not advised to use stack operations in aboutToAppear, as the > page has not yet finished building at this stage, which may lead to issues such as white screens or navigation > failures.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPathStack-pushDestination(info: NavPathInfo, animated?: boolean): Promise<void>--><!--Device-NavPathStack-pushDestination(info: NavPathInfo, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [NavPathInfo](arkts-arkui-navpathinfo-c.md) | Yes |
| animated | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100005](../errorcode-router.md#100005-builder-function-not-registered-during-navigation) |
| [100006](../errorcode-router.md#100006-navdestination-not-found) |

## pushDestination

```TypeScript
pushDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>
```

Pushes the navigation destination page specified by **info** onto the routing stack. This API uses a promise to return the result. Depending on the [LaunchMode](arkts-arkui-launchmode-e.md#launchmode) specified in the **options** parameter, different behaviors will be implemented. > **NOTE：**> > You are not advised to use stack operations in aboutToAppear, as the > page has not yet finished building at this stage, which may lead to issues such as white screens or navigation > failures.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPathStack-pushDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>--><!--Device-NavPathStack-pushDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [NavPathInfo](arkts-arkui-navpathinfo-c.md) | Yes |
| options | [NavigationOptions](arkts-arkui-navigationoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100005](../errorcode-router.md#100005-builder-function-not-registered-during-navigation) |
| [100006](../errorcode-router.md#100006-navdestination-not-found) |

## pushDestinationByName

```TypeScript
pushDestinationByName(name: string, param: Object, animated?: boolean): Promise<void>
```

Pushes the navigation destination page specified by **name**, with the data specified by **param**, to the routing stack. This API uses a promise to return the result. > **NOTE：**> > You are not advised to use stack operations in aboutToAppear, as the > page has not yet finished building at this stage, which may lead to issues such as white screens or navigation > failures.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPathStack-pushDestinationByName(name: string, param: Object, animated?: boolean): Promise<void>--><!--Device-NavPathStack-pushDestinationByName(name: string, param: Object, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| param | Object | Yes |
| animated | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100005](../errorcode-router.md#100005-builder-function-not-registered-during-navigation) |
| [100006](../errorcode-router.md#100006-navdestination-not-found) |

## pushDestinationByName

```TypeScript
pushDestinationByName(name: string, param: Object, onPop: import('../api/@ohos.base').Callback<PopInfo>, animated?: boolean): Promise<void>
```

Pushes the navigation destination page specified by **name**, with the data specified by **param**, to the routing stack. This API uses the **onPop** callback to handle the result returned when the page is popped out of the stack. It uses a promise to return the result. > **NOTE：**> > You are not advised to use stack operations in aboutToAppear, as the > page has not yet finished building at this stage, which may lead to issues such as white screens or navigation > failures.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPathStack-pushDestinationByName(name: string, param: Object, onPop: import('../api/@ohos.base').Callback<PopInfo>, animated?: boolean): Promise<void>--><!--Device-NavPathStack-pushDestinationByName(name: string, param: Object, onPop: import('../api/@ohos.base').Callback<PopInfo>, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| param | Object | Yes |
| [onPop](arkts-arkui-navpathinfo-c.md) | import('../api/@ohos.base').Callback&lt;[PopInfo](arkts-arkui-popinfo-i.md)&gt; | Yes |
| animated | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100005](../errorcode-router.md#100005-builder-function-not-registered-during-navigation) |
| [100006](../errorcode-router.md#100006-navdestination-not-found) |

## pushPath

```TypeScript
pushPath(info: NavPathInfo, animated?: boolean): void
```

Pushes the navigation destination page specified by **info** onto the routing stack.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavPathStack-pushPath(info: NavPathInfo, animated?: boolean): void--><!--Device-NavPathStack-pushPath(info: NavPathInfo, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [NavPathInfo](arkts-arkui-navpathinfo-c.md) | Yes |
| animated | boolean | No |

## pushPath

```TypeScript
pushPath(info: NavPathInfo, options?: NavigationOptions): void
```

Pushes the navigation destination page specified by **info** onto the routing stack. Depending on the [LaunchMode](arkts-arkui-launchmode-e.md#launchmode) specified in the **options** parameter, different behaviors will be implemented.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPathStack-pushPath(info: NavPathInfo, options?: NavigationOptions): void--><!--Device-NavPathStack-pushPath(info: NavPathInfo, options?: NavigationOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [NavPathInfo](arkts-arkui-navpathinfo-c.md) | Yes |
| options | [NavigationOptions](arkts-arkui-navigationoptions-i.md) | No |

## pushPathByName

```TypeScript
pushPathByName(name: string, param: unknown, animated?: boolean): void
```

Pushes the navigation destination page specified by **name**, with the data specified by **param**, to the routing stack.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavPathStack-pushPathByName(name: string, param: unknown, animated?: boolean): void--><!--Device-NavPathStack-pushPathByName(name: string, param: unknown, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| param | unknown | Yes |
| animated | boolean | No |

## pushPathByName

```TypeScript
pushPathByName(name: string, param: Object, onPop: import('../api/@ohos.base').Callback<PopInfo>, animated?: boolean): void
```

Pushes the navigation destination page specified by **name**, with the data specified by **param**, to the routing stack. This API uses the **onPop** callback to receive the result returned when the page is popped out of the stack.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPathStack-pushPathByName(name: string, param: Object, onPop: import('../api/@ohos.base').Callback<PopInfo>, animated?: boolean): void--><!--Device-NavPathStack-pushPathByName(name: string, param: Object, onPop: import('../api/@ohos.base').Callback<PopInfo>, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| param | Object | Yes |
| [onPop](arkts-arkui-navpathinfo-c.md) | import('../api/@ohos.base').Callback&lt;[PopInfo](arkts-arkui-popinfo-i.md)&gt; | Yes |
| animated | boolean | No |

## removeByIndexes

```TypeScript
removeByIndexes(indexes: Array<number>): number
```

Removes the navigation destination pages specified by **indexes** from the routing stack.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPathStack-removeByIndexes(indexes: Array<number>): number--><!--Device-NavPathStack-removeByIndexes(indexes: Array<number>): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [indexes](../../apis-arkdata/arkts-apis/arkts-arkdata-distributeddata-schema-c.md) | Array & lt;number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## removeByName

```TypeScript
removeByName(name: string): number
```

Removes the navigation destination page specified by **name** from the routing stack.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPathStack-removeByName(name: string): number--><!--Device-NavPathStack-removeByName(name: string): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## removeByNavDestinationId

```TypeScript
removeByNavDestinationId(navDestinationId: string): boolean
```

Removes the navigation destination page specified by **navDestinationId** from the routing stack. **navDestinationId** can be obtained from the onReady callback of **NavDestination** or from [NavDestinationInfo](../arkts-apis/arkts-arkui-uiobserver-navdestinationinfo-i.md#navdestinationinfo).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPathStack-removeByNavDestinationId(navDestinationId: string): boolean--><!--Device-NavPathStack-removeByNavDestinationId(navDestinationId: string): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| navDestinationId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## replaceDestination

```TypeScript
replaceDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>
```

Performs a replacement operation on the routing stack. This API uses a promise to return the result. Its behavior varies depending on the value of [LaunchMode](arkts-arkui-launchmode-e.md#launchmode) specified in **options**.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-NavPathStack-replaceDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>--><!--Device-NavPathStack-replaceDestination(info: NavPathInfo, options?: NavigationOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [NavPathInfo](arkts-arkui-navpathinfo-c.md) | Yes |
| options | [NavigationOptions](arkts-arkui-navigationoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100005](../errorcode-router.md#100005-builder-function-not-registered-during-navigation) |
| [100006](../errorcode-router.md#100006-navdestination-not-found) |

## replacePath

```TypeScript
replacePath(info: NavPathInfo, animated?: boolean): void
```

Replaces the top of the routing stack with the navigation destination page specified by **info**.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPathStack-replacePath(info: NavPathInfo, animated?: boolean): void--><!--Device-NavPathStack-replacePath(info: NavPathInfo, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [NavPathInfo](arkts-arkui-navpathinfo-c.md) | Yes |
| animated | boolean | No |

## replacePath

```TypeScript
replacePath(info: NavPathInfo, options?: NavigationOptions): void
```

Replaces the top page on the routing stack. Depending on the [LaunchMode](arkts-arkui-launchmode-e.md#launchmode) specified in the **options** parameter, different behaviors will be implemented.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPathStack-replacePath(info: NavPathInfo, options?: NavigationOptions): void--><!--Device-NavPathStack-replacePath(info: NavPathInfo, options?: NavigationOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [NavPathInfo](arkts-arkui-navpathinfo-c.md) | Yes |
| options | [NavigationOptions](arkts-arkui-navigationoptions-i.md) | No |

## replacePathByName

```TypeScript
replacePathByName(name: string, param: Object, animated?: boolean): void
```

Replaces the top of the routing stack with the page specified by **name**.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPathStack-replacePathByName(name: string, param: Object, animated?: boolean): void--><!--Device-NavPathStack-replacePathByName(name: string, param: Object, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| param | Object | Yes |
| animated | boolean | No |

## setInterception

```TypeScript
setInterception(interception: NavigationInterception): void
```

Sets the interception callback for navigation page redirection.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPathStack-setInterception(interception: NavigationInterception): void--><!--Device-NavPathStack-setInterception(interception: NavigationInterception): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| interception | [NavigationInterception](arkts-arkui-navigationinterception-i.md) | Yes |

## setPathStack

```TypeScript
setPathStack(pathStack: Array<NavPathInfo>, animated?: boolean): void
```

Updates the array of route page information in this routing stack to the specified content and performs route transitions. > **NOTE：**> > 1. You can add or remove pages in batches based on the existing stack. Among the pages added in batches, only the > visible pages will trigger creation; other pages, although added to the stack, will not be created immediately. > They will only be created when they become visible. > > 2. For routing stacks updated through the batch push functionality, the lifecycle events of each page are > triggered from the top to the bottom of the stack. This differs from the triggering order of other push APIs, > which are triggered from the bottom to the top of the stack. > > 3. You can operate existing pages using **navDestinationId** (unique ID) in [NavPathInfo](arkts-arkui-navpathinfo-c.md#navpathinfo). > This ID is system-generated and globally unique (it can be obtained using the > [getPathStack](#getpathstack) API and should not be manually reassigned). If the specified ID > does not exist in the current routing stack, it indicates a new page. If it exists and the corresponding name is > the same, it indicates reuse of an existing page.

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-NavPathStack-setPathStack(pathStack: Array<NavPathInfo>, animated?: boolean): void--><!--Device-NavPathStack-setPathStack(pathStack: Array<NavPathInfo>, animated?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pathStack | Array&lt;[NavPathInfo](arkts-arkui-navpathinfo-c.md)&gt; | Yes |
| animated | boolean | No |

## size

```TypeScript
size(): number
```

Obtains the stack size.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavPathStack-size(): number--><!--Device-NavPathStack-size(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |
