# getAllDisplay

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## getAllDisplay

```TypeScript
function getAllDisplay(callback: AsyncCallback<Array<Display>>): void
```

Obtains all Display objects. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getAllDisplays](arkts-arkui-display-getalldisplays-f.md)(callback: AsyncCallback&lt;Array&lt;Display&gt;&gt;)

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Display](arkts-arkui-display-display-i.md)&gt;&gt; | Yes |


## getAllDisplay

```TypeScript
function getAllDisplay(): Promise<Array<Display>>
```

Obtains all Display objects. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getAllDisplays](arkts-arkui-display-getalldisplays-f.md)()

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[Display](arkts-arkui-display-display-i.md)&gt;&gt; |
