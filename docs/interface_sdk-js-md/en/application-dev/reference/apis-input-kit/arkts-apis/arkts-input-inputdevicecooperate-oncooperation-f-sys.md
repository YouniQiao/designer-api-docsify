# on_cooperation (System API)

## Modules to Import

```TypeScript
import { inputDeviceCooperate } from '@kit.InputKit';
```

## on_cooperation('cooperation')

```TypeScript
function on(type: 'cooperation', callback: AsyncCallback<{ deviceDescriptor: string, eventMsg: EventMsg }>): void
```

Registers a listener for screen hopping state changes. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 23

**Substitutes:** [on](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-oncooperate-f-sys.md#on_cooperatecooperate)

<!--Device-inputDeviceCooperate-function on(type: 'cooperation', callback: AsyncCallback<{ deviceDescriptor: string, eventMsg: EventMsg }>): void--><!--Device-inputDeviceCooperate-function on(type: 'cooperation', callback: AsyncCallback<{ deviceDescriptor: string, eventMsg: EventMsg }>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Cooperator

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'cooperation' | Yes | Event type. The value is **cooperation**. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;{ deviceDescriptor: string, eventMsg: EventMsg }&gt; | Yes |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api.<br>**Applicable version:** 12 and later |

**Examples**

```TypeScript
import { inputDeviceCooperate } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          let callback = (msg: object) => {
            console.info(`Keyboard mouse crossing event: ${JSON.stringify(msg)}`);
            return false;
          }
          try {
            inputDeviceCooperate.on('cooperation', callback);
          } catch (error) {
            console.error(`Register failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

