# EnableAlertBeforeBackPageOptions

Defines the **EnableAlertBeforeBackPage** parameter.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** [EnableAlertOptions](../../apis-na/arkts-apis/arkts-na-router-enablealertoptions-i.md#EnableAlertOptions)

<!--Device-unnamed-export interface EnableAlertBeforeBackPageOptions--><!--Device-unnamed-export interface EnableAlertBeforeBackPageOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { BackRouterOptions } from 'BackRouterOptions';
import { DisableAlertBeforeBackPageOptions } from 'DisableAlertBeforeBackPageOptions';
import { EnableAlertBeforeBackPageOptions } from 'EnableAlertBeforeBackPageOptions';
import { RouterOptions } from 'RouterOptions';
import { RouterState } from 'RouterState';
```

## cancel

```TypeScript
cancel?: (errMsg: string) => void
```

Called when the **Cancel** button in the confirm dialog box is clicked. **errMsg** indicates the returned information.

**Type:** (errMsg: string) =&gt; void

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** [EnableAlertOptions](../../apis-na/arkts-apis/arkts-na-router-enablealertoptions-i.md#EnableAlertOptions)

<!--Device-EnableAlertBeforeBackPageOptions-cancel?: (errMsg: string) => void--><!--Device-EnableAlertBeforeBackPageOptions-cancel?: (errMsg: string) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## complete

```TypeScript
complete?: () => void
```

Called when the dialog box is closed.

**Type:** () =&gt; void

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** [EnableAlertOptions](../../apis-na/arkts-apis/arkts-na-router-enablealertoptions-i.md#EnableAlertOptions)

<!--Device-EnableAlertBeforeBackPageOptions-complete?: () => void--><!--Device-EnableAlertBeforeBackPageOptions-complete?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## message

```TypeScript
message: string
```

Content displayed in the confirm dialog box.

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** message

<!--Device-EnableAlertBeforeBackPageOptions-message: string--><!--Device-EnableAlertBeforeBackPageOptions-message: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## success

```TypeScript
success?: (errMsg: string) => void
```

Called when the **OK** button in the confirm dialog box is clicked. **errMsg** indicates the returned information.

**Type:** (errMsg: string) =&gt; void

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** [EnableAlertOptions](../../apis-na/arkts-apis/arkts-na-router-enablealertoptions-i.md#EnableAlertOptions)

<!--Device-EnableAlertBeforeBackPageOptions-success?: (errMsg: string) => void--><!--Device-EnableAlertBeforeBackPageOptions-success?: (errMsg: string) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

