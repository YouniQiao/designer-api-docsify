# NavPushPathHelper

On the initial launch, the atomic service only downloads and installs the main package and its dependencies. Therefore, if the NavDestination resides in a different HSP subpackage that is not a dependency of the main package, you'll need to use **NavPushPathHelper** to download and install the corresponding HSP subpackage first. After that, push the specified **NavDestination** page information onto the stack. This way, you enable Navigation to support dynamic loading of the HSP subpackage before the navigation occurs.

**Since:** 12

**Deprecated since:** -1

<!--Device-unnamed-export declare class NavPushPathHelper--><!--Device-unnamed-export declare class NavPushPathHelper-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { NavPushPathHelper } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(navPathStack: NavPathStack)
```

A constructor used to create a **NavPushPathHelper** object.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-constructor(navPathStack: NavPathStack)--><!--Device-NavPushPathHelper-constructor(navPathStack: NavPathStack)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| navPathStack | [NavPathStack](../arkts-components/arkts-arkui-navpathstack-c.md) | Yes |

## pushDestination

```TypeScript
pushDestination(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>
```

Checks for the target subpackage and, if it is not present, initiates a download using the specified module name. Once the subpackage is downloaded, the API pushes the NavDestination page specified by the **info** parameter onto the navigation stack. This API uses a promise to handle asynchronous operations.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-pushDestination(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-pushDestination(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| moduleName | string | Yes |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes |
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
| [300001](../errorcode-router.md#300001-hsp-download-failure-before-redirection) |
| [100006](../errorcode-router.md#100006-navdestination-not-found) |

## pushDestination

```TypeScript
pushDestination(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>
```

Checks for the target subpackage and, if it is not present, initiates a download using the specified module name. Once the subpackage is downloaded, the API pushes the NavDestination page specified by the **info** parameter onto the navigation stack. This API uses a promise to handle asynchronous operations. Depending on the LaunchMode specified in the **options** parameter, different behaviors will be triggered.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-pushDestination(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>--><!--Device-NavPushPathHelper-pushDestination(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| moduleName | string | Yes |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes |
| options | [NavigationOptions](../arkts-components/arkts-arkui-navigationoptions-i.md) | No |

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
| [300001](../errorcode-router.md#300001-hsp-download-failure-before-redirection) |
| [100006](../errorcode-router.md#100006-navdestination-not-found) |

## pushDestinationByName

```TypeScript
pushDestinationByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>
```

Checks for the target subpackage and, if it is not present, initiates a download using the specified module name. Once the subpackage is downloaded, the API pushes the NavDestination page specified by the **name** parameter onto the navigation stack, along with the data specified by **param**. This API uses a promise to handle asynchronous operations.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-pushDestinationByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-pushDestinationByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| moduleName | string | Yes |
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
| [300001](../errorcode-router.md#300001-hsp-download-failure-before-redirection) |
| [100006](../errorcode-router.md#100006-navdestination-not-found) |

## pushDestinationByName

```TypeScript
pushDestinationByName(moduleName: string, name: string, param: Object,
    onPop: Callback<PopInfo>, animated?: boolean): Promise<void>
```

Checks for the target subpackage and, if it is not present, initiates a download using the specified module name. Once the subpackage is downloaded, the API pushes the NavDestination page specified by the **name** parameter onto the navigation stack, along with the data specified by **param**. The **onPop** callback handles the return results when the page is popped from the stack. This API uses a promise to handle asynchronous operations.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-pushDestinationByName(moduleName: string, name: string, param: Object,    onPop: Callback<PopInfo>, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-pushDestinationByName(moduleName: string, name: string, param: Object,    onPop: Callback<PopInfo>, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| moduleName | string | Yes |
| name | string | Yes |
| param | Object | Yes |
| [onPop](../arkts-components/arkts-arkui-navpathinfo-c.md) | Callback&lt;[PopInfo](../arkts-components/arkts-arkui-popinfo-i.md)&gt; | Yes |
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
| [300001](../errorcode-router.md#300001-hsp-download-failure-before-redirection) |
| [100006](../errorcode-router.md#100006-navdestination-not-found) |

## pushPath

```TypeScript
pushPath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>
```

Checks for the target subpackage and, if it is not present, initiates a download using the specified module name. Once the subpackage is downloaded, the API pushes the NavDestination page specified by the **info** parameter onto the navigation stack. This API uses a promise to handle asynchronous operations.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-pushPath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-pushPath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| moduleName | string | Yes |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes |
| animated | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [300001](../errorcode-router.md#300001-hsp-download-failure-before-redirection) |

## pushPath

```TypeScript
pushPath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>
```

Checks for the target subpackage and, if it is not present, initiates a download using the specified module name. Once the subpackage is downloaded, the API pushes the NavDestination page specified by the **info** parameter onto the navigation stack. This API uses a promise to handle asynchronous operations. Depending on the LaunchMode specified in the **options** parameter, different behaviors will be triggered.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-pushPath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>--><!--Device-NavPushPathHelper-pushPath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| moduleName | string | Yes |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes |
| options | [NavigationOptions](../arkts-components/arkts-arkui-navigationoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [300001](../errorcode-router.md#300001-hsp-download-failure-before-redirection) |

## pushPathByName

```TypeScript
pushPathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>
```

Checks for the target subpackage and, if it is not present, initiates a download using the specified module name. Once the subpackage is downloaded, the API pushes the NavDestination page specified by the **name** parameter onto the navigation stack, along with the data specified by **param**. This API uses a promise to handle asynchronous operations.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-pushPathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-pushPathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| moduleName | string | Yes |
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
| [300001](../errorcode-router.md#300001-hsp-download-failure-before-redirection) |

## pushPathByName

```TypeScript
pushPathByName(moduleName: string, name: string, param: Object,
    onPop: Callback<PopInfo>, animated?: boolean): Promise<void>
```

Checks for the target subpackage and, if it is not present, initiates a download using the specified module name. Once the subpackage is downloaded, the API pushes the NavDestination page specified by the **name** parameter onto the navigation stack, along with the data specified by **param**. The **onPop** callback handles the return results when the page is popped from the stack. This API uses a promise to handle asynchronous operations.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-pushPathByName(moduleName: string, name: string, param: Object,    onPop: Callback<PopInfo>, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-pushPathByName(moduleName: string, name: string, param: Object,    onPop: Callback<PopInfo>, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| moduleName | string | Yes |
| name | string | Yes |
| param | Object | Yes |
| [onPop](../arkts-components/arkts-arkui-navpathinfo-c.md) | Callback&lt;[PopInfo](../arkts-components/arkts-arkui-popinfo-i.md)&gt; | Yes |
| animated | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [300001](../errorcode-router.md#300001-hsp-download-failure-before-redirection) |

## replacePath

```TypeScript
replacePath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>
```

Checks for the target subpackage and, if it is not present, initiates a download using the specified module name. Once the subpackage is downloaded, the API pops the top page from the current navigation stack and pushes the NavDestination page specified by the **info** parameter onto the stack. This API uses a promise to handle asynchronous operations.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-replacePath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-replacePath(moduleName: string, info: NavPathInfo, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| moduleName | string | Yes |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes |
| animated | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [300001](../errorcode-router.md#300001-hsp-download-failure-before-redirection) |

## replacePath

```TypeScript
replacePath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>
```

Checks for the target subpackage and, if it is not present, initiates a download using the specified module name. Once the subpackage is downloaded, the API pops the top page from the current navigation stack. This API uses a promise to handle asynchronous operations. Depending on the LaunchMode specified in the **options** parameter, different behaviors will be triggered.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-replacePath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>--><!--Device-NavPushPathHelper-replacePath(moduleName: string, info: NavPathInfo, options?: NavigationOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| moduleName | string | Yes |
| info | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) | Yes |
| options | [NavigationOptions](../arkts-components/arkts-arkui-navigationoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [300001](../errorcode-router.md#300001-hsp-download-failure-before-redirection) |

## replacePathByName

```TypeScript
replacePathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>
```

Checks for the target subpackage and, if it is not present, initiates a download using the specified module name. Once the subpackage is downloaded, the API pops the top page from the current navigation stack and pushes the page specified by the **name** parameter onto the stack. This API uses a promise to handle asynchronous operations.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavPushPathHelper-replacePathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>--><!--Device-NavPushPathHelper-replacePathByName(moduleName: string, name: string, param: Object, animated?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| moduleName | string | Yes |
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
| [300001](../errorcode-router.md#300001-hsp-download-failure-before-redirection) |
