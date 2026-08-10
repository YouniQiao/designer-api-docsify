# unregister

## Modules to Import

```TypeScript
import { continuationManager } from 'kits/@kit.AbilityKit';
```

## unregister

```TypeScript
function unregister(token: number, callback: AsyncCallback<void>): void
```

解注册流转管理服务，传入注册时获取的token进行解注册，使用AsyncCallback方式作为异步方法。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.off(type:

**Model restriction:** This API can be used only in the stage model.

<!--Device-continuationManager-function unregister(token: number, callback: AsyncCallback<void>): void--><!--Device-continuationManager-function unregister(token: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| token | number | Yes | 注册后的token。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当解注册成功，err为undefined，否则返回错误对象。 |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
continuationManager.unregister(token, (err) => {
  if (err.code != 0) {
    console.error('unregister failed, cause: ' + JSON.stringify(err));
    return;
  }
  console.info('unregister finished. ');
});
```


## unregister

```TypeScript
function unregister(token: number): Promise<void>
```

解注册流转管理服务，传入注册时获取的token进行解注册，使用Promise方式作为异步方法。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.off(type:

**Model restriction:** This API can be used only in the stage model.

<!--Device-continuationManager-function unregister(token: number): Promise<void>--><!--Device-continuationManager-function unregister(token: number): Promise<void>-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| token | number | Yes | 注册后的token。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise形式返回接口调用结果。 |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = 1;
continuationManager.unregister(token)
  .then(() => {
    console.info('unregister finished. ');
  }).catch((err: BusinessError) => {
    console.error('unregister failed, cause: ' + JSON.stringify(err));
});
```

