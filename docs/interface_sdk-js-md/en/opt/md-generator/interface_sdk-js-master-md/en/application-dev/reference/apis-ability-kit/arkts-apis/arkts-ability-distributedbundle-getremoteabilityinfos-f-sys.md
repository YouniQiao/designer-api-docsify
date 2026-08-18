# getRemoteAbilityInfos (System API)

## Modules to Import

```TypeScript
```

## getRemoteAbilityInfos

```TypeScript
function getRemoteAbilityInfos(elementNames: Array<ElementName>,
    callback: AsyncCallback<Array<RemoteAbilityInfo>>): void
```

Obtains the information about remote abilities that match the given element names. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** null

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-distributedBundle-function getRemoteAbilityInfos(elementNames: Array<ElementName>,    callback: AsyncCallback<Array<RemoteAbilityInfo>>): void--><!--Device-distributedBundle-function getRemoteAbilityInfos(elementNames: Array<ElementName>,    callback: AsyncCallback<Array<RemoteAbilityInfo>>): void-End-->

**System capability:** SystemCapability.BundleManager.DistributedBundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| elementNames | Array&lt;[ElementName](arkts-ability-elementname-elementname-depr-i.md)&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[RemoteAbilityInfo](arkts-ability-remoteabilityinfo-remoteabilityinfo-depr-i-sys.md)&gt;&gt; | Yes |


## getRemoteAbilityInfos

```TypeScript
function getRemoteAbilityInfos(elementNames: Array<ElementName>): Promise<Array<RemoteAbilityInfo>>
```

Obtains the information about remote abilities that match the given element names. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** null

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-distributedBundle-function getRemoteAbilityInfos(elementNames: Array<ElementName>): Promise<Array<RemoteAbilityInfo>>--><!--Device-distributedBundle-function getRemoteAbilityInfos(elementNames: Array<ElementName>): Promise<Array<RemoteAbilityInfo>>-End-->

**System capability:** SystemCapability.BundleManager.DistributedBundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| elementNames | Array&lt;[ElementName](arkts-ability-elementname-elementname-depr-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[RemoteAbilityInfo](arkts-ability-remoteabilityinfo-remoteabilityinfo-depr-i-sys.md)&gt;&gt; |
