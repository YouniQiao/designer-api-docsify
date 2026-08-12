# sendDialogResult (System API)

## Modules to Import

```TypeScript
import { dialogSession } from '@kit.AbilityKit';
```

## sendDialogResult

```TypeScript
function sendDialogResult(dialogSessionId: string, targetWant: Want, isAllowed: boolean): Promise<void>
```

Sends a request for a dialog box. This API uses a promise to return the result.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

<!--Device-dialogSession-function sendDialogResult(dialogSessionId: string, targetWant: Want, isAllowed: boolean): Promise<void>--><!--Device-dialogSession-function sendDialogResult(dialogSessionId: string, targetWant: Want, isAllowed: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dialogSessionId | string | Yes |
| targetWant | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| isAllowed | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |


## sendDialogResult

```TypeScript
function sendDialogResult(dialogSessionId: string, targetWant: Want, isAllowed: boolean, callback: AsyncCallback<void>): void
```

Sends a request for a dialog box. This API uses an asynchronous callback to return the result.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

<!--Device-dialogSession-function sendDialogResult(dialogSessionId: string, targetWant: Want, isAllowed: boolean, callback: AsyncCallback<void>): void--><!--Device-dialogSession-function sendDialogResult(dialogSessionId: string, targetWant: Want, isAllowed: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dialogSessionId | string | Yes |
| targetWant | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| isAllowed | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
