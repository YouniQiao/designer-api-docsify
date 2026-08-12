# hasMatchedCallLog

## Modules to Import

```TypeScript
import { contact } from '@kit.ContactsKit';
```

## hasMatchedCallLog

```TypeScript
function hasMatchedCallLog(context: Context, phoneNumber: string, minDuration: number): Promise<boolean>
```

Checks whether there are call records that meet the specified conditions. By default, call records within the last6 hours are queried. This API applies only to carrier calls. This API uses a promise to return the result.

**Since:** 24

**Required permissions:** ohos.permission.CHECK_CALL_LOG

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-contact-function hasMatchedCallLog(context: Context, phoneNumber: string, minDuration: int): Promise<boolean>--><!--Device-contact-function hasMatchedCallLog(context: Context, phoneNumber: string, minDuration: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| phoneNumber | string | Yes |
| minDuration | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [16700002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#16700002-parameter-check-failed) |
| [16700001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#16700001-system-internal-error) |

## Examples

In the examples in this document, this.context is used to obtain the UIAbilityContext, where this represents a UIAbility instance inherited from UIAbility. If you need to use the capabilities provided by UIAbilityContext in the UI, see [Obtaining the Context of UIAbility](../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { contact } from '@kit.ContactsKit';
import { common } from '@kit.AbilityKit';

// Obtain the context in the component.
const context = this.getUIContext().getHostContext() as common.UIAbilityContext;

const phoneNumber = '138xxxxxxxx';
const minDuration = 60;
// Call the API to query. By default, call logs within the last 6 hours are queried.
contact.hasMatchedCallLog(context, phoneNumber, minDuration).then((hasMatch:boolean) => {
  console.info(`Has matched call log: ${hasMatch}`);
});
```


## hasMatchedCallLog

```TypeScript
function hasMatchedCallLog(context: Context, phoneNumber: string, minDuration: number, withinTime: number): Promise<boolean>
```

Checks whether there are call records that meet the specified conditions. This API applies only to carrier calls.This API uses a promise to return the result.

**Since:** 24

**Required permissions:** ohos.permission.CHECK_CALL_LOG

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-contact-function hasMatchedCallLog(context: Context, phoneNumber: string, minDuration: int, withinTime: int): Promise<boolean>--><!--Device-contact-function hasMatchedCallLog(context: Context, phoneNumber: string, minDuration: int, withinTime: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| phoneNumber | string | Yes |
| minDuration | number | Yes |
| withinTime | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [16700002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#16700002-parameter-check-failed) |
| [16700001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#16700001-system-internal-error) |

## Examples

In the examples in this document, this.context is used to obtain the UIAbilityContext, where this represents a UIAbility instance inherited from UIAbility. To use the capabilities provided by UIAbilityContext in the UI, see [Obtaining the Context of UIAbility](../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { contact } from '@kit.ContactsKit';
import { common } from '@kit.AbilityKit';

// Obtain the context in the component.
const context = this.getUIContext().getHostContext() as common.UIAbilityContext;

const phoneNumber = '138xxxxxxxx';
const minDuration = 60;
const withinTime = 2 * 60 *60;

// Call the API to query.
contact.hasMatchedCallLog(context, phoneNumber, minDuration, withinTime).then((hasMatch:boolean) => {
  console.info(`Has matched call log: ${hasMatch}`);
});
```
