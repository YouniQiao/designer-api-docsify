# start (System API)

## Modules to Import

```TypeScript
import { inputDeviceCooperate } from '@kit.InputKit';
```

## start

```TypeScript
function start(sinkDeviceDescriptor: string, srcInputDeviceId: number, callback: AsyncCallback<void>): void
```

Starts screen hopping. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** [activateCooperate](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-activatecooperate-f-sys.md#activateCooperate-(System-API))

<!--Device-inputDeviceCooperate-function start(sinkDeviceDescriptor: string, srcInputDeviceId: number, callback: AsyncCallback<void>): void--><!--Device-inputDeviceCooperate-function start(sinkDeviceDescriptor: string, srcInputDeviceId: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Cooperator

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sinkDeviceDescriptor | string | Yes |
| srcInputDeviceId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [4400002](../errorcode-cooperator.md#4400002-input-device-operation-failed) |
| [4400001](../errorcode-cooperator.md#4400001-incorrect-target-device-descriptor) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
          const sinkDeviceDescriptor = "descriptor";
          let srcInputDeviceId = 0;
          try {
            inputDeviceCooperate.start(sinkDeviceDescriptor, srcInputDeviceId, (error: BusinessError) => {
              if (error) {
                console.error(`Failed to start keyboard mouse crossing, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                return;
              }
              console.info(`Succeeded in starting keyboard mouse crossing.`);
            });
          } catch (error) {
            console.error(`Failed to start keyboard mouse crossing, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## start

```TypeScript
function start(sinkDeviceDescriptor: string, srcInputDeviceId: number): Promise<void>
```

Starts screen hopping. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** [activateCooperate](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-activatecooperate-f-sys.md#activateCooperate-(System-API))

<!--Device-inputDeviceCooperate-function start(sinkDeviceDescriptor: string, srcInputDeviceId: number): Promise<void>--><!--Device-inputDeviceCooperate-function start(sinkDeviceDescriptor: string, srcInputDeviceId: number): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Cooperator

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sinkDeviceDescriptor | string | Yes |
| srcInputDeviceId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [4400002](../errorcode-cooperator.md#4400002-input-device-operation-failed) |
| [4400001](../errorcode-cooperator.md#4400001-incorrect-target-device-descriptor) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
          const sinkDeviceDescriptor = "descriptor";
          const srcInputDeviceId = 0;
          inputDeviceCooperate.start(sinkDeviceDescriptor, srcInputDeviceId).then(() => {
            console.info(`Succeeded in starting keyboard mouse crossing.`);
          }).catch((error: BusinessError) => {
            console.error(`Failed to start keyboard mouse crossing, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          });
        })
    }
  }
}
```
