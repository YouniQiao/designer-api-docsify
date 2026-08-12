# recycleForms (System API)

## Modules to Import

```TypeScript
import { formHost } from '@kit.FormKit';
```

## recycleForms

```TypeScript
function recycleForms(formIds: Array<string>): Promise<void>
```

Recycles widgets, that is, reclaiming widget memory. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.REQUIRE_FORM

**Model restriction:** This API can be used only in the stage model.

<!--Device-formHost-function recycleForms(formIds: Array<string>): Promise<void>--><!--Device-formHost-function recycleForms(formIds: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formIds | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16501000](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501000-internal-function-error) |
| [16500060](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500060-service-connection-failure) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [16500050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500050-ipc-failure) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
