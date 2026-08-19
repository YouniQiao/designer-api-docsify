# getState (System API)

## Modules to Import

```TypeScript
import { inputDeviceCooperate } from '@kit.InputKit';
```

## getState

```TypeScript
function getState(deviceDescriptor: string, callback: AsyncCallback<{ state: boolean }>): void
```

Obtains the state of the screen hopping switch. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** [getCooperateSwitchState](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-getcooperateswitchstate-f-sys.md)

<!--Device-inputDeviceCooperate-function getState(deviceDescriptor: string, callback: AsyncCallback<{ state: boolean }>): void--><!--Device-inputDeviceCooperate-function getState(deviceDescriptor: string, callback: AsyncCallback<{ state: boolean }>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Cooperator

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceDescriptor | string | Yes | Descriptor of the target device for screen hopping. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;{ state: boolean }&gt; | Yes |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api.<br>**Applicable version:** 12 and later |

**Examples**

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
          let deviceDescriptor = "descriptor";
          try {
            inputDeviceCooperate.getState(deviceDescriptor, (error: BusinessError, data: object) => {
              if (error) {
                console.error(`Get the status failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`Get the status success, data: ${JSON.stringify(data)}`);
            });
          } catch (error) {
            console.error(`Get the status failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## getState

```TypeScript
function getState(deviceDescriptor: string): Promise<{ state: boolean }>
```

Checks whether screen hopping is enabled. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** [getCooperateSwitchState](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-getcooperateswitchstate-f-sys.md)

<!--Device-inputDeviceCooperate-function getState(deviceDescriptor: string): Promise<{ state: boolean }>--><!--Device-inputDeviceCooperate-function getState(deviceDescriptor: string): Promise<{ state: boolean }>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Cooperator

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceDescriptor | string | Yes | Descriptor of the target device for screen hopping. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;{ state: boolean | > } Promise used to return the state of the screen hopping switch. **true** if enabled and **false** if disabled.<br>**Applicable version:** 12 and later |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api.<br>**Applicable version:** 12 and later |

**Examples**

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
          let deviceDescriptor = "descriptor";
          try {
            inputDeviceCooperate.getState(deviceDescriptor).then((data: object) => {
              console.info(`Get the status success, data: ${JSON.stringify(data)}`);
            }, (error: BusinessError) => {
              console.error(`Get the status failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            });
          } catch (error) {
            console.error(`Get the status failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

