# isSecureMode

## Modules to Import

```TypeScript
```

## isSecureMode

```TypeScript
function isSecureMode(callback: AsyncCallback<boolean>): void
```

Checks whether the screen lock of the current device is secure.

**Since:** 23

**Deprecated since:** 9

<!--Device-screenLock-function isSecureMode(callback: AsyncCallback<boolean>): void--><!--Device-screenLock-function isSecureMode(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.ScreenLock

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';

screenLock.isSecureMode((err: BusinessError, data: Boolean)=>{
  if (err) {
    console.error(`Failed to obtain whether the device is in secure mode, Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in Obtaining whether the device is in secure mode. result: ${data}`);
});
```


## isSecureMode

```TypeScript
function isSecureMode(): Promise<boolean>
```

Checks whether the screen lock of the current device is secure.

**Since:** 23

**Deprecated since:** 9

<!--Device-screenLock-function isSecureMode(): Promise<boolean>--><!--Device-screenLock-function isSecureMode(): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.ScreenLock

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';

screenLock.isSecureMode().then((data: Boolean) => {
  console.info(`Succeeded in Obtaining whether the device is in secure mode. result: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain whether the device is in secure mode, Code: ${err.code}, message: ${err.message}`);
});
```
