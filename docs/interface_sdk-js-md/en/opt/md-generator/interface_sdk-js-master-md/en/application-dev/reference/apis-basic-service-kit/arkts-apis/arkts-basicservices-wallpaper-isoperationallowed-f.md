# isOperationAllowed

## Modules to Import

```TypeScript
```

## isOperationAllowed

```TypeScript
function isOperationAllowed(callback: AsyncCallback<boolean>): void
```

Checks whether a user is allowed to set wallpapers. Returns true if a user is allowed to set wallpapers. returns false otherwise.

**Since:** 7

**Deprecated since:** 9

<!--Device-wallpaper-function isOperationAllowed(callback: AsyncCallback<boolean>): void--><!--Device-wallpaper-function isOperationAllowed(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.isOperationAllowed((error: BusinessError, data: Boolean) => {
    if (error) {
        console.error(`failed to isOperationAllowed because: ${JSON.stringify(error)}`);
        return;
    }
    console.info(`success to isOperationAllowed: ${JSON.stringify(data)}`);
});
```


## isOperationAllowed

```TypeScript
function isOperationAllowed(): Promise<boolean>
```

Checks whether a user is allowed to set wallpapers. Returns true if a user is allowed to set wallpapers. returns false otherwise.

**Since:** 7

**Deprecated since:** 9

<!--Device-wallpaper-function isOperationAllowed(): Promise<boolean>--><!--Device-wallpaper-function isOperationAllowed(): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.isOperationAllowed().then((data: Boolean) => {
    console.info(`success to isOperationAllowed: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`failed to isOperationAllowed because: ${JSON.stringify(error)}`);
});
```
