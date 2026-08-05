# GetStatusOptions

Object that contains the API calling result.

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

<!--Device-unnamed-export interface GetStatusOptions--><!--Device-unnamed-export interface GetStatusOptions-End-->

**System capability:** SystemCapability.PowerManager.BatteryManager.Lite

## complete

```TypeScript
complete?: () => void
```

Called when an API call is complete.

**Type:** () =&gt; void

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

<!--Device-GetStatusOptions-complete?: () => void--><!--Device-GetStatusOptions-complete?: () => void-End-->

**System capability:** SystemCapability.PowerManager.BatteryManager.Lite

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

Called when an API call has failed. **data** indicates the error information, and **code** indicates the error code.

**Type:** (data: string, code: number) =&gt; void

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

<!--Device-GetStatusOptions-fail?: (data: string, code: number) => void--><!--Device-GetStatusOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.PowerManager.BatteryManager.Lite

## success

```TypeScript
success?: (data: BatteryResponse) => void
```

Called when an API call is successful. **data** is a return value of the \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ type.

**Type:** (data: BatteryResponse) =&gt; void

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

<!--Device-GetStatusOptions-success?: (data: BatteryResponse) => void--><!--Device-GetStatusOptions-success?: (data: BatteryResponse) => void-End-->

**System capability:** SystemCapability.PowerManager.BatteryManager.Lite

