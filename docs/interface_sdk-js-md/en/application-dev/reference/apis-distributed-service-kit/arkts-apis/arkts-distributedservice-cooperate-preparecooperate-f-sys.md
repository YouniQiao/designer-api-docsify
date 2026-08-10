# prepareCooperate (System API)

## Modules to Import

```TypeScript
import { cooperate } from 'kits/@kit.DistributedServiceKit';
```

## prepareCooperate

```TypeScript
function prepareCooperate(callback: AsyncCallback<void>): void
```

准备键鼠穿越，使用Callback异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.COOPERATE_MANAGER

<!--Device-cooperate-function prepareCooperate(callback: AsyncCallback<void>): void--><!--Device-cooperate-function prepareCooperate(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，准备键鼠穿越成功时，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. &lt;br&gt;3. Parameter verification failed.  **ArkTS mode:** This error code applies only to ArkTS-Dyn. |
| 201 | Permission denied. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  cooperate.prepareCooperate((error: BusinessError) => {
    if (error) {
      console.error(`Keyboard mouse crossing prepareCooperate failed, error: ${JSON.stringify(error,
        [`code`, `message`])}`);
      return;
    }
    console.info(`Keyboard mouse crossing prepareCooperate success.`);
  });
} catch (error) {
  console.error(`Keyboard mouse crossing prepareCooperate failed, error: ${JSON.stringify(error,
    [`code`, `message`])}`);
}
```


## prepareCooperate

```TypeScript
function prepareCooperate(): Promise<void>
```

准备键鼠穿越，使用Promise异步方式返回结果。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.COOPERATE_MANAGER

<!--Device-cooperate-function prepareCooperate(): Promise<void>--><!--Device-cooperate-function prepareCooperate(): Promise<void>-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. &lt;br&gt;3. Parameter verification failed.  **ArkTS mode:** This error code applies only to ArkTS-Dyn. |
| 201 | Permission denied. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  cooperate.prepareCooperate().then(() => {
    console.info(`Keyboard mouse crossing prepareCooperate success.`);
  }, (error: BusinessError) => {
    console.error(`Keyboard mouse crossing prepareCooperate failed, error: ${JSON.stringify(error,
      [`code`, `message`])}`);
  });
} catch (error) {
  console.error(`Keyboard mouse crossing prepareCooperate failed, error: ${JSON.stringify(error,
    [`code`, `message`])}`);
}
```

