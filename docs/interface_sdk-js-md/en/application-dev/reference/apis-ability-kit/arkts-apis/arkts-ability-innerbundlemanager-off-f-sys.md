# off (System API)

## Modules to Import

```TypeScript
import { innerBundleManager, BundleStatusCallback } from 'kits/@kit.AbilityKit';
```

## off('BundleStatusChange')

```TypeScript
function off(type: 'BundleStatusChange', callback: AsyncCallback<string>): void
```

Unregisters the callback that receives bundle status changes. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API has been supported since API version 8 and deprecated since API version 9. You are advised to use
> off
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** off

**Required permissions:** ohos.permission.LISTEN_BUNDLE_CHANGE

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'BundleStatusChange' | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |


## off('BundleStatusChange')

```TypeScript
function off(type: 'BundleStatusChange'): Promise<string>
```

Unregisters the callback that receives bundle status changes. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API has been supported since API version 8 and deprecated since API version 9. You are advised to use
> off
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** off

**Required permissions:** ohos.permission.LISTEN_BUNDLE_CHANGE

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'BundleStatusChange' | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |
