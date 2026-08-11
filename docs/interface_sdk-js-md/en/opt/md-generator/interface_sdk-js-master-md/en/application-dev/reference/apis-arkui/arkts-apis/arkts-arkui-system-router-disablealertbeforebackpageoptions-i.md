# DisableAlertBeforeBackPageOptions

Defines the **DisableAlertBeforeBackPage** parameter.

**Since:** 6

**Deprecated since:** 8

**Substitutes:** ohos.router#RouterOptions

<!--Device-unnamed-export interface DisableAlertBeforeBackPageOptions--><!--Device-unnamed-export interface DisableAlertBeforeBackPageOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { BackRouterOptions, DisableAlertBeforeBackPageOptions, RouterOptions, RouterState, EnableAlertBeforeBackPageOptions } from 'kits/@kit.ArkUI';
```

## cancel

```TypeScript
cancel?: (errMsg: string) => void
```

Called when the dialog box fails to be closed. **errMsg** indicates the returned information.

**Since:** 6

**Deprecated since:** 8

**Substitutes:** ohos.router#RouterOptions

<!--Device-DisableAlertBeforeBackPageOptions-cancel?: (errMsg: string) => void--><!--Device-DisableAlertBeforeBackPageOptions-cancel?: (errMsg: string) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| errMsg | string | Yes |

## complete

```TypeScript
complete?: () => void
```

Called when the dialog box is closed.

**Since:** 6

**Deprecated since:** 8

**Substitutes:** ohos.router#RouterOptions

<!--Device-DisableAlertBeforeBackPageOptions-complete?: () => void--><!--Device-DisableAlertBeforeBackPageOptions-complete?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## success

```TypeScript
success?: (errMsg: string) => void
```

Called when the dialog box is closed. **errMsg** indicates the returned information.

**Since:** 6

**Deprecated since:** 8

**Substitutes:** ohos.router#RouterOptions

<!--Device-DisableAlertBeforeBackPageOptions-success?: (errMsg: string) => void--><!--Device-DisableAlertBeforeBackPageOptions-success?: (errMsg: string) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| errMsg | string | Yes |
