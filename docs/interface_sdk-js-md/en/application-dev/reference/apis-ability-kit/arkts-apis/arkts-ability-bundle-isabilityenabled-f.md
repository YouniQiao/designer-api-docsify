# isAbilityEnabled

## Modules to Import

```TypeScript
import { bundle } from 'kits/@kit.AbilityKit';
```

## isAbilityEnabled

```TypeScript
function isAbilityEnabled(info: AbilityInfo, callback: AsyncCallback<boolean>): void
```

根据给定的AbilityInfo查询ability是否已经启用，使用callback异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

<!--Device-bundle-function isAbilityEnabled(info: AbilityInfo, callback: AsyncCallback<boolean>): void--><!--Device-bundle-function isAbilityEnabled(info: AbilityInfo, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [AbilityInfo](arkts-ability-abilityinfo-abilityinfo-depr-i.md) | Yes | Ability的配置信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | 回调函数，返回boolean代表是否启用。 |


## isAbilityEnabled

```TypeScript
function isAbilityEnabled(info: AbilityInfo): Promise<boolean>
```

根据给定的AbilityInfo查询ability是否已经启用，使用Promise异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

<!--Device-bundle-function isAbilityEnabled(info: AbilityInfo): Promise<boolean>--><!--Device-bundle-function isAbilityEnabled(info: AbilityInfo): Promise<boolean>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [AbilityInfo](arkts-ability-abilityinfo-abilityinfo-depr-i.md) | Yes | Ability的配置信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise形式返回boolean代表是否启用。 |

