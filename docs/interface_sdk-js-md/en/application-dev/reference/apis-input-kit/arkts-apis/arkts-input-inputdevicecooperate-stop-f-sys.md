# stop (System API)

## Modules to Import

```TypeScript
import { inputDeviceCooperate } from 'inputDeviceCooperate';
```

## stop

```TypeScript
function stop(callback: AsyncCallback<void>): void
```

Stops screen hopping. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 23

**Substitutes:** [deactivateCooperate](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-deactivatecooperate-f-sys.md#deactivateCooperate-(System-API))

<!--Device-inputDeviceCooperate-function stop(callback: AsyncCallback<void>): void--><!--Device-inputDeviceCooperate-function stop(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Cooperator

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback. If the operation is successful, **err** is **undefined**. Otherwise, **error** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api.<br>**Applicable version:** 12 and later |

## Examples

```TypeScript
import { inputDeviceCooperate } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            inputDeviceCooperate.stop((error: BusinessError) => {
              if (error) {
                console.error(`Stop Keyboard mouse crossing failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`Stop Keyboard mouse crossing success.`);
            });
          } catch (error) {
            console.error(`Stop Keyboard mouse crossing failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## stop

```TypeScript
function stop(): Promise<void>
```

Stops screen hopping. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 23

**Substitutes:** [deactivateCooperate](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-deactivatecooperate-f-sys.md#deactivateCooperate-(System-API))

<!--Device-inputDeviceCooperate-function stop(): Promise<void>--><!--Device-inputDeviceCooperate-function stop(): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Cooperator

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api.<br>**Applicable version:** 12 and later |

## Examples

```TypeScript
import { inputDeviceCooperate } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            inputDeviceCooperate.stop().then(() => {
              console.info(`Stop Keyboard mouse crossing success.`);
            }, (error: BusinessError) => {
              console.error(`Stop Keyboard mouse crossing failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            });
          } catch (error) {
            console.error(`Stop Keyboard mouse crossing failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

