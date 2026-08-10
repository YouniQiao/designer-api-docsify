# FillRequestCallback (System API)

自动填充或者生成密码时的回调对象，可以通过此回调通知客户端成功或者失败。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface FillRequestCallback--><!--Device-unnamed-export interface FillRequestCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

## onCancel

```TypeScript
onCancel(fillContent?: string): void
```

通知自动填充已被取消。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FillRequestCallback-onCancel(fillContent?: string): void--><!--Device-FillRequestCallback-onCancel(fillContent?: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fillContent | string | No | 表示通知自动填充取消后，返回给输入法框架的填充内容。<br>**Since:** 12 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1.The input parameter is not valid parameter; &lt;br&gt;2. Mandatory parameters are left unspecified.<br>**Applicable version:** 12 and later |
| 16000050 | Internal error. |
| 202 | Permission denied, non-system app called system api. |

## onFailure

```TypeScript
onFailure(): void
```

通知自动填充请求已失败。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FillRequestCallback-onFailure(): void--><!--Device-FillRequestCallback-onFailure(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000050 | Internal error. |
| 202 | Permission denied, non-system app called system api. |

## onSuccess

```TypeScript
onSuccess(response: FillResponse): void
```

通知自动填充请求已成功完成。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FillRequestCallback-onSuccess(response: FillResponse): void--><!--Device-FillRequestCallback-onSuccess(response: FillResponse): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| response | [FillResponse](arkts-ability-autofillrequest-fillresponse-i-sys.md) | Yes | 自动填充响应信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Mandatory parameters are left unspecified. |
| 16000050 | Internal error. |
| 202 | Permission denied, non-system app called system api. |

## setAutoFillPopupConfig

```TypeScript
setAutoFillPopupConfig(autoFillPopupConfig: AutoFillPopupConfig): void
```

动态调整气泡弹窗的尺寸和位置。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FillRequestCallback-setAutoFillPopupConfig(autoFillPopupConfig: AutoFillPopupConfig): void--><!--Device-FillRequestCallback-setAutoFillPopupConfig(autoFillPopupConfig: AutoFillPopupConfig): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| autoFillPopupConfig | [AutoFillPopupConfig](arkts-ability-autofillpopupconfig-i-sys.md) | Yes | 气泡弹窗尺寸和位置信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Mandatory parameters are left unspecified. |
| 16000050 | Internal error. |
| 202 | Permission denied, non-system app called system api. |

