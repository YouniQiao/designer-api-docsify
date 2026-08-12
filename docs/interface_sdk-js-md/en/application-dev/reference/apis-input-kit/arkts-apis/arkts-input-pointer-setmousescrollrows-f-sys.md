# setMouseScrollRows (System API)

## Modules to Import

```TypeScript
import { pointer } from '@kit.InputKit';
```

## setMouseScrollRows

```TypeScript
function setMouseScrollRows(rows: int, callback: AsyncCallback<void>): void
```

Sets the number of mouse scroll lines. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-pointer-function setMouseScrollRows(rows: int, callback: AsyncCallback<void>): void--><!--Device-pointer-function setMouseScrollRows(rows: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rows | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Number of mouse scroll lines. The value ranges from 1 to 100. The default value is **3**. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permission error. |

## Examples

```TypeScript
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            pointer.setMouseScrollRows(1, (error: BusinessError) => {
              if (error) {
                console.error(`setMouseScrollRows failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
                return;
              }
              console.info(`setMouseScrollRows success`);
            });
          } catch (error) {
            console.error(`setMouseScrollRows failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```


## setMouseScrollRows

```TypeScript
function setMouseScrollRows(rows: int): Promise<void>
```

Sets the number of mouse scroll lines. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-pointer-function setMouseScrollRows(rows: int): Promise<void>--><!--Device-pointer-function setMouseScrollRows(rows: int): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rows | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Number of mouse scroll lines. The value ranges from 1 to 100. The default value is **3**. |

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
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            pointer.setMouseScrollRows(20).then(() => {
              console.info(`setMouseScrollRows success`);
            }).catch((error: BusinessError) => {
              console.error(`Set mouse scroll rows failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            })
          } catch (error) {
            console.error(`setMouseScrollRows failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```

