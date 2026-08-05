# MediaQueryListener

Defines the Listener of mediaquery.

**Inheritance/Implementation:** MediaQueryListener extends [MediaQueryResult](arkts-arkui-mediaquery-mediaqueryresult-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-mediaquery-export interface MediaQueryListener extends MediaQueryResult--><!--Device-mediaquery-export interface MediaQueryListener extends MediaQueryResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offChange

```TypeScript
offChange(callback?: Callback<MediaQueryResult>): void
```

Deregisters a callback with the corresponding query condition by using the handle. This callback is not triggered when the media attributes chang.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MediaQueryListener-offChange(callback?: Callback<MediaQueryResult>): void--><!--Device-MediaQueryListener-offChange(callback?: Callback<MediaQueryResult>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;MediaQueryResult&gt; | No |  |

## onChange

```TypeScript
onChange(callback: Callback<MediaQueryResult>): void
```

Registers a callback with the corresponding query condition by using the handle. This callback is triggered when the media attributes change.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MediaQueryListener-onChange(callback: Callback<MediaQueryResult>): void--><!--Device-MediaQueryListener-onChange(callback: Callback<MediaQueryResult>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;MediaQueryResult&gt; | Yes |  |

