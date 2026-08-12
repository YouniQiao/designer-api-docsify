# Router

The **Router** module provides APIs to access pages through URIs.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [router](arkts-router.md#router)

<!--Device-unnamed-export default class Router--><!--Device-unnamed-export default class Router-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

## Modules to Import

```TypeScript
import { BackRouterOptions, DisableAlertBeforeBackPageOptions, RouterOptions, RouterState, EnableAlertBeforeBackPageOptions } from '@kit.ArkUI';
```

## back

```TypeScript
static back(options?: BackRouterOptions): void
```

Returns to the previous or a specified page.

> **NOTE：**
> 
> In the example, the **uri** field indicates the page route, which is specified by the **pages** list in the
> configuration file.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [back](ohos.router.router#back)

<!--Device-Router-static back(options?: BackRouterOptions): void--><!--Device-Router-static back(options?: BackRouterOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [BackRouterOptions](arkts-arkui-system-router-backrouteroptions-i.md) | No |

## clear

```TypeScript
static clear(): void
```

Clears all historical pages in the stack and retains only the current page at the top of the stack.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [clear](ohos.router.router#clear)

<!--Device-Router-static clear(): void--><!--Device-Router-static clear(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disableAlertBeforeBackPage

```TypeScript
static disableAlertBeforeBackPage(options?: DisableAlertBeforeBackPageOptions): void
```

Disables the display of a confirm dialog box before returning to the previous page.

**Since:** 6

**Deprecated since:** 8

**Substitutes:** [hideAlertBeforeBackPage](ohos.router.router#hideAlertBeforeBackPage)

<!--Device-Router-static disableAlertBeforeBackPage(options?: DisableAlertBeforeBackPageOptions): void--><!--Device-Router-static disableAlertBeforeBackPage(options?: DisableAlertBeforeBackPageOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [DisableAlertBeforeBackPageOptions](arkts-arkui-system-router-disablealertbeforebackpageoptions-i.md) | No |

## enableAlertBeforeBackPage

```TypeScript
static enableAlertBeforeBackPage(options: EnableAlertBeforeBackPageOptions): void
```

Enables the display of a confirm dialog box before returning to the previous page.

**Since:** 6

**Deprecated since:** 8

**Substitutes:** [showAlertBeforeBackPage](ohos.router.router#showAlertBeforeBackPage)

<!--Device-Router-static enableAlertBeforeBackPage(options: EnableAlertBeforeBackPageOptions): void--><!--Device-Router-static enableAlertBeforeBackPage(options: EnableAlertBeforeBackPageOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [EnableAlertBeforeBackPageOptions](arkts-arkui-system-router-enablealertbeforebackpageoptions-i.md) | Yes |

## getLength

```TypeScript
static getLength(): string
```

Obtains the number of pages in the current stack.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [getLength](ohos.router.router#getLength)

<!--Device-Router-static getLength(): string--><!--Device-Router-static getLength(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getParams

```TypeScript
static getParams(): ParamsInterface
```

Obtains parameter information about the current page.

**Since:** 7

**Deprecated since:** 8

**Substitutes:** [getParams](ohos.router.router#getParams)

<!--Device-Router-static getParams(): ParamsInterface--><!--Device-Router-static getParams(): ParamsInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ParamsInterface](arkts-arkui-paramsinterface-t.md) |

## getState

```TypeScript
static getState(): RouterState
```

Obtains state information about the current page.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [getState](ohos.router.router#getState)

<!--Device-Router-static getState(): RouterState--><!--Device-Router-static getState(): RouterState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RouterState](arkts-arkui-system-router-routerstate-i.md) |

## push

```TypeScript
static push(options: RouterOptions): void
```

Navigates to a specified page in the application.

> **NOTE：**
> 
> The page routing stack supports a maximum of 32 pages.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [push](ohos.router.router#push)

<!--Device-Router-static push(options: RouterOptions): void--><!--Device-Router-static push(options: RouterOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | Yes |

## replace

```TypeScript
static replace(options: RouterOptions): void
```

Replaces the current page with another one in the application and destroys the current page.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [replace](ohos.router.router#replace)

<!--Device-Router-static replace(options: RouterOptions): void--><!--Device-Router-static replace(options: RouterOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | Yes |
