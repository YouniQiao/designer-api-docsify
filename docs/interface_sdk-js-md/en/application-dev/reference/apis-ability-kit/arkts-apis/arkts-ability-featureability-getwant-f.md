# getWant

## Modules to Import

```TypeScript
import { featureAbility } from 'kits/@kit.AbilityKit';
```

## getWant

```TypeScript
function getWant(callback: AsyncCallback<Want>): void
```

获取要拉起的Ability对应的Want。使用callback异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Model restriction:** This API can be used only in the FA model.

<!--Device-featureAbility-function getWant(callback: AsyncCallback<Want>): void--><!--Device-featureAbility-function getWant(callback: AsyncCallback<Want>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Want](arkts-ability-app-ability-want-want-c.md)&gt; | Yes | 回调函数，返回want信息。 |

## Examples

```TypeScript
import { featureAbility } from '@kit.AbilityKit';

featureAbility.getWant((error, data) => {
  if (error && error.code !== 0) {
    console.error(`getWant fail, error: ${JSON.stringify(error)}`);
  } else {
    console.info(`getWant success, data: ${JSON.stringify(data)}`);
  }
});
```


## getWant

```TypeScript
function getWant(): Promise<Want>
```

获取要拉起的Ability对应的Want。使用Promise异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Model restriction:** This API can be used only in the FA model.

<!--Device-featureAbility-function getWant(): Promise<Want>--><!--Device-featureAbility-function getWant(): Promise<Want>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Want](arkts-ability-app-ability-want-want-c.md)&gt; | Promise对象，返回want信息。 |

## Examples

```TypeScript
import { featureAbility } from '@kit.AbilityKit';

featureAbility.getWant().then((data) => {
  console.info(`getWant data: ${JSON.stringify(data)}`);
});
```

