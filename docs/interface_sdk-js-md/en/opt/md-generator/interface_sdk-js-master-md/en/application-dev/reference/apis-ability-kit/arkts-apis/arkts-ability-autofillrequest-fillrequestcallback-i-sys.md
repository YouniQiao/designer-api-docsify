# FillRequestCallback (System API)

Implements callbacks for an auto-fill request, which is used to automatically fill in or generate a password. The callbacks can be used to notify the client of the success or failure of the request.

**Since:** 11

<!--Device-unnamed-export interface FillRequestCallback--><!--Device-unnamed-export interface FillRequestCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

## onCancel

```TypeScript
onCancel(fillContent?: string): void
```

Called when an auto-fill request is canceled.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

<!--Device-FillRequestCallback-onCancel(fillContent?: string): void--><!--Device-FillRequestCallback-onCancel(fillContent?: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fillContent | string | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## onFailure

```TypeScript
onFailure(): void
```

Called when an auto-fill request fails to be processed.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

<!--Device-FillRequestCallback-onFailure(): void--><!--Device-FillRequestCallback-onFailure(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## onSuccess

```TypeScript
onSuccess(response: FillResponse): void
```

Called when an auto-fill request is successfully processed.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

<!--Device-FillRequestCallback-onSuccess(response: FillResponse): void--><!--Device-FillRequestCallback-onSuccess(response: FillResponse): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| response | [FillResponse](arkts-ability-autofillrequest-fillresponse-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## setAutoFillPopupConfig

```TypeScript
setAutoFillPopupConfig(autoFillPopupConfig: AutoFillPopupConfig): void
```

Sets the size and position of an auto-fill pop-up.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-FillRequestCallback-setAutoFillPopupConfig(autoFillPopupConfig: AutoFillPopupConfig): void--><!--Device-FillRequestCallback-setAutoFillPopupConfig(autoFillPopupConfig: AutoFillPopupConfig): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| autoFillPopupConfig | [AutoFillPopupConfig](arkts-ability-autofillpopupconfig-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
