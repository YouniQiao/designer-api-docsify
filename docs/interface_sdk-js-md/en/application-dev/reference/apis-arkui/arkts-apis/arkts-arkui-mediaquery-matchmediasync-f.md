# matchMediaSync

## Modules to Import

```TypeScript
import { mediaquery } from 'kits/@kit.ArkUI';
```

## matchMediaSync

```TypeScript
function matchMediaSync(condition: string): MediaQueryListener
```

设置媒体查询的查询条件，并返回对应的监听句柄。

> **说明：**
> 
> -matchMediaSync需先通过[UIContext](arkts-arkui-uicontext.md)中的
> [getMediaQuery](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getmediaquery)方法获取
> [MediaQuery](arkts-arkui-uicontext.md)对象，然后通过该对象进行调用。
> 
> - 从API version 10开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [getMediaQuery](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getmediaquery)方法获取当前UI上下文关联的
> [MediaQuery](arkts-arkui-uicontext.md)对象。

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
| condition | string | Yes | 媒体事件的匹配条件，具体可参考[媒体查询语法规则](../../../ui/arkts-layout-development-media-query.md#语法规则)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [MediaQueryListener](arkts-arkui-mediaquery-mediaquerylistener-i.md) | 媒体事件监听句柄，用于注册和注销监听回调。 |

## Examples

```TypeScript
import { mediaquery } from '@kit.ArkUI';

let listener: mediaquery.MediaQueryListener = mediaquery.matchMediaSync('(orientation: landscape)'); // Listen for landscape events.
```

