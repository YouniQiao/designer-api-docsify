# startDeviceManager

## Modules to Import

```TypeScript
import { continuationManager } from 'kits/@kit.AbilityKit';
```

## startDeviceManager

```TypeScript
function startDeviceManager(token: number, callback: AsyncCallback<void>): void
```

拉起设备选择模块，可显示组网内可选择设备列表信息，无过滤条件，使用AsyncCallback方式作为异步方法。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.startDiscovering](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#startdiscovering)(discoverParam:

**Model restriction:** This API can be used only in the stage model.

<!--Device-continuationManager-function startDeviceManager(token: number, callback: AsyncCallback<void>): void--><!--Device-continuationManager-function startDeviceManager(token: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| token | number | Yes | 注册后的token。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当模块选择完成，err为undefined，否则返回错误对象。 |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
continuationManager.startDeviceManager(token, (err) => {
  if (err.code != 0) {
    console.error('startDeviceManager failed, cause: ' + JSON.stringify(err));
    return;
  }
  console.info('startDeviceManager finished. ');
});
```


## startDeviceManager

```TypeScript
function startDeviceManager(token: number, options: ContinuationExtraParams, callback: AsyncCallback<void>): void
```

拉起设备选择模块，可显示组网内可选择设备列表信息，使用AsyncCallback方式作为异步方法。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.startDiscovering](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#startdiscovering)(discoverParam:

**Model restriction:** This API can be used only in the stage model.

<!--Device-continuationManager-function startDeviceManager(token: number, options: ContinuationExtraParams, callback: AsyncCallback<void>): void--><!--Device-continuationManager-function startDeviceManager(token: number, options: ContinuationExtraParams, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| token | number | Yes | 注册后的token。 |
| options | [ContinuationExtraParams](arkts-ability-continuationmanager-continuationextraparams-t.md) | Yes | 过滤可选择设备列表的额外参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当模块选择完成，err为undefined，否则返回错误对象。 |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
continuationManager.startDeviceManager(
  token,
  {
    deviceType: ["00E"]
  },
  (err) => {
    if (err.code != 0) {
      console.error('startDeviceManager failed, cause: ' + JSON.stringify(err));
      return;
    }
    console.info('startDeviceManager finished. ');
});
```


## startDeviceManager

```TypeScript
function startDeviceManager(token: number, options?: ContinuationExtraParams): Promise<void>
```

拉起设备选择模块，可显示组网内可选择设备列表信息，使用Promise方式作为异步方法。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.startDiscovering](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#startdiscovering)(discoverParam:

**Model restriction:** This API can be used only in the stage model.

<!--Device-continuationManager-function startDeviceManager(token: number, options?: ContinuationExtraParams): Promise<void>--><!--Device-continuationManager-function startDeviceManager(token: number, options?: ContinuationExtraParams): Promise<void>-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| token | number | Yes | 注册后的token。 |
| options | [ContinuationExtraParams](arkts-ability-continuationmanager-continuationextraparams-t.md) | No | 过滤可选择设备列表的额外参数，该参数可缺省。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise形式返回接口调用结果。 |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = -1;
continuationManager.startDeviceManager(
  token,
  {
    deviceType: ["00E"]
  }).then(() => {
    console.info('startDeviceManager finished. ');
  }).catch((err: BusinessError) => {
    console.error('startDeviceManager failed, cause: ' + JSON.stringify(err));
});
```

