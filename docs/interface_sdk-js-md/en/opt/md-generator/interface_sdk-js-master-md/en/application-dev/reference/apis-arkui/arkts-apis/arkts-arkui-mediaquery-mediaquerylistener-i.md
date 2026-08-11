# MediaQueryListener

Implements the media query listener, including the first query result when the listener is applied for. The specified media query condition, for example, **'(width <= 600vp)'**, is compared system information. If related information is not initialized during the first query, **matches** returns **false**.

Inherits from [MediaQueryResult](arkts-arkui-mediaquery-mediaqueryresult-i.md).

**Inheritance/Implementation:** MediaQueryListener extends [MediaQueryResult](arkts-arkui-mediaquery-mediaqueryresult-i.md)

**Since:** 7

<!--Device-mediaquery-interface MediaQueryListener extends MediaQueryResult--><!--Device-mediaquery-interface MediaQueryListener extends MediaQueryResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { mediaquery } from 'kits/@kit.ArkUI';
```

## off('change')

```TypeScript
off(type: 'change', callback?: Callback<MediaQueryResult>): void
```

Deregisters a media query listener, so that no callback is triggered when the media attributes change.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-MediaQueryListener-off(type: 'change', callback?: Callback<MediaQueryResult>): void--><!--Device-MediaQueryListener-off(type: 'change', callback?: Callback<MediaQueryResult>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'change' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MediaQueryResult&gt; | No |

## Examples

```TypeScript
import { mediaquery } from '@kit.ArkUI';

let listener: mediaquery.MediaQueryListener = mediaquery.matchMediaSync('(orientation: landscape)'); // Listen for landscape events.
function onPortrait(mediaQueryResult:mediaquery.MediaQueryResult) {
  if (mediaQueryResult.matches) {
    // do something here
  } else {
    // do something here
  }
}
listener.on('change', onPortrait) // Register the media query listener.
listener.off('change', onPortrait) // Unregister the callback.
```

## on('change')

```TypeScript
on(type: 'change', callback: Callback<MediaQueryResult>): void
```

Registers a media query listener. The callback is triggered when the media attributes change.

> **NOTE：**
> 
> The **on** or **off** function cannot be called in the registered callback.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-MediaQueryListener-on(type: 'change', callback: Callback<MediaQueryResult>): void--><!--Device-MediaQueryListener-on(type: 'change', callback: Callback<MediaQueryResult>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'change' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MediaQueryResult&gt; | Yes |

## Examples

For details, see [off('change')](#offchange).
