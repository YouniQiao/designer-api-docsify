# startContinuationDeviceManager

## Modules to Import

```TypeScript
import { continuationManager } from 'kits/@kit.AbilityKit';
```

## startContinuationDeviceManager

```TypeScript
function startContinuationDeviceManager(token: number, callback: AsyncCallback<void>): void
```

拉起设备选择模块，可显示组网内可选择设备列表信息，无过滤条件，使用AsyncCallback方式作为异步方法。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 22

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-continuationManager-function startContinuationDeviceManager(token: number, callback: AsyncCallback<void>): void--><!--Device-continuationManager-function startContinuationDeviceManager(token: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| token | number | Yes | 注册后的token。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当模块选择完成，err为undefined，否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

let token: number = -1;
try {
  continuationManager.startContinuationDeviceManager(token, (err) => {
    if (err.code != 0) {
      console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
      return;
    }
    console.info('startContinuationDeviceManager finished. ');
  });
} catch (err) {
  console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
}
```


## startContinuationDeviceManager

```TypeScript
function startContinuationDeviceManager(
    token: number,
    options: ContinuationExtraParams,
    callback: AsyncCallback<void>
  ): void
```

拉起设备选择模块，可显示组网内可选择设备列表信息，使用AsyncCallback方式作为异步方法。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 22

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-continuationManager-function startContinuationDeviceManager(    token: number,    options: ContinuationExtraParams,    callback: AsyncCallback<void>  ): void--><!--Device-continuationManager-function startContinuationDeviceManager(    token: number,    options: ContinuationExtraParams,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| token | number | Yes | 注册后的token。 |
| options | [ContinuationExtraParams](arkts-ability-continuationmanager-continuationextraparams-t.md) | Yes | 过滤可选择设备列表的额外参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当模块选择完成，err为undefined，否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

let token: number = -1;
try {
  continuationManager.startContinuationDeviceManager(
    token,
    {
      deviceType: ["00E"]
    },
    (err) => {
      if (err.code != 0) {
        console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
        return;
      }
      console.info('startContinuationDeviceManager finished. ');
  });
} catch (err) {
  console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
}
```


## startContinuationDeviceManager

```TypeScript
function startContinuationDeviceManager(token: number, options?: ContinuationExtraParams): Promise<void>
```

拉起设备选择模块，可显示组网内可选择设备列表信息，使用Promise方式作为异步方法。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 22

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-continuationManager-function startContinuationDeviceManager(token: number, options?: ContinuationExtraParams): Promise<void>--><!--Device-continuationManager-function startContinuationDeviceManager(token: number, options?: ContinuationExtraParams): Promise<void>-End-->

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

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; &lt;br&gt;2. Parameter verification failed; |
| 201 | Permission denied. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

## Examples

```TypeScript
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = -1;
try {
  continuationManager.startContinuationDeviceManager(
    token,
    {
      deviceType: ["00E"]
    }).then(() => {
      console.info('startContinuationDeviceManager finished. ');
    }).catch((err: BusinessError) => {
      console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
    });
} catch (err) {
  console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
}
```

