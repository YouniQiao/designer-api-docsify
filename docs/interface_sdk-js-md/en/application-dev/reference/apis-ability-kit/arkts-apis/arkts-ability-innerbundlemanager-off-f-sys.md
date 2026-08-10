# off (System API)

## Modules to Import

```TypeScript
import { BundleStatusCallback } from 'kits/@kit.AbilityKit';
```

## off('BundleStatusChange')

```TypeScript
function off(type: 'BundleStatusChange', callback: AsyncCallback<string>): void
```

取消注册Callback。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [off](@ohos.bundle.bundleMonitor:bundleMonitor.off(type: BundleChangedEvent, callback?: Callback&lt;BundleChangedInfo&gt;))
> 替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleMonitor#off

**Required permissions:** ohos.permission.LISTEN_BUNDLE_CHANGE

<!--Device-innerBundleManager-function off(type: 'BundleStatusChange', callback: AsyncCallback<string>): void--><!--Device-innerBundleManager-function off(type: 'BundleStatusChange', callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'BundleStatusChange' | Yes | 指示应执行命令，只支持BundleStatusChange。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 程序启动作为入参的回调函数，返回正确结果或错误信息。 |


## off('BundleStatusChange')

```TypeScript
function off(type: 'BundleStatusChange'): Promise<string>
```

取消注册Callback。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [off](@ohos.bundle.bundleMonitor:bundleMonitor.off(type: BundleChangedEvent, callback?: Callback&lt;BundleChangedInfo&gt;))
> 替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleMonitor#off

**Required permissions:** ohos.permission.LISTEN_BUNDLE_CHANGE

<!--Device-innerBundleManager-function off(type: 'BundleStatusChange'): Promise<string>--><!--Device-innerBundleManager-function off(type: 'BundleStatusChange'): Promise<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'BundleStatusChange' | Yes | 指示应执行命令，只支持BundleStatusChange。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise形式返回正确结果或错误信息。 |

