# EnableAlertBeforeBackPageOptions

Defines the **EnableAlertBeforeBackPage** parameter.

**Since:** 6

**Deprecated since:** 8

**Substitutes:** EnableAlertOptions

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { BackRouterOptions, DisableAlertBeforeBackPageOptions, RouterOptions, RouterState, EnableAlertBeforeBackPageOptions } from '@kit.ArkUI';
```

## cancel

```TypeScript
cancel?: (errMsg: string) => void
```

Called when the **Cancel** button in the confirm dialog box is clicked. **errMsg** indicates the returned
information.

**Type:** (errMsg: string) => void

**Since:** 6

**Deprecated since:** 8

**Substitutes:** EnableAlertOptions

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## complete

```TypeScript
complete?: () => void
```

Called when the dialog box is closed.

**Type:** () => void

**Since:** 6

**Deprecated since:** 8

**Substitutes:** EnableAlertOptions

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## message

```TypeScript
message: string
```

Content displayed in the confirm dialog box.

**Type:** string

**Since:** 6

**Deprecated since:** 8

**Substitutes:** message

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## success

```TypeScript
success?: (errMsg: string) => void
```

Called when the **OK** button in the confirm dialog box is clicked. **errMsg** indicates the returned information.

**Type:** (errMsg: string) => void

**Since:** 6

**Deprecated since:** 8

**Substitutes:** EnableAlertOptions

**System capability:** SystemCapability.ArkUI.ArkUI.Full

