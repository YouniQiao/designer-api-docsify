# setKeyDownDuration (System API)

## Modules to Import

```TypeScript
import { shortKey } from '@kit.InputKit';
```

## setKeyDownDuration

```TypeScript
function setKeyDownDuration(businessKey: string, delay: int, callback: AsyncCallback<void>): void
```

Sets the delay for starting an ability using shortcut keys. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-shortKey-function setKeyDownDuration(businessKey: string, delay: int, callback: AsyncCallback<void>): void--><!--Device-shortKey-function setKeyDownDuration(businessKey: string, delay: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.ShortKey

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| businessKey | string | Yes | Unique service ID registered on the multimodal side. It corresponds to **businessId** in the **ability_launch_config.json** file. You need to query this parameter on your own before calling the API. |
| delay | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Delay for starting an ability using shortcut keys, in milliseconds. This field is valid only when shortcut keys are pressed. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permission error. |

## Examples

```TypeScript
import { shortKey } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            shortKey.setKeyDownDuration("businessId", 500, (error: BusinessError) => {
              if (error) {
                console.error(`Set key down duration failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`Set key down duration success`);
            });
          } catch (error) {
            console.error(`Set key down duration failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## setKeyDownDuration

```TypeScript
function setKeyDownDuration(businessKey: string, delay: int): Promise<void>
```

Sets the delay for starting an ability using shortcut keys. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-shortKey-function setKeyDownDuration(businessKey: string, delay: int): Promise<void>--><!--Device-shortKey-function setKeyDownDuration(businessKey: string, delay: int): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.ShortKey

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| businessKey | string | Yes | Unique service ID registered on the multimodal side. It corresponds to **businessId** in the **ability_launch_config.json** file. You need to query this parameter on your own before calling the API. |
| delay | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Delay for starting an ability using shortcut keys, in milliseconds. This field is valid only when shortcut keys are pressed. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permission error. |

## Examples

```TypeScript
import { shortKey } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            shortKey.setKeyDownDuration("businessId", 500).then(() => {
              console.info(`Set key down duration success`);
            }).catch((error: BusinessError) => {
              console.error(`Set key down failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`Set key down duration failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

