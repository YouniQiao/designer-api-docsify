# isChangePermitted

## Modules to Import

```TypeScript
import { wallpaper } from 'kits/@kit.BasicServicesKit';
```

## isChangePermitted

```TypeScript
function isChangePermitted(callback: AsyncCallback<boolean>): void
```

Checks whether to allow the application to change the wallpaper for the current user.Returns true if the application is allowed to set a wallpaper for the current user. returns false otherwise.

**Since:** 7

**Deprecated since:** 9

<!--Device-wallpaper-function isChangePermitted(callback: AsyncCallback<boolean>): void--><!--Device-wallpaper-function isChangePermitted(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.isChangePermitted((error: BusinessError, data: Boolean) => {
    if (error) {
        console.error(`failed to isChangePermitted because: ${JSON.stringify(error)}`);
        return;
    }
    console.info(`success to isChangePermitted: ${JSON.stringify(data)}`);
});
```


## isChangePermitted

```TypeScript
function isChangePermitted(): Promise<boolean>
```

Checks whether to allow the application to change the wallpaper for the current user.Returns true if the application is allowed to set a wallpaper for the current user. returns false otherwise.

**Since:** 7

**Deprecated since:** 9

<!--Device-wallpaper-function isChangePermitted(): Promise<boolean>--><!--Device-wallpaper-function isChangePermitted(): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.isChangePermitted().then((data: Boolean) => {
    console.info(`success to isChangePermitted: ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
    console.error(`failed to isChangePermitted because: ${JSON.stringify(error)}`);
});
```
