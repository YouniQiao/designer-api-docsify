# on (System API)

## Modules to Import

```TypeScript
import { BundleStatusCallback } from 'kits/@kit.AbilityKit';
```

## on('BundleStatusChange')

```TypeScript
function on(type: 'BundleStatusChange',
    bundleStatusCallback: BundleStatusCallback, callback: AsyncCallback<string>): void
```

Registers a callback to receive bundle status changes. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> This API has been supported since API version 8 and deprecated since API version 9. You are advised to use
> [on](@ohos.bundle.bundleMonitor:bundleMonitor.on(type: BundleChangedEvent, callback: Callback&lt;BundleChangedInfo&gt;))
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleMonitor#on

**Required permissions:** ohos.permission.LISTEN_BUNDLE_CHANGE

<!--Device-innerBundleManager-function on(type: 'BundleStatusChange',    bundleStatusCallback: BundleStatusCallback, callback: AsyncCallback<string>): void--><!--Device-innerBundleManager-function on(type: 'BundleStatusChange',    bundleStatusCallback: BundleStatusCallback, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'BundleStatusChange' | Yes |
| bundleStatusCallback | [BundleStatusCallback](arkts-ability-bundlestatuscallback-t-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |


## on('BundleStatusChange')

```TypeScript
function on(type: 'BundleStatusChange', bundleStatusCallback: BundleStatusCallback): Promise<string>
```

Registers a callback to receive bundle status changes. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> This API has been supported since API version 8 and deprecated since API version 9. You are advised to use
> [on](@ohos.bundle.bundleMonitor:bundleMonitor.on(type: BundleChangedEvent, callback: Callback&lt;BundleChangedInfo&gt;))
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleMonitor#on

**Required permissions:** ohos.permission.LISTEN_BUNDLE_CHANGE

<!--Device-innerBundleManager-function on(type: 'BundleStatusChange', bundleStatusCallback: BundleStatusCallback): Promise<string>--><!--Device-innerBundleManager-function on(type: 'BundleStatusChange', bundleStatusCallback: BundleStatusCallback): Promise<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'BundleStatusChange' | Yes |
| bundleStatusCallback | [BundleStatusCallback](arkts-ability-bundlestatuscallback-t-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |
