# unprepareCooperate (System API)

## Modules to Import

```TypeScript
import { cooperate } from '@kit.DistributedServiceKit';
```

## unprepareCooperate

```TypeScript
function unprepareCooperate(callback: AsyncCallback<void>): void
```

Cancels the preparation for screen hopping. This API uses an asynchronous callback to return the result.

**Since:** 11

**Required permissions:** ohos.permission.COOPERATE_MANAGER

<!--Device-cooperate-function unprepareCooperate(callback: AsyncCallback<void>): void--><!--Device-cooperate-function unprepareCooperate(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  cooperate.unprepareCooperate((error: BusinessError) => {
    if (error) {
      console.error(`Keyboard mouse crossing unprepareCooperate failed, error: ${JSON.stringify(error,
        [`code`, `message`])}`);
      return;
    }
    console.info(`Keyboard mouse crossing unprepareCooperate success.`);
  });
} catch (error) {
  console.error(`Keyboard mouse crossing unprepareCooperate failed, error: ${JSON.stringify(error,
    [`code`, `message`])}`);
}
```


## unprepareCooperate

```TypeScript
function unprepareCooperate(): Promise<void>
```

Cancels the preparation for screen hopping. This API uses a promise to return the result.

**Since:** 11

**Required permissions:** ohos.permission.COOPERATE_MANAGER

<!--Device-cooperate-function unprepareCooperate(): Promise<void>--><!--Device-cooperate-function unprepareCooperate(): Promise<void>-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  cooperate.unprepareCooperate().then(() => {
    console.info(`Keyboard mouse crossing unprepareCooperate success.`);
  }, (error: BusinessError) => {
    console.error(`Keyboard mouse crossing unprepareCooperate failed, error: ${JSON.stringify(error,
      [`code`, `message`])}`);
  });
} catch (error) {
  console.error(`Keyboard mouse crossing unprepareCooperate failed, error: ${JSON.stringify(error,
    [`code`, `message`])}`);
}
```
