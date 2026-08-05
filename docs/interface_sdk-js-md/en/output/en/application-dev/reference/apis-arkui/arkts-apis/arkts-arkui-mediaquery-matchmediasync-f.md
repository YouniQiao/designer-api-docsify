# matchMediaSync

## matchMediaSync

```TypeScript
function matchMediaSync(condition: string): MediaQueryListener
```

Sets the media query condition. This API returns the corresponding media query listener. > **NOTE** > > - This API is supported since API version 7 and deprecated since API version 18. You are advised to use > \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ instead. Before calling this API, you > need to obtain the \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_ object using the > \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_ method in > \_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_. > > - Since API version 10, you can use the > \_\_\_MD\_LINK\_DESC\_USD\_4\_\_\_ API in > [UIContext]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_ to obtain the > [MediaQuery]\_\_\_JSDOC\_LINK\_DESC\_USD\_6\_\_\_ object associated with the current UI context.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 18

**Substitutes:** ohos.arkui.UIContext.MediaQuery#matchMediaSync

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-mediaquery-function matchMediaSync(condition: string): MediaQueryListener--><!--Device-mediaquery-function matchMediaSync(condition: string): MediaQueryListener-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| condition | string | Yes | Media query condition. For details, see \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Media query listener, which is used to register or deregister the listening |

**Example**

```TypeScript
import { mediaquery } from '@kit.ArkUI';

let listener: mediaquery.MediaQueryListener = mediaquery.matchMediaSync('(orientation: landscape)'); // Listen for landscape events.
```

