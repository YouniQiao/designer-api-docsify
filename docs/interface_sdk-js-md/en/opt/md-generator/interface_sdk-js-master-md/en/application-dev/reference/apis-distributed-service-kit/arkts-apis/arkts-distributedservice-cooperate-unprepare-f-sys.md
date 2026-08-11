# unprepare (System API)

## Modules to Import

```TypeScript
import { cooperate } from 'kits/@kit.DistributedServiceKit';
```

## unprepare

```TypeScript
function unprepare(callback: AsyncCallback<void>): void
```

Cancels the preparation for screen hopping. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [unprepareCooperate](arkts-distributedservice-cooperate-unpreparecooperate-f-sys.md#unpreparecooperate)(callback:

<!--Device-cooperate-function unprepare(callback: AsyncCallback<void>): void--><!--Device-cooperate-function unprepare(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  cooperate.unprepare((error: BusinessError) => {
    if (error) {
      console.error(`Keyboard mouse crossing unprepare failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
      return;
    }
    console.info(`Keyboard mouse crossing unprepare success.`);
  });
} catch (error) {
  console.error(`Keyboard mouse crossing unprepare failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
}
```


## unprepare

```TypeScript
function unprepare(): Promise<void>
```

Cancels the preparation for screen hopping. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [unprepareCooperate](arkts-distributedservice-cooperate-unpreparecooperate-f-sys.md#unpreparecooperate)()

<!--Device-cooperate-function unprepare(): Promise<void>--><!--Device-cooperate-function unprepare(): Promise<void>-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  cooperate.unprepare().then(() => {
    console.info(`Keyboard mouse crossing unprepare success.`);
  }, (error: BusinessError) => {
    console.error(`Keyboard mouse crossing unprepare failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
  });
} catch (error) {
  console.error(`Keyboard mouse crossing unprepare failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
}
```
