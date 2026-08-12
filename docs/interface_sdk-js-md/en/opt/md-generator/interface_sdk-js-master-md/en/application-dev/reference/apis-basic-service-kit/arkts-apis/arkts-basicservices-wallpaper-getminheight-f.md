# getMinHeight

## Modules to Import

```TypeScript
import { wallpaper } from '@kit.BasicServicesKit';
```

## getMinHeight

```TypeScript
function getMinHeight(callback: AsyncCallback<number>): void
```

Obtains the minimum height of the wallpaper. in pixels. returns 0 if no wallpaper has been set.

**Since:** 7

**Deprecated since:** 9

<!--Device-wallpaper-function getMinHeight(callback: AsyncCallback<number>): void--><!--Device-wallpaper-function getMinHeight(callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getMinHeight((error: BusinessError, data: Number) => {
    if (error) {
        console.error(`failed to getMinHeight because: ${JSON.stringify(error)}`);
        return;
    }
    console.info(`success to getMinHeight: ${JSON.stringify(data)}`);
});
```


## getMinHeight

```TypeScript
function getMinHeight(): Promise<number>
```

Obtains the minimum height of the wallpaper. in pixels. returns 0 if no wallpaper has been set.

**Since:** 7

**Deprecated since:** 9

<!--Device-wallpaper-function getMinHeight(): Promise<number>--><!--Device-wallpaper-function getMinHeight(): Promise<number>-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getMinHeight().then((data: Number) => {
    console.info(`success to getMinHeight: ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
    console.error(`failed to getMinHeight because: ${JSON.stringify(error)}`);
});
```
