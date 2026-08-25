# getDefaultDisplay

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## getDefaultDisplay

```TypeScript
function getDefaultDisplay(callback: AsyncCallback<Display>): void
```

Obtains the default Display object. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getDefaultDisplaySync](arkts-arkui-display-getdefaultdisplaysync-f.md)

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Display](arkts-arkui-display-display-i.md)&gt; | Yes |


## getDefaultDisplay

```TypeScript
function getDefaultDisplay(): Promise<Display>
```

Obtains the default Display object. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getDefaultDisplaySync](arkts-arkui-display-getdefaultdisplaysync-f.md)

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Display](arkts-arkui-display-display-i.md)&gt; |
