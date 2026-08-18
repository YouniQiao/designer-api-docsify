# MediaQueryListener

Defines the Listener of mediaquery.

**Inheritance/Implementation:** MediaQueryListener extends [MediaQueryResult](arkts-arkui-mediaquery-mediaqueryresult-i.md#mediaqueryresult)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-mediaquery-export interface MediaQueryListener--><!--Device-mediaquery-export interface MediaQueryListener-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { mediaquery } from '@kit.ArkUI';
```

## offChange

```TypeScript
offChange(callback?: Callback<MediaQueryResult>): void
```

Deregisters a callback with the corresponding query condition by using the handle. This callback is not triggered when the media attributes chang.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MediaQueryListener-offChange(callback?: Callback<MediaQueryResult>): void--><!--Device-MediaQueryListener-offChange(callback?: Callback<MediaQueryResult>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MediaQueryResult](arkts-arkui-mediaquery-mediaqueryresult-i.md)&gt; | No |  |

## onChange

```TypeScript
onChange(callback: Callback<MediaQueryResult>): void
```

Registers a callback with the corresponding query condition by using the handle. This callback is triggered when the media attributes change.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MediaQueryListener-onChange(callback: Callback<MediaQueryResult>): void--><!--Device-MediaQueryListener-onChange(callback: Callback<MediaQueryResult>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MediaQueryResult](arkts-arkui-mediaquery-mediaqueryresult-i.md)&gt; | Yes |  |

