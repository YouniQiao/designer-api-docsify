# getRemoteAbilityInfos (System API)

## Modules to Import

```TypeScript
import { distributedBundle } from 'kits/@kit.AbilityKit';
```

## getRemoteAbilityInfos

```TypeScript
function getRemoteAbilityInfos(elementNames: Array<ElementName>,
    callback: AsyncCallback<Array<RemoteAbilityInfo>>): void
```

根据给定的ElementName获取有关远程设备AbilityInfos信息，使用callback异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [null]

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-distributedBundle-function getRemoteAbilityInfos(elementNames: Array<ElementName>,    callback: AsyncCallback<Array<RemoteAbilityInfo>>): void--><!--Device-distributedBundle-function getRemoteAbilityInfos(elementNames: Array<ElementName>,    callback: AsyncCallback<Array<RemoteAbilityInfo>>): void-End-->

**System capability:** SystemCapability.BundleManager.DistributedBundleFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elementNames | Array&lt;[ElementName](arkts-ability-elementname-elementname-depr-i.md)&gt; | Yes | ElementName信息，最大数组长度为10。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[RemoteAbilityInfo](arkts-ability-remoteabilityinfo-remoteabilityinfo-depr-i-sys.md)&gt;&gt; | Yes | 程序启动作为入参的回调函数，返回远程基本能力信息。 |


## getRemoteAbilityInfos

```TypeScript
function getRemoteAbilityInfos(elementNames: Array<ElementName>): Promise<Array<RemoteAbilityInfo>>
```

根据给定的ElementName获取有关远程设备AbilityInfos信息，使用Promise异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [null]

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-distributedBundle-function getRemoteAbilityInfos(elementNames: Array<ElementName>): Promise<Array<RemoteAbilityInfo>>--><!--Device-distributedBundle-function getRemoteAbilityInfos(elementNames: Array<ElementName>): Promise<Array<RemoteAbilityInfo>>-End-->

**System capability:** SystemCapability.BundleManager.DistributedBundleFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elementNames | Array&lt;[ElementName](arkts-ability-elementname-elementname-depr-i.md)&gt; | Yes | ElementName信息，最大数组长度为10。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[RemoteAbilityInfo](arkts-ability-remoteabilityinfo-remoteabilityinfo-depr-i-sys.md)&gt;&gt; | Promise形式返回远程基本能力信息。 |

